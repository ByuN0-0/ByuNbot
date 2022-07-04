from secrets import token_urlsafe
from click import BadArgumentUsage
from discord.ext import commands
import time
import discord
import asyncio
import bb_rcp
import bb_macro
import bb_embed

bot = commands.Bot(command_prefix='.') #명령어 선입력 '.'
f = open("C:\\Users\\isly7\\Desktop\\Discord_Bot\\bbToken.txt", 'r')    #토큰.txt를 열어서 token 변수에 토큰 입력
token = f.readline()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('test'))      #봇 상태 변경
    print("BB.Client Successfully access\n")
    print("------------------------ below bb.bot Client log ------------------------")    #실행 상태 출력

@bot.event
async def on_message(msg):      #봇의 메세지에 대답하지 않게 하는 함수
    if msg.author.bot:
        return None
    await bot.process_commands(msg)

@bot.command(aliases=['대답'])
async def echo2(ctx, *args):
    parameter = ' '.join(args)
    await ctx.reply(f'echo {parameter}')

# --------------------------------------아래는 매크로, 가위바위보등등 명령어 --------------------------------------
@bot.command(aliases=['?'])
async def 도움말(ctx):
    await bb_embed.도움말(ctx)
@bot.command(aliases=['hi'])
async def 안녕(ctx):
    await bb_macro.안녕(ctx)
@bot.command()
async def 죽어(ctx):
    await bb_macro.죽어(ctx)
@bot.command()
async def 지건(ctx):
    await bb_macro.지건(ctx)
@bot.command()
async def ggez(ctx):
    await bb_macro.ggez(ctx)
@bot.command()
async def 주사위굴려(ctx):
    await bb_macro.주사위굴려(ctx)
@bot.command()
async def 꽁승(ctx):
    await bb_macro.꽁승(ctx)
@bot.command()
async def 굴려(ctx):
    await bb_macro.굴려(ctx)
@bot.command()
async def 탑차이(ctx):
    await bb_macro.탑차이(ctx)
@bot.command(aliases=['scissors'])
async def 가위(ctx):
    await bb_rcp.가위(ctx)
@bot.command(aliases=['rock'])
async def 바위(ctx):
    await bb_rcp.바위(ctx)
@bot.command(aliases=['paper'])
async def 보(ctx):
    await bb_rcp.보(ctx)
# -------------------------------------- 아래는 명령어 예외처리 --------------------------------------

@bot.command(aliases=['청소', '삭제'])
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.channel.send(f"{amount}개의 메세지를 삭제하였습니다.")
    print(time.ctime(),clear.__name__)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.channel.send('없는 명령어야')
        print(time.ctime(),"    didn't find the commands/ err")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.channel.send('숫자를 적어라')
        print(time.ctime(),"    didn't match the parameter/ err")

bot.run(token)
