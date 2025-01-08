import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # Load the environment variables from .env file

# Initialize bot with command prefix
intents = discord.Intents.default()
intents.message_content = True  # Allows reading messages for moderation
intents.members = True  # Allows access to members for moderation actions
bot = commands.Bot(command_prefix="!", intents=intents)

# List of inappropriate words (example)
BAD_WORDS = ["badword1", "badword2", "badword3"]

# Command: Ban User
@bot.command(name="ban")
async def ban(ctx, member: discord.Member = None, *, reason="No reason provided"):
    """Ban a member from the server."""
    if member is None:
        await ctx.send("You need to specify a member to ban. Usage: `!ban <member> [reason]`")
        return
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f"{member.name} has been banned for: {reason}")
    else:
        await ctx.send("You don't have permission to ban members.")

# Command: Kick User
@bot.command(name="kick")
async def kick(ctx, member: discord.Member = None, *, reason="No reason provided"):
    """Kick a member from the server."""
    if member is None:
        await ctx.send("You need to specify a member to kick. Usage: `!kick <member> [reason]`")
        return
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f"{member.name} has been kicked for: {reason}")
    else:
        await ctx.send("You don't have permission to kick members.")

# Command: Clear Messages
@bot.command(name="clear")
async def clear(ctx, amount: int):
    """Clear a given amount of messages."""
    if amount <= 0:
        await ctx.send("Please specify a positive number of messages to delete.")
        return
    if ctx.author.guild_permissions.manage_messages:
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {len(deleted)} messages.", delete_after=5)
    else:
        await ctx.send("You don't have permission to clear messages.")

# Anti-Bad Word filter
@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Don't check bots

    # Check for bad words in message
    if any(word in message.content.lower() for word in BAD_WORDS):
        await message.delete()
        await message.channel.send(f"⚠️ {message.author.name}, your message contained inappropriate language and has been deleted.", delete_after=5)

    await bot.process_commands(message)  # Allow other commands to be processed

# Command: Set a custom Bad Words list
@bot.command(name="setbadwords")
async def set_bad_words(ctx, *args):
    """Set or update the list of bad words for moderation."""
    global BAD_WORDS
    BAD_WORDS = list(args)
    await ctx.send(f"Bad words list updated: {BAD_WORDS}")

# Command: Show Moderation Help Section
@bot.command(name="moderation_help")
async def custom_help(ctx):
    help_message = """
    **Bot Commands**:

    `!ban <member> [reason]` - Bans a member from the server.
    `!kick <member> [reason]` - Kicks a member from the server.
    `!clear <amount>` - Clears a specified number of messages from the chat.
    `!setbadwords <word1> <word2> ...` - Sets or updates the list of bad words.

    Use `!help <command>` to get more details on a specific command.
    """
    await ctx.send(help_message)

# Run the bot with your token
bot.run(os.getenv('DISCORD_TOKEN'))  # Ensure that the token is loaded from the .env file

@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user}")
    print(f"Bot is connected to {len(bot.guilds)} server(s).")
