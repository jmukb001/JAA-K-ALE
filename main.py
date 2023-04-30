# testing.py
import os
import random
import discord
from discord import Embed
import Pet

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

pet = Pet.Pet()
x = -1


intents = discord.Intents.all() #discord.py has changed
intents.members = True # Subscribe to the privileged members intent.
bot = commands.Bot(command_prefix='t!', intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

    channel = guild.system_channel

    # Create an embed object for the welcome message
    embed = Embed(
        title="Tamabotchi - A Virtual Pet.. In a Virtual World",
        description="\n\nThe beginning of a new...\n\nGet started with your Tamabotchi by typing in the command **t!choose**\n\nTo see a list of a commands, type the command **t!commands**`",
        color=0xe09cff,
    )
    embed.set_thumbnail(
       url="https://i.pinimg.com/originals/77/37/e2/7737e26e01ee102e8d76727d87714c6e.png"
    )
    await channel.send(embed=embed)

@bot.command(name='pet')
async def pet_command(ctx):
    await ctx.send("Display Pet")


@bot.command(name='RPS')
async def play_game(ctx):
   
    # Get the channel from the context
    channel = ctx.channel

    # Create an embed object with information about a game of rock-paper-scissors
    embed = Embed(
        title="Rock, Paper, Scissors!",
        description="Play a game of rock-paper-scissors against the user",
        color=0xf0f0f0,
    )
    embed.set_thumbnail(
        url="https://media.istockphoto.com/id/1056840214/vector/rock-paper-scissors-vector-illustration.jpg?s=612x612&w=0&k=20&c=6KEBfon5f9BXXhLiu9JfOk6EHsM193SiWMcqDjN1jqM="
    )

    # Send the message with the embed
    await channel.send(content="", tts=False, embed=embed)


    options = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(options)
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in options
    
    await ctx.send("Enter 'rock', 'paper', or 'scissors': ")

    user_choice = await bot.wait_for('message', check=check)
    user_choice = user_choice.content.lower()
    
    await ctx.send("Bot is thinking. . .")
    await ctx.send(f"Bot chooses {bot_choice}")
    
    if user_choice == bot_choice:
        await ctx.send("It's a tie!")
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        #images\MONTY-HAPPY.png
        file = discord.File("MONTY-HAPPY.png")
        await ctx.send(file=file)
        await ctx.send("You win!")
    else:
        file = discord.File("MONTY-MAD.png")
        await ctx.send(file=file)
        await ctx.send("Bot wins!")


@bot.command(name='HoL')
async def play_H_L(ctx):

#=====================================
    channel = ctx.channel
    embed = Embed(
        title= "Higher or Lower",
        description= "I'm thinking of a number. You guess a number, and I'll tell you if the number is higher or lower, until you guess the number\n\nYou have 10 tries. Let's play!",
        color= 0x36cb4a,
    )

    embed.set_thumbnail(
        url="https://media.discordapp.net/attachments/1101918931222008010/1102120728536567868/Untitled_Artwork.png?width=1024&height=1024"
    )
    await channel.send(content="", tts=False, embed=embed)
#=====================================

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
            file = discord.File("MONTY-MAD.png")
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
            file = discord.File("MONTY-HAPPY.png")
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
        
@bot.command(name='choose')
async def choose_pet(ctx):

    #=====================================
    channel = ctx.channel
    embed = Embed(
        title= "Choose your server's Tamagotchi!",
        description= "You can choose between Monty the Dog and Frankie the Axolotl!\n this your new baby, treat it well \u2661",
        color= 0xe09cff,
    )

    await channel.send(content="", tts=False, embed=embed)
    #=====================================

    await ctx.send("Select either Monty (0) or Frankie (1)")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdigit()
    user_choice = await bot.wait_for('message', check=check)
    user_input = int(user_choice.content)
    
    pet_name = ""
    if user_input == 0:
        pet_name = "Monty"
    elif user_input == 1:
        user_input == 'Axolotl'
        pet_name = "Frankie"
        
    
    pet.setName(pet_name)
    pet.setType(user_input)

    
    await ctx.send("Your pet " + pet.name + " says hi!")
    file = discord.File(pet.sprites[pet.type][0])
    await ctx.send(file=file)
    
@bot.command(name='commands')
async def rightdirection_command(ctx):
    help_embed = discord.Embed(title='List of Commands', description='Here are the available commands for your pet:')
    help_embed.add_field(name='t!RPS', value='Play Rock, Paper, Scissors with your pet', inline=False)
    help_embed.add_field(name='t!HoL', value='Play Higher or Lower game with your pet', inline=False)
    help_embed.add_field(name='t!slots', value='Play Slots with your pet', inline=False)
    help_embed.add_field(name='t!pet', value='Interact with your virtual pet', inline=False)
    help_embed.add_field(name='t!feed', value='Feed your virtual pet', inline=False)
    help_embed.add_field(name='t!sleep', value='Put your virtual pet to sleep', inline=False)

    await ctx.send(embed=help_embed)

bot.run(TOKEN)
