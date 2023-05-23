from dotenv import load_dotenv
import os
import discord

from app.open_chat.connect_openai import chatgpt_response,real_chat
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
#
# class inet(discord.Intents):
#     intents = discord.Intents.default()
#
#     intents.messages = True
#
#
#
# client = discord.Client(intents=intents)
#
# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')
#
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content:
#         await message.channel.send('Hello!')
#
# client.run(discord_token)

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as: ", self.user)
    async def on_message(self, message):
        print(message.content)
        if (message.author  == self.user):
            return
        await message.channel.send(f'ChatGPT: {real_chat(message.content)}')

intents = discord.Intents.default()

intents.message_content = True
client = MyClient(intents=intents)
client.run(discord_token)











