from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools
import random
import json


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ngo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        from .pages import initial_page_sequence
        aaa = [i.__name__.split('_') for i in initial_page_sequence]
        page_blocks = [list(group) for key, group in itertools.groupby(aaa, key=lambda x: x[0])]
        for p in self.get_players():
            pb=page_blocks.copy()
            random.shuffle(pb)
            level1 = list(itertools.chain.from_iterable(pb))
            level2 = ['_'.join(i) for i in level1]
            p.page_sequence = json.dumps(level2)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    page_sequence = models.StringField()

    participant_vars_dump = models.StringField()

    allocation_self = models.CurrencyField(min=0, max=100)
    allocation_ngo = models.CurrencyField(min=0, max=100)
    allocation1_1 = models.CurrencyField(min=0, max=100, label='Keep for self')
    allocation1_2 = models.CurrencyField(min=0, max=100, label='Keep for self')
    allocation1_3 = models.CurrencyField(min=0, max=100, label='Keep for self')
    allocation1_4 = models.CurrencyField(min=0, max=100, label='Keep for self')
    allocation2 = models.CurrencyField(min=0, max=100, label='Give an amount to this charity')
    allocation3 = models.CurrencyField(min=0, max=100, label='Give an amount to this charity')
    allocation4 = models.CurrencyField(min=0, max=100, label='Give an amount to this charity')
    allocation5 = models.CurrencyField(min=0, max=100, label='Give an amount to this charity')

