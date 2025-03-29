import discord
import asyncio
import yt_dlp
ytdl = yt_dlp.YoutubeDL()

TOKEN = 'MTMzMDM4MzUxMTA1MTMwNDk3MA.GceKkL.HEuBUDuHnOI6HxCf653di19TEoVMGfaw07bdQY'
PREFIX = '.'

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = discord.Client(intents=intents)

yt_dlp.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

@client.event
async def on_ready():
    print(f'¡El bot {client.user} está listo!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send('✨¡Hola! Soy Crystal08🤍 y estoy listo para ayudarte. Mi prefijo es "." y prueba ".help" para ver mas opciones.')

    if message.content.startswith(PREFIX):
        command = message.content[len(PREFIX):].strip().split(' ')[0]
        args = message.content.split(' ')[1:]

        if command == 'help':
            help_message = """
            **🛠️Comandos disponibles:**
            `.clear`: Limpia hasta 1000 mensajes.
            `.mute`: Aislar temporalmente a un miembro.
            `.kick`: Expulsa a un miembro del servidor.
            `.ban`: Banea a un miembro del servidor.
            **🔍Otros comandos:**
            `.unmute`: Deshabilita el silencio de un miembro.
            `.unban`: Desbanea a un miembro del servidor.
            **🎵Comandos de música:**
            `.play`: Reproduce una canción.
            `.stop`: Detiene la reproducción de música.
            `.skip`: Salta a la siguiente canción.
            """
            await message.channel.send(help_message)

        elif command == 'clear':
            if message.author.guild_permissions.manage_messages:
                try:
                    amount = int(args[0])
                    if amount > 1000:
                        await message.channel.send('No puedes eliminar más de 1000 mensajes. Elije al menos una cantidad minima de 1000.')
                    else:
                        await message.channel.purge(limit=amount + 1)
                        await message.channel.send(f' 🎉Han sido eliminados {amount} mensajes correctamente.')
                except (ValueError, IndexError):
                    await message.channel.send('Uso: `.clear <cantidad>`\nEjemplo: `.clear 10`')
            else:
                await message.channel.send('⚠️No tienes permiso para usar este comando.')

        elif command == 'mute':
            if message.author.guild_permissions.mute_members:
                try:
                    member = message.mentions[0]
                    duration = args[1].lower()
                    role = discord.utils.get(message.guild.roles, name='Muted')
                    if not role:
                        role = await message.guild.create_role(name='Muted')
                        for channel in message.guild.channels:
                            await channel.set_permissions(role, send_messages=False)
                    await member.add_roles(role)
                    await message.channel.send(f'⚠️{member.mention} ha sido silenciado durante {duration}.')

                    seconds = None

                    if duration == '1 minuto':
                        seconds = 60
                    elif duration == '5 minutos':
                        seconds = 300
                    elif duration == '10 minutos':
                        seconds = 600
                    elif duration == '1 hora':
                        seconds = 3600
                    elif duration == '1 dia':
                        seconds = 86400
                    elif duration == '1 semana':
                        seconds = 604800

                    if seconds:
                        await asyncio.sleep(seconds)
                        await member.remove_roles(role)
                        await message.channel.send(f'✅{member.mention} ha sido des-silenciado.')
                    else:
                        await message.channel.send('Duración no válida. Las opciones son: 1 minuto, 5 minutos, 10 minutos, 1 hora, 1 dia, 1 semana.')

                except (IndexError, discord.errors.Forbidden):
                    await message.channel.send('Uso: `.mute @usuario <duración>`\nDuraciones disponibles: 1 minuto, 5 minutos, 10 minutos, 1 hora, 1 dia, 1 semana.')
            else:
                await message.channel.send('No tienes permiso para usar este comando.')

        elif command == 'unmute':
            if message.author.guild_permissions.mute_members:
                try:
                    member = message.mentions[0]
                    role = discord.utils.get(message.guild.roles, name='Muted')
                    await member.remove_roles(role)
                    await message.channel.send(f'{member.mention} ha sido des-silenciado.')
                except (IndexError, AttributeError):
                    await message.channel.send('Uso: `.unmute @usuario`')
            else:
                await message.channel.send('No tienes permiso para usar este comando.')

        elif command == 'kick':
            if message.author.guild_permissions.kick_members:
                try:
                    member = message.mentions[0]
                    reason = ' '.join(args[1:]) or 'No especificada'
                    await member.kick(reason=reason)
                    await message.channel.send(f'{member.mention} ha sido expulsado. Razón: {reason}')
                except IndexError:
                    await message.channel.send('Uso: `.kick @usuario [razón]`\nEjemplo: `.kick @UsuarioMolesto Spam excesivo`')
                except discord.errors.Forbidden:
                    await message.channel.send('No tengo permiso para expulsar a este usuario.')
            else:
                await message.channel.send('⚠️No tienes permiso para usar este comando.')

        elif command == 'ban':
            if message.author.guild_permissions.ban_members:
                try:
                    member = message.mentions[0]
                    reason = ' '.join(args[1:]) or 'No especificada'
                    await member.ban(reason=reason)
                    await message.channel.send(f'{member.mention} ha sido baneado. Razón: {reason}')
                except IndexError:
                    await message.channel.send('Uso: `.ban @usuario [razón]`\nEjemplo: `.ban @UsuarioMolesto Spam excesivo`')
                except discord.errors.Forbidden:
                    await message.channel.send('No tengo permiso para banear a este usuario.')
            else:
                await message.channel.send('⚠️No tienes permiso para usar este comando.')

        elif command == 'unban':
            if message.author.guild_permissions.ban_members:
                try:
                    banned_users = await message.guild.bans()
                    member_name, member_discriminator = args[0].split('#')

                    for ban_entry in banned_users:
                        user = ban_entry.user

                        if (user.name, user.discriminator) == (member_name, member_discriminator):
                            await message.guild.unban(user)
                            await message.channel.send(f'Desbaneado {user.mention}')
                            return
                    await message.channel.send('No se encontró al usuario baneado.')
                except ValueError:
                    await message.channel.send('Uso: `.unban Usuario#0000`\nEjemplo: `.unban Usuario#1234`')
                except discord.errors.Forbidden:
                    await message.channel.send('No tengo permiso para desbanear usuarios.')
            else:
                await message.channel.send('⚠️No tienes permiso para usar este comando.')

        elif command == 'play':
            if message.author.voice:
                channel = message.author.voice.channel
                try:
                    voice_client = await channel.connect()
                except discord.ClientException:
                    voice_client = client.voice_clients[0]

                if not voice_client:
                    return

                url = args[0]
                try:
                    data = ytdl.extract_info(url, download=False)
                    filename = ytdl.prepare_filename(data)
                except:
                    await message.channel.send('No se pudo reproducir la canción.')
                    return

                voice_client.play(discord.FFmpegPCMAudio(filename, **ffmpeg_options))
                await message.channel.send(f'Reproduciendo: {data["title"]}')
            else:
                await message.channel.send('Debes estar en un canal de voz para usar este comando.')

client.run(TOKEN)            
