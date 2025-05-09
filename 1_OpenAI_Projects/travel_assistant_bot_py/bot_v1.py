import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_ai(prompt):
    """
    Function to ask the AI a question and get a response.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "You are a travel assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
        )
        return response.choices[0].message.content.strip()
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

"""
This is the first version of our chatbot.

Features implemented:
1. used load_dotenv to pass the OPENAI_API_KEY as env variable and
fetch it using os.getenv()
2. imported openai and configured api key in it
3. used openai to send request to the model and get response
4. openai.chat.completions.create to create a chat completion

model="gpt-4.1" is used to specify the model we want to use.
5. used temperature, max_tokens, top_p, frequency_penalty, presence_penalty
    and stop to control the response generation.

- temperature: Controls the randomness of the output. Lower values make the output more deterministic, while higher values make it more random.
- max_tokens: The maximum number of tokens to generate in the response. This limits the length of the output.
- top_p: Controls the diversity of the output. It uses nucleus sampling, where the model considers only the top p% of the probability mass.
- frequency_penalty: Controls the penalty for using frequent tokens. Higher values make the model less likely to repeat itself.
- presence_penalty: Controls the penalty for using new tokens. Higher values make the model more likely to introduce new topics.

"""
