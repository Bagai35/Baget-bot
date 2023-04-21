import disnake, aiohttp, colorthief, io
from disnake.ext import commands
from dotenv import load_dotenv
from io import BytesIO
#######################################################################################################################

bot = commands.InteractionBot();

channelIDS = 1098290420250845254;

#######################################################################################################################

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


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



@bot.slash_command(description="bot say 'Pong'")
async def ping(inter):
    await inter.response.send_message("Pong");


@bot.slash_command(description="server information")
async def serverinfo(ctx):
    guild = ctx.guild
    embed = disnake.Embed(title=f"{guild.name}", description=guild.description or "No description", color=disnake.Color.blue())

    embed.add_field(name="Created at", value=guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)
    embed.add_field(name="Region", value=str(guild.region).capitalize(), inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.set_thumbnail(url=guild.icon.url)
    await ctx.send(embed=embed)


@bot.slash_command(description="Отправит картинку Неко :3")
async def neko_pic(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://nekos.life/api/v2/img/neko') as resp:
            if resp.status != 200:
                return await ctx.send('Could not fetch the picture')

            data = await resp.json()
            embed = disnake.Embed(title="Ня :3,")
            embed.set_image(url=data['url'])

            await ctx.send(embed=embed)



@bot.slash_command(description="18+ Neko")
async def neko_hentai(ctx):
    if not ctx.channel.is_nsfw():
        return await ctx.response.send_message("This command can only be used in NSFW channels.")
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.waifu.pics/nsfw/neko') as resp:
            if resp.status != 200:
                return await ctx.send('Could not fetch the picture')

            data = await resp.json()
            embed = disnake.Embed(title="Ну ты и шалунишка")
            embed.set_image(url=data['url'])

            await ctx.send(embed=embed)



@bot.slash_command(description="Аватарка пользователя")
async def avatar(ctx, user: disnake.Member):
    async with aiohttp.ClientSession() as session:
        async with session.get(str(user.avatar.url)) as resp:
            if resp.status != 200:
                return await ctx.send('Could not fetch the picture')
            data = await resp.read()
    color = colorthief.ColorThief(io.BytesIO(data)).get_color(quality=1)
    embed_color = disnake.Colour.from_rgb(color[0], color[1], color[2])
    embed = disnake.Embed(title=f"Аватарка {user.name} :3", color=embed_color)
    embed.set_image(url=user.avatar.url)

    await ctx.send(embed=embed)
bot.run('TOKEN')
