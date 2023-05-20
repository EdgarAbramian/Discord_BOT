from dotenv import load_dotenv
import openai
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

def chatgpt_response(prompt):
    completion = openai.ChatCompletion.create(  # Change the function Completion to ChatCompletion
        model='gpt-3.5-turbo',
        messages=[  # Change the prompt parameter to the messages parameter
            {
                'role': 'system', 'content': "You are Chat GPT working in real time, you should help users answering to their questions",
                'role': 'user', 'content': prompt,
            }
        ],
        temperature=0.7
    )
    return completion["choices"][0]['message']["content"]
