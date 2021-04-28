from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Prime(Page):
    form_model = 'player'
    form_fields = ['q5']

    def vars_for_template(self):
        return {
            'prime_image': 'placebo_2/prime_tiger.png'
        }



page_sequence = [
    Prime
]
