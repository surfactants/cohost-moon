from cohost.models.block import MarkdownBlock

import random

import string # for string.Formatter
print(7)

from moonphase import phase
from cohost_login import login

project = login().getProject('themoon')
title = 'the moon is gay'
'''
phase = phase()
# title = f'the moon is {phase}'

lastTitle = project.getPosts()[0].headline

# print(f'last retrieved title is {lastTitle}')

if not phase:
    print('\tEMPTY TITLE RETURNED, ABORTING...')
    quit()
    
if title == lastTitle:
    print('\tTITLE ALREADY FOUND! ({})')
    quit()
'''

tags = [ 'The Cohost Lunar Feed' ]

markdown: string

title = title + ' (' + phase() + ')'

markdown = str('updated the bot to use [SPICE](https://naif.jpl.nasa.gov/naif/spiceconcept.html)'\
               + '\nsource may be viewed [here](https://github.com/surfactants/cohost-moon)')

blocks = [ MarkdownBlock(markdown) ]

print(title)
print(markdown)
print("end")
project.post(title, blocks, tags=tags)
