import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1521829665432408115

EMOJIS = ["🟢", "🟡", "🔵", "❌"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id != CHANNEL_ID:
        return

    # React only if the message has an image attachment
    has_image = any(
        attachment.content_type
        and attachment.content_type.startswith("image/")
        for attachment in message.attachments
    )

    if not has_image:
        return

    for emoji in EMOJIS:
        await message.add_reaction(emoji)


client.run(TOKEN)
