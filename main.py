# testing.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.all() #discord.py has changed
intents.members = True # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='t!', intents=intents)
bot.load_extension('RPS')

@bot.event

async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
            
    print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

@bot.command(name='pet')
async def pet_command(ctx):
    await ctx.send("Display Pet")

@bot.command(name='RPS')
async def play_game(ctx):
    """Play a game of rock-paper-scissors against the user"""
    options = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(options)
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in options
    
    await ctx.send("Enter 'rock', 'paper', or 'scissors': ")
    user_choice = await bot.wait_for('message', check=check)
    user_choice = user_choice.content.lower()
    
    await ctx.send(f"Bot chooses {bot_choice}")
    
    if user_choice == bot_choice:
        await ctx.send("It's a tie!")
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        #images\MONTY-HAPPY.png
        file = discord.File("images\MONTY-HAPPY.png")
        await ctx.send(file=file)
        await ctx.send("You win!")
    else:
        file = discord.File("images\MONTY-MAD.png")
        await ctx.send(file=file)
        await ctx.send("Bot wins!")


@bot.command(name='HoL')
async def play_H_L(ctx):
    """Play a game of higher or lower against me!!!!!!!\n"""
    """I'm thinking of a number. You guess a number, and I'll tell you if the number is higher or lower, until you guess the number!!\n"""
    """You have 10 tries. Let's play! \n"""

    secret_number = random.randint(1, 100)

    counter = 0


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()

    await ctx.send("Guess a number: ")
    user_choice = await bot.wait_for('message', check=check)
    user_input = int(user_choice.content)

    print(secret_number) #FIXME


    while secret_number != user_choice:
        if counter == 5:
            file = discord.File("images\MONTY-MAD.png")
            await ctx.send(file=file)
            await ctx.send("You lose. You should study binary search")
            break
        elif user_input > secret_number:
            await ctx.send("Lower.")
            counter = counter + 1
        elif user_input < secret_number:
            await ctx.send("Higher.")
            counter = counter + 1
        else:
            file = discord.File("images\MONTY-HAPPY.png")
            await ctx.send(file=file)
            congrats = "You little genius. You got! It only took you "
            congrats += str(counter)

            if counter == 1:
                congrats += " try!! What are the odds?"
            else:
                congrats += " tries!"

            await ctx.send(congrats)
            break

        await ctx.send("Guess again: \n")

        user_choice = await bot.wait_for('message', check=check)
        user_input = int(user_choice.content)


bot.run(TOKEN)