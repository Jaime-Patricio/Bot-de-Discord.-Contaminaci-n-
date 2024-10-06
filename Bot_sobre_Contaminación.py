import discord
import requests
import os
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', help_command = commands.DefaultHelpCommand(
    no_category = "Comandos"

), intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


descomposicion={
    "botella":500,
    "lata":50,
    "bolsa":150,
    "vidrio":4000
}
@bot.command()
async def impacto(ctx,objeto:str):
    objeto=objeto.lower()
    if objeto in descomposicion:
        tiempo=descomposicion[objeto]
        await ctx.send(f"El objeto {objeto} dura aproximadamente {tiempo} en descomponerse.")
        if tiempo>=100:
            await ctx.send(f"Vayase preocupando. Por favor.")
        elif tiempo>=50:
            await ctx.send(f"Ok, algo preocupante.")

    else: 
        await ctx.send("No registro este objeto.")

bot.run("Aquí iría tu token.")
