import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1521829665432408115

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

EMOJIS = ["🟢", "🟡", "🔵", "❌"]

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == CHANNEL_ID:
        for emoji in EMOJIS:
            await message.add_reaction(emoji)

client.run(TOKEN)
