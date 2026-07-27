import discord
from discord import app_commands
import subprocess
import platform
import logging

TOKEN = "MTUyODg4MDY5NDAwMzEwNTk5Mw.GFXu4g.CdlDlEpTKY8mlcGBDd3REEece4frePHHG6cpKw"

# Put your Discord user ID here
ALLOWED_USERS = {
    708651602860310598
}

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)


class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


bot = MyBot()


def allowed(user):
    return user.id in ALLOWED_USERS


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("OS:", platform.system())


@bot.tree.command(
    name="run",
    description="Run an allowed command on this computer"
)
@app_commands.describe(command="Command to run")
async def run(interaction: discord.Interaction, command: str):

    if not allowed(interaction.user):
        await interaction.response.send_message(
            "❌ Not authorized"
        )
        return

    await interaction.response.defer()

    logging.info(
        f"{interaction.user} ran: {command}"
    )

    try:

        if platform.system() == "Windows":
            shell = True
        else:
            shell = True


        result = subprocess.run(
            command,
            shell=shell,
            capture_output=True,
            text=True,
            timeout=30
        )

        output = (
            result.stdout +
            result.stderr
        )

        if not output:
            output = "Command completed."

        if len(output) > 1900:
            output = output[:1900] + "\n..."

        await interaction.followup.send(
            f"```\n{output}\n```"
        )


    except subprocess.TimeoutExpired:
        await interaction.followup.send(
            "Command timed out."
        )

    except Exception as e:
        await interaction.followup.send(
            f"Error: {e}"
        )


@bot.tree.command(
    name="system",
    description="Show system information"
)
async def system(interaction: discord.Interaction):

    if not allowed(interaction.user):
        await interaction.response.send_message(
            "❌ Not authorized"
        )
        return

    info = f"""
OS: {platform.system()}
Version: {platform.version()}
Machine: {platform.machine()}
Python: {platform.python_version()}
"""

    await interaction.response.send_message(
        f"```\n{info}\n```"
    )


bot.run(TOKEN)