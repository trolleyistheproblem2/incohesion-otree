from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
from random import shuffle

doc = """
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner_v2'
    players_per_group = 2
    num_rounds = 8

    # instructions1_template = 'prisoner/Instructions1.html'
    # instructions2_template = 'prisoner/Instructions2.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(200)
    both_defect_payoff = c(100)

    game1_rounds = [1,2,3,4,5,6,7,8,9,10,11,12]
    #game2_rounds = [1, 7, 5, 4]

    outgroup_rounds = [7, 2, 3, 8,9,10]
    ingroup_rounds = [1, 4, 5, 6,11,12]



class Group(BaseGroup):
    pass

class Player(BasePlayer):

    def get_partner(self):
        return self.get_others_in_group()[0]


    decision = models.StringField(
        choices=['Cooperate', 'Defect'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )

    question1 = models.IntegerField(label= "How much you would earn if you pick MINUS and your partner picks MINUS?",
                                   choices=[[1,'100'],[2,'120'],[3,'10'],[4,'20']],
                                   widget=widgets.RadioSelect
                                   )

    question2 = models.IntegerField(label="How much you would earn if you pick PLUS and your partner picks PLUS?",
                                    choices=[[1, '10'], [2, '120'], [3, '100'], [4, '20']],
                                    widget=widgets.RadioSelect
                                    )

    question3 = models.IntegerField(label="How much will your partner earn if you pick MINUS and your partner picks PLUS?",
                                    choices=[[1, '20'], [2, '100'], [3, '120'], [4, '10']],
                                    widget=widgets.RadioSelect
                                    )



    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):


        payoff_matrix = {
            'Cooperate':
                {
                    'Cooperate': self.subsession.both_cooperate_payoff,
                    'Defect': self.subsession.betrayed_payoff
                },
            'Defect':
                {
                    'Cooperate': self.subsession.betray_payoff,
                    'Defect': self.subsession.both_defect_payoff
                }
        }

        if self.subsession.round_number == self.session.vars['choice_PD_1']:
            self.payoff = payoff_matrix[self.decision][self.other_player().decision]
            self.participant.vars['payoff_prisoner_sym'] = self.payoff
        else:
            self.payoff = 0

        print('payoff matrix is', payoff_matrix)

    session_vars_dump = models.StringField()


class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating_session PD')
        if self.round_number == 1:
            self.session.vars['choice_PD_1'] = random.randint(1, Constants.num_rounds)
            self.session.vars['selected_game_for_payoff'] = random.randint(1, 2)

    # payoff if 1 player defects and the other cooperates"""
    betray_payoff = models.CurrencyField(initial=120)
    betrayed_payoff = models.CurrencyField(initial=10)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = models.CurrencyField(initial=100)
    both_defect_payoff = models.CurrencyField(initial=20)

    chosen_game_type = models.IntegerField(min=1, max=2)



    def do_my_shuffle(self):

        if self.round_number in Constants.outgroup_rounds:

            players = self.get_players()

            High_players = [p for p in players if p.participant.vars['senior'] == 'High']
            Low_players = [p for p in players if p.participant.vars['senior'] == 'Low']

            random.shuffle(High_players)
            random.shuffle(Low_players)
            print('shuffled Highs', High_players)
            print('shuffled Lows', Low_players)
            # x = [[i] for i in M_players]
            # print(x)

            # y = shuffle(x)

            # print('y is', y)

            # print('M_players is',M_players)
            group_matrix = []

            # pop elements from M_players until it's empty
            while High_players:
                new_group = [
                    High_players.pop(),
                    Low_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_group_matrix(group_matrix)
            print('Group Matrix for this', self.round_number, 'round is', group_matrix)

        elif self.round_number in Constants.ingroup_rounds:

            players = self.get_players()

            High_players = [p for p in players if p.participant.vars['senior'] == 'High']
            Low_players = [p for p in players if p.participant.vars['senior'] == 'Low']

            random.shuffle(High_players)
            random.shuffle(Low_players)
            print('shuffled Highs', High_players)
            print('shuffled Lows', Low_players)

            group_matrix = []


            while High_players:
                new_group = [
                    High_players.pop(),
                    High_players.pop(),
                ]
                group_matrix.append(new_group)
            while Low_players:
                new_group = [
                    Low_players.pop(),
                    Low_players.pop(),
                ]
                group_matrix.append(new_group)

            self.set_group_matrix(group_matrix)
            print('Group Matrix for this', self.round_number, 'round is', group_matrix)


        if self.round_number in Constants.game1_rounds:
            self.chosen_game_type = 1
            self.betray_payoff = c(120)
            self.betrayed_payoff = c(10)
            self.both_cooperate_payoff = c(100)
            self.both_defect_payoff = c(20)
            print('both defect payoff is', self.both_defect_payoff)

        elif self.round_number in Constants.game2_rounds:
            self.chosen_game_type = 2
            self.betray_payoff = c(120)
            self.betrayed_payoff = c(10)
            self.both_cooperate_payoff = c(100)
            self.both_defect_payoff = c(20)
            print('both defect payoff is', self.both_defect_payoff)