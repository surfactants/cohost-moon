from cohost.models.block import MarkdownBlock

from phase import phase
from cohost_login import login

from log import log

project = login().getProject('themoon')

phase = phase()
title = f'the moon is {phase}'

if not phase:
    quit()

blocks = [MarkdownBlock('')]

post_tags = ['The Cohost Lunar Feed']

print(title)
project.post(title,
             blocks,  # empty post body
             tags=post_tags)
