import boto3

def create_subdomain(domain_name, distribution):
    route53 = boto3.client("route53")
    params = {
        'HostedZoneId': "Z15GUTXJHUYAHD", #route53の該当ドメイン（今はhachipochi.net）のホストゾーンを指定する # TODO ssmのparameter storeを利用する
        'ChangeBatch': {
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': domain_name,
                        'Type': 'A',
                        'AliasTarget': {
                            'HostedZoneId': 'Z2FDTNDATAQYW2', # 固定で入れる # TODO ssmのparameter storeを利用する
                            'DNSName': f"{distribution['DomainName']}.",
                            'EvaluateTargetHealth': False
                        }
                    }
                }
            ]
        }
    }
    route53.change_resource_record_sets(**params)