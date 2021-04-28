from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Prime(Page):
    form_model = 'player'
    form_fields = ['q6', 'q7']

    def vars_for_template(self):
        return {
            'prime_image': 'prime_2/prime_station.png'
        }

class PrimeQ2(Page):
    form_model = 'player'
    form_fields = ['q3', 'q4']

page_sequence = [
    Prime
]
