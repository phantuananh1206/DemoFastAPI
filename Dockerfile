FROM python:3.11-slim

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# RUN pip install poetry

# COPY pyproject.toml ./
# RUN poetry install

COPY . /src

WORKDIR /src

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
