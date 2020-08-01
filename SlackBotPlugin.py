#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	SlackBotPlugin
# CreatedDate:  2019-07-19 12:32:53 +0900
# LastModified: 2020-08-01 10:20:57 +0900
#

import json
import re
from pathlib import Path

import pigpio
from slackbot.bot import listen_to, respond_to

from irrp_class import irrp


def format_json():
    file_path = Path(__file__).parent.resolve() / 'pigpio.json'

    with open(file_path, 'r') as f:
        d = json.load(f)

    d_new = dict()
    for k in d.keys():
        if re.search('[0-9]$', k):
            d_new[k] = d[k]
        else:
            i_post = 0
            num = 0
            d_tmp = d[k]
            for i in range(len(d_tmp)):
                if d_tmp[i] > 10000:
                    d_new[f'{k}{num}'] = d_tmp[i_post:(i+1)]
                    i_post = i+1
                    num += 1
            if i_post < i+1:
                d_new[f'{k}{num}'] = d_tmp[i_post:(i+1)]

    with open(file_path, 'w') as f:
        json.dump(d_new, f, indent=4)


@listen_to('Record .*')
@respond_to('Record .*')
def record(message, *something):
    file_path = Path(__file__).parent.resolve() / 'pigpio.json'
    name = message.body['text'].replace('Record ', '')

    pi = pigpio.pi()
    if not pi.connected:
        exit(0)

    ir = irrp(pi,
              GPIO=18,
              FILE=file_path,
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
    file_path = Path(__file__).parent.resolve() / 'pigpio.json'
    name = message.body['text'].replace('Play ', '')

    with open(file_path, 'r') as f:
        d = json.load(f)

    id_list = list()
    i = 0
    while 1:
        if f'{name}{i}' in d:
            id_list.append(f'{name}{i}')
        elif i == 0:
            message.reply(f'Not found {name}')
            return
        else:
            break

        i += 1

    pi = pigpio.pi()
    if not pi.connected:
        exit(0)

    # id is set for daikin
    # if your signal is short, you set `ID=[name]`
    ir = irrp(pi,
              GPIO=17,
              FILE=file_path,
              ID=id_list,
              POST=130,
              GAP=1)
    ir.playback()
    message.reply(f'Played {name}')

    pi.stop()
