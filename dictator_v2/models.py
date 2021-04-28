from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'dictator_v2'
    players_per_group = 2
    num_rounds = 8

    instructions_template = 'dictator_v2/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(100)
    outgroup_rounds = [4, 8, 6, 2]
    ingroup_rounds = [5, 1, 3, 7]



class Subsession(BaseSubsession):

    def creating_session(self):
        print('in creating_session')


        if self.round_number == 1:
        print('Group Matrix for this',self.round_number,'round is',group_matrix)
            self.session.vars['choice_dictator_1'] = random.randint(1, Constants.num_rounds)
def do_my_shuffle(self):

    if self.round_number in Constants.outgroup_rounds:
        players = self.get_players()

        High_players = [p for p in players if p.participant.vars['senior'] == 'High']
        Low_players = [p for p in players if p.participant.vars['senior'] == 'Low']

        random.shuffle(High_players)
        random.shuffle(Low_players)
        print('shuffled Highs', High_players)
        print('shuffled Lows', Low_players)

        group_matrix = []

        # pop elements from M_players until it's empty
        while High_players:
            new_group = [
                High_players.pop(),
                Low_players.pop(),
            ]
            group_matrix.append(new_group)

        self.set_group_matrix(group_matrix)

    elif self.round_number in Constants.ingroup_rounds:
        players = self.get_players()

        High_players = [p for p in players if p.participant.vars['senior'] == 'High']
        Low_players = [p for p in players if p.participant.vars['senior'] == 'Low']

        random.shuffle(High_players)
        random.shuffle(Low_players)
        print('shuffled Highs', High_players)
        print('shuffled Lows', Low_players)

        group_matrix = []

        # pop elements from M_players until it's empty
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



class Group(BaseGroup):
        pass



class Player(BasePlayer):

    # participant_vars_dump = models.StringField()
    payoff = models.CurrencyField()

    def get_partner(self):
        return self.get_others_in_group()[0]

    kept = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0, max=Constants.endowment,
    )

    sent = models.CurrencyField(
        doc="""Amount dictator decided to keep for himself""",
        min=0, max=Constants.endowment,
    )

