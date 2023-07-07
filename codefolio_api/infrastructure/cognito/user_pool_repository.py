import boto3


def get(access_token):
    client = boto3.client('cognito-idp', region_name="ap-northeast-1")
    response = client.get_user(
        AccessToken=access_token
    )

    return response["Username"]