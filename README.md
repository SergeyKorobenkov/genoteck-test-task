## Genoteck test-task
Тестовое задания для компании Genoteck. Создание Cloud Function в сервисе Yandex.Cloud, для переработки изображение в превью размерами 65х65, возвращаемое в формате base64.

## Ссылка на развернутую функцию:
```
GET/POST https://functions.yandexcloud.net/d4e0b5a386mtqeocbs5t
```
### Формат тела запроса при обращении к функции (application/json): 

```
{
    "queryStringParameters": {
        "link": "<string>"
    }
}
```

## Как развернуть функцию в Yandex.Cloud
1. Склонируйте данный репозиторий.
2. Установите и сконфигурируйте **yc CLI утилиту**. Подробнее о том как это делается можно почиать тут:
```
https://cloud.yandex.ru/docs/cli/quickstart#install
```
3. Сделайте файл **deploy.sh** исполняемым:
```
sudo chmod +x deploy.sh
```
4. Запустите **deploy.sh**:
```
./deploy.sh
```
5. Готово, теперь вы обладатель новой Cloud Function!
