# Discord Moderation Bot

This is a simple yet powerful Discord moderation bot built with Python and the [discord.py](https://discordpy.readthedocs.io/) library. It includes a set of moderation commands and an anti-bad word filter to help manage your server.

## Features

- **Ban a member**: Ban a member from the server with an optional reason.
- **Kick a member**: Kick a member from the server with an optional reason.
- **Clear messages**: Delete a specified number of messages in a channel.
- **Bad word filter**: Automatically deletes messages containing predefined bad words.
- **Custom bad word list**: Update and manage the list of bad words dynamically.

## Prerequisites

To run this bot, you'll need:

- Python 3.11+ installed on your system.
- A [Discord Bot Token](https://discord.com/developers/applications) (saved in a `.env` file).
- `discord.py` and `python-dotenv` libraries installed.

### Install Dependencies

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Ahmad-Akram7/discord-moderation-bot.git
   cd discord-moderation-bot

    Install the required dependencies:

pip install -r requirements.txt

Create a .env file in the root directory of the project and add your Discord Bot Token:

    DISCORD_TOKEN=your-bot-token

Commands
!ban <@user> [reason]

Ban a user from the server. Optionally, you can provide a reason for the ban.

Example:

!ban @User spamming

!kick <@user> [reason]

Kick a user from the server. Optionally, you can provide a reason for the kick.

Example:

!kick @User inappropriate behavior

!clear <number>

Delete a specific number of messages from the current channel.

Example:

!clear 10

!setbadwords <word1> <word2> ...

Set or update the list of bad words to be filtered by the bot.

Example:

!setbadwords badword1 badword2 badword3

!help

Displays a list of all available commands and how to use them.
Running the Bot

After setting up the .env file with your bot token, you can start the bot with the following command:

python main.py

Bot Permissions

Ensure your bot has the required permissions to perform its tasks:

    Ban Members: Required to ban users from the server.
    Kick Members: Required to kick users from the server.
    Manage Messages: Required to clear messages from the channel.
    Administrator (optional): Provides full access to all actions, if the bot is having permission issues.

Ensure the bot’s role is placed above other roles in the server's role hierarchy to have the necessary authority to ban, kick, or clear messages from other members.
Contributing

Feel free to fork this repository, open issues, or create pull requests if you would like to contribute to the bot.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using the Discord Moderation Bot! Happy moderating! 🎉


