# Image de l'API de sentiment.
#
#   docker build -t sentiment-api .
#   docker run --rm -p 8000:8000 -e API_KEYS="une-cle-de-16-caracteres:client" sentiment-api
#
# Le modèle n'est jamais versionné (règle 2 du cours) : l'image le réentraîne pendant sa
# construction, avec les mêmes commandes que la CI (make_demo.py puis train.py).
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Seulement ce que l'API et l'entraînement utilisent : pas mlflow, ni streamlit, ni les outils de test
RUN pip install "pandas==2.2.*" "scikit-learn==1.5.*" "joblib==1.4.*" \
    "fastapi==0.115.*" "uvicorn==0.30.*" "pydantic==2.9.*"

COPY src/ src/
COPY sentiment_app/ sentiment_app/
COPY api/ api/

# Entraînement pendant la construction : le modèle est dans l'image, pas dans Git
RUN mkdir -p data models && python src/make_demo.py && python src/train.py

# L'API ne tourne pas en root
RUN useradd --create-home api && chown -R api /app
USER api

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/v1/health')"

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
