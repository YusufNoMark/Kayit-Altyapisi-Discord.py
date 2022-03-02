import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():

  print("Ben Ok")
  

  
@client.event
async def on_member_join(member):
  guild = member.guild
  kayıtsızrol = discord.utils.get(guild.roles, name="KAYITSIZ") #üye geldiğinde verilecek rol KAYITSIZ kısmına yazmalısın.
  await member.add_roles(kayıtsızrol)
  channel = discord.utils.get(member.guild.text_channels, name="kayıt") # KANAL ADI kısmına kanalın adını giriniz.
  await channel.send(f"Yeni Bir Üye Geldi!, Hoş Geldin {member.mention}")
  

@client.command()
@commands.has_role("YAZ") # bu kısma hangi rolün bu komutu kullanabileceğini yazınız
async def kayıt(ctx, member: discord.Member, nick):
  guild = ctx.guild
  kayıtlırol = discord.utils.get(guild.roles, name="KAYITLI")
  kayıtsızrol = discord.utils.get(guild.roles, name="KAYITSIZ") # üye kayıt olduğun verilecek rolü KAYITLI kısmına yazmalısın. 
  await member.add_roles(kayıtlırol)
  await member.remove_roles(kayıtsızrol)
  await member.edit(nick=f"{nick}") # kullanıcının belirlenen adını değişir.
  await ctx.channel.send("Kayıt Başarılı!!")
  
  
  
client.run("TOKEN")
