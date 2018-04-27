# Newbie Project

Data Management Tool based on Django Admin

## Pre-requisitions
`Python 3` `Django 2`

    pip install django

    pip install git+git://github.com/sshwsfc/xadmin.git@django2

## Before Push to Github
Clear your personal data:

    python clear.py

## After Pull from Github
Initialize database:

    python build.py new

## When models change significantly
Rebuild database:

    python build.py rebuild

[回到顶部](# Newbie Project)