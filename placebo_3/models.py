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
    name_in_url = 'placebo_3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q6 = models.IntegerField(label='Do you often visit the Zoo?',
                                choices = [[1,'Yes'],
                                    [2,'No']],
                             widget=widgets.RadioSelectHorizontal
                             )


    q7 = models.IntegerField(label='Have you ever seen a Tiger in the wild?',
                             choices=[[1, 'Yes'],
                                      [2, 'No']],
                             widget=widgets.RadioSelectHorizontal
                             )

