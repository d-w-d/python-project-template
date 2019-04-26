#! /bin/bash

echo '''

    ======================
    RUNNING PRECOMMIT HOOK
    ======================

'''

if [[ ! -z ${DONT_FORMAT_ON_CODE_COMMIT+x} ]]; then
    # Auto-format all python scripts
    .venv/bin/autopep8 -ir src/**
    .venv/bin/autopep8 -ir tests/**
else
    echo """
        Skipping auto-format!!!
    """
fi
