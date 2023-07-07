import boto3


def create(domain_name):
    cloudfront = boto3.client("cloudfront")
    s3_domain = f'{domain_name}.s3.ap-northeast-1.amazonaws.com'
    acm_arn = "arn:aws:acm:us-east-1:724412619408:certificate/7188221c-26b0-456c-a521-886b312407cf"
    result = cloudfront.create_distribution(
        DistributionConfig={
            "CallerReference": domain_name,
            "Aliases": {
                "Quantity": 1,
                "Items": [domain_name]
            },
            "DefaultRootObject": 'index.html',
            "Comment": domain_name,
            "Enabled": True,
            "Origins": {
                "Quantity": 1, 
                "Items": [
                    {
                        "Id": s3_domain,
                        "DomainName": s3_domain,
                        'OriginShield' : { 'Enabled': False },
                        "S3OriginConfig": {"OriginAccessIdentity": ''}
                    }
                ]
            },
            "DefaultCacheBehavior": {
                'AllowedMethods': {
				    'CachedMethods': {
					    'Items': ['HEAD','GET'],
					    'Quantity': 2,
				    },
				    'Items': ['HEAD', 'GET'],
				    'Quantity': 2,
			    },
                "TargetOriginId": s3_domain,
                "ViewerProtocolPolicy": 'redirect-to-https',
                'SmoothStreaming': False,
			    'Compress': True,
                "MinTTL": 1000,
                "ForwardedValues": {
                    "Cookies": {'Forward':'all'},
                    "Headers": {"Quantity": 0},
                    "QueryString": False,
                    "QueryStringCacheKeys": {"Quantity": 0},
                }
            },
            'ViewerCertificate': {
			# cname を設定する場合 ACM で発行した証明書を指定しないとディストリビューションが作成できない
			    'ACMCertificateArn': acm_arn,
			    'Certificate': acm_arn,
			    'CertificateSource': 'acm',
			    'MinimumProtocolVersion': 'TLSv1.2_2021',
			    'SSLSupportMethod': 'sni-only',
		    },
            'CustomErrorResponses': {
			    'Items': [
				    {
					    'ErrorCachingMinTTL': 600,
				        'ErrorCode': 404,
				        'ResponseCode': '404',
				        'ResponsePagePath': '/error.html',
				    },
				    {
					    'ErrorCachingMinTTL': 600,
					    'ErrorCode': 403,
					    'ResponseCode': '403',
					    'ResponsePagePath': '/error.html',
				    },
			    ],
			    'Quantity': 2, 
		    }
        }
    )
    return result


