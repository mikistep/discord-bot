from public_messages import send_public_message

BOT_COMMAND_PREFIX = '--'
HELP_COMMAND = 'HELP'

async def handle_public_message(message):
    if is_command(message.content):
        await process_command(message)


def is_command(message_content):
    return message_content.startswith(BOT_COMMAND_PREFIX)


async def process_command(message):
    for command in COMMANDS_AND_HANDLERS:
        if message.content.upper().startswith((BOT_COMMAND_PREFIX + command).upper()):
            return await COMMANDS_AND_HANDLERS[command](message, command)
    context = {"help_command_with_prefix": BOT_COMMAND_PREFIX + HELP_COMMAND.lower()}
    await send_public_message(message.channel, 'UNKNOWN_COMMAND', context)


async def handle_help_command(message, command_name):
    await send_public_message(message.channel, 'HELP_COMMAND', {"bot_command_prefix": BOT_COMMAND_PREFIX})


def is_server_admin(message_author):
    return message_author.guild_permissions.administrator


# use only when 'message_content' is a valid bot command
def get_command_arguments(message_content):
    return message_content.upper().split()[1:]


async def handle_liga_legend(message, command_name):
    await send_public_message(message.channel, 'PLATINUM_BATTLE')

async def handle_today(message, command_name):
    await send_public_message(message.channel, 'GAMES_TODAY')
    
async def handle_champion(message, command_name):
    args = get_command_arguments(message.content)
    EXPECTED_NUMBER_OF_ARGUMENTS = 1
    if len(args) != EXPECTED_NUMBER_OF_ARGUMENTS:
        return f'expected 1 arguments, got {len(args)}'
    await send_public_message(message.channel, 'CHAMPION_SCORE', {"champion": args[0]})
    
async def handle_win(message, command_name):
    args = get_command_arguments(message.content)
    EXPECTED_NUMBER_OF_ARGUMENTS = 2
    if len(args) != EXPECTED_NUMBER_OF_ARGUMENTS:
        return f'expected 2 arguments, got {len(args)}'
    await send_public_message(message.channel, 'WRITE_WIN', {"player": args[0] ,"champion": args[1]})
    
async def handle_total(message, command_name):
    await send_public_message(message.channel, 'TOTAL_SCORE')
    
async def handle_update(message, command_name):
    await send_public_message(message.channel, 'SHEET_UPDATE')


COMMANDS_AND_HANDLERS = {
    HELP_COMMAND: handle_help_command,
    'ELO': handle_liga_legend,
    '24H': handle_today,
    'TOTAL': handle_total,
    'CHAMP': handle_champion,
    'WIN': handle_win,
    'UPDATE': handle_update,
}