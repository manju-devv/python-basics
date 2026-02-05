# pip - preferred installer program
# Some people also say “Pip Installs Packages”

# pip is Python's package manager.
# It helps you download, install, update, and remove external Python libraries.


# A virtual environment (venv) is an isolated Python workspace where you can install project-specific
# packages without affecting your main (global) Python installation or other projects.

# Virtual environment = separate Python setup per project.

#  Why do we need a Virtual Environment?
# ️ Avoid package version conflicts

# Different projects often need different versions of the same library.

# Example:

# Project A → needs django 3

# Project B → needs django 5

# Without venv  → they clash
# With venv  → each project gets its own version safely.

# to install use pip3 install virtialenv
# after
# python3 -m venv env
# to activate : source env/bin/activate


# flow
# python3 -m venv env
# source env/bin/activate


# ✅ pip3 install <package>
# 👉 Uses whatever pip3 your system finds first in PATH.
# That might be:
# system Python
# Homebrew Python
# some other Python
# NOT your virtual env 😬
# So sometimes packages install in the wrong place.
# ✅ python -m pip install <package>
# 👉 Uses pip that belongs to THIS Python interpreter.
# If you’re in:
# virtual env → installs into that env ✅
# system python → installs globally
# It is 100% guaranteed correct.


import pandas

print(pandas.__version__)


# pip3 freeze
# pip3 freeze shows a list of all Python packages + their exact versions that are installed in your current environment.


# pip3 freeze > requirements.txt
# creates a requirements.txt file that has all the dependencies


# and to install all those use
# pip3 install -r requirements.txt
