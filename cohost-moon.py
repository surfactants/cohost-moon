import pylunar

from cohost.models.user import User
from cohost.models.block import MarkdownBlock

import random

import string # for string.Formatter

def phase():
    mi = pylunar.MoonInfo((42, 21, 30), (-71, 3, 35))
    return mi.phase_name().lower().replace('_', ' ')

user = User.login("lmao@no.way"
                , "hunter2")

project = user.getProject('themoon')
title = f'the moon is now {phase()}'

lastTitle = project.getPosts()[0].headline

if title == lastTitle:
    quit()

random.seed()

def numericString(n):
    s = '<WUH-OH! UNDEFINED NUMERIC CONSTANT!>'
    if n == 1:
        s = 'a'
    elif n == 2:
        s = 'two'
    elif n == 3:
        s = 'three'
    elif n == 4:
        s = 'four'
    elif n == 5:
        s = 'five'
    elif n == 6:
        s = 'six'
    elif n == 7:
        s = 'seven'
    elif n == 8:
        s = 'eight'
    elif n == 9:
        s = 'nine'
    elif n == 10:
        s = 'ten'
    return s

def randomLine(filename):
    file = open(filename)
    line = next(file)
    for num, nline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = nline
    return line.replace('\n', '')
    

def topic():
    return randomLine("topic.txt")

def formatNum(s):
    n = random.randrange(1, 9)
    pl = ''
    if n > 1:
        pl = 's'
        s = s.format(pl = 's')
    s = s.format(num = numericString(n), pl = pl)
    return s

def message():
    s = randomLine("msg.txt")
    # args = string.Formatter.parse(s)
    s = s.format(topic = topic(), topic2 = topic(), num = '{num}', pl = '{pl}')
    args = [args[1] for args in string.Formatter().parse(s) if args[1] is not None]
    if args.count('num'):
        s = formatNum(s)
    return s

tags = [ ]

markdown = ''

blocks = [
    MarkdownBlock(markdown)
]

quit()

project.post(title, blocks, tags=tags)

