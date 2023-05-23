from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')


MEM = []
def chatgpt_response(prompt):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=prompt,
        temperature=0.7
    )
    return completion["choices"][0]['message']["content"]

def real_chat(prompt):
    d = {"role": "user", "content": prompt}
    MEM.append(d)
    if(len(MEM) == 5):
        del MEM[0]
    ans = chatgpt_response(MEM)
    return ans