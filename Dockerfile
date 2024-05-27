FROM python:3.9

# Установим необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libopencv-dev \
    libjpeg-dev \
    zlib1g-dev

# Обновление pip до последней версии
RUN pip install --upgrade pip

# Установим рабочую директорию
WORKDIR /app

# Скопируем файл requirements.txt и установим зависимости
COPY format_image/requirements.txt ./
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

# Скопируем исходный код приложения
COPY ./format_image ./format_image

# Определим команду по умолчанию
CMD ["python3", "format_image/manage.py", "runserver", "0.0.0.0:8000"]
