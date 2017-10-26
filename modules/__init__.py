"""
Part of rgng: Random Game Name Generator
Entry module of rgng, contains the factory method to create Tokens
Enrique Arriaga, 2017

Python port of the generator used in the Android app
https://play.google.com/store/apps/details?id=com.vgname.vgnamegenerator
"""
from modules.src.token import S1VsS2, VTheS, Edition, Numeral, CompoundWord, RandomWord, Subtitle


class TokenFactory(object):
    @staticmethod
    def create_token(token_type):
        """factory method, raise exception of token_type is not supported
        """
        if token_type == 'S1VsS2':
            token = S1VsS2()
        elif token_type == 'VTheS':
            token = VTheS()
        elif token_type == 'Edition':
            token = Edition()
        elif token_type == 'Numeral':
            token = Numeral()
        elif token_type == 'CompoundWord':
            token = CompoundWord()
        elif token_type == 'RandomWord':
            token = RandomWord()
        elif token_type == 'Subtitle':
            token = Subtitle()
        else:
            raise ValueError("Unsupported Token type: ", token_type)
        return token
