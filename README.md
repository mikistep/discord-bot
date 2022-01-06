# discord-bot

This is a project that creates a discord bot that processes commands made on discord and interacts with Google Sheets API.

The bot was made to store results of 1v1 matches in League of Legends on each champion. It can be also used for other games.

The readme is incomplete.

## Setup

To run the bot you need to

1. Clone the repository to your local device
2. Download necessary python libraries
3. Create your discord bot https://discordpy.readthedocs.io/en/stable/discord.html
4. Create google API credentials and enable Google Sheets https://developers.google.com/workspace/guides/create-credentials
5. Create Google Excel Spreadsheet and grant access to the bot, arange the spreadsheet according to later section
6. Create file `data.json` and put following data:
```
{
    "sheet_id": "YOUR_SHEET_ID",
    "BOT_TOKEN": "YOUR_BOT_TOKEN"
}
```
7. Create file `credentials.json` and put your google credentials there.
8. Run `python main.py`

## Spreadsheet Layout

| | A | B      | C       |
|-|---|--------|---------|
|1|   | X name | Y name  |
|2|   | X score| Y score |
|3| champ 1  | X on champ 1 | Y on champ 1|
|4| champ 2  | X on champ 2 | Y on champ 2|
|...| champ ...  | X on champ ... | Y on champ  ... |

## Commands

There are commands for:

1. printing total match score
2. printing champion score
3. scoring a win