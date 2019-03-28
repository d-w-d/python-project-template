# PYTHON-VSCODE DEV-ENVIRONMENT SETUP

## What's This?

This is a template python project with instructions for setting up in [VSCode](https://code.visualstudio.com) with all the development bells and whistles.

## Why Visual Studio Code (VSCode)?

Writing serious code without an IDE or feature-rich text-editor is like trying to run in the olympics without shoes. So take the time to master at least one IDE/editor for your major software needs. I highly recommend Microsoft's text editor [Visual Studio Code](https://code.visualstudio.com) (often abbreviated to `VSCode`). Beware: VSCode is not to be confused with Microsoft's IDE [Visual Studio](https://visualstudio.microsoft.com)).

VSCode is free and its functionality is easily extended with plethora of community-written 'extensions' that make VSCode end up feeling more like a fully-fledged IDE than a text editor.

![Image of VSCode Editor](https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png)

VSCode is open-source and especially popular for web-development; it's best known for its javascript/typescript support, but its growing popularity means that extensions are becoming increasingly available across all major languages and configuration-file formats. (In addition to javascript, I've personally found it to be great for python, bash and php.)

## General Set Up

### Customizing VSCode with User and Workspace Settings

There is a small but non-negligible learning curve for VSCode. The single most important thing to understand is how you customize your experience. You do this by setting values in two special `json` files. One of these files is for your global 'user' settings, and the other is for your local 'workspace' settings.

The workspace settings go in your project directory within a `.vscode` folder. You can see one in this repository, with settings specific to python development. These workspace settings take precedence over your user settings.

VSCode comes with myriad settings, each with a default value that applies unless you override that value by providing a setting in your user and/or workspace settings. For example, VSCode's default tab size is given by the default setting `"editor.tabSize": 4`. If you add, for example, `"editor.tabSize": 2` to your user-settings `json` file, then your tab key will generate 2 spaces in all your files. If, however, in one of your workspaces you have the file `.vscode/settings.json` with `"editor.tabSize": 6`, then files in that folder will get 6 spaces, etc. etc.

### VSCode Extensions

The VSCode interface lets you easily search and install a host of awesome `extensions` that give VSCode additional powers. Here I want to mention some extensions that I recommend you install no matter what programming language you plan to use.

One such example is [Indent Rainbow](https://github.com/oderwat/vscode-indent-rainbow) that adds color to your indentation, helping you to trace your code blocks up and down the page. In general, when you add an extension, additional settings with defaults will be made available to your VSCode set up.

For example, if you install `Indent Rainbow`, then your default settings will receive entries prefixed with `indentRainbow`, such as this one:

```jsonc
{
    // ...,
    "indentRainbow.colors": [
        "rgba(255,255,64,0.07)",
        "rgba(127,255,127,0.07)",
        "rgba(255,127,255,0.07)",
        "rgba(79,236,236,0.07)"
    ]
    // ...
}
```

So if you want to customize the sequence of colors that show up when you indent blocks of code, then you'd copy this setting to your user or workspace `settings.json` file (and edit the cyclic sequence of colors).

These are the VSCode plugins that I recommend no matter what languages you plan to work with:

-   Trailing Spaces
-   Git Lens
-   Rainbow Brackets
-   Rainbow Indent
-   Better Comments

## Python Development

In addition to the general set-up recommendations given above, I'll now describe the extensions, scripts, configuration files and directory structure that I recommend whenever starting out on a python project. The idea of such a template repository is that you can simply run `git clone` in order to get going quickly and productively with a python project.

### Scripts, scripts, scripts

I highly recommend that you write scripts liberally when developing code. Any command or sequence of commands that you expect to perform routinely -- even if they seem trivial -- are best committed to a script. Why? First, even if the commands that you use to operate the code seem trivial now, they may not seem at all trivial when you come back to the code in a year. Second, others who use your code will be able to operate your codebase far more quickly and intelligently if you leave them scripts.

So choose a shell and commit yourself to attaining a blackbelt at that art form. I chose \`bash\`.

By convention, I reserve the underscore '\_' as my script-name prefix, and I like to give my scripts lengthy names so its clear what they're all about.

### Installing Python and Using Virtual Environments

#### Python Version 3.5+

This repo is designed for starting NEW python projects following guidelines and constraints for python 3.5 or higher. If your goal is take legacy code and integrate it with python3 scripts within this template project, then you have two basic approaches:

-   launch your e.g. legacy python2 script(s) as a shell process as suggested [here](https://stackoverflow.com/a/42229700/8620332) (recommended);
-   undertake a painful rehabilitation of your legacy code so that it is python3-compliant as outlined [here](https://docs.python.org/3/howto/pyporting.html) (not recommended).

#### Virtual Environment

Python has been around a while (since the early 90s) and so its many ways of managing executable versions and python packages has evolved into a confusing ecosystem of competing tools (`virtualenv`, `pipenv`, `pyvenv`, `venv`, `conda`, etc.) each claiming to be 'the right way'.

The approach taken is based on the [official python recommendation](https://docs.python.org/3/library/venv.html) to use the `venv` module when using python 3.6 or higher. I highly recommend you _memorize_ the following sequence as part of your python know-how:

```bash
    cd my_new_python_project
    /path/to/python3 -m venv VENV_NAME
    source VENV_NAME/bin/activate
    # ... do stuff ...
    deactivate
```

Sourcing the `activation` script adjusts your working shell by adding/altering the following `env` variables:

-   It adjusts PS1 so that your command prompt displays the name you gave to your virtual environment
-   It adds an env variable enabling the former value of PS1 to be restored upon deactivation; in my case that env var is `ITERM_ORIG_PS1`
-   It creates an env variable `VIRTUAL_ENV` pointing to the virtualenv directory you just created
-   It prepends your `PATH` env variable with a path pointing to `/path/to/my_new_python_project/.venv/bin`; this ensures that the first which

#### Installation on Mac

Mac comes with python2 installed. I recommend getting the latest build by installing it with homebrew: `brew install python`. Once installed, locate your python interpreter (`/usr/local/bin/python3` for brew version) and use this path to set the env variable `PYTHON_3_5_OR_HIGHER` in your `.env` file (see below).

#### Initialization Script

This repo includes a script called `_initial_setup.sh` that makes it easy and consistent to start up your python virtual environment. The first thing it does is to load in the contents of the `.env` file in order to locate the `python3` executable on your machine.

(The `.env` file is not committed to the git repo since, in general, it will contain passwords and directory structures that you want to keep confidential, so copy `.env-template` to `.env` and fill in the paths for `PYTHON_3_5_OR_HIGHER`, etc.)

`_initial_setup.sh` is designed to fail unless it is _sourced_ from your command line (and not executed with e.g. `sh`). Once it creates the python virtual environment and activates it, it upgrades pip and installs all packages specified in `requirements.txt` to your virtual environment.

Running `source _initial_setup.sh` is idempotent, so get in the habit of running regularly whenever you want to get up and running with your development. Once activated, your virtual environment's name `.venv` will be displayed at your command prompt.

#### Adding Packages

As you develop within your virtual environment, you'll be adding python packages using `pip install PACKAGENAME`, which will install the package to `.venv`. To make a permanent record of an installed package, run `sh _freeze_requirements` to get it added to `requirements.txt`. Once added to `requirements.txt`, this package will be installed/confirmed-as-installed whenever you run your `_initial_setup.sh` script.

#### Directory Structure

All scripts and configuration files are in the root directory. The source code for your application is in `src`. This repo includes a super simple application (`src/main.py`) that loads in and prints a variable from a simple example [homemade python package](https://www.programiz.com/python-programming/package). Once the virtual environment is activated you run your application using `_run_app.sh` (a simple wrapper around `python src/main.py`).

### VSCode Set Up

Many of the following features require the VSCode extension supported by Microsoft [Python](https://github.com/Microsoft/vscode-python). So search for and install `Python Extension Pack` which will install this and some other useful tools for developing python code.

#### Python Module Resolution in VSCode

VSCode equipped with the extensions just mentioned will analyze your code and flag a wide variety of errors. But VSCode needs to know where your code is. By default, it will look for python scripts in the root directory, but if you have your code in a nested dir, as we have here in `src`, then we need to let VSCode know this. To accomplish this:

-   For consistency, we want VSCode to analyze our code with the same interpreter that we'll be using to execute our code. To point VSCode to the interpreter in our virtual environment add `"python.pythonPath": ".venv/bin/python"` to `.vscode/settings.json`
-   Add the environment variable `PYTHONPATH` to your `.env` file and equate set it to colon-separated paths to any directory where you want VSCode to look for python scripts. In our case, we can minimally set it to `PYTHONPATH=src`.
-   To get VSCode to load in our `.env` file and digest the contents of the `PYTHONPATH` env variable, add `"python.envFile": "${workspaceRoot}/.env"` to `.vscode/settings.json`
-   There are two engines for VSCode intellisense -- 'Microsoft's' and 'Jedi'. To ensure we're using Microsoft's engine, add the setting `"python.jediEnabled": false` to `.vscode/settings.json`.

#### Intellisense in VSCode

Intellisense allows you to view and select intelligent options as you type code. For example, if you type out a class-instance handler and type and apply dot notation '.' then any available methods or properties provided by that class will be shown in a drop-down list. The steps given above will give you intellisense in VSCode. However, VSCode will also give 'snippet suggestions' in the same drop-down list. These are shortcuts for producing common syntax in python but, in my opinion, they are rarely helpful and get in the way of the more useful suggestions that result from the engine analyzing your code. I therefore recommend you switch them off when working with python by adding `"editor.snippetSuggestions": "none"` to `.vscode/settings.json`.

#### Auto-Formatting in VSCode

You do NOT want to spend time/effort lining up code blocks, tabbing brackets, etc. while coding. By getting your editor to automatically format your code according to industry standards, you'll save time and make it easier to collaborate with others. To enable auto-formatting in VSCode:

-   `pip install autopep8` (and freeze with `sh _freeze_requirements.sh`)
-   If it is not set in your user settings already, then add `"editor.formatOnSave": true` to your `.vscode/settings.json` file.
    -   Note: if you prefer not to have your code formatted on each save, then you can run formatting manually with `shift+option+f`
    -   Note: on some occasions you may want to save without formatting; this can be done by the key sequence `command+k;s` (`command+k` at the same time followed by pressing `s`)

#### Linting in VSCode

Auto-formatting normally solves formatting problems in our code. But we also want to see warnings of poor code features in the VSCode interface ahead of auto-formatting, and in cases where auto-formatting doesn't solve the problem (for example, by declaring unused variables). The process of analyzing functional code and automatically getting it into a state that follows best practices is known as 'linting'. The main linting tool in python is called `pylint`. To enable it in VSCode:

-   `pip install pylint` (and freeze with `sh _freeze_requirements.sh`)
-   Add `"python.linting.pylintEnabled": true` to `.vscode/settings.json`
-   Add a pylint configuration file `.pylintrc` to your root dir

Note: in addition to flagging problems in the VSCode interface, you can also run `pylint src` from the command line to analyze your code and print out a report.

#### Type Safety in VSCode

Python is a dynamically typed language, which basically means that types are applied loosely and not a big part of the traditional python mindset. However, seeing the success of typescript in the world of javascript, which also has very non-strict types, I am personally encouraged to apply typescript-like analysis in my VSCode experience. To enable type-safety analysis in VSCode we need to set up [mypy](http://mypy-lang.org):

-   Add `"python.linting.mypyEnabled": true` to `.vscode/settings.json`
-   `pip install mypy flake8-mypy` (and freeze with `sh _freeze_requirements.sh`)
    -   Note: to get `mypy` to work we seem to need the `flake8` linter, though we are not using `flake8` as our actual linter, rather, we're using `pylint`. I considered using `flake8` as the linter, but it seems less complete at this point in time than pylint; for example, it doesn't seem to support the flagging of unused global variables.
-   Add a mypy configuration file `mypy.ini` to your root dir

### Unit Testing

If you want to employ test-driven development, then you'll need to run python's tool for unit testing `pytest` from the root dir (or any files that you wish to target). `pytest` will look for functions in your code beginning with `test_`, run them, and report the results of the `assert` command.

This repo places all unit tests in files prefixed `test_*.py` (which is what `pytest` looks for) in the `tests` directory. You can then run tests by the command `pytest` in order to print out a testing report.
