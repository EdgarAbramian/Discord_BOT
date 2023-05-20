from app.disc_bot.connect_discord import discord_token, client


if __name__ == '__main__':
    client.run(discord_token)