# PYTHON-VSCODE DEV-ENVIRONMENT SETUP

## What's This?

This is a template python project with instructions for setting up in [VSCode](https://code.visualstudio.com) with all the development bells and whistles.

## Why Visual Studio Code (VSCode)?

Writing serious code without an IDE or feature-rich text-editor is like trying to run in the olympics without shoes. So take the time to master at least one IDE/editor for your major software needs. I recommend Microsoft's text editor [Visual Studio Code](https://code.visualstudio.com) (often abbreviated to `VSCode`). Beware: VSCode is not to be confused with Microsoft's IDE [Visual Studio](https://visualstudio.microsoft.com)).

VSCode is free and its functionality can be easily extended by choosing from the many community-written 'extensions' that make VSCode end up feeling more like a fully-fledged IDE than a text editor.

![Image of VSCode Editor](https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png)

VSCode is open-source and especially popular for web-development; it's best known for its javascript/typescript support, but its growing popularity means that extensions are becoming increasingly available across all major languages and configuration-file formats.

## General Set Up

### Installing VSCode

If you're a Mac user, then I recommend that whenever you can install something via homebrew, you install it via homebrew.

```bash
brew search vscode
==> Casks
visual-studio-code  visual-studio-code-insiders

brew cask install visual-studio-code
```

If you're using Linux or PC, then try searching for it in your package manager; if unavailable, then download the application from [here](https://code.visualstudio.com).

### Launching VSCode from Command Line

VSCode on a Mac comes with a command-line tool `code`, which I almost always use to open files or directories directly in VSCode:

```bash
code -n XXX
```

I use this so often that I've created an alias for it: `alias alvsc='code -n'` allowing me to open the PWD like so `alvsc .`.

### Customizing VSCode with User and Workspace Settings

There is a small but non-negligible learning curve for VSCode. The single most important thing to understand is how you customize your experience. You do this by setting values in two special `json` files. One of these files is for your global 'User Settings', and the other is for your local 'Workspace Settings'.

To get to an interface to adjust either of these sets of settings, go to `Code > Preferences > Settings`. You'll get shown an interface that lets you choose between `User Settings` and `Workspace Settings`; under the hood, this interface is adjusting values in simple JSON files. To see the raw JSON files, you can click on the icon with curly brackets near the top right corner of the settings interface.

When you create any non-default `Workspace Settings` in the UI, VSCode will generate a corresponding `.vscode` folder in your project root directory and will place a `settings.json` file in it. This is was determines the way VSCode and its extensions behave for files _in this folder_. You can see one in this repository, with settings specific to python development. These workspace settings take precedence over your `User Settings`. (Likewise, when you set global `User Settings`, a JSON file is updated somewhere on your system; on a Mac, this file is located at `~/Library/Application\ Support/Code/User/settings.json`).

VSCode comes with myriad possible settings to place in these json files. For example, if you want to increase the size of the displayed text, you can add the following key-value pair to your user or workspace json file:

```jsonc
{
  //...
  "window.zoomLevel": 1
  //...
}
```

If you do NOT place such a key-value pair in one of your json files, then VSCode will apply a default value. In the example above, you can see the description of the setting and its default value by searching for `window.zoomLevel` in the settings UI.

Another example: VSCode's default tab size is given by the default setting `"editor.tabSize": 4`. If you add, for example, `"editor.tabSize": 2` to your user-settings `json` file, then your tab key will generate 2 spaces in all files that you open and use tab in in VSCode. If, however, in one of your work spaces you have the file `.vscode/settings.json` with `"editor.tabSize": 6`, then files in that particular folder will get 6 spaces, etc. etc.

### VSCode Extensions

The VSCode interface lets you easily search and install a host of `extensions` that give VSCode additional powers. Here I want to mention some extensions that I recommend you install no matter what programming language you plan to use.

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

- Trailing Spaces
- Git Lens
- Rainbow Brackets
- Rainbow Indent
- Better Comments

## Python Development

In addition to the general set-up recommendations given above, I'll now describe the extensions, scripts, configuration files and directory structure that I recommend when starting out on a python3 project, and as embodied in this repo. The idea of such a template repository is that you can run `git clone [this repo url on github]` in order to get going quickly and productively with a python project.

### Scripting

I recommend that you write scripts liberally when developing code. Any command or sequence of commands that you expect to perform routinely -- even if they seem trivial -- are best committed to a script. There are three reasons for this:

1. Even if the commands that you use to operate the code seem trivial to you now, they may not seem at all trivial when you come back to the code in a year.
2. Others who use your code will be able to operate your codebase far more quickly and intelligently if you leave them well-labelled scripts.
3. Scripts also provide a sensible place to put comments to make the operation of your code base clear and easy-to-use.

So choose a shell-script protocol and commit yourself to attaining a black belt at that art form. This repo uses \`bash\`.

By convention, I reserve the underscore '\_' as my script-name prefix, and I like to give my scripts lengthy names so it's clear what they're all about.

### Python3 Versioning, Virtual Environments & Package Management

#### Python Version 3.5+

This repo is designed for starting NEW python projects following guidelines and constraints for python 3.5 or higher. If your goal is take legacy code in python2 and integrate it with python3 scripts within this template project, then you'll have to choose between two basic approaches:

- launch your legacy python2 script(s) as a shell process as suggested [here](https://stackoverflow.com/a/42229700/8620332) (recommended);
- undertake a painful rehabilitation of your legacy code so that it is python3-compliant as outlined [here](https://docs.python.org/3/howto/pyporting.html) (not recommended).

If you want to run your project with a specific version of python, e.g. python3.6, then it's best to install that version directly using the main package manager on your OS (`homebrew`, `apt`, `yum`, etc.). If that is not an option, then the next-best thing is to use the [pyenv](https://github.com/pyenv/pyenv) tool. In any case, I recommend getting the latest version of python3, which will be available from your OS package manager.

Once installed on your OS, locate your python3 executable and use the full path to that executable to set the env variable `PYTHON_3_5_OR_HIGHER` in your `.env` file (see below).

#### Virtual Environments

Python has been around a while (since the early 90s) and so its many ways of managing executable versions and packages has evolved into a confusing ecosystem of competing tools (`virtualenv`, `pipenv`, `pyvenv`, `venv`, `conda`, etc.) each claiming to be 'the right way'.

The approach taken here is based on the [official python recommendation](https://docs.python.org/3/library/venv.html) to use the `venv` module when using python 3.6 or higher. I highly recommend you _memorize_ the following sequence as part of your general python know-how:

```bash
    cd my_new_python_project
    /path/to/python3 -m venv VENV_NAME
    source VENV_NAME/bin/activate
    # ... do stuff ...
    deactivate
```

Sourcing the `activate` script adjusts your working shell by adding/altering the following `env` variables:

- It adjusts `$PS1` so that your command prompt displays the name you gave to your virtual environment
- It adds an `env` variable enabling the former value of `$PS1` to be restored upon deactivation; on my Mac that `env` variable is `ITERM_ORIG_PS1`
- It creates an `env` variable `VIRTUAL_ENV` pointing to the virtual-environment directory you just activated
- It prepends your `env` variable `$PATH` with a path pointing to `/path/to/my_new_python_project/.venv/bin`; this ensures that the first python executable found by the `which` tool will be linked to the `python3` executable you used to create the virtual-environment folder.

<!-- (Note: although this repo will also use the `pipenv` tool (see below), and this tool can also be used to create virtual environments, this repo uses the recommended `python3 -m venv VENV_NAME` approach to creating and activating virtual environments because the equivalent way of doing this with `pipenv` is, IMO, convoluted and confusing.) -->

WHen you want to deactivate your virtual environment, just use the command `deactivate`.

#### Package Management

The 'classic' way to install and manage packages is using `pip`. When you create a virtual environment with `python3` as this repo requires, then your active instance of `pip` will be given within your local virtual-env directory (in this repo, that's `.venv/bin/pip`). You could then use pip to install packages (e.g. `pip install requests`) and, on the classic approach, you could then "freeze" requirements by the command `pip freeze > requirements.txt`, which outputs all packages locally installed to `.venv` to get listed in the output file `requirements.txt`.

The more modern way to manage packages is with the `pipenv` tool. `pipenv` was designed to handle _everything_ to do with virtual environments and package management, but we're only using it here for package management. Unlike `pip`, the `pipenv` tool will generate a "lock file" that enables deterministic builds and handles potentially conflicting dependency-package requirements. (This is analogous to `Gemfile.lock` in ruby and `package-lock.json` in node; see [here](https://pipenv.readthedocs.io/en/latest/) for more info on the subject.)

So, to operate this repo, you need to have `pipenv` globally installed on your system. To get `pipenv` either install it with your OS package manager (e.g. `brew install pipenv`), or run the following global commands (i.e. not with a virtual environment activated):

```bash
pip3 install pipenv
### Test for success:
which pipenv
```

By the way, this repo also includes a script `_freeze_requirements.sh` which will record all packages installed to your project's virtual environment in the file `requirements.txt`. So if you run into difficulties with `pipenv` (which I did recently when installing on a raspberry pi), you can fall back to the 'classic' way of managing packages; just run script `_pip_install.sh` to install the contents of `requirements.txt` to your venv, and use `_freeze_requirements.sh` to update `requirements.txt` for version control.

### Operating This Repo

#### Initialization Script

This repo includes a script called `_initial_setup.sh` that makes it easy and consistent to start up your python virtual environment.

The first thing this script does is to load in the contents of the `.env` file in order to locate the `python3` executable on your machine. (The `.env` file is not committed to the git repo since, in general, it will contain passwords and directory structures that you want to keep confidential, so copy `.env-template` to `.env` and fill in the paths for `PYTHON_3_5_OR_HIGHER`, etc.)

`_initial_setup.sh` is designed to fail unless it is _sourced_ from your command line (and not executed with e.g. `sh`).

<!-- Once it creates the python virtual environment and activates it, it upgrades pip and installs all packages specified in `requirements.txt` to your virtual environment. -->

Once it creates the python virtual environment and activates it, it uses `pipenv` to install requirements specified in the `Pipfile`.

Running `source _initial_setup.sh` is an idempotent process, so it doesn't hurt to run it multiple times, and you are encourgaed of getting into the habit of running this script regularly to make sure your acting within a fully-configured development mode. Once activated, your virtual environment's name `.venv` will be displayed at your command prompt.

#### Adding Packages

As you develop your coe within your virtual environment, you'll be adding python packages using `pipenv install PACKAGENAME` or `pipenv install --dev PACKAGENAME`, which will install the new package to `.venv` and add it to the `Pipfile` and `Pipefile.lock` files.

I recommend that you install packages without the `--dev` flag iff the package will be needed at application runtime (e.g. `flask`). If the package is only needed for development (e.g. `pytest`), then use `--dev`.

#### Directory Structure

All scripts and configuration files are in the root directory. The source code for your application is in `src`. This repo includes a super simple application (`src/main.py`) that loads in and prints a variable from a simple example [homemade python package](https://www.programiz.com/python-programming/package). Once the virtual environment is activated you run your application using `_run_app.sh` (a simple wrapper around `python src/main.py`).

### VSCode Set Up

Many of the following features require the VSCode extension supported by Microsoft [Python](https://github.com/Microsoft/vscode-python). So search for and install `Python Extension Pack` which will install this and some other useful tools for developing python code.

#### Python Module Resolution in VSCode

VSCode equipped with the extensions just mentioned will analyze your code and flag a wide variety of issues and errors. But VSCode needs to know where your code is. By default, it will look for python scripts in the root directory, but if you have your code in a nested dir, such as we have here in `src`, then we need to let VSCode know this. To accomplish this:

- For consistency, we want VSCode to analyze our code with the same interpreter that we'll be using to execute our code. To point VSCode to the interpreter in our virtual environment, add `"python.pythonPath": ".venv/bin/python"` to `.vscode/settings.json`
- Add the environment variable `PYTHONPATH` to your `.env` file and set it to colon-separated paths to any directory where you want VSCode to look for python scripts. In our case, we can minimally want to set it to `PYTHONPATH=src`.
- To get VSCode to load in our `.env` file and digest the contents of the `PYTHONPATH` `env` variable, add `"python.envFile": "${workspaceRoot}/.env"` to `.vscode/settings.json`
- There are two engines for VSCode intellisense -- 'Microsoft's' and 'Jedi'. To ensure we're using Microsoft's engine, add the setting `"python.jediEnabled": false` to `.vscode/settings.json`.

#### Intellisense in VSCode

Intellisense allows you to view and select intelligent options as you type code. For example, if you type out a class-instance handler and type and apply dot notation '.' then any available methods or properties provided by that class will be shown in a drop-down list. The steps given above will give you intellisense in VSCode. However, VSCode will also give 'snippet suggestions' in the same drop-down list. These are shortcuts for producing common syntax in python but, in my opinion, they are rarely helpful and they get in the way of the more useful suggestions that result from the engine analyzing your code. I therefore recommend you switch off these snippet suggestions when working with python code by adding `"editor.snippetSuggestions": "none"` to `.vscode/settings.json`.

#### Auto-Formatting in VSCode

You do NOT want to spend time/effort lining up code blocks, tabbing brackets, etc. while coding. By getting your editor to automatically format your code according to industry standards, you'll save time and make it easier to collaborate with others. To enable auto-formatting in VSCode with the popular `autopep8` library:

- Run `pipenv install --dev autopep8`
- If it is not set in your user settings already, then add `"editor.formatOnSave": true` to your `.vscode/settings.json` file.
  - Note: if you prefer not to have your code formatted on each save, then you can run formatting manually with `shift+option+f`
  - Note: on some occasions you may want to save without formatting; this can be done by the key sequence `command+k;s` (`command+k` at the same time followed by pressing `s` separately.)

#### Auto-Formatting with Git Pre-Commit Hook

To ensure that we have consistent code formatting across developers' contributions, this repo includes a script called `_precommit_hook.sh`. The initialization script will link this script to `.git/hooks/pre-commit`, which is what `git` looks to run just before running the commit. With this in place, `autopep8` will run and format your code whenever you try to add a git commit.

#### Linting in VSCode

Auto-formatting normally solves formatting problems in our code. But we also want to see warnings of poor code features in the VSCode interface ahead of auto-formatting, and in cases where auto-formatting doesn't solve the problem (for example, when you declare an unused variable). The process of analyzing functional code and automatically getting it into a state that follows best practices is known as 'linting'. The main linting tool in python is called `pylint`. To enable it in VSCode:

- `pipenv install --dev pylint`
- Add `"python.linting.pylintEnabled": true` to `.vscode/settings.json`
- Add a pylint configuration file `.pylintrc` to your root dir

Note: in addition to flagging problems in the VSCode interface, you can also run `pylint src` from the command line to analyze your code in the `src` directory and print out a report (or run `sh _lint_code.sh`). This can be useful in continuous-integration scenarios where you want your code to pass certain quality-control standards before getting merged or deployed.

#### Type Safety in VSCode

Python is a dynamically typed language, which basically means that types are applied loosely and not a big part of the traditional python mindset. However, seeing the success of typescript in the world of javascript (which also has very non-strict types),I am personally encouraged to apply typescript-like analysis to my python code and visualized with VSCode. To enable type-safety analysis in VSCode, we need to set up [mypy](http://mypy-lang.org):

- Add `"python.linting.mypyEnabled": true` to `.vscode/settings.json`
- `pipenv install --dev mypy flake8-mypy`
  - Note: to get `mypy` to work we seem to need the `flake8` linter, though we are not using `flake8` as our actual linter, rather, we're using `pylint`. I considered using `flake8` as the linter, but it seems less complete at this point in time than `pylint`; for example, it doesn't seem to support the flagging of unused global variables.
- Add a mypy configuration file `mypy.ini` to your root dir in order to customize how strict you want typing analysis to be applied. (The settings provided in this repo are very strict!)

### Unit Testing

If you want to employ test-driven development, then you'll need to run python's tool for unit testing `pytest` from the root dir (or any files that you wish to target). `pytest` will look for functions in your code beginning with `test_`, run them, and report the results of the `assert` command.

This repo places all unit tests in files prefixed `test_*.py` (which is what `pytest` looks for) in the `tests` directory. You can then run tests by the command `pytest --verbose tests` in order to print out a testing report to screen. You can also run these tests with the script `_tests.sh`. If any of these tests fail then they will cause most continuous-integration pipelines to fail, thus providing a safety mechanism when committing code.

If all goes well, then you'll have a rich python-coding experience with VSCode. Enjoy!

![](https://s3.amazonaws.com/dwds-misc/vscode-python-screenshot.png)
