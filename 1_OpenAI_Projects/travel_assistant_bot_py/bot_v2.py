import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation = []
conversation.append(
    {"role": "system", "content": "You are a travel assistant."}
)


def ask_ai(prompt):
    conversation.append({"role": "user", "content": prompt})

    """
    Function to ask the AI a question and get a response.
    """
    try:
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

        reply = response.choices[0].message.content.strip()
        conversation.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    print("Welcome to the Travel Assistant Bot!")
    print("Ask me anything about travel, and I'll do my best to help you.")
    print("Type 'exit' to quit the program.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = ask_ai(user_input)
        print(f"AI: {response}")


if __name__ == "__main__":
    main()
