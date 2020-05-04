#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	SlackBotPlugin
# CreatedDate:  2019-07-19 12:32:53 +0900
# LastModified: 2020-05-04 14:58:27 +0900
#

import json
import re

import pigpio
from slackbot.bot import listen_to, respond_to

from irrp_class import irrp


def format_json():
    file_name = 'pigpio.json'
    with open(file_name, 'r') as f:
        d = json.load(f)

    d_new = dict()
    for k in d.keys():
        if len(d[k]) > max_length:
            l = len(d[k]) // max_length + 1
            List = d[k]
            for i in range(l):
                d_new[f'{k}{i}'] = \
                    List[max_length*i:(max_length*(i+1) if i != l - 1 else len(List))]
        else:
            d_new[k] = d[k]

    with open(file_name, 'w') as f:
        json.dump(d_new, f, indent=4)


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
              ID=name,
              POST=130,
              NO_CONFIRM=True)
    ir.record()

    message.reply(f'Recorded {name}')

    format_json()
    message.reply(f'Formatted {name}')

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
              ID=[f'{name}0', f'{name}1'],
              POST=130,
              GAP=1)
    ir.playback()

    message.reply(f'Played {name}')

    pi.stop()
