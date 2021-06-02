import discord
import time
from discord.ext import commands
import os, sqlite3
pr='.'
ph=[]
vh=[]
n=[]
pa=['<@724586867227623495>','<@693017644353323018>','<@752578603513938010>','<@719198278360760350>','<@434785097401499648>','<@552127419138572318>','<@436900440580292608>','<@689080862062805047>','<@520652881066590208>','<@789921476077420554>','<@688076916439515204>','<@551102946998353930>','<@605165277952475297>','<@756123748960305194>','<@750243974400311307>','<@608704245213954079>','<@757855048465383474>','<@752518766281097237>','<@755105403175698494>','<@756042790198050896>','<@610529864205729837>',"<@755093656364384276>",'<@752484065537425448>','<@752436614382485534>','<@752538068938129458>','<@523058530283028480>','<@752482899873234945>','<@755854075626782872>','<@752467669831123054>','<@586117526572892170>','<@756043268772462625>','<@402736764596387841>']
pa1=['<@755854075626782872>', '<@608704245213954079>', '<@757855048465383474>', '<@756123748960305194>', '<@586117526572892170>', '<@520652881066590208>', '<@752538068938129458>', '<@752436614382485534>', '<@789921476077420554>', '<@752578603513938010>', '<@752518766281097237>', '<@755093656364384276>', '<@434785097401499648>', '<@689080862062805047>', '<@755105403175698494>', '<@552127419138572318>']
pa2=['<@605165277952475297>','<@724586867227623495>','<@436900440580292608>','<@688076916439515204>','<@756043268772462625>','<@402736764596387841>','<@750243974400311307>','<@693017644353323018>','<@719198278360760350>','<@756042790198050896>','<@610529864205729837>','<@752484065537425448>','<@523058530283028480>','<@752467669831123054>','<@752482899873234945>','<@551102946998353930>']

client = commands.Bot(command_prefix= str(pr) )
client.remove_command("help")


@client.command()
async def p(ctx):
    global ph
    if time.strftime("%a")=='Tue'and time.strftime("%X")>'08:44:00'and time.strftime("%X")<'09:31:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Mon'and time.strftime("%X")>'09:50:00'and time.strftime("%X")<'10:35:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Mon'and time.strftime("%X")>'10:55:00'and time.strftime("%X")<'11:40:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Mon'and time.strftime("%X")>'12:00:00'and time.strftime("%X")<'12:45:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Mon'and time.strftime("%X")>'13:05:00'and time.strftime("%X")<'13:50:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Fri'and time.strftime("%X")>'08:44:00'and time.strftime("%X")<'09:31:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Fri'and time.strftime("%X")>'09:50:00'and time.strftime("%X")<'10:35:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Thu'and time.strftime("%X")>'12:00:00'and time.strftime("%X")<'12:45:00':
        ph.append('<@%s>'%ctx.author.id)
    elif time.strftime("%a")=='Thu'and time.strftime("%X")>'15:05:00'and time.strftime("%X")<'15:50:00':
        ph.append('<@%s>'%ctx.author.id)
    else:
        await ctx.send('Сорі, але уроку ще нема.')
@client.command()
async def pk(ctx):
    global ph
    global pa
    global pa1
    global pa2
    global n  
    if time.strftime("%a")=='Tue'and time.strftime("%X")>'08:44:00'and time.strftime("%X")<'09:31:00':
        n = list(set(pa) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
            time.sleep(1)
    elif time.strftime("%a")=='Mon'and time.strftime("%X")>'09:50:00'and time.strftime("%X")<'10:35:00':
        n = list(set(pa2) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
    elif time.strftime("%a")=='Mon'and time.strftime("%X")>'10:55:00'and time.strftime("%X")<'11:40:00':
        n = list(set(pa2) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
    elif time.strftime("%a")=='Mon' and time.strftime("%X")>'12:00:00'and time.strftime("%X")<'12:45:00':
        n = list(set(pa1) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
    elif time.strftime("%a")=='Mon' and time.strftime("%X")>'13:05:00'and time.strftime("%X")<'13:50:00':
        n = list(set(pa1) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
    elif time.strftime("%a")=='Fri' and time.strftime("%X")>'08:44:00'and time.strftime("%X")<'09:31:00':
        n = list(set(pa) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
            time.sleep(1)
    elif time.strftime("%a")=='Fri' and time.strftime("%X")>'09:50:00'and time.strftime("%X")<'10:35:00':
        n = list(set(pa) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
            time.sleep(1)
    elif time.strftime("%a")=='Thu' and time.strftime("%X")>'12:00:00'and time.strftime("%X")<'12:45:00':
        n = list(set(pa2) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
    elif time.strftime("%a")=='Thu' and time.strftime("%X")>'15:05:00'and time.strftime("%X")<'15:50:00':
        n = list(set(pa1) ^ set(ph))
        k=len(n)  
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
    else:
        await ctx.send('Сорі, але уроку ще нема.')
@client.command()
async def pn(ctx):
    global ph
    global pa
    global pa1
    global pa2
    global n 
    n = list(set(pa1) ^ set(ph))
    k=len(n) 
    if ph!=[]:
        ph=[]
        for i in range(0, k):
            await ctx.send(n[0])
            del n[0]
    elif ph==[]:
        await ctx.send('Сорі, але уроку ще нема.')

@client.command()
async def v(ctx, a1: discord.Member, a2):
    global vh
    global ph
    print(ph+';')
    if ph!=[]:
        print('first if complete')
        if str(ctx.author.id) == '428159463002734595' or str(ctx.author.id) == '752538068938129458' or str(ctx.author.id) == '752467669831123054':
            vh.append(str(a1) + ' надано відмітку ' + a2)
            await ctx.send(str(a1) + ' надано відмітку ' + a2)
        elif a2=='ba' and str(ctx.author.id) == '428159463002734595':
            role=ctx.guild.get_role(823463203186671657)
            await a1.add_roles(role)
    elif ph==[]:
        print('first elif complete')
        await ctx.send('Сорі, але уроку ще нема.')
    


@client.command()
async def va(ctx):
        global vh
        k = len(vh)
        for i in range(0, k):
            await ctx.send(vh[0])
            del vh[0]
            time.sleep(1)
@client.command()
async def c(ctx):
        global vh
        global ph
        ph=[]
        vh=[]
        print(ph)
        print(vh)
        await ctx.send('Дані були знищені.')


#https://discord.com/api/oauth2/authorize?client_id=842673765572804628&permissions=8&scope=bot
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='ARK: Survival Evolved'))


client.run('ODA2ODkxMDg0ODg1MjYyMzM2.YBwB4Q.v9LWyQKfXdp2VSXhws_OWHFve9o')
