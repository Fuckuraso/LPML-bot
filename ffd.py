import discord
import time
from discord.ext import commands
import os, sqlite3
pr='.'
ph=[]
vh=[]

pa=['<@724586867227623495>','<@693017644353323018>','<@752578603513938010>','<@719198278360760350>','<@434785097401499648>','<@552127419138572318>','<@436900440580292608>','<@689080862062805047>','<@520652881066590208>','<@789921476077420554>','<@688076916439515204>','<@551102946998353930>','<@605165277952475297>','<@756123748960305194>','<@750243974400311307>','<@608704245213954079>','<@757855048465383474>','<@752518766281097237>','<@755105403175698494>','<@756042790198050896>','<@610529864205729837>',"<@755093656364384276>",'<@752484065537425448>','<@752436614382485534>','<@752538068938129458>','<@523058530283028480>','<@752482899873234945>','<@755854075626782872>','<@752467669831123054>','<@586117526572892170>','<@756043268772462625>','<@402736764596387841>']
client = commands.Bot(command_prefix= str(pr) )
client.remove_command("help")


@client.command()
async def p(ctx):
    global ph
    ph.append('<@%s>'%ctx.author.id)
    print(ph)
    await ctx.send(ph[0])
@client.command()
async def pn(ctx):
    global ph
    global pa
    n = list(set(pa) ^ set(ph))
    k=len(n)
    print(k)
    for i in range(0, k):
        await ctx.send(n[0])
        del n[0]
        time.sleep(1)
@client.command()
async def v(ctx, a1, a2):
    global vh
    vh.append(a1 + ' надано відмітку ' + a2)
    print(vh)


@client.command()
async def va(ctx):
        global vh
        k = len(vh)
        for i in range(0, k):
            await ctx.send(vh[0])
            del vh[0]
            time.sleep(1)

#https://discord.com/api/oauth2/authorize?client_id=842673765572804628&permissions=8&scope=bot
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='ARK'))


client.run('ODA2ODkxMDg0ODg1MjYyMzM2.YBwB4Q.yzJv8n6crbdGBpXQtXFR9uT5XV0')
