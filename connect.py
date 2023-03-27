import boto3

import config

database = boto3.resource(
    'dynamodb',
    endpoint_url = config.USER_STORAGE_URL,
    region_name = 'ru-central1',
    aws_access_key_id = config.AWS_PUBLIC_KEY,
    aws_secret_access_key = config.AWS_SECRET_KEY
)

forecast = database.Table('ИМЯ ВАШЕЙ ТАБЛИЦЫ')

