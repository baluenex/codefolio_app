from infrastructure.cloudfront import cloudfront_repository
from infrastructure.route53 import route53_repository

def create(event, context):
    top_domain = event['queryStringParameters']['top_domain']
    domain_name = f"{top_domain}.hachipochi.net"
    # cloudfrontを作成する
    result = cloudfront_repository.create(domain_name)
    distribution = result["Distribution"]["Id"]
    # サブドメインのAliasを作成する
    route53_repository.create_subdomain(domain_name, distribution)


# test用コード
if __name__ == "__main__":
    event = {
        'queryStringParameters' : {
            'top_domain' : 'hoge'
        }
    }
    context = {}
    create(event, context)
