import discord
import random
import traceback
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='*', intents=intents)


@bot.event
async def on_ready():
print(f' logged in as{bot.user} ')
@bot.event
async def on_command_error(ctx, error):
# You can customise or elaborate the error message
error_message = f "Oops! Something went wrong! 😅 \nError: { error}"
# Send error message
await ctx.send(error_message)
# Save error message to file
with open('hata_mesajlari.txt', 'a', encoding='utf-8') as f:
f.write(f" Error for {ctx.command} command: {traceback.format_exc()}\n")
@bot.command()
async def hello(ctx):
await ctx.send(f'*Hello!* I am {bot.user}, a Discord chat bot! 😄')
@bot.command()
async def transformation(ctx):
with open(r'm2l1\geri-donusum-kutulari.jpg', 'rb') as f:
picture = discord.File(f)
await ctx.send(file=picture)
@bot.command()
async def self_intro(ctx):
intro = (
"I'm a Discord bot,"
"I'm here to provide you with fun commands! 😄\n"
"Here are some commands:\n"
"*hello - I send you greetings!\n"
"*joke - I share a funny joke!\n"
"*word - I share a proverb!"
)
await ctx.send(intro)
@bot.command()
async def biraz_gül_oğlum(ctx):
with open(r'm2l1\png-transparent-smile-emoji-face-mouth-perspiration-anxious-face-smiley-emoticon.png', 'rb') as f:
gulucuk = discord.File(f)
await ctx.send(file=gulucuk)
@bot.command()
async def selam(ctx):
await ctx.send(f "Hello {ctx.author.name}! How are you? 😊")
@bot.command()
async def flag(ctx):
with open(r'm2l1\Unh1OwPF_400x400.jpg', 'rb') as f:
# Let's store the converted Discord library file in this variable!
picture = discord.File(f)
# We can then send this file as a parameter!
await ctx.send(file=picture)
@bot.command()
async def izmirmarş(ctx):
with open(r'm2l1\Haluk Levent - İzmir Marşı.mp3' , 'rb') as f:
sarki = discord.File(f)
await ctx.send(file=sarki)
@bot.command()
async def çanakkalemarş(ctx):
with open(r'm2l1\Çanakkale in aynalı Çarşı, ana i'm going against the enemy .....mp3', 'rb') as f:
çanakkale = discord.File(f)
