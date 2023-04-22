
import disnake, aiohttp, colorthief, io, requests

from disnake.ext import commands


#######################################################################################################################

bot = commands.InteractionBot();

#######################################################################################################################

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


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

'''
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

'''





#######################################################################################################################
#bot.run('MTA5ODYyMzg2OTMxODg3MzExOQ.GrD4hc.wmK8q4vqNtDEEAsiQh0aJwTKonF8yTOMkb7pas');
bot.run('MTA5NTI4Mzk3NDQ5NjA1OTM5Mg.GluV3E.uVXXLRXnt1zdoJd4RjZIAWU8Pbv852gFvp7IJ0');
