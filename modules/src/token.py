"""
Part of rgng: Random Game Name Generator
Module containing abstract Token class and all its children
Enrique Arriaga, 2017

Python port of the generator used in the Android app
https://play.google.com/store/apps/details?id=com.vgname.vgnamegenerator
"""
import json
import os

from abc import ABCMeta
from numpy.random import choice, randint

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = DIR_PATH + "/../../data/"

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

S_S1_VS_S2 = ["vs.", "and"]
P_S1_VS_S2_VS = 0.66
P_S1_VS_S2_AND = 0.34
P_S1_VS_S2 = [P_S1_VS_S2_VS, P_S1_VS_S2_AND]

S_NUMERAL = ["roman", "decimal"]
P_NUMERAL_ROMAN = 0.66
P_NUMERAL_DECIMAL = 0.34
P_NUMERAL = [P_NUMERAL_ROMAN, P_NUMERAL_DECIMAL]
MAX_NUMBER_ROMAN = 15
MAX_NUMBER_DECIMAL = 9

S_COMPOUNDWORD_QS = [1, 2, 3]  # number of qualifiers to append
P_COMPOUNDWORD_QS = [0.90, 0.08, 0.02]

S_RANDOMWORD_SS = [2, 3, 4]  # number of syllables
P_RANDOMWORD_SS = [0.35, 0.5, 0.15]

P_SUBTITLE_PROTA = [0.5, 0.5]
P_SUBTITLE_INITIAL_THE = [0.33, 0.67]
P_SUBTITLE_PLURAL = [0.5, 0.5]
P_SUBTITLE_OF = [0.5, 0.5]
P_SUBTITLE_ADJ = [0.25, 0.75]


class Token(object):
    """
    Abstract class to represent Token, a part of the game title
    """
    __metaclass__ = ABCMeta

    def __init__(self, name):
        """
        Open, parse and store in self.data the information found in
        data/{__class__.__name__}.json
        """
        try:
            with open(DATA_DIR + name + ".json") as data:
                self.data = json.load(data)
        except IOError:
            print "Cannot open file for ", name



class S1VsS2(Token):
    """
    Class representing names of the type
        Plants vs Zombies
    """
    def __init__(self):
        super(S1VsS2, self).__init__(self.__class__.__name__)
        subjects_list = self.data['subjects']
        self.subject1 = choice(subjects_list)
        self.particle = choice(S_S1_VS_S2, p=P_S1_VS_S2)
        self.subject2 = choice(subjects_list)  # yes, they can be the same!

    def __str__(self):
        return self.subject1 + " " + self.particle + " " + self.subject2


class RandomWord(Token):
    """
    Class representing names formed from random syllables
        Mezapo
        Tolkoroi
    """
    def __init__(self):
        super(RandomWord, self).__init__(self.__class__.__name__)
        syllables_list = self.data['syllables']
        how_many_syllables = choice(S_RANDOMWORD_SS, p=P_RANDOMWORD_SS)
        self.syllables = []
        for _ in range(0, how_many_syllables):
            self.syllables.append(choice(syllables_list))

    def __str__(self):
        return "".join(self.syllables).capitalize()


class VTheS(Token):
    """
    Class representing names of the type
        Cut the Rope
    """
    def __init__(self):
        super(VTheS, self).__init__(self.__class__.__name__)
        verbs = self.data['verbs']
        subjects = self.data['subjects']
        self.verb = choice(verbs)
        self.particle = "the"
        self.subject = choice(subjects)

    def __str__(self):
        return self.verb + " " + self.particle + " " + self.subject


class CompoundWord(Token):
    """
    Class representing names of the type
        OverLords
        HeptaMegaNinjas
    """
    def __init__(self):
        super(CompoundWord, self).__init__(self.__class__.__name__)
        qualifiers_list = self.data['qualifiers']
        subjects = self.data['subjects']
        how_many_qualifiers = choice(S_COMPOUNDWORD_QS, p=P_COMPOUNDWORD_QS)
        self.qualifiers = []
        for _ in range(0, how_many_qualifiers):
            self.qualifiers.append(choice(qualifiers_list))
        self.subject = choice(subjects)

    def __str__(self):
        return "".join(self.qualifiers) + self.subject


class Subtitle(Token):
    """
    Class representing names of the type
        Eternal Paranoia
        Odd Crown
        The Dragon of Strange Light
    """
    def __init__(self):
        super(Subtitle, self).__init__(self.__class__.__name__)
        self.the = ''
        self.protagonist_name = ''
        self.of_particle = ''
        self.adjective = ''
        self.second_subject = ''
        protagonists = self.data['protagonists']
        adjectives = self.data['adjectives']
        subjects = self.data['subjects']
        have_protagonist = choice(S_TRUEFALSE, p=P_SUBTITLE_PROTA)
        if have_protagonist:
            protagonist = choice(protagonists)
            self.protagonist_name = protagonist['name']
            if (protagonist["optional_the"] and
                    choice(S_TRUEFALSE, p=P_SUBTITLE_INITIAL_THE)):
                self.the = "The"
            if(protagonist["optional_plural"] and
               choice(S_TRUEFALSE, p=P_SUBTITLE_PLURAL)):
                self.protagonist_name += 's'
            if(protagonist["obligatory_of"] or
               (choice(S_TRUEFALSE, p=P_SUBTITLE_OF) and
                protagonist["optional_of"])
              ):
                self.of_particle = "of"
        if not have_protagonist or choice(S_TRUEFALSE, p=P_SUBTITLE_ADJ):
            self.adjective = choice(adjectives)
        self.second_subject = choice(subjects)

    def __str__(self):
        """ string representation is:
            the + protagonist['name'] + plural + of + adjective + second_subject
            the   dragon                s        of   eternal     fire
        """
        parts = [self.the, self.protagonist_name, self.of_particle,
                 self.adjective, self.second_subject]
        return " ".join([word for word in parts if word != ""])


class Edition(Token):
    """
    Class representing an edition to add at the end
        (GOTY Edition)
    """
    def __init__(self):
        super(Edition, self).__init__(self.__class__.__name__)
        editions_list = self.data['editions']
        self.edition = choice(editions_list)

    def __str__(self):
        return '(' + self.edition + ')'


class Numeral(Token):
    """
    Class representing a numeral, in roman or decimal
        VIII or 8
    """
    def __init__(self):
        super(Numeral, self).__init__(self.__class__.__name__)
        number_type = choice(S_NUMERAL, p=P_NUMERAL)
        if number_type == "roman":
            self.number = self.data['romans'][str(randint(2, MAX_NUMBER_ROMAN))]
        elif number_type == "decimal":
            self.number = str(randint(2, MAX_NUMBER_DECIMAL))
        else:
            raise ValueError("Invalid number type")

    def __str__(self):
        return self.number
