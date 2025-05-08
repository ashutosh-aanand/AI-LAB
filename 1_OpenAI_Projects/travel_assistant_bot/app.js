import dotenv from "dotenv";
dotenv.config();

import OpenAI from "openai";
const client = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY
});

const response = await client.responses.create({
    model: "gpt-4.1",
    input: "Hi",
});

console.log(response.output_text);
