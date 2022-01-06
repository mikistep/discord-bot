# This file contains content of all messages that are sent by the bot
# on public channels, including some logic behind messages
# that contain serial data.

from discord import message
from opgg import legendary_platinum_battle
from opgg import neverending_climb
from logic import calc_total_score, calc_update
from logic import calc_champion_score
from logic import calc_write_win


async def send_public_message(channel, message_type, context=None):
    print(channel, message_type)
    await channel.send(render_message_content(message_type, context))


def render_message_content(message_type, context):
    print(message_type)
    if message_type in PUBLIC_MESSAGES_CONTENTS:
        return PUBLIC_MESSAGES_CONTENTS[message_type](context)
    raise Exception(f'Unknown message type: "{message_type}"')


# CONTEXT: help_command_with_prefix
def msg_unknown_command(context):
    return f'Unknown command. Use {context["help_command_with_prefix"]} to see available commands.'


def msg_help_command(context):
    bot_command_prefix = context["bot_command_prefix"]
    message = """===== AVAILABLE COMMANDS =====

{0}total - show overall match result

{0}champ [champion_name] - show result on a champion

{0}win [player_name] [champion_name] - save win for a player on a champion

{0}update - update players and champions.
""".format(bot_command_prefix)
    return message

# CONTEXT: command_name_with_prefix
def msg_wrong_number_of_args(context):
    return f'Invalid number of arguments. Usage: {context["command_name_with_prefix"]} [event_name]'


def msg_total_score(context):
    return calc_total_score()

def msg_champion_score(context):
    return calc_champion_score(context["champion"])

def msg_write_win(context):
    return calc_write_win(context["player"] ,context["champion"])

def msg_platinum_battle(context):
    return legendary_platinum_battle()


def msg_games_today(context):
    return neverending_climb()

def msg_sheet_update(context):
    return calc_update()



PUBLIC_MESSAGES_CONTENTS = {
    'UNKNOWN_COMMAND': msg_unknown_command,
    'HELP_COMMAND': msg_help_command,
    'PLATINUM_BATTLE': msg_platinum_battle,
    'GAMES_TODAY': msg_games_today,
    'TOTAL_SCORE': msg_total_score,
    'CHAMPION_SCORE': msg_champion_score,
    'WRITE_WIN': msg_write_win,
    'SHEET_UPDATE': msg_sheet_update,
}