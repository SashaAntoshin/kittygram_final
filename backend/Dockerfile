FROM python:3.12-slim

WORKDIR /app

# Установи системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install gunicorn==23.0.0

COPY requirements.txt .

# Обнови pip и установи Cython (опционально)
RUN pip install --upgrade pip setuptools wheel cython

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Создаем директории для статических файлов и медиа
RUN mkdir -p collected_static media

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:9000", "kittygram_backend.wsgi"]