import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        msg = 'Try using !<spec> for a link to icy-veins resources. Note: For Frost Mage/DK, specify class (frostdk, frostmage)'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!arms'):
        msg = 'Hello {0.author.mention}, here is the link for arms info: https://www.icy-veins.com/wow/arms-warrior-pve-dps-guide'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!fury'):
        msg = 'Hello {0.author.mention}, here is the Fury Warrior info: https://www.icy-veins.com/wow/fury-warrior-pve-dps-guide'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')
