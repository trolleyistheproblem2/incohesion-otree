from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'incohesion_prime_v1',
        'display_name': "Incohesion - Prime_v1",
        'num_demo_participants': 4,
        'app_sequence': ['survey_v3', 'prime', 'prisoner_v1', 'prime_2', 'dictator_v1','prime_3', 'ngo', 'post_survey'],
    },
    {
        'name': 'incohesion_control_v1',
        'display_name': "Incohesion - Placebo_v1",
        'num_demo_participants': 4,
        'app_sequence': ['survey_v3', 'placebo', 'prisoner_v1', 'placebo_2', 'dictator_v1','placebo_3', 'ngo', 'post_survey'],
    },
{
        'name': 'incohesion_prime_v2',
        'display_name': "Incohesion - Prime_v2",
        'num_demo_participants': 4,
        'app_sequence': ['survey_v3', 'prime', 'prisoner_v2', 'prime_2', 'dictator_v2','prime_3', 'ngo', 'post_survey'],
    },
    {
        'name': 'incohesion_control_v2',
        'display_name': "Incohesion - Placebo_v2",
        'num_demo_participants': 4,
        'app_sequence': ['survey_v3', 'placebo', 'prisoner_v2', 'placebo_2', 'dictator_v2','placebo_3', 'ngo', 'post_survey'],
    },
    {
        'name': 'ngo',
        'display_name': "ngo",
        'num_demo_participants': 1,
        'app_sequence': ['ngo'],
    },
{
        'name': 'post_survey',
        'display_name': "post_survey",
        'num_demo_participants': 1,
        'app_sequence': ['post_survey'],
    },
{
        'name': 'prisoner_v1',
        'display_name': "prisoner_v1",
        'num_demo_participants': 4,
        'app_sequence': ['prisoner_v1'],
    }


]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'INR'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'k)kndh8y(qgsfv2!q(yiz!$5qduzn#5+cc4n8enh&ko&io=e2)'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
