# Newbie Project

Data Management Tool based on Django XAdmin

## Pre-requisitions
`Python 3` `Django 2` `XAdmin for Django 2`

    pip install django

    pip install git+git://github.com/sshwsfc/xadmin.git@django2

## Fix
`\Lib\site-packages\xadmin\views\list.py line 75`
-text = mark_safe(wrap % text)
+text = mark_safe(wrap.replace('%s', text))

## Before Push to Github
Clear your personal data:

    python clear.py

## After Pull from Github
Initialize database:

    python build.py new

## When models change significantly
Rebuild database:

    python build.py rebuild
