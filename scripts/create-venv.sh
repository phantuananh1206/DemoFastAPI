python -m venv venv
venv/Scripts/activate
pip freeze > requirements.txt
pip install poetry
poetry install