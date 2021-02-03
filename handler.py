import base64
import json

from io import BytesIO
from PIL import Image
from urllib.request import urlopen


def handler(event, context):
    parser = json.loads(event['body'])
    url = parser['queryStringParameters']["link"]

    result = urlopen(url=url)
    if result.getcode() != 200:
        return {
        'statusCode': 404,
        'body': 'problem with link',

        }

    imgdata = result.read()
    img = Image.open(BytesIO(imgdata))
    img = img.resize((65, 65), Image.ANTIALIAS)
    

    buff = BytesIO()
    img.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())

    return {
        'statusCode': 200,
        'body': f'{img_str}',
        }