from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import random

class Intro(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class ngo1(Page):

    form_model = 'player'
    form_fields = ['allocation2']

    timeout_submission = { 'allocation2': 90}

    def before_next_page(self):
        self.player.allocation1_1 = 100 - self.player.allocation2

    def vars_for_template(self):
        return {
            'image_path1': 'ngo/R1.jpg',
            'image_path2': 'ngo/R2.jpg',
        }

    # def error_message(self, values):
    #     print('values is', values)
    #     if values["allocation1_1"] + values["allocation2"] != 100:
    #         return 'The total amount must add up to 100'

class ngo2(Page):

    form_model = 'player'
    form_fields = ['allocation3']

    timeout_submission = {'allocation3': 90}

    def before_next_page(self):
        self.player.allocation1_2 = 100 - self.player.allocation3

    def vars_for_template(self):
        return {
            'image_path1': 'ngo/R1.jpg',
            'image_path3': 'ngo/R3.jpg',
        }

    # def error_message(self, values):
    #     print('values is', values)
    #     if values["allocation1_2"] + values["allocation3"] != 100:
    #         return 'The total amount must add up to 100'

class ngo3(Page):

    form_model = 'player'
    form_fields = ['allocation4']

    timeout_submission = {'allocation4': 90}

    def before_next_page(self):
        self.player.allocation1_3 = 100 - self.player.allocation4

    def vars_for_template(self):
        return {
            'image_path1': 'ngo/R1.jpg',
            'image_path4': 'ngo/R4.jpg',
        }

    # def error_message(self, values):
    #     print('values is', values)
    #     if values["allocation1_3"] + values["allocation4"] != 100:
    #         return 'The total amount must add up to 100'

class ngo4(Page):

    form_model = 'player'
    form_fields = ['allocation5']

    timeout_submission = {'allocation5': 90}

    def before_next_page(self):
        self.player.allocation1_4 = 100 - self.player.allocation5

    def vars_for_template(self):
        return {
            'image_path1': 'ngo/R1.jpg',
            'image_path5': 'ngo/R5.jpg',
        }

    # def error_message(self, values):
    #     print('values is', values)
    #     if values["allocation1_4"] + values["allocation5"] != 100:
    #         return 'The total amount must add up to 100'




class Process(Page):
    def before_next_page(self):
        self.participant.vars['choice_ngo_payoff'] = random.randint(1,4)

        if self.participant.vars['choice_ngo_payoff'] == 1:
            self.player.allocation_self = self.player.allocation1_1
            self.player.allocation_ngo = self.player.allocation2
        elif self.participant.vars['choice_ngo_payoff'] == 2:
            self.player.allocation_self = self.player.allocation1_2
            self.player.allocation_ngo = self.player.allocation3
        elif self.participant.vars['choice_ngo_payoff'] == 3:
            self.player.allocation_self = self.player.allocation1_3
            self.player.allocation_ngo = self.player.allocation4
        elif self.participant.vars['choice_ngo_payoff'] == 4:
            self.player.allocation_self = self.player.allocation1_4
            self.player.allocation_ngo = self.player.allocation5


        self.participant.vars['ngo_payoff'] = self.player.allocation_self

        self.participant.vars['game_excluded'] = random.randint(1,3)

        if self.participant.vars['game_excluded'] == 1:

            self.participant.payoff = c(100) + self.participant.vars[
                'payoff_dictator'] + self.participant.vars['ngo_payoff']
            self.participant.vars['pd_payoff'] = self.participant.vars['payoff_prisoner_sym']

        elif self.participant.vars['game_excluded'] == 2:

            self.participant.payoff = c(100) + self.participant.vars['payoff_prisoner_sym']  + self.participant.vars['ngo_payoff']
            self.participant.vars['pd_payoff'] = self.participant.vars['payoff_prisoner_sym']

        elif self.participant.vars['game_excluded'] == 3:

            self.participant.payoff = c(100) + self.participant.vars['payoff_prisoner_sym'] + self.participant.vars[
                'payoff_dictator']
            self.participant.vars['pd_payoff'] = self.participant.vars['payoff_prisoner_sym']

        self.player.participant_vars_dump = str(self.participant.vars)
        print('Player kept INR', self.player.allocation_self)

class Thanks(Page):
    def vars_for_template(self):
        return dict(
            ngo_number = self.participant.vars['choice_ngo_payoff'],
            game_excluded = self.participant.vars['game_excluded']
        )




start_pages = [
    Intro
]

end_pages = [
    Process,
    Thanks
]

initial_page_sequence = [
    ngo1,
    ngo2,
    ngo3,
    ngo4

]

page_sequence = [
]


class MyPage(Page):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()


for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (MyPage,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])

page_sequence = start_pages + page_sequence + end_pages