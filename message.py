import discord
import asyncio
import sys
import os
import random
sys.path.append("./.")

client = discord.Client()
token = 'NzQzNzY0NzQ4NDc4MzE2NTQ1.X0j2gw.gtcHnmQc00Z6wf3LnYYVSnVT7eA'
GuidId = '713732221873291264'
UserList = []
emojiList = [':smile:', ':laughing:', ':slight_smile:', ':hot_pepper:', ':smirk:']
enp = []


@client.event
async def on_ready():
    spam_text = 'null'
    print("Started Text Spam with " + client.user.name)
    UserList = []
    for guild in client.guilds:
        print(str(guild.id) + ", " + guild.name)
        if str(guild.id) == GuidId:
            print("Start fetching member id from" + str(guild))
            UserList = guild.member
            for m in UserList:
                print(str(m.id) + ", " + m.name)   
    for member in UserList:
        if(member.id != client.user.id):
            if os.path.exists('text.txt'):
                lines = open('text.txt').read().splitlines()
                spam_text = random.choice(lines)

            userNames = open('dm_spam_text.txt')
            text = userNames.read().strip().split()
            if member.id in text:
                print(member.name + ' was already messaged')
            else:
                try:
                    await client.send_message(member, spam_text+" "+random.choice(emojiList)+random.choice(emojiList))
                    print('Sent message to ' + member.name)
                    file = open('dm_spam_text.txt', 'a')
                    file.writelines(member.id + '\n')
                    file.close()
                    for remaining in range(31, 0, -1):
                        # Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                        sys.stdout.write("\r")
                        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                        sys.stdout.flush()
                        await asyncio.sleep(1)
                    sys.stdout.write("\rComplete!                    \n")
                except Exception:
                    print('Something went wrong (;3;) relaunching...')

print('Start running client...')
client.run(token, bot=False)
