from colorama import Fore, init, Style
init(convert = False)
import time,os,datetime
import string
from random import *
import discord 
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
import aiohttp, tasksio


with open('tokens.txt','r') as handle:
        tokens = handle.readlines()

for line in open('proxies.txt'):
        self.proxies.append(line.replace('\n',""))
      print(f"Trying Proxies Successfull")
    except:
      print(f"Failed to Load Proxies From Proxies.txt")
    self.headers = {"Authorization": "Bot {}".format(self.token)}
    self.apii = random.randint(7, 8);
    self.api = random.randint(6, 9);
    
    rotate = cycle(self.proxies)

client = discord.Client()

@client.command(pass_context=True)
async def dm(ctx, *, message):
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"Sent {user.name} a DM.")
            except:
                print(f"Couldn't DM {user.name}.")
        print("Sent all the server a DM.")

      
client.run(tokens, bot=0, reconnect=1)