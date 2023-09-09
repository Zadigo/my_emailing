# %%
import os
import pathlib
import requests
import random
from django import setup
from django.conf import settings

# %%
BASE_DIR = pathlib.Path('.').absolute()

# %%
try:
    settings.configure(
        BASE_DIR=BASE_DIR,
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'campaigns',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    )
except:
    pass

# %%
os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'True')

# %%
setup()


# %%
def create_leads():
    from campaigns import models
    campaign = models.Campaign.objects.create(**{
        'name': 'SIEC'
    })

    url = 'https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/liste-des-prenoms-2020@aix-en-provence/records?limit=60'
    response = requests.get(url)
    if response.ok:
        data = response.json()['results']
        for _ in range(len(data)):
            firstname = random.choice(data)['nom']
            lastname = random.choice(data)['nom']
            
            models.Lead.objects.create(**{
                'campaign': campaign,
                'firstname': firstname.lower().title(),
                'lastname': lastname.lower().title(),
                'email': 'cariboj656@nickolis.com'
            })


# %%
create_leads()
