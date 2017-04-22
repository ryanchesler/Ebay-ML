import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!killjews'):
    	jews = 10
    	while jews >0:
    		jews -=1
    		j = str(jews)
    		await client.send_message(message.channel, "there are %d jews remaining"%jews)
    	if jews == 0:
    		await client.send_message(message.channel, "checkmate atheists")

client.run('MzAyNTg4NjU2NzI2ODM1MjAw.C9LvOA.Ro2Xrd9WD0gvj7w3x-OTYH0PJE0')
