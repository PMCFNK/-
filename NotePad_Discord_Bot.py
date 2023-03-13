import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='NP!')

front_command = "NP!"

user_input = ""
user_output = ""
check_number = 0

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("메모장에 메모하는중 [NP!명령어] [성빈#2621]"))

@bot.command()
async def 명령어(ctx):
    await ctx.send(embed = discord.Embed(title='메모장 명령어',description="""
\nNP!메모 [내용을 저장할 단어] [메모내용] -> 해당 단어에 메모내용을 저장합니다.
\nNP!출력 [내용을 저장한 단어] -> 해당단어에 저장한 메모내용을 불러오고 출력합니다.""", color = 0xFFFFFF))

@bot.command()
async def 메모(ctx, arg1, arg2):
    global check_number
    temp_f = open("user.txt","r")
    datafile = temp_f.readlines()
    if len(datafile) == 0:
        temp_f.close()
        temp_f = open("user.txt","w")
        temp_f.write(ctx.author.name + " " + str(arg1) + " " + str(arg2) +"\n")
        await ctx.send("해당 메모를 저장했어요! :D")
    else:
        for i in range(len(datafile)):
            if arg1 in datafile[i]:
                temp_f.close()
                temp_f = open("user.txt","w")
                datafile[i] = ctx.author.name + " " + str(arg1) + " " + str(arg2) +"\n"
                temp_f.write('\n'.join(datafile))
                await ctx.send("이미 "+str(arg1)+" 관련 입력이 있어서 지금 입력으로 바꿨어요!")
                check_number = 1
                break
    
    if check_number == 0:
        temp_f = open("user.txt","w")
        temp_f.write(ctx.author.name + " " + str(arg1) + " " + str(arg2) +"\n")
        await ctx.send("해당 메모를 저장했어요! :D")
    
    check_number = 0
    temp_f.close()



@bot.command()
async def 출력(ctx, arg1):
    global check_number
    temp_f = open("user.txt","r")
    datafile = temp_f.readlines()
    if len(datafile) == 0:
        await ctx.channel.send("아직 등록된게 없어요! 첫번째로 등록해보세요 :D")
    else:
        for i in range(len(datafile)):
            if arg1 in datafile[i]:
                info = datafile[i].split()
                msg = await ctx.send(str(info[2]))
                await msg.reply(str(info[0]) + " " + "님이 해당 메모를 작성해주셨어요! :D")
                check_number = 1
                break

    if check_number == 0:
        await ctx.channel.send("아직 등록된게 없어요! 첫번째로 등록해보세요 :D")

    check_number = 0

bot.run('')
