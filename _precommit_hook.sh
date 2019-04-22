#! /bin/bash

echo '''

    ======================
    RUNNING PRECOMMIT HOOK
    ======================

'''

# Auto-format all python scripts
.venv/bin/autopep8 -ir src/**
.venv/bin/autopep8 -ir tests/**
git add .
