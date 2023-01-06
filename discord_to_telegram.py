'''
@author: Rohit Sharma
date: 06-01-2023

Description:  This python script will look at a specific discord channel each message that comes in. 
Then if the message has certain key words it would like to parse words and numbers out of the text of the message. 
Then take the message and reformat it to a new specific format. In last write the new formatted message to a 
specific telegram channel and to a file on the local device.

'''

import discord
import re
import telegram

# create a Discord client
client = discord.Client()

# create a Telegram bot
bot = telegram.Bot('paste-your-bot-token')

# listen for messages in a specific Discord channel
@client.event
async def on_message(message):
    if message.channel.name == 'my-channel':
    # parse words and numbers out of the message
        words = re.findall(r'\b\w+\b', message.content)
        numbers = re.findall(r'\b\d+\b', message.content)

        # reformat the message
        new_message = f'{message.author}: {message.content}'

        # write the message to a file
        with open('my-file.txt', 'a') as f:
            f.write(new_message + '\n')

        # send the message to a Telegram channel
        bot.send_message(chat_id='paste-your-channel-id', text=new_message)

# start the Discord client
client.run('paste-your-bot-token')
