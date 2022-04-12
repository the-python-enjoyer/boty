
import discord
from discord.ext import commands, tasks
from requests import get
import json

intents = discord.Intents.all()
TOKEN = 'no token 4 u guys'
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')
players = {}

    
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Kwack Them All. Leave nobody"))
    print("Kwack!!")
    
    
@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0xffe987, timestamp=ctx.message.created_at)
    embed.add_field(name='Help commands', value='I made this list for u kwacky friend', inline=False)
    embed.add_field(name='Kwack_all', value='Dm s to all on server ( I feel kwacky ban for this action )', inline=True)
    embed.add_field(name='meme', value='Makes u kwack all in tears!', inline=True)
    embed.add_field(name='hi', value='Greetings', inline=True)
    embed.set_footer(text=f"Help commands")
    await ctx.channel.send(embed=embed)
    
#przyjemne ale nie^
    
@bot.command()
async def kwack_all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
            except:
                print("Kaput")
    else:
        await ctx.send("NO U CAN'T DO IT ITS ILLEGALLLLLLLLL!!!q")
        
#jak się zepsuje to chyba mnie cos strzeli^

@bot.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = 0xffe987).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)
    
#Izi steal^
@bot.command()
async def hi(ctx):
   await ctx.reply("**Kwack!** (*what do u want from duck?*)")
#what the duck^
        
       
bot.run(TOKEN)
    