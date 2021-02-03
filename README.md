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

## How to deploy function to your Folder in Cloud
1. Copy this repo to your local machine.
2. Install **yc CLI utils** and choose your working folder. You can read more about this here:
```
https://cloud.yandex.ru/docs/cli/quickstart#install
```
3. Make the **deploy.sh** executable:
```
sudo chmod +x deploy.sh
```
4. Run **deploy.sh** by using command:
```
./deploy.sh
```
5. And its done. Congratulations, you just create your new Cloud Function for create preview from base image. Enjoy!