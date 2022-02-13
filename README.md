# Django Resume

[![author](https://img.shields.io/badge/author-Francisco&nbsp;Bustamante-red.svg)](https://www.linkedin.com/in/flsbustamante/) 
[![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/) 
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/chicolucio/django-resume/issues)
[![Build Status](https://app.travis-ci.com/chicolucio/django-resume.svg?branch=master)](https://app.travis-ci.com/chicolucio/django-resume)

Simple CV / resume Django app. Available at: https://resumeflsb.herokuapp.com/

## Usage

1. clone the repo
2. create a virtual environment with Python 3.8+ (Needed for Django 4.0)
3. activate the virtual environment
4. install dependencies
5. configure instance .env
6. run tests

```bash
git clone https://github.com/chicolucio/django-resume
cd django-resume
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
pytest
```

The HTML/CSS files in this repo were adapted from [this
video](https://www.youtube.com/watch?v=F5WXNI3Dq8U).

## Deploy and CI

1. create a Heroku instance
2. send config to Heroku
3. define a SECRET_KEY to the instance
4. set DEBUG=False
5. send code to Heroku

```bash
heroku create nameyourinstance

heroku config:set SECRET_KEY='set your secret key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com

git push heroku master --force
```

You can use the following function to generate your secret key:

```python
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

Sure, you can use an oneliner in your terminal:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

You can use the `.travis.yml` to config your Travis CI. And `.pyup.yml` to 
config PyUp.

## More

- [LinkedIn](https://www.linkedin.com/in/flsbustamante/)
- [Portfolio](https://franciscobustamante.com.br/portfolio)
- [Curriculum Vitae](https://franciscobustamante.com.br/about/)
