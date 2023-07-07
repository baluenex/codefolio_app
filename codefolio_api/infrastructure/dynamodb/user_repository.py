import boto3
import os
from datetime import datetime


def create(username, email):
    users_table = boto3.resource("dynamodb").Table(f"{os.environ['ENV']}_codefolio_users")
    users_table.put_item(Item={
        "id": username,
        "email": email,
        "user_type": "indivisual",
        "created_at": datetime.now().isoformat()
    })


def get(username):
    users_table = boto3.resource("dynamodb").Table(f"{os.environ['ENV']}_codefolio_users")
    response = users_table.get_item(Key={"id": username})
    if "Item" in response:
        return response["Item"]
    else:
        return {}


def update(username, key, value):
    users_table = boto3.resource("dynamodb").Table(f"{os.environ['ENV']}_codefolio_users")
    users_table.update_item(
        Key={
            "id": username
        },
        UpdateExpression=f"set {key} = :value",
        ExpressionAttributeValues={
            #":key": key,
            ":value": value
        }
    )