# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : sixBit                #
# File Name             : config.py             #
# --------------------------------------------- #

# Telegram
token = '<YOUR BOT TOKEN>'  # More: https://core.telegram.org/bots#3-how-do-i-create-a-bot

# MySQL
mysql_host = 'localhost'
mysql_db   = '<DB>'
mysql_user = '<USER>'
mysql_pw   = '<PASSWORD>'

# Support Chat (Chat ID)
support_chat =                  # example: -1001429781350

# Misc
time_zone           = 'GMT+2'   # Supports team time zone
bad_words_toggle    = True      # Enable / disable bad words filter
spam_toggle         = True      # Enable / disable spam filter
spam_protection     = 5         # How many consecutive messages can be sent without a reply from the team
open_ticket_emoji   = 24        # After X amount of HOURS an emoji will pop up at /tickets

# Messages
text_messages = {
    'start': 'Hi {}, how can we help you today?',
}

# Regex (https://regex101.com/)
regex_filter = {
    'bad_words': r'(?i)^(.*?(\b\w*fuck|shut up|dick|bitch|bastart|cunt|bollocks|bugger|rubbish|wanker|twat|suck|ass|pussy|arsch\w*\b)[^$]*)$'
}