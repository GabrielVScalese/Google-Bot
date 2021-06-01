import discord
from discord.ext import commands, tasks
import os
from keep_alive import keep_alive
import datetime
import pytz

from Google import Google
from Covid import Covid
from Cases import Cases

client = commands.Bot(command_prefix='!g')

channel_id = 829726928474472469 # noticias's channel

tz = pytz.timezone('America/Sao_Paulo')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('!gcommands'))
  print('Bot is ready!')

@client.command()
async def commands(ctx):
  embed=discord.Embed(title="Commands", description="Here there are all commands",color=0xFF5733)

  embed.set_author(name='Adama', icon_url='https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=w300-rw')

  embed.add_field(name="!gcommands", value="The bot shows all commands", inline=False)

  # embed.add_field(name="!gs_news", value="The bot researches news from your search", inline=False)

  embed.add_field(name="!ganswers", value="The bot researches answers from your search", inline=False)

  embed.add_field(name="!gimages", value="The bot researches images from your search", inline=False)

  embed.add_field(name="!gcovid", value="The bot researches Covid-19 statistics from country", inline=False)

  embed.set_footer(text='by gabriel s', icon_url='https://pbs.twimg.com/profile_images/1316750214/evandro_400x400.jpg')

  await ctx.send(embed=embed)

@client.command()
async def answers (ctx, num, *args):
  search = " ".join(args[:])

  try:
    search_num = int(num)
  except:
    await ctx.send('**❗  Invalid number of search, canceled request**')
    return

  await ctx.send(f'**🔎  Searching {search_num} answers: {search}**')

  answers = Google.get_answers(search, search_num)

  await ctx.send(f'**🆗  Found {len(answers)} answers**')

  if len(answers) == 0:
    await ctx.send('**🔎 Nothing found ** ')

  for answer in answers:
    embed = discord.Embed(title=answer.get_title(), url=answer.get_link(),description=answer.get_snippet(),color=0xFF5733)

    await ctx.send(embed=embed)

@client.command()
async def images (ctx, num, *args):
  search = " ".join(args[:])

  try:
    search_num = int(num)
  except:
    await ctx.send('**❗  Invalid number of search, canceled request**')
    return
  
  if search_num > 10:
    await ctx.send('**❗  Invalid number of search (the number must be less than 10), canceled request**')
    return

  await ctx.send(f'**🔎  Searching {search_num} images: {search}**')

  images = Google.get_images(search, search_num)

  await ctx.send(f'**🆗  Found {len(images)} images**')

  if len(images) == 0:
    await ctx.send('**🔎 Nothing found ** ')

  for image in images:
    await ctx.send(image)

# @client.command()
# async def covid (ctx, *args):
#   country = " ".join(args[:])

#   country = country.capitalize()

#   if " " in country:
#     first_name = country.split(' ')[0]
#     last_name = country.split(' ')[1].capitalize()
#     country = f'{first_name} {last_name}'

#   await ctx.send(f'**🔎  Searching Covid-19 statistics in {country}**')

#   country_cases = Covid.get_cases(country)

#   await ctx.send(f'**🆗  Found Covid-19 statistics**')

#   if country_cases == None:
#     await ctx.send('**❗  Not found country, canceled request**')
#     return

#   embed = discord.Embed(title=country, color=0xFF5733)

#   embed.set_thumbnail(url=country_cases.get_flag())

#   embed.add_field(name='Capital', value=country_cases.get_capital(), inline=True)

#   embed.add_field(name='Continent', value=country_cases.get_continent(), inline=True)

#   embed.add_field(name='Population', value=country_cases.get_population(), inline=True)

#   embed.add_field(name='Confirmed', value=country_cases.get_confirmed(), inline=True)

#   embed.add_field(name='Recovered', value=country_cases.get_recovered(), inline=True)

#   embed.add_field(name='Deaths', value=country_cases.get_deaths(), inline=True)

#   embed.add_field(name='Life expectancy', value=country_cases.get_life_expectancy(), inline=True)

#   await ctx.send(embed=embed)


@tasks.loop(hours=1)
async def called_once_a_day():
  now = datetime.datetime.now(tz)
  br_news = Google.get_news(now, "br")
  us_news = Google.get_news(now, "us")

  news = []
  news.extend(us_news)
  news.extend(br_news)

  channel = client.get_channel(channel_id)

  print(news)

  for i in range(0, 3):
    if i > len(news) - 1:
      return

    print(news[i]['title'])
    embed = discord.Embed(title=news[i]['title'], url=news[i]['url'],description=news[i]['description'],color=0xFF5733)

    i = i + 1

    await channel.send(embed=embed)
    
@called_once_a_day.before_loop
async def before():
  await client.wait_until_ready()

called_once_a_day.start()
keep_alive() 
client.run(os.getenv('TOKEN'))