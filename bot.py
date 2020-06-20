#Created by : Toddy


import discord 
from discord.ext import commands 
from discord.ext.commands import has_permissions

prefix = "/"

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

token_ = open("token.txt", "r")

token = (token_.readline())

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: '{prefix}'\n-----")
   
    await bot.change_presence(activity=discord.Game(name=f"/help"))

@bot.command()
async def invite(ctx):

    await ctx.send("https://discord.gg/2FFJX87")
    
@bot.command()
async def help(ctx):                        
    embed=discord.Embed(title="Help", color=0x00000ff)
    embed.add_field(name="/help", value="sends this message", inline=False)
    embed.add_field(name="/invite", value="send an invite to the server", inline=False)
    embed.add_field(name="/echo", value="repeats your message")
    await ctx.send(embed=embed)



@bot.command()
async def echo(ctx, *, message=None):

    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)

bot.run(token) 
