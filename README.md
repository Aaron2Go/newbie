# newbie

Data Management Tool based on Django Admin

# Pre-requisitions
'Python 3' 'Django 2'

    pip install django

    pip install grappelli

    pip install feedparser

# Before Push to Github
Clear your personal data:

    python clear.py

# After Pull from Github
Initialize database:

    python build.py new

# When models change significantly
Rebuild database:

    python build.py rebuild
