from cohost.models.user import User
from cohost.models.block import MarkdownBlock

import random

import string # for string.Formatter

from moonphase import phase
import cohost_login

project = cohost_login.login().getProject('themoon')
title = f'the moon is now {phase()}'

lastTitle = project.getPosts()[0].headline

# print(f'last retrieved title is {lastTitle}')

if title == lastTitle or title == '':
    print('TITLE ALREADY FOUND! ({})')
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

markdown = message()

markdown = ""

blocks = [
    MarkdownBlock(markdown)
]

print(title)
print(markdown)

project.post(title, blocks, tags=tags)

