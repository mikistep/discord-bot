import discord
from commands_processing import handle_public_message




async def handle_message(client, message):
    if message.author == client.user:
        return # bot should ignore messages sent by itself
    else:
        await handle_public_message(message)