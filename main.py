import discord
from logic import initialize
from message_processing import handle_message
import json

BOT_TOKEN = json.loads(open ('data.json', "r").read())["BOT_TOKEN"]

def main():
    client = discord.Client()
    initialize()

    @client.event
    async def on_ready():
        print('Bot is active as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        await handle_message(client, message)

    client.run(BOT_TOKEN)


if __name__ == '__main__':
    main()