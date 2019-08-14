export PIPENV_VENV_IN_PROJECT=1
export PIPENV_IGNORE_VIRTUALENVS=1

python3 -m pipenv install 

python3 -m pipenv run python --version