#! /bin/bash

# Check you have an activated venv and you're in the right directory for it
if [[ $VIRTUAL_ENV == $PWD'/.venv' ]]; then
    echo "Upgrading pip in present virtual environment"
    pip install --upgrade pip
    echo "Installing requirements in present virtual environment"
    pip install -r requirements.txt
else
    echo "
    ---------------------------------------------------------------------------------
        You need to have THIS directory's .venv activated to install requirements!

        You are now in:    $PWD
        Your venv is from: $([ -z ${VIRTUAL_ENV+x} ] && echo "NONE" || echo "$VIRTUAL_ENV")
    ---------------------------------------------------------------------------------
    "
fi
