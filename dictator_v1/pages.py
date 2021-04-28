from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1
    #def before_next_page(self):


class MakingGroups2(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.do_my_shuffle()


class Process5(Page):

    def vars_for_template(self):
        return {
                'partner_age': self.player.get_partner().participant.vars['age'],
                'partner_city': self.player.get_partner().participant.vars['city'],
                'partner_senior': self.player.get_partner().participant.vars['senior'],
                'partner_income': self.player.get_partner().participant.vars['income'],
                'partner_college': self.player.get_partner().participant.vars['college'],
                'partner_study_year': self.player.get_partner().participant.vars['study_year'],
                'partner_religion': self.player.get_partner().participant.vars['religion'],
            }


class Offer(Page):
    form_model = 'player'
    form_fields = ['sent']

    def before_next_page(self):
        # self.player.participant_vars_dump = str(self.participant.vars)
        self.player.kept = Constants.endowment - self.player.sent

    #def is_displayed(self):
       # return self.player.id_in_group == 1

    def vars_for_template(self):
        return {
            'partner_age': self.player.get_partner().participant.vars['age'],
            'partner_city': self.player.get_partner().participant.vars['city'],
            'partner_senior': self.player.get_partner().participant.vars['senior'],
            'partner_income': self.player.get_partner().participant.vars['income'],
            'partner_college': self.player.get_partner().participant.vars['college'],
            'partner_study_year': self.player.get_partner().participant.vars['study_year'],
            'partner_religion': self.player.get_partner().participant.vars['religion'],

            'player_age': self.player.participant.vars['age'],
            'player_city': self.player.participant.vars['city'],
            'player_senior': self.player.participant.vars['senior'],
            'player_income': self.player.participant.vars['income'],
            'player_college': self.player.participant.vars['college'],
            'player_study_year': self.player.participant.vars['study_year'],
            'player_religion': self.player.participant.vars['religion'],

        }

    #def before_next_page(self):
     #   self.player.participant_vars_dump = str(self.participant.vars)

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        player1 = group.get_player_by_id(1)
        player2 = group.get_player_by_id(2)

        if self.subsession.round_number == self.session.vars['choice_dictator_1']:
            player1.payoff = Constants.endowment - player2.kept + player1.kept
            player2.payoff = Constants.endowment - player1.kept + player2.kept
            player1.participant.vars['payoff_dictator'] = player1.payoff
            player2.participant.vars['payoff_dictator'] = player2.payoff
        else:
            player1.payoff = 0
            player2.payoff = 0

class Results(Page):
    def is_displayed(self):
        return False

page_sequence = [
    Introduction,
    MakingGroups2,
    Offer,
    ResultsWaitPage,
    Results,

]
