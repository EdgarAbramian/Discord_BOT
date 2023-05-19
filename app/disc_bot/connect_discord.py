from dotenv import load_dotenv
import os
import discord
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as: ", self.user)
    async def on_message(self, message):
        print(message.content)
        if (message.author  == self.user):
            return
        await message.channel.send(f'{message.content}')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(discord_token)













