# Tessa - Discord reactions bot

`tessa` is a very simple Discord.py bot that automatically adds configured
reactions to any message posted in the specified channels.

## Installation

The minimum required interpreter version is **Python 3.9**.

There are a couple of required dependencies that need to be installed first
for `tessa` to run correctly:

```
python3 -m pip install -U discord.py jsonc_parser
```

## Configuration

See the included `tessa_example.jsonc` file for configuration examples. The
file should be renamed to `tessa.jsonc` and put in the same directory as the
`tessa` executable. An alternative option is to specify an explicit path to
the configuration file by invoking the bot with `-c <path to file>`.

**Before running, you will need to set up the bot on a Discord account, obtain
the client token and add it to the configuration file, and join the bot to the
desired guilds.** Proceed to the next section for more information on this
process.

`tessa` supports a few additional command line arguments:

* `-d / --debug`
  Increases log verbosity to the absolute maximum for hacking and debugging.

## Generating a bot token

1. Go into Discord’s [Developer Portal](https://discordapp.com/developers/applications/me)
   and create a new Application.

2. After creating your new Application with the desired name, description and
   icon, on the left pane choose Bot, then choose Add Bot, then confirm the
   action.

3. The first time you see the Bot page, you will see the option to Copy the
   generated token to clipboard. **If you navigate away from this page before
   copying the token, you will need to Reset it to a new one first,
   invalidating the previous token.**

4. Paste the token into the configuration file as the `token` option.

## Joining the bot to guilds

1. Return to the [Developer Portal](https://discordapp.com/developers/applications/me)
   and select the bot’s parent application from the My Applications section.

2. In the application’s General Information page, scroll down to the
   Application ID and choose Copy.

3. In order to join the bot to a guild, replace the Application ID into the
   `APPID` portion of the URL below, and visit it as a user with the guild
   Administrator privilege:

```
https://discordapp.com/oauth2/authorize?&client_id=APPID&scope=bot&permissions=73792
```
