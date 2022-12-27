import pylunar

from cohost.models.user import User
from cohost.models.block import MarkdownBlock

# obfuscate
cookie = 'im foolish but not enough to publish my login cookie'
user = User.loginWithCookie(cookie)

def phase():
    mi = pylunar.MoonInfo((42, 21, 30), (-71, 3, 35))
    return mi.phase_name().lower().replace('_', ' ')

project = user.getProject('themoon')
title = ''
tags = [ ]

markdown = 'the moon is currently **{}**'.format(phase())

blocks = [
    MarkdownBlock(markdown)
]

project.post(title, blocks, tags=tags)
