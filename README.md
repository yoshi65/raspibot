# raspibot
slackbot for infrared remote control of raspberry pi

## Preparation
### APIToken.dat
    Write API token for slackbot.
    https://api.slack.com/bot-users#getting-started
### ChannelId.dat
    Write channel id.
    https://api.slack.com/methods/channels.list/test

## Usage
```
python bot.py
```

## Tree
```
raspibot
├── APIToken.dat
├── ChannelId.dat
├── SlackBotPlugin.py
├── bot.py
├── irrp_class.py
├── pigpio.json
└── slackbot_settings.py
```

## Dependencies
* python3.6
* pip
    * pigpio
    * Slackbot
