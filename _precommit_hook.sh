#! /bin/bash

echo '''

    ======================
    RUNNING PRECOMMIT HOOK
    ======================

'''

echo ">>>>"$DONT_FORMAT_ON_CODE_COMMIT

if [ $DONT_FORMAT_ON_CODE_COMMIT ]; then
    echo """
        Skipping auto-format!!!
    """
else
    # Auto-format all python scripts
    .venv/bin/autopep8 -ir src/**
    .venv/bin/autopep8 -ir tests/**
fi
