from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
from statistics import median


class Subsession(BaseSubsession):
    def creating_session(self):
        assert len(self.get_players()) % 2 == 0, 'The number of players should be even'

    def split_on_income(self):
        ps = sorted(self.get_players(), key=lambda x: x.income)


        low = ps[:len(ps) // 2]
        high = ps[len(ps) // 2:]
        for p in low:
            p.participant.vars['senior'] = 'Low'
        for p in high:
            p.participant.vars['senior'] = 'High'
        print(p.participant.vars)

class Constants(BaseConstants):
    name_in_url = 'survey_v3'
    players_per_group = None
    num_rounds = 1

class Group(BaseGroup):

    pass

class Player(BasePlayer):

    subject_id = models.IntegerField(
        min=1,max=30,
        label='Subject ID'
    )

    gender = models.StringField(
        choices=['Male', 'Female'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    age = models.IntegerField(min=0,max=30,label='What is your age?', choices=range(18,31))

    city = models.StringField(choices=['Pune', 'Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Other'],
                              widget=widgets.RadioSelect,
                              label= 'What city are you residing in right now?')

    college = models.StringField(choices=['Poona College', 'Fergusson College', 'Bharti Vidyapeeth', 'Other'],
                                 widget=widgets.RadioSelect,
                                 label='What college are you studying in?')

    major = models.StringField(choices=['Economics', 'MBA', 'Other'],
                               widget=widgets.RadioSelect,
                               label='What is your major of study in college?')

    study_year = models.StringField(choices=['Undergraduate 1', 'Undergraduate 2', 'Undergraduate 3', 'Undergraduate 4', 'Postgraduate 1', 'Postgraduate 2', 'Other'],
                                    widget=widgets.RadioSelect,
                                    label='What year of your study are you in?')
    religion = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain'],
                                  widget=widgets.RadioSelect,
                                  label='What religion have you been brought up with?')

    income = models.IntegerField(min=0, max=100000000, label='''What is your family's monthly income? Please enter your best estimate in rupees in the box below.''')

    status_check = models.StringField(choices=[
                                                ['High', 'High Income'],
                                                ['Low', 'Low Income']
                                                ],
                                      widget=widgets.RadioSelect,
                                      label='Which financial status group were you assigned to?')

    info_check = models.StringField(choices=['Name', 'Religion'],
                                    widget=widgets.RadioSelect,
                                    label='What information will other participants NOT receive about you?'
                                    )

    def set_all_in_vars(self):
        self.participant.vars['age'] = self.age
        self.participant.vars['city'] = self.city
        self.participant.vars['college'] = self.college
        self.participant.vars['major'] = self.major
        self.participant.vars['study_year'] = self.study_year
        self.participant.vars['religion'] = self.religion
        self.participant.vars['income'] = self.income
        print(self.participant.vars)





