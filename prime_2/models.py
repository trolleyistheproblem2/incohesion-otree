from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from statistics import median

author = 'Shardul Vaidya, CESS India'

doc = """
folks reading a prime paragraph and answering a few questions
"""


class Constants(BaseConstants):
    name_in_url = 'prime_2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q5 = models.LongStringField(label='Please describe in one sentence how the text made you feel. ')



