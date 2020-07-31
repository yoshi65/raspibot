#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	slackbot_settings
# CreatedDate:  2019-07-19 12:28:20 +0900
# LastModified: 2020-08-01 00:05:00 +0900
#

from pathlib import Path


api_token = Path(__file__).parent.resolve() / 'APIToken.dat'
with open(api_token, 'r') as f:
    tmp = f.read().replace('\n', '')
API_TOKEN = tmp

# default response
default_reply = "Sorry, I'm not sure"

# list of package of plugin
PLUGINS = [
    'SlackBotPlugin',
]
