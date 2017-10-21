"""
Part of rgng: Random Game Name Generator
Entry module, contains the main function, generate_name()
Enrique Arriaga, 2017

Python port of the generator used in the Android app
https://play.google.com/store/apps/details?id=com.vgname.vgnamegenerator
"""

from numpy.random import choice
from modules import TokenFactory as Factory

# in numpy, we use two arguments for random.choice(), the first one is
# a list of possible values, and the second one is a list with the same size,
# with the probabilities of each value (all the values should add to 1)
#
# here, the constants starting with S_ are the sets of possible values
#       and the constants with P_ are probabilities of these values
# For instance, these are the possible values of number of syllables
#     S_RANDOMWORD_SS = [2,    3,   4]
# And their probabilities
#     P_RANDOMWORD_SS = [0.35, 0.5, 0.15]
S_TRUEFALSE = [True, False]
P_TITLE = [0.33, 0.67]
P_SUBTITLE = [0.33, 0.67]
S_TITLE_TYPES = [{'type': 'S1VsS2', 'p_subtitle': [0.1, 0.9]},
                 {'type': 'VTheS', 'p_subtitle': [0, 1]},
                 {'type': 'CompoundWord', 'p_subtitle': [0.33, 0.67]},
                 {'type': 'RandomWord', 'p_subtitle': [0.33, 0.67]}]
P_TITLE_TYPES = [0.15, 0.15, 0.35, 0.35]
P_NUMERAL = [0.3, 0.7]
P_EDITION = [0.03, 0.97]

def generate_name():
    """main function"""
    title = choice(S_TITLE_TYPES, p=P_TITLE_TYPES)
    has_title = choice(S_TRUEFALSE, p=P_TITLE)
    has_subtitle = choice(S_TRUEFALSE, p=title['p_subtitle'])
    tokens = []

    if has_title:
        tokens.append(Factory.create_token(title['type']))
        if choice(S_TRUEFALSE, p=P_NUMERAL):
            tokens.append(Factory.create_token('Numeral'))

    if not has_title or has_subtitle:
        if has_title:
            tokens.append(":")
        tokens.append(Factory.create_token('Subtitle'))

    if choice(S_TRUEFALSE, p=P_EDITION):
        tokens.append((Factory.create_token('Edition')))

    name = " ".join([str(t) for t in tokens]).replace(" :", ":")
    return name


if __name__ == '__main__':
    print generate_name()
