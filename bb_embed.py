import discord
import asyncio
import time
from discord.ext import commands


async def 도움말(ctx):
    embed = discord.Embed(title="ByunBot", description="Bb 도움말 실험중", color=0x4432a8)
    embed.add_field(name="1. 인사", value=".안녕", inline=False)
    embed.add_field(name="2. 매크로", value=".ggez\n.굴려\n.꽁승\n.주사위굴려\n.탑차이", inline=False)
    embed.add_field(name="3. 채팅청소", value=".clear (삭제, 청소) [숫자](지정된 수 만큼 삭제)", inline=False)
    embed.add_field(name="4. 가위바위보", value=".가위(scissors)\n.바위(rock)\n.보(paper)", inline=False)
    embed.add_field(name="5. etc", value=".죽어\n", inline=False)
    await ctx.channel.send(" ", embed=embed)
    await print(time.ctime(), 도움말.__name__)
