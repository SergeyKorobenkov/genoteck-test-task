## Genoteck test-task
This repo created for test-task for Genoteck company.

## Link to cloud function:
```
GET/POST https://functions.yandexcloud.net/d4e0b5a386mtqeocbs5t
```
### Required request-body:

```
{
    "queryStringParameters": {
        "link": "<string>"
    }
}
```


## How to create new function by API:

1) Look for Clouds where you can create new function, do request with Bearer Auth-Token:
```
GET https://resource-manager.api.cloud.yandex.net/resource-manager/v1/clouds
```

2) Look for Folders in Cloud where you can create new function. Do request with Bearer Auth-Token (Required cloudId as query-parameter):
```
GET https://resource-manager.api.cloud.yandex.net/resource-manager/v1/folders
```

3) Create your function. Do request with Bearer Auth-Token:
```
POST https://serverless-functions.api.cloud.yandex.net/functions/v1/functions
```
Required next parameters in request-body:
```
{
  "folderId": "string",
  "name": "string",
  "description": "string",
  "labels": "object"
}
```

### You can recieve your Bearer Auth-Token with this command:
```
curl -d "{\"yandexPassportOauthToken\":\"<IAM-TOKEN>\"}" "https://iam.api.cloud.yandex.net/iam/v1/tokens"
```
### How to find your IAM-TOKEN:
```
https://cloud.yandex.ru/docs/iam/concepts/authorization/iam-token
```