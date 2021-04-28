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
    name_in_url = 'prime'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.LongStringField(label='Please describe in one sentence what the text was about:')
    q2 = models.IntegerField(label='To what extent do you agree or disagree with the renaming of Urdu/Muslim city names?',
                             choices=[[1,'Fully Agree'],
                                    [2,'Somewhat Agree'],
                                    [3,'Neither Agree Nor Disagree'],
                                    [4,'Somewhat Disagree'],
                                    [5, 'Fully Disagree']],
                             widget=widgets.RadioSelectHorizontal
                             )
    q3 = models.IntegerField(
        label='I believe people look up to me and respect me.',
        choices=[[1, 'Fully Agree'],
                 [2, 'Somewhat Agree'],
                 [3, 'Neither Agree Nor Disagree'],
                 [4, 'Somewhat Disagree'],
                 [5, 'Fully Disagree']],
        widget=widgets.RadioSelect
        )
    q4 = models.IntegerField(
        label='I feel I have much to be proud of.',
        choices=[[1, 'Fully Agree'],
                 [2, 'Somewhat Agree'],
                 [3, 'Neither Agree Nor Disagree'],
                 [4, 'Somewhat Disagree'],
                 [5, 'Fully Disagree']],
        widget=widgets.RadioSelect
        )



