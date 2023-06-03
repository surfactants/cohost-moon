from cohost.models.block import MarkdownBlock

import random

from moonphase import phase
from cohost_login import login

project = login().getProject('themoon')

phase = phase()
title = f'the moon is {phase}'

lastTitle = project.getPosts()[0].headline

if not phase:
    print('\tEMPTY TITLE RETURNED, ABORTING...')
    quit()
    
if title == lastTitle:
    print('\tTITLE ALREADY FOUND! ({})')
    quit()

blocks = [ MarkdownBlock('') ]

tags = [ 'The Cohost Lunar Feed' ]

print(title)
project.post(title,
             blocks, # empty post body
             tags = tags) # without the redundant assignment it becomes a content warning lol
