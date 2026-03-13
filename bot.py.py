with open("test.txt", "w") as f:
    f.write("hello")

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_ID = 1462135740606710016  
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        role = message.guild.get_role(ROLE_ID)
        await message.author.add_roles(role)
        await message.channel.send("Thank you for using code MAARS #ad!")

    await bot.process_commands(message)

bot.run("MTQ4MTg2OTM0MDAxNzE2ODU1OA.G31DH1.vUSFXuVBxw41YNPxqu1eZeT2jcAacRgp80i1FY")

