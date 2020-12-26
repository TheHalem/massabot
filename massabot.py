# bot.py
import os

import discord

TOKEN = ""

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )


@client.event
async def on_reaction_add(reaction, user):
    print(f'{reaction.emoji}')


@client.event
async def on_message(message):

    failHardo = ("<:WideHardo1:744316977924800633> <:WideHardo2:744317025345863831> <:WideHardo3:744317070925365379> <:WideHardo4:744317111865966592>", "<:WideHardo1:744316977924800633> <:WideHardo2:744317025345863831> <:WideHardo3:744317070925365379>",
                 "<:WideHardo1:744316977924800633> <:WideHardo2:744317025345863831>", "<:WideHardo2:744317025345863831> <:WideHardo3:744317070925365379> <:WideHardo4:744317111865966592>", "<:WideHardo3:744317070925365379> <:WideHardo4:744317111865966592>", "<:WideHardo2:744317025345863831> <:WideHardo3:744317070925365379>",
                 "<:WideHardo1:744316977924800633> <:WideHardo4:744317111865966592>")

    if message.content == '<:WideHardo1:744316977924800633><:WideHardo2:744317025345863831><:WideHardo3:744317070925365379><:WideHardo4:744317111865966592>':
        await message.add_reaction('<:FakeFocus:792162631568850945>')

    if any(bad_word in message.content for bad_word in failHardo):
        response = "<:WideHardo1:744316977924800633><:WideHardo2:744317025345863831><:WideHardo3:744317070925365379><:WideHardo4:744317111865966592>"
        await message.add_reaction('<:schade:736239412022607892>')
        await message.channel.send(response)


client.run(TOKEN)
