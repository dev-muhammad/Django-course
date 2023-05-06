## Урок 11

# Автодокуменатация Swagger

## Содержание

1. Open API 3
2. Пакеты автодокументации
3. Настройка пакета drf-spectacular
4. Fixture

## Команда создания фикстуры

```
python manage.py dumpdata myapp.MyModel --indent 4 > fixtures/my_model.json
```

## Команда импорта из фикстуры

```
python manage.py loaddata fixtures/my_model.json
```
