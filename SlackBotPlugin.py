#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	SlackBotPlugin
# CreatedDate:  2019-07-19 12:32:53 +0900
# LastModified: 2019-07-26 13:39:50 +0900
#

import re

import pigpio
from slackbot.bot import listen_to, respond_to

from irrp_class import irrp


@listen_to('Record .*')
@respond_to('Record .*')
def record(message, *something):
    pi = pigpio.pi()
    if not pi.connected:
        exit(0)

    name = message.body['text'].replace('Record ', '')

    ir = irrp(pi,
              GPIO=18,
              FILE='pigpio.json',
              ID=[name],
              POST=130,
              NO_CONFIRM=True)
    ir.record()

    message.reply(f'Recorded {name}')

    pi.stop()


@listen_to('Play .*')
@respond_to('Play .*')
def play(message, *something):
    pi = pigpio.pi()
    if not pi.connected:
        exit(0)

    name = message.body['text'].replace('Play ', '')

    # id is set for daikin
    # if your signal is short, you set `ID=[name]`
    ir = irrp(pi,
              GPIO=17,
              FILE='pigpio.json',
              ID=[f'{name}1', f'{name}2', f'{name}3'],
              POST=130,
              GAP=1)
    ir.playback()

    message.reply(f'Played {name}')

    pi.stop()
