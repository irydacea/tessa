# Tessa - Discord reactions bot

`tessa` is a very simple Discord.py bot that automatically adds configured
reactions to any message posted in the specified channels.

## Installation

The minimum required interpreter version is **Python 3.6**.

There are a few required dependencies that need to be installed first for
`tessa` to run correctly:

```
python -m pip install -U discord.py
python -m pip install -U jsonc_parser
```

## Configuration

See the included `tessa_example.jsonc` file for configuration examples. The
file should be renamed to `tessa.jsonc` and put in the same directory as the
`tessa` executable. An alternative option is to specify an explicit path to
the configuration file by invoking the bot with `-c <path to file>`.

**Before running, you will need to set up the bot on a Discord account, obtain
the client token and add it to the configuration file, and join the bot to the
desired guilds.** (TODO: document this process)

`tessa` supports a few additional command line arguments:

* `-v / --verbose`
  Increases log verbosity for diagnostic purposes.
* `-d / --debug`
  Increases log verbosity to the absolute maximum for hacking and debugging.
