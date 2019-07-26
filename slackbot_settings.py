#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	slackbot_settings
# CreatedDate:  2019-07-19 12:28:20 +0900
# LastModified: 2019-07-26 12:58:04 +0900
#

with open('APIToken.dat', 'r') as f:
    tmp = f.read().replace('\n', '')
API_TOKEN = tmp

# default response
default_reply = "Sorry, I'm not sure"

# list of package of plugin
PLUGINS = [
    'SlackBotPlugin',
]
