#!/usr/bin/env python3
'''
codename Tessa

Copyright (C) 2022 - 2023 by Iris Morelle <iris@irydacea.me>
See COPYING for use and distribution terms.
'''

_FITZPATRICK_MODIFIERS = (
    '\U0001F3FB', # EMOJI MODIFIER FITZPATRICK TYPE-1-2
    '\U0001F3FC', # EMOJI MODIFIER FITZPATRICK TYPE-3
    '\U0001F3FD', # EMOJI MODIFIER FITZPATRICK TYPE-4
    '\U0001F3FE', # EMOJI MODIFIER FITZPATRICK TYPE-5
    '\U0001F3FF', # EMOJI MODIFIER FITZPATRICK TYPE-6
)

def neutral_skintone(emoji: str) -> str:
    '''
    Returns the specified string without Fitzpatrick skin type modifiers.
    '''
    return emoji.translate({ord(char): None for char in _FITZPATRICK_MODIFIERS})
