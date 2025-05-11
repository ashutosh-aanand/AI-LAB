import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# print(openai.api_key)

models = openai.models.list()

print("List of models available for my account:")
print("-------------------------------------------")
for model in models:
    print(f"{model.id}")
