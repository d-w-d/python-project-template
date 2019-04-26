#! /bin/bash

### Set your environment variables in file '.env' before sourcing this script.
### Source this script before running/working on your python3 project.
### The main logic of this script is placed in the main() function.
### We only want the main function to be called if this script is sourced (not sh-ed);
### (that way we can export environment variables defined herein or in .env)
### This script uses a 'trick' to tell if it's being sourced or sh-ed; see below.

main() {

    clear
    echo """
        =======================================================

                Initializing Python Virtual Environment

        =======================================================
    """

    sleep 1

    ### 1. Get rid of caches NOT in .venv
    find . -type d ! -path './.venv/*' -name '__pycache__' -exec rm -rf {} +
    find . -type d ! -path './.venv/*' -name '.pytest_cache' -exec rm -rf {} +
    find . -type d ! -path './.venv/*' -name '.pytest_cache' -exec rm -rf {} +

    ### 2. Load vars defined in .env
    if [ -f $PWD/.env ]; then
        echo "Loading env vars from .env"
        eval $(cat .env | sed 's/^/export /')
    else
        echo "No .env file found!"
        return 1
    fi

    ### 3. Check for existence of `.venv` dir
    if [ ! -d $PWD/.venv ]; then
        echo "Virtual Environment Not Found -- Creating '.venv'"
        $PYTHON_3_5_OR_HIGHER -m venv .venv
    fi

    ### 4. Activate VENV
    source ./.venv/bin/activate

    ### 5. Install package dependencies for project
    if [[ $1 == 'pip' ]]; then
        # Specify 'pip' to use pip install
        echo "Installing dependencies with pip"
        bash _pip_install.sh
    else
        # Default installation is with pipenv
        echo "Installing dependencies with pipenv"
        PIPENV_VERBOSITY=-1 pipenv install --dev
    fi

    ### 6. Link git pre-commit-hook script
    ln -fs $PWD/_precommit_hook.sh $PWD/.git/hooks/pre-commit

}

## Trick to check if this script is being sourced or sh-ed; executes 'main' iff sourced
unset BASH_SOURCE 2>/dev/null
test ".$0" == ".$BASH_SOURCE" && echo "You must <SOURCE> (not SH) this script!!!" || main "$@"
