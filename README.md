# utransnet-gateway

Данный докер представляет собой utransnet-gateway и минимально необходимая среда окружения описанная в файле docker-compose.yml и запускающаяся соответствующей командой.

# Предустановки
Прежде всего необходимо создать папку configs и создать там локальные файлы конфигурации, которые не синхроинизируются с git'ом.

**Примеры конфигураций**

Путь: configs/settings.py</br>
**Файл локальных настроек проекта**
```
from .production import * 

ALLOWED_HOSTS = ['web']

DATABASES = {  
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
} 
```

Путь: configs/nginx.conf
Конфигурация nginx сервера, который запускается как часть минимально необходимой среды окружения 

# Запуск и управление
```
docker-compose up # Запуск
docker-compose up -d # Запуск в фоновом режиме
docker-compose up --build # Запуск с пересборкой образов
docker container stop $(docker ps -a -q) # Остановка всех контейнеров
docker rm $(docker ps -a -q) # Удаление всех контейнеров
```

