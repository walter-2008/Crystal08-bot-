import discord
from discord.ext import commands
import asyncio
TOKEN = "1330383511051304970"
PREFIX = "."
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} ha iniciado sesión")
@bot.command(name="clear")
async def clear(ctx, cantidad: int):
    if cantidad <= 1000:
        await ctx.channel.purge(limit=cantidad + 1)
        await ctx.send(f"Se han eliminado {cantidad} mensajes")
    else:
        await ctx.send(
            "La cantidad de mensajes a eliminar no puede ser mayor a 1000")
@bot.command(name="ban")
async def ban(ctx, usuario: discord.Member, *, razon: str):
    await usuario.ban(reason=razon)
    await ctx.send(f"{usuario.mention} ha sido baneado")
@bot.command(name="kick")
async def kick(ctx, usuario: discord.Member, *, razon: str):
    await usuario.kick(reason=razon)
    await ctx.send(f"{usuario.mention} ha sido expulsado")
@bot.command(name="mute")
async def mute(ctx, usuario: discord.Member, tiempo: str):
    tiempo = tiempo.lower()
    if tiempo == "1m":
        await ctx.guild.create_role(
            name=f"Mute-{usuario.id}",
            permissions=discord.Permissions(send_messages=False))
        await usuario.add_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await asyncio.sleep(60)
        await usuario.remove_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await ctx.guild.delete_role(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
    elif tiempo == "4m":
        await ctx.guild.create_role(
            name=f"Mute-{usuario.id}",
            permissions=discord.Permissions(send_messages=False))
        await usuario.add_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await asyncio.sleep(240)
        await usuario.remove_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await ctx.guild.delete_role(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
    elif tiempo == "10m":
        await ctx.guild.create_role(
            name=f"Mute-{usuario.id}",
            permissions=discord.Permissions(send_messages=False))
        await usuario.add_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await asyncio.sleep(600)
        await usuario.remove_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await ctx.guild.delete_role(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
    elif tiempo == "1h":
        await ctx.guild.create_role(
            name=f"Mute-{usuario.id}",
            permissions=discord.Permissions(send_messages=False))
        await usuario.add_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await asyncio.sleep(3600)
        await usuario.remove_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await ctx.guild.delete_role(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
    elif tiempo == "1d":
        await ctx.guild.create_role(
            name=f"Mute-{usuario.id}",
            permissions=discord.Permissions(send_messages=False))
        await usuario.add_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await asyncio.sleep(86400)
        await usuario.remove_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await ctx.guild.delete_role(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
    elif tiempo == "1s":
        await ctx.guild.create_role(
            name=f"Mute-{usuario.id}",
            permissions=discord.Permissions(send_messages=False))
        await usuario.add_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await asyncio.sleep(604800)
        await usuario.remove_roles(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
        await ctx.guild.delete_role(
            discord.utils.get(ctx.guild.roles, name=f"Mute-{usuario.id}"))
@bot.command(name="crear-canal")
async def crear_canal(ctx, nombre_canal: str, tipo_canal: str):
    if tipo_canal.lower() == "texto":
        await ctx.guild.create_text_channel(nombre_canal)
        await ctx.send(f"Se ha creado el canal de texto {nombre_canal}")
    elif tipo_canal.lower() == "voz":
        await ctx.guild.create_voice_channel(nombre_canal)
        await ctx.send(f"Se ha creado el canal de voz {nombre_canal}")
    else:
        await ctx.send(
            "Tipo de canal inválido. Por favor, ingrese 'texto' o 'voz'")
