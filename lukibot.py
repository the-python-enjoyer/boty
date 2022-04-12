import os
import discord
import random
from discord.ext import commands
from datetime import datetime

TOKEN = 'no token 4 u guys'
client = commands.Bot(command_prefix='L')
client.remove_command('help')
players = {}
colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Lhelp"))
    print("Done")
    
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('========Dziękuje za dodanie mnie na serwer. Mój prefix to L ,  wpisz Lhelp by dowiedzieć się więcej ========')
        break

#-----------------------HELP-----------------------------------------
@client.command()
async def help(message):
        embedVar = discord.Embed(title="Lista Komend", description="Komendy LukiBot", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="https://emoji.gg/assets/emoji/1598-blurple-support.png")
        embedVar.add_field(name="Eat", value="Nakarm Luki!", inline=False)
        embedVar.add_field(name="Drive", value="Zabierz Luki na wycieczkę!", inline=False)
        embedVar.add_field(name="Dance", value="Zatańczcie!", inline=False)
        embedVar.add_field(name="Slap", value="Auć!", inline=False)
        embedVar.add_field(name="Flip", value="POG", inline=False)
        embedVar.add_field(name="Hfive", value="Piąteczka mordeczko", inline=False)
        embedVar.add_field(name="Hug", value="Przytul Luki", inline=False)
        embedVar.add_field(name="Take", value="Ciekawe gdzie Luki cie bierze", inline=False)
        embedVar.add_field(name="Tgrass", value="Dotknij trawy i przejdź się z Luki!", inline=False)
        embedVar.add_field(name="Scare", value="Jak mogłeś!", inline=False)
        embedVar.add_field(name="Xayoo", value="Poggers bonus", inline=False)
        embedVar.set_footer(text="Koniec listy komend", icon_url="https://emoji.gg/assets/emoji/9023-blurple-employee.png")
        await message.channel.send(embed=embedVar)
#----------------------------------------------------------------------
        
@client.command()
async def Eat(message):
        embedVar = discord.Embed(title="Dałeś jeść Luki", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot")
        embedVar.set_image(url="https://media.discordapp.net/attachments/944176849007828992/944524551495249950/patryk-czopur.gif")
        embedVar.set_footer(text="Luki jest pełny!", icon_url="https://emoji.gg/assets/emoji/7232_WumpusCookie.png")
        await message.channel.send(embed=embedVar)
#------------------------EAT--------------------------------------------
@client.command()
async def Drive(message):
        embedVar = discord.Embed(title="Luki tak nie może się doczekać jazdy że zapomniał jak wejść do auta!", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944540615079772160/luki-szuka-wejscia.gif")
        embedVar.set_footer(text="Luki jest szczęśliwy na ogrzewanym siedzeniu!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
        await message.channel.send(embed=embedVar)
#-------------------------DRIVE----------------------------------------
@client.command()
async def Dance(message):
        embedVar = discord.Embed(title="Luki! Ale ty nawalasz na tym parkiecie", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944550507811315743/lukisteve-luki-taniec.gif")
        embedVar.set_footer(text="Miłej potańcówki młodziaki!", icon_url="https://emoji.gg/assets/emoji/2184_wumpus_color_gif.gif")
        await message.channel.send(embed=embedVar)
#-------------------------DANCE---------------------------------------
@client.command()
async def Slap(message):
        embedVar = discord.Embed(title="Oh no! our Luki... Is broken!", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944552520154501130/lukisteve-xayoo.gif")
        embedVar.set_footer(text="Auć", icon_url="https://emoji.gg/assets/emoji/9148-pressf.gif")
        await message.channel.send(embed=embedVar)
        
#-------------------------SLAP----------------------------------------
@client.command()
async def Flip(message):
        embedVar = discord.Embed(title="POG flip", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944553173757100082/lukisteve-salto.gif")
        embedVar.set_footer(text="Dobrze że robił to na łóżku", icon_url="https://emoji.gg/assets/emoji/1162-pogslide.gif")
        await message.channel.send(embed=embedVar)
        
#-----------------------FLIP------------------------------------------
@client.command()
async def Hfive(message):
        embedVar = discord.Embed(title="Piąteczka!", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944553174168125480/lukisteve-oooo.gif")
        embedVar.set_footer(text="Dobra morda zawsze daje piąteczki", icon_url="https://emoji.gg/assets/emoji/3751-blue-fire.gif")
        await message.channel.send(embed=embedVar)
        
#--------------------HFIVE-------------------------------------------
@client.command()
async def Hug(message):
        embedVar = discord.Embed(title="Przytulasek", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944553226190065674/lukisteve-holak.gif")
        embedVar.set_footer(text="AW <3", icon_url="https://emoji.gg/assets/emoji/3018-pinkheart.gif")
        await message.channel.send(embed=embedVar)
        
#-------------------HUG-----------------------
@client.command()
async def Take(message):
        embedVar = discord.Embed(title="Luki:U're mine now", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944553174528847902/lukisteve-luki.gif")
        embedVar.set_footer(text="Ciekawe gdzie cie bierze", icon_url="https://emoji.gg/assets/emoji/7368-bullymaguire.gif")
        await message.channel.send(embed=embedVar)
        
#----------------TAKE------------
@client.command()
async def Tgrass(message):
        embedVar = discord.Embed(title="Poszedłeś nareszcie dotknąć trawy z Luki", description=": D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944557300872519750/lukisteve-japczan.gif")
        embedVar.set_footer(text="Odpocznij przyjacielu", icon_url="https://emoji.gg/assets/emoji/3335-mysticalpeter.gif")
        await message.channel.send(embed=embedVar)
        
#----------------TGRASS------------
@client.command()
async def Scare(message):
        embedVar = discord.Embed(title="Przestraszyłeś go!", description="D :", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/786514235433811982/944557300373393500/lukisteve-horror.gif")
        embedVar.set_footer(text="jak mogłeś", icon_url="https://emoji.gg/assets/emoji/7962-hilathink.gif")
        await message.channel.send(embed=embedVar)
        
#---------------Scare--------------------      
@client.command()
async def Xayoo(message):
        embedVar = discord.Embed(title="Xayoo! co ty tu robisz", description=":D", color = random.choice(colors), timestamp=datetime.utcnow())
        embedVar.set_author(name="LukiBot", icon_url="")
        embedVar.set_image(url="https://media.discordapp.net/attachments/943942213207990347/944561583881863228/xayoo-okulary-jd-koks.gif")
        embedVar.set_footer(text="POGGERS", icon_url="https://media.discordapp.net/attachments/943942213207990347/944561583881863228/xayoo-okulary-jd-koks.gif")
        await message.channel.send(embed=embedVar)
        
client.run(TOKEN)