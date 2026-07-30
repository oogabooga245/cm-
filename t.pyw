import discord
from discord import app_commands
import platform
import socket
import psutil
import time
import datetime
import logging
import os
import subprocess


# ==========================
# CONFIG
# ==========================

TOKEN = os.getenv("TOKEN")

ADMIN_IDS = [
    708651602860310598
]

START_TIME = time.time()


# ==========================
# LOGGING
# ==========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# ==========================
# BOT SETUP
# ==========================

intents = discord.Intents.default()

client = discord.Client(
    intents=intents
)

tree = app_commands.CommandTree(client)


# ==========================
# HELPERS
# ==========================

def is_admin(user_id):
    return user_id in ADMIN_IDS


def uptime():
    seconds = int(time.time() - START_TIME)

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    return f"{days}d {hours}h {minutes}m {seconds}s"


# ==========================
# EVENTS
# ==========================

@client.event
async def on_ready():

    await tree.sync()

    logging.info(
        f"Logged in as {client.user}"
    )

    print("----------------")
    print("Bot Online")
    print(f"User: {client.user}")
    print(f"ID: {client.user.id}")
    print("----------------")


# ==========================
# COMMANDS
# ==========================


@tree.command(
    name="ping",
    description="Check bot latency"
)
async def ping(interaction: discord.Interaction):

    latency = round(
        client.latency * 1000
    )

    await interaction.response.send_message(
        f"🏓 Pong!\nLatency: {latency}ms"
    )


@tree.command(
    name="status",
    description="Show bot status"
)
async def status(interaction: discord.Interaction):

    if not is_admin(interaction.user.id):
        await interaction.response.send_message(
            "❌ Permission denied",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"""
✅ Bot Status

Online: Yes
Uptime: {uptime()}
Servers: {len(client.guilds)}
Users: {len(client.users)}
"""
    )


@tree.command(
    name="info",
    description="Show system information"
)
async def info(interaction: discord.Interaction):

    if not is_admin(interaction.user.id):
        await interaction.response.send_message(
            "❌ Permission denied",
            ephemeral=True
        )
        return

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()

    embed = discord.Embed(
        title="System Information",
        color=0x00ff99
    )

    embed.add_field(
        name="Hostname",
        value=socket.gethostname(),
        inline=False
    )

    embed.add_field(
        name="Operating System",
        value=platform.platform(),
        inline=False
    )

    embed.add_field(
        name="Python",
        value=platform.python_version()
    )

    embed.add_field(
        name="CPU Usage",
        value=f"{cpu}%"
    )

    embed.add_field(
        name="RAM Usage",
        value=f"{ram.percent}%"
    )

    embed.add_field(
        name="Uptime",
        value=uptime()
    )

    await interaction.response.send_message(
        embed=embed
    )


@tree.command(
    name="time",
    description="Show computer time"
)
async def server_time(interaction: discord.Interaction):

    now = datetime.datetime.now()

    await interaction.response.send_message(
        f"🕒 {now}"
    )


# ==========================
# RUN help.pl
# ==========================

@tree.command(
    name="run_help",
    description="Run help.pl with four arguments"
)
@app_commands.describe(
    ip="First argument",
    port="Second argument",
    size="Third argument",
    time="Fourth argument"
)
async def run_help(
    interaction: discord.Interaction,
    ip: str,
    port: str,
    size: str,
    time: str
):

    if not is_admin(interaction.user.id):
        await interaction.response.send_message(
            "❌ Permission denied",
            ephemeral=True
        )
        return

    await interaction.response.defer()

    try:

        command = [
            "perl",
            "help.pl",
            ip,
            port,
            size,
            time
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=os.getcwd()
        )

        output = result.stdout

        if result.stderr:
            output += "\nERROR:\n" + result.stderr

        if not output:
            output = "help.pl completed with no output."

        if len(output) > 1900:
            output = output[:1900] + "\n...(truncated)"

        await interaction.followup.send(
            f"✅ Executed:\n\n"
            f"```\n{' '.join(command)}\n```\n\n"
            f"Output:\n"
            f"```\n{output}\n```"
        )

    except subprocess.TimeoutExpired:
        await interaction.followup.send(
            "⏱️ help.pl timed out."
        )

    except Exception as e:
        await interaction.followup.send(
            f"❌ Error:\n```\n{e}\n```"
        )

    except subprocess.TimeoutExpired:

        await interaction.followup.send(
            "⏱️ help.pl timed out."
        )


    except Exception as e:

        await interaction.followup.send(
            f"❌ Error:\n```\n{e}\n```"
        )


# ==========================
# START
# ==========================

client.run(TOKEN)