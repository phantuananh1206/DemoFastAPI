python -m venv venv
source venv/Scripts/activate
pip freeze > requirements.txt
pip install poetry
poetry install