"""
In v2 we had added past conversation context
This made the model context aware and improved the conversation, 
as the model knew about past conversation as well.

But this has certain drawbacks:
1. The model is not able to remember the context of the conversation
   after a certain number of tokens. This means that if the conversation
   goes on for too long, the model will forget the earlier parts of the
   conversation.
2. The conversation context grows with each message, which means that the
   model will take longer to respond as the conversation goes on.

In v3 we will clean up the conversation context and only keep the last 5 messages
and keep a summary for the cleaned up messages.

so the conversation will store at max 10 messages
and the last 5 messages will be cleaned up and replaced with a summary of the last 5 messages.
   
"""

import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

limit = 10
buffer = 2


def summarize_conversation(conversation):
    """
    Function to summarize the last 5 messages in the conversation.
    """
    try:
        # Create a summary prompt
        summary_prompt = "Summarize the following conversation:\n"
        for message in conversation:
            summary_prompt += f"{message['role']}: {message['content']}\n"

        # Get the summary from the AI
        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "You are a travel assistant summariser. Summarise this, include the key terms only"},
                {"role": "user", "content": summary_prompt}
            ],
            temperature=0.5,
            max_tokens=50,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def ask_ai(prompt, conversation):
    """
    Function to ask the AI a question and get a response.
    """
    try:
        # Add the user message to the conversation
        conversation.append({"role": "user", "content": prompt})

        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=conversation,
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
        )
        # Add the AI response to the conversation
        conversation.append(
            {"role": "assistant", "content": response.choices[0].message.content.strip()})

        # If the conversation is too long, summarize the oldest 5 messages
        # and replace them with a summary
        print(f"conversation length {len(conversation)}")
        if len(conversation) > limit:
            # Summarize the first 5 messages
            summary = summarize_conversation(conversation[1:-buffer])
            # Replace the first 5 messages with the summary
            print("Summarizing Conversation -----")
            print(f"summary till now {summary}")
            print("-------------------------------------------")
            # conversation = conversation[:1] + \
            #     [{"role": "system", "content": summary}] + \
            #     conversation[-buffer:]  # conversation[buffer + 1:]
            del conversation[1:-buffer]
            conversation.insert(1, {"role": "system", "content": summary})
            print(f"conversation after summary {conversation}")
            print("-------------------------------------------")
            print("Conversation cleaned up.")
            print("-------------------------------------------")

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    print("Welcome to the Travel Assistant Bot!")
    print("Ask me anything about travel, and I'll do my best to help you.")
    print("Type 'exit' to quit the program.")

    # Initialize conversation context
    conversation = [
        {"role": "system", "content": "You are a travel assistant."}
    ]

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = ask_ai(user_input, conversation)
        print(f"AI: {response}")

        print("---------------################-------------------------")
        print(f"conversation length {len(conversation)}")
        print(f"conversation {conversation}")
        print("---------------################-------------------------")


if __name__ == "__main__":
    main()
