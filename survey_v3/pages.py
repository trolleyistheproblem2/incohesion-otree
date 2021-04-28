from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    form_model = 'player'
    form_fields = ['subject_id']


class PreIntro(Page):
    pass

class Info(Page):
    form_model = 'player'
    #form_fields = ['income']
    form_fields = ['age', 'study_year',  'religion', 'income']

    def before_next_page(self):
        self.player.set_all_in_vars()

    #def city_error_message(self, city):
      #  print('just checking', city)
      #  if city != 1:
     #       return '''Please check your answer!'''

    def religion_error_message(self, religion):
        print('just checking', religion)
        if religion != 'Muslim':
            return '''Please check your answer!'''

    #def college_error_message(self, college):
     #   print('just checking', college)
      #  if college != 1:
       #     return '''Please check your answer!'''



class MedianCalc(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.split_on_income()



class Result(Page):
    def vars_for_template(self):
        return {
            'player_age': self.player.participant.vars['age'],
            'player_city': self.player.participant.vars['city'],
            'player_senior': self.player.participant.vars['senior'],
            'player_income': self.player.participant.vars['income'],
            'player_college': self.player.participant.vars['college'],
            'player_study_year': self.player.participant.vars['study_year'],
            'player_religion': self.player.participant.vars['religion'],
            'high_indicator': 'survey_v3/high_indicator.png',
            'low_indicator': 'survey_v3/low_indicator.png',
        }

class AttentionCheck(Page):
    form_model = 'player'

    form_fields = ['status_check', 'info_check']

    def status_check_error_message(self, status_check):
        print('just checking', status_check)
        if status_check != self.participant.vars['senior']:
            return '''Please check your answer!'''

    def info_check_error_message(self, info_check):
        print('just checking', info_check)
        if info_check != 'Name':
            return '''Your name will not be displayed to your partners!'''


page_sequence = [
    Welcome,
    PreIntro,
    Info,
    MedianCalc,
    Result,
    AttentionCheck
]
