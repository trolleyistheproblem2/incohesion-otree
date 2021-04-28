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
    name_in_url = 'prime_3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q6 = models.IntegerField(label='Did you know about this policy measure before? ',
                                choices = [[1,'Yes'],
                                    [2,'No']],
                             widget=widgets.RadioSelectHorizontal
                             )


    q7 = models.IntegerField(label='Do you think this policy measure is fair or unfair?',
                             choices=[[1, 'Very fair'],
                                      [2, 'Somewhat fair'],
                                      [3,'Neither fair nor unfair'],
                                      [4,'Not so fair'],
                                      [5,'Completely unfair ']],
                             widget=widgets.RadioSelectHorizontal
                             )

