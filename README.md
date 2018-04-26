# newbie

Data Management Tool based on Django Admin

# Pre-requesitions
Python 3; Django 2; Django Suit 0.2; Django Suit Dashboard

    pip install django

    pip install django-suit

    pip install django-suit-dashboard

# Before Push to Github
Clear your personal data:

    python clear.py

# After Pull from Github
Initialize database:

    python build.py new

# When models change significantly
Rebuild database:

    python build.py rebuild
