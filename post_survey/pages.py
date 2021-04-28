from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
import random



class Questions(Page):
    form_model = 'player'
    form_fields = ['gender','state_origin','state_origin_text', 'mother_occupation', 'father_occupation','caste_category','caste_name','group_religion','group_class',
                   'group_caste', 'group_india','group_maharashtra','exclusion','discrimination','safety','vote_2019',
                   'politician_religion','religion_attention','conflict','position','representation','chicken','lamb','beef','pork']

    # def before_next_page(self):
    #     return self.player.set_random_game()



class Result(Page):
    def vars_for_template(self):

        #self.player.game_selected_for_payoff = self.participant.vars['selected_game_for_payoff']


            # self.participant.payoff = c(100) + self.participant.vars['payoff_prisoner_sym'] + self.participant.vars['payoff_dictator'] + self.participant.vars['ngo_payoff']
            # self.participant.vars['pd_payoff'] = self.participant.vars['payoff_prisoner_sym']
            return {
                'payment': self.player.payoff,
                'prisoner_payoff': self.participant.vars['pd_payoff'],
                'dictator_payoff': self.participant.vars['payoff_dictator'],
                'ngo_payoff': self.participant.vars['ngo_payoff'],
                'game_excluded' : self.participant.vars['game_excluded']
            }



page_sequence = [
    Questions,
    Result
]
