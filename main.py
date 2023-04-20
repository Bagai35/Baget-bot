import disnake
from disnake.ext import commands

bot = disnake.Client();

channelIDS = 1098290420250845254


@bot.slash_command(description="Responds with 'World'")
async def hello(inter):
    await inter.response.send_message("World")


@bot.event
async def on_ready():
    print('READY')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(channelIDS);
    await channel.send(
        embed=disnake.Embed(description=f'Пользователь {member} присел к костру', color=disnake.Color.yellow()));


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(channelIDS);
    await channel.send(
        embed=disnake.Embed(description=f'Пользователь {member} вышел из круга', color=disnake.Color.yellow()));


bot.run("MTA5NTI4Mzk3NDQ5NjA1OTM5Mg.Gny7LH.9fKgG5NMt9sGU4bVgieMIarhLWy8elWn6ZbLN4");
