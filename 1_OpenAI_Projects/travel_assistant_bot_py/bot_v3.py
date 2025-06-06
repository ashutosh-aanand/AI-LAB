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
    Function to summarize a subset of conversation.
    """
    try:
        # Create a summary prompt
        summary_prompt = (
            "You are a travel assistant summarizer. Summarize the following conversation "
            "in a concise and meaningful way. Focus on key points, avoid unnecessary details, "
            "and ensure the summary captures the main topics discussed:\n\n"
        )
        for message in conversation:
            summary_prompt += f"{message['role']}: {message['content']}\n"

        # Get the summary from the AI
        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "You are a travel assistant summariser"},
                {"role": "user", "content": summary_prompt}
            ],
            temperature=0.3,  # lowered the temperature for more deterministic output
            max_tokens=70,  # increased max tokens for a longer summary
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

"""
limit: 
    Defines the maximum number of messages the conversation can store at any time.
    In this case, limit = 10, meaning the conversation will store at most 10 messages 
    (including the system message, user messages, and AI responses).
buffer:
    Defines the number of messages to keep after summarizing the conversation.
    In this case, buffer = 2, meaning that after summarizing, the last 2 messages 
    (the user message and the AI response) will be kept in the conversation.

After summarizing, the conversation will contain:
    1. The system message
    2. The summary of the last 5 messages
    3. The last 2 messages (user message and AI response)
    Total: 1 + 1 + 2 = 4 messages in the conversation.

    This allows the conversation to be cleaned up while still retaining the context of the last few messages.

I lowered the temperature for summarization prompt, to get a more deterministic output.

"""
