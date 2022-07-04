import random
import time

def rcp():
    a = random.randint(0, 2)
    return a


async def 가위(ctx):
    a = rcp()
    if a == 0:
        await ctx.channel.send("BB는 가위를 냈습니다. 비겼습니다.")
    elif a == 1:
        await ctx.channel.send("BB는 바위를 냈습니다. 졌습니다.")
    else:
        await ctx.channel.send("BB는 보를 냈습니다. 이겼습니다. ")
    await print(time.ctime(), 가위.__name__)

async def 바위(ctx):
    a = rcp()
    if a == 0:
        await ctx.channel.send("BB는 가위를 냈습니다. 이겼습니다.")
    elif a == 1:
        await ctx.channel.send("BB는 바위를 냈습니다. 비겼습니다.")
    else:
        await ctx.channel.send("BB는 보를 냈습니다. 졌습니다. ")
    await print(time.ctime(), 바위.__name__)

async def 보(ctx):
    a = rcp()
    if a == 0:
        await ctx.channel.send("BB는 가위를 냈습니다. 졌습니다.")
    elif a == 1:
        await ctx.channel.send("BB는 바위를 냈습니다. 이겼습니다.")
    else:
        await ctx.channel.send("BB는 보를 냈습니다. 비겼습니다. ")
    await print(time.ctime(), 보.__name__)