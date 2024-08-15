import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def merhaba(ctx):
    await ctx.send(f'*Merhaba!* Ben {bot.user}, bir Discord sohbet botuyum! 😄')
@bot.command()
async def dönüşüm(ctx):
    with open(r'm2l1\m2l2\geri-donusum-kutulari.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def birazgülolum(ctx):
    with open(r'm2l1\png-transparent-smile-emoji-face-mouth-perspiration-anxious-face-smiley-emoticon.png', 'rb') as f:
        gulucuk = discord.File(f)
    await ctx.send(file=gulucuk)
@bot.command()
async def bayrak(ctx):
    with open(r'm2l1\Unh1OwPF_400x400.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
@bot.command()
async def izmirmarş(ctx):
    with open(r'm2l1\Haluk Levent - İzmir Marşı.mp3', 'rb') as f:
        sarki = discord.File(f)
    await ctx.send(file=sarki)
@bot.command()
async def çanakkalemarş(ctx):
    with open(r'm2l1\Çanakkale içinde aynalı çarşı, ana ben gidiyorum düşmana karşı .....mp3', 'rb') as f:
        çanakkale = discord.File(f)
    await ctx.send(file=çanakkale)
@bot.command()
async def istiklalmarş(ctx):
    with open(r'm2l1\İstiklal Marşı.mp3', 'rb') as f:
        mars = discord.File(f)
    await ctx.send(file=mars)
@bot.command()
async def atam(ctx):
    with open(r'm2l1\Ataturk.jpg', 'rb') as f:
        resim = discord.File(f)
    await ctx.send(file=resim)
@bot.event
async def on_command_error(ctx, error):
        await ctx.send("Oops! Bir şeyler ters gitti! 😅")
@bot.command()
async def nasılsın(ctx):
    cevaplar = [
        "Harikayım, teşekkür ederim! 😄",
        "Biraz yorgunum, ama iyiyim! 😊",
        "Muhteşemim! Sen nasılsın? 😎"
    ]
    await ctx.send(random.choice(cevaplar))
@bot.command()
async def benimresmim(ctx):
    await ctx.send(bot.user.avatar.url)
@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Evet, Tevfiğin botu çok havalı.')


bot.run("Token")
