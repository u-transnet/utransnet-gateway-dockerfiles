[![English](https://thumb.ibb.co/jDrVkd/gb.png)](README.md) [![Russian](https://thumb.ibb.co/cjYMrJ/ru.png)](README.ru.md)

# utransnet-gateway-dockerfiles
Данный докер представляет собой [utransnet-gateway](https://github.com/u-transnet/utransnet-gateway) и минимально необходимая среда окружения описанная в файле docker-compose.yml и запускающаяся соответствующей командой.

## Installation
Установите docker версии 17.12.0-ce и выше и docker-compose версии 1.18.0 и выше.
```
git clone https://github.com/u-transnet/utransnet-gateway-dockerfiles
```

## Getting started
Прежде всего необходимо создать папку configs и создать там локальные файлы конфигурации, которые не синхроинизируются с git'ом.

**Configuration example**

Путь: configs/settings.py</br>
**Файл локальных настроек проекта**
Файл configs/settings.py соответствует файлу в settings/local.py с тем отличием, что в данный файл необходимо
добавить/переопределить следующие настройки.
``` 
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

## Start and manage
```
docker-compose up # Запуск web-интерфейса и всех шлюзов
docker-compose up -d # Запуск в фоновом режиме
docker-compose up nginx db web # Запуск только web-интерфейса
docker compose up db bts_trns # Запуск только шлюза BitShares - Transnet
docker compose up db trns_bts # Запуск только шлюза Transnet - BitShares
docker-compose up --build # Запуск с пересборкой образов
docker-compose up --build --no-cache # Запуск с пересборкой образов с очисткой кэша
docker container stop $(docker ps -a -q) # Остановка всех контейнеров
docker rm $(docker ps -a -q) # Удаление всех контейнеров
```


## Contributing
We'd love to have your helping hand on our project! See [CONTRIBUTING.md](CONTRIBUTING.md) for more information on what we're looking for and how to get started.

## License
Project is under the MIT license. See [LICENSE](LICENSE) for more information.

