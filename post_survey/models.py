from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
from statistics import median


class Subsession(BaseSubsession):
    pass

class Constants(BaseConstants):
    name_in_url = 'post_survey'
    players_per_group = None
    num_rounds = 1

class Group(BaseGroup):
    pass

class Player(BasePlayer):


    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    state_origin = models.StringField(label= 'Did you grow up in Maharashtra?',
                                        choices=['Yes', 'No'],
                                        widget=widgets.RadioSelect)

    state_origin_text = models.StringField(label='If not, which state did you grow up in?',
                                    blank=True)

    mother_occupation = models.StringField(label='''What is your mother's job?''')

    father_occupation = models.StringField(label='''What is your father's job?''')

    caste_category = models.StringField(label= 'What caste category do you belong to?',
                                        choices=['General Caste', 'Other Backward Castes', 'Scheduled Castes', 'Scheduled Tribes', 'Others' ],
                                        widget=widgets.RadioSelect)

    caste_name = models.StringField(label='If you know the name of your caste or jaati, please enter it below.',
                                    blank=True)

    group_religion = models.StringField(choices=['0','1','2','3','4','5','6','7','8','9','10'],
                                 widget=widgets.RadioSelectHorizontal,
                                 label='Please rate on a scale from 0-10 how important your religion is for your sense of who you are, where 0 means not at all important and 10 means very important')

    group_class = models.StringField(choices=['0','1','2','3','4','5','6','7','8','9','10'],
                                        widget=widgets.RadioSelectHorizontal,
                                        label='Please rate on a scale from 0-10 how important your financial status is for your sense of who you are, where 0 means not at all important and 10 means very important')

    group_caste = models.StringField(choices=['0','1','2','3','4','5','6','7','8','9','10'],
                                        widget=widgets.RadioSelectHorizontal,
                                        label='Please rate on a scale from 0-10 how important your caste is for your sense of who you are, where 0 means not at all important and 10 means very important')

    group_india = models.StringField(choices=['0','1','2','3','4','5','6','7','8','9','10'],
                                        widget=widgets.RadioSelectHorizontal,
                                        label='Please rate on a scale from 0-10 how important being an Indian is for your sense of who you are, where 0 means not at all important and 10 means very important')

    group_maharashtra = models.StringField(choices=['0','1','2','3','4','5','6','7','8','9','10'],
                                        widget=widgets.RadioSelectHorizontal,
                                        label='Please rate on a scale from 0-10 how important being a Maharashtrian is for your sense of who you are, where 0 means not at all important and 10 means very important')

    exclusion = models.StringField(choices=['Often', 'Sometime', 'Rarely', 'Never'],
                                 widget=widgets.RadioSelect,
                                 label='Do you often feel excluded from mainstream Indian society?')

    safety = models.StringField(choices=['Often', 'Sometime', 'Rarely', 'Never'],
                                   widget=widgets.RadioSelect,
                                   label='Do you ever fear for your safety  in public spaces?')

    discrimination = models.StringField(choices=['Often', 'Sometime', 'Rarely', 'Never'],
                                   widget=widgets.RadioSelect,
                                   label='Do you often feel discriminated against?')

    vote_2019 = models.StringField(choices=['Yes', 'No'],
                                   widget=widgets.RadioSelect,
                                   label='Did you vote in the 2019 elections?')


    politics_interest = models.StringField(choices=['Very interested', 'Quite interested', 'Not so interested', 'Not at all interested'],
                               widget=widgets.RadioSelect,
                               label='How interested are you in politics?')

    politician_point = models.IntegerField(choices=[[1, 'Fully Agree'],
                 [2, 'Somewhat Agree'],
                 [3, 'Neither Agree Nor Disagree'],
                 [4, 'Somewhat Disagree'],
                 [5, 'Fully Disagree']],
                                        widget=widgets.RadioSelect,
                                        label='To what extent do you agree or disagree with the following statement: “There is no point in voting, the politicians will never listen to my concerns”')

    politician_religion = models.IntegerField(choices=[[1, 'Fully Agree'],
                 [2, 'Somewhat Agree'],
                 [3, 'Neither Agree Nor Disagree'],
                 [4, 'Somewhat Disagree'],
                 [5, 'Fully Disagree']],
                                        widget=widgets.RadioSelect,
                                        label='To what extent do you agree or disagree with the following statement: “A Muslim politician is more likely to represent my interests than a Hindu poltician”.')

    religion_attention = models.IntegerField(choices=[[1, 'Fully Agree'],
                 [2, 'Somewhat Agree'],
                 [3, 'Neither Agree Nor Disagree'],
                 [4, 'Somewhat Disagree'],
                 [5, 'Fully Disagree']],
                                        widget=widgets.RadioSelect,
                                        label='To what extent do you agree or disagree with the following statement: People I meet pay too much attention to my religion before getting to know me' )

    religion_interests = models.IntegerField(choices=[[1, 'Fully Agree'],
                 [2, 'Somewhat Agree'],
                 [3, 'Neither Agree Nor Disagree'],
                 [4, 'Somewhat Disagree'],
                 [5, 'Fully Disagree']],
                                     widget=widgets.RadioSelect,
                                     label='To what extent do you agree or disagree with the following statement: People from my religious community have similar interests and concerns')

    conflict = models.IntegerField(choices=[[1, 'Fully Agree'],
                                                      [2, 'Somewhat Agree'],
                                                      [3, 'Neither Agree Nor Disagree'],
                                                      [4, 'Somewhat Disagree'],
                                                      [5, 'Fully Disagree']],
                                             widget=widgets.RadioSelect,
                                             label='Minorities should make every effort to avoid conflict with Hindus')

    position = models.IntegerField(choices=[[1, 'Fully Agree'],
                                            [2, 'Somewhat Agree'],
                                            [3, 'Neither Agree Nor Disagree'],
                                            [4, 'Somewhat Disagree'],
                                            [5, 'Fully Disagree']],
                                   widget=widgets.RadioSelect,
                                   label='People from my religious community should work together to improve their position in society')

    representation = models.IntegerField(choices=[[1, 'Fully Agree'],
                                            [2, 'Somewhat Agree'],
                                            [3, 'Neither Agree Nor Disagree'],
                                            [4, 'Somewhat Disagree'],
                                            [5, 'Fully Disagree']],
                                   widget=widgets.RadioSelect,
                                   label='Measures should be taken to increase the representation of minorities in politics ')

    chicken = models.IntegerField(choices=[[1, 'Very willing'],
                                                  [2, 'Somewhat willing'],
                                                  [3, 'Not so willing'],
                                                  [4, 'Not at all willing']],
                                         widget=widgets.RadioSelect,
                                         label='How willing are you to consume chicken?')

    lamb = models.IntegerField(choices=[[1, 'Very willing'],
                                           [2, 'Somewhat willing'],
                                           [3, 'Not so willing'],
                                           [4, 'Not at all willing']],
                                  widget=widgets.RadioSelect,
                                  label='How willing are you to consume lamb?')

    beef = models.IntegerField(choices=[[1, 'Very willing'],
                                           [2, 'Somewhat willing'],
                                           [3, 'Not so willing'],
                                           [4, 'Not at all willing']],
                                  widget=widgets.RadioSelect,
                                  label='How willing are you to consume beef?')

    pork = models.IntegerField(choices=[[1, 'Very willing'],
                                           [2, 'Somewhat willing'],
                                           [3, 'Not so willing'],
                                           [4, 'Not at all willing']],
                                  widget=widgets.RadioSelect,
                                  label='How willing are you to consume pork?')

