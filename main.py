import asyncio
import interactions
from interactions.models.internal.context import SlashContext
from interactions import SlashContext, OptionType, slash_option
import discord
import random
import os
from interactions import Client, Intents
from interactions.ext import prefixed_commands
from interactions.ext.prefixed_commands import prefixed_command, PrefixedContext
from discord.ext import commands
from discord import app_commands
from discord.ext import commands, tasks
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.presences = True
intents.members = True

keep_alive()

my_secret = os.environ['botToken']
BOT_TOKEN = my_secret
CHANNEL_ID = 1250160769400569948

bot = commands.Bot(command_prefix="a.",intents=discord.Intents.all())

Stars = {
    "Carina Nebula" : ["Stars/Carina Nebula-1.jpeg","Stars/Carina Nebula-2.jpeg","Stars/Carina Nebula-3.jpeg","Stars/Carina Nebula-4.jpeg","Stars/Carina Nebula-5.jpeg","Stars/Carina Nebula-6.jpeg","Stars/Carina Nebula-7.jpeg","Stars/Carina Nebula-8.jpeg","Stars/Carina Nebula-9.jpeg","Stars/Carina Nebula-0.jpeg"],
    "NGC 1333" : ["Stars/NGC 1333-1.jpeg","Stars/NGC 1333-2.jpeg","Stars/NGC 1333-3.jpeg","Stars/NGC 1333-4.jpeg","Stars/NGC 1333-5.jpeg","Stars/NGC 1333-6.jpeg","Stars/NGC 1333-7.jpeg","Stars/NGC 1333-8.jpeg","Stars/NGC 1333-9.jpeg","Stars/NGC 1333-0.jpeg"],
    "TW Hya" : ["Stars/TW Hya-1.jpeg","Stars/TW Hya-2.jpeg","Stars/TW Hya-3.jpeg","Stars/TW Hya-4.jpeg","Stars/TW Hya-5.jpeg","Stars/TW Hya-6.jpeg","Stars/TW Hya-7.jpeg","Stars/TW Hya-8.jpeg","Stars/TW Hya-9.jpeg","Stars/TW Hya-0.jpeg"],
    "HH 7-11" : ["Stars/HH 7-11-1.jpeg","Stars/HH 7-11-2.jpeg","Stars/HH 7-11-3.jpeg","Stars/HH 7-11-4.jpeg","Stars/HH 7-11-5.jpeg","Stars/HH 7-11-6.jpeg","Stars/HH 7-11-7.jpeg","Stars/HH 7-11-8.jpeg","Stars/HH 7-11-9.jpeg","Stars/HH 7-11-0.jpeg"],
    "AB Aurigae" : ["Stars/AB Aurigae-1.jpeg","Stars/AB Aurigae-2.jpeg","Stars/AB Aurigae-3.jpeg","Stars/AB Aurigae-4.jpeg","Stars/AB Aurigae-5.jpeg","Stars/AB Aurigae-6.jpeg","Stars/AB Aurigae-7.jpeg","Stars/AB Aurigae-8.jpeg","Stars/AB Aurigae-9.jpeg","Stars/AB Aurigae-0.jpeg"],
    "HD 169142" : ["Stars/HD 169142-1.jpeg","Stars/HD 169142-2.jpeg","Stars/HD 169142-3.jpeg","Stars/HD 169142-4.jpeg","Stars/HD 169142-5.jpeg","Stars/HD 169142-6.jpeg","Stars/HD 169142-7.jpeg","Stars/HD 169142-8.jpeg","Stars/HD 169142-9.jpeg","Stars/HD 169142-0.jpeg"],
    "Luhman 16" : ["Stars/Luhman 16-1.jpeg","Stars/Luhman 16-2.jpeg","Stars/Luhman 16-3.jpeg","Stars/Luhman 16-4.jpeg","Stars/Luhman 16-5.jpeg","Stars/Luhman 16-6.jpeg","Stars/Luhman 16-7.jpeg","Stars/Luhman 16-8.jpeg","Stars/Luhman 16-9.jpeg","Stars/Luhman 16-0.jpeg"],
    "V830 Tau b" : ["Stars/V830 Tau b-1.jpeg","Stars/V830 Tau b-2.jpeg","Stars/V830 Tau b-3.jpeg","Stars/V830 Tau b-4.jpeg","Stars/V830 Tau b-5.jpeg","Stars/V830 Tau b-6.jpeg","Stars/V830 Tau b-7.jpeg","Stars/V830 Tau b-8.jpeg","Stars/V830 Tau b-9.jpeg","Stars/V830 Tau b-0.jpeg"],
    "V 1298 Tau b" : ["Stars/V 1298 Tau b-1.jpeg","Stars/V 1298 Tau b-2.jpeg","Stars/V 1298 Tau b-3.jpeg","Stars/V 1298 Tau b-4.jpeg","Stars/V 1298 Tau b-5.jpeg","Stars/V 1298 Tau b-6.jpeg","Stars/V 1298 Tau b-7.jpeg","Stars/V 1298 Tau b-8.jpeg","Stars/V 1298 Tau b-9.jpeg","Stars/V 1298 Tau b-0.jpeg"],
    "WASP-18b" : ["Stars/WASP-18b-1.jpeg","Stars/WASP-18b-2.jpeg","Stars/WASP-18b-3.jpeg","Stars/WASP-18b-4.jpeg","Stars/WASP-18b-5.jpeg","Stars/WASP-18b-6.jpeg","Stars/WASP-18b-7.jpeg","Stars/WASP-18b-8.jpeg","Stars/WASP-18b-9.jpeg","Stars/WASP-18b-0.jpeg"],
    "WASP-39b" : ["Stars/WASP-39b-1.jpeg","Stars/WASP-39b-2.jpeg","Stars/WASP-39b-3.jpeg","Stars/WASP-39b-4.jpeg","Stars/WASP-39b-5.jpeg","Stars/WASP-39b-6.jpeg","Stars/WASP-39b-7.jpeg","Stars/WASP-39b-8.jpeg","Stars/WASP-39b-9.jpeg","Stars/WASP-39b-0.jpeg"],
    "WASP-43b" : ["Stars/WASP-43b-1.jpeg","Stars/WASP-43b-2.jpeg","Stars/WASP-43b-3.jpeg","Stars/WASP-43b-4.jpeg","Stars/WASP-43b-5.jpeg","Stars/WASP-43b-6.jpeg","Stars/WASP-43b-7.jpeg","Stars/WASP-43b-8.jpeg","Stars/WASP-43b-9.jpeg","Stars/WASP-43b-0.jpeg"],
    "HR 8799" : ["Stars/HR 8799-1.jpeg","Stars/HR 8799-2.jpeg","Stars/HR 8799-3.jpeg","Stars/HR 8799-4.jpeg","Stars/HR 8799-5.jpeg","Stars/HR 8799-6.jpeg","Stars/HR 8799-7.jpeg","Stars/HR 8799-8.jpeg","Stars/HR 8799-9.jpeg","Stars/HR 8799-0.jpeg"],
    "Beta Pictoris" : ["Stars/Beta Pictoris-1.jpeg","Stars/Beta Pictoris-2.jpeg","Stars/Beta Pictoris-3.jpeg","Stars/Beta Pictoris-4.jpeg","Stars/Beta Pictoris-5.jpeg","Stars/Beta Pictoris-6.jpeg","Stars/Beta Pictoris-7.jpeg","Stars/Beta Pictoris-8.jpeg","Stars/Beta Pictoris-9.jpeg","Stars/Beta Pictoris-0.jpeg"],
    "2M 1207" : ["Stars/2M 1207-1.jpeg","Stars/2M 1207-2.jpeg","Stars/2M 1207-3.jpeg","Stars/2M 1207-4.jpeg","Stars/2M 1207-5.jpeg","Stars/2M 1207-6.jpeg","Stars/2M 1207-7.jpeg","Stars/2M 1207-8.jpeg","Stars/2M 1207-9.jpeg","Stars/2M 1207-0.jpeg"],
    "TRAPPIST-1" : ["Stars/TRAPPIST-1-1.jpeg","Stars/TRAPPIST-1-2.jpeg","Stars/TRAPPIST-1-3.jpeg","Stars/TRAPPIST-1-4.jpeg","Stars/TRAPPIST-1-5.jpeg","Stars/TRAPPIST-1-6.jpeg","Stars/TRAPPIST-1-7.jpeg","Stars/TRAPPIST-1-8.jpeg","Stars/TRAPPIST-1-9.jpeg","Stars/TRAPPIST-1-0.jpeg"]
}
StarsDictionary = {
    "Carina-Nebula" : "https://en.wikipedia.org/wiki/Carina_Nebula",
    "NGC-1333" : "https://en.wikipedia.org/wiki/NGC_1333",
    "TW-Hya" : "https://en.wikipedia.org/wiki/TW_Hydrae",
    "HH 7-11" : "https://en.wikipedia.org/wiki/HH_7-11",
    "AB Aurigae" : "https://en.wikipedia.org/wiki/AB_Aurigae",
    "HD 169142" : "https://en.wikipedia.org/wiki/HD_169142",
    "Luhman 16" : "https://en.wikipedia.org/wiki/Luhman_16",
    "V830 Tau b" : "https://en.wikipedia.org/wiki/V830_Tau_b",
    "V 1298 Tau b" : "https://en.wikipedia.org/wiki/V_1298_Tau_b",
    "WASP-18b" : "https://en.wikipedia.org/wiki/WASP-18b",
    "WASP-39b" : "https://en.wikipedia.org/wiki/WASP-39b",
    "WASP-43b" : "https://en.wikipedia.org/wiki/WASP-43b",
    "HR 8799" : "https://en.wikipedia.org/wiki/HR_8799",
    "Beta Pictoris" : "https://en.wikipedia.org/wiki/Beta_Pictoris",
    "2M 1207" : "https://en.wikipedia.org/wiki/2M_1207",
    "TRAPPIST-1" : "https://en.wikipedia.org/wiki/TRAPPIST-1"
}
CorrectStar = {}
WorkInProgress = {
    "HH 7-11" : "",
    "AB Aurigae" : "",
    "HD 169142" : "",
    "Luhman 16" : "",
    "V830 Tau b" : "",
    "V 1298 Tau b" : "",
    "WASP-18b" : "",
    "WASP-39b" : "",
    "WASP-43b" : "",
    "HR 8799" : "",
    "Beta Pictoris" : "",
    "2M 1207" : "",
    "TRAPPIST-1" : ""
}
WorkInProgressDictionary = {
    "HH 7-11" : "",
    "AB Aurigae" : "",
    "HD 169142" : "",
    "Luhman 16" : "",
    "V830 Tau b" : "",
    "V 1298 Tau b" : "",
    "WASP-18b" : "",
    "WASP-39b" : "",
    "WASP-43b" : "",
    "HR 8799" : "",
    "Beta Pictoris" : "",
    "2M 1207" : "",
    "TRAPPIST-1" : ""
}

def find_key_in_dict(search_string, dictionary):
    if search_string in dictionary:
        return (search_string, dictionary[search_string])
    else:
        return None
        
@bot.event
async def on_ready():
    print("Astro ID Bot is working!")
    update_status.start()

@tasks.loop(seconds=5)  # Check every 5 seconds
async def update_status():
    user_id = 1156385983781154817  # Replace with the actual user ID
    member = None

    for guild in bot.guilds:
        member = guild.get_member(user_id)
        if member:
            break

    if not member:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Nothing"))
        return

    for activity in member.activities:
        if isinstance(activity, discord.Spotify):
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{activity.title} by {activity.artist}"))
            return

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Shiven Patel"))

@bot.command()
async def apollo(ctx):
    await ctx.send("# Apollo Manual:\nTo ask for an image, type a.i \nTo answer, type a.a [insert answer here]. Make sure to add dashes between spaces \nTo skip, type a.s\nTo get a new image of the insect, use a.p \nTo ask for a hint, use a.h and specify if you want the number of letters, the first letter, or the last letter\nTo ask for the list avaliable in the bot, use a.l \nHave fun! \n")

@bot.command()
async def h(ctx, hint):
    if hint == "counts":
        countsStar = len(CorrectStar[ctx.author.id])
        await ctx.send(f"The number of letters is **{countsStar}**.")
    elif hint == "first":
        firstletterStar = CorrectStar[ctx.author.id][0]
        await ctx.send(f"The first letter is **{firstletterStar}**.")
    elif hint == "last":
        lastletterStar = CorrectStar[ctx.author.id][-1]
        await ctx.send(f"The last letter is **{lastletterStar}**.")
    else:
        await ctx.send("Invalid hint. Please use 'counts', 'first', or 'last'.")

@bot.command()
async def i(ctx):
    global randomImage
    global randomStar
    randomStar, randomImage = random.choice(list(Stars.items()))
    CorrectStar[ctx.author.id] = randomStar.lower()
    await ctx.send("**Here is your image:**")
    await ctx.send(file=discord.File(random.choice(randomImage)))

@bot.command()
async def p(ctx):
    global randomImage
    await ctx.send("**Sure, here is another image:**")
    await ctx.send(file=discord.File(random.choice(randomImage)))
"""user_id = ctx.author.id
user_stats = {user_id: {"correct": 0, "incorrect": 0}}"""
@bot.command()
async def a(ctx, answer):
    if ctx.author.id in CorrectStar:
        correct_answerStar = CorrectStar[ctx.author.id]
        if answer == correct_answerStar:
            result = find_key_in_dict(randomStar, StarsDictionary)
            key, value = result
            await ctx.send(f"Correct! The answer was **{correct_answerStar.upper()}**! Here is the link to the Star: {value}")
            """if ctx.author.id in user_stats:
                user_stats[ctx.author.id]["correct"] += 1
            else:
                user_stats[ctx.author.id] = {"correct": 1, "incorrect": 0}"""
        else:
            result = find_key_in_dict(randomStar, StarsDictionary)
            key, value = result
            await ctx.send(f"Incorrect. The answer was **{correct_answerStar.upper()}**! Here is the link to the star: {value}")
            # if ctx.author.id in user_stats:
                # user_stats[ctx.author.id]["incorrect"] += 1
            # else:
                # user_stats[ctx.author.id] = {"correct": 0, "incorrect": 1}
        del CorrectStar[ctx.author.id]  
    else:
        await ctx.send("You have not asked for an image yet.")

"""@bot.command()
async def progress(ctx):
    correct_count = user_stats[ctx.author.id]["correct"]
    incorrect_count = user_stats[ctx.author.id]["incorrect"]
    await ctx.send(f"You have identified {correct_count} stars correctly and {incorrect_count} incorrectly.")"""

@bot.command()
async def s(ctx):
    AnswerStar = CorrectStar[ctx.author.id]
    result = find_key_in_dict(randomStar, StarsDictionary)
    key, value = result
    await ctx.send(f"Skipped! The answer was **{AnswerStar.upper()}**! Here is the link to the star: {value}")
    del CorrectStar[ctx.author.id]

@bot.command()
async def l(ctx):
    await ctx.send("**Here are the stars:**")
    await ctx.send(f"\nCarina Nebula\nNGC 1333\nTW Hya\nHH 7-11\nAB Aurigae\nHD 169142\nLuhman 16\nV830 Tau b\nV 1298 Tau b\nWASP-18b\nWASP-39b\nWASP-43b\nHR 8799\nBeta Pictoris\n2M 1207\nTRAPPIST-1")

@bot.command()
async def star(ctx, *, askedStar):
    if askedStar in Stars:
        result = find_key_in_dict(askedStar, Stars)
        key, value = result
        randomStarImage = random.choice(value)
        await ctx.send(f"Here is a picture of the star: ", file=discord.File(randomStarImage))
    else:
        await ctx.send("Invalid star. Please use one of the following stars: Carina Nebula, NGC 1333, TW Hya, HH 7-11, AB Aurigae, HD 169142, Luhman 16, V830 Tau b, V 1298 Tau b, WASP-18b, WASP-39b, WASP-43b, HR 8799, Beta Pictoris, 2M 1207, TRAPPIST-1")


bot.run(BOT_TOKEN)
