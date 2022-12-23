# устанавливаем базовый образ
FROM python:3.9-alpine

# Устанавка рабочего директория внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /open_cart_test

# Копирование зависимостей
# Для того чтобы не пересобирать их каждый раз при сборке образа
COPY requirements.txt .

# Установка зависимостей
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Этот параметр можно переопределить при СОЗДАНИИ контейнера т.е. run команде
# например: sudo docker run tests:latest pytest --browser MicrosoftEdge --url http://192.168.0.207:8081/
# sudo docker run tests:latest - запустит с дефолтными параметрами
#CMD ["pytest", "--browser", "chrome", "--url", "http://192.168.0.207:8081/"]

# Этот параметр дополняет, а не переписывает, но надо всегда указывать входные параметры
# например: sudo docker run tests:latest --browser MicrosoftEdge --url http://192.168.0.207:8081/
ENTRYPOINT ["pytest"]
