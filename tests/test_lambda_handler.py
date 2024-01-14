from unittest import TestCase
from wxflightpath.lambda_handler import *
import re
class TestLambda_handler(TestCase):
    event1 = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/path/to/resource",
        "rawQueryString": "flightpath=LFRU,LFRU",
        "cookies": [
            "cookie1",
            "cookie2"
        ],
        "headers": {
            "Header1": "value1",
            "Header2": "value1,value2"
        },
        "queryStringParameters": {
            "flightpath":'LFPX,LFRU'
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "api-id",
            "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                        "notBefore": "May 28 12:30:02 2019 GMT",
                        "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
            },
            "authorizer": {
                "jwt": {
                    "claims": {
                        "claim1": "value1",
                        "claim2": "value2"
                    },
                    "scopes": [
                        "scope1",
                        "scope2"
                    ]
                }
            },
            "domainName": "id.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "id",
            "http": {
                "method": "POST",
                "path": "/path/to/resource",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1/32",
                "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
        },
        "body": [
            "LFRO",
            "LFRU"
        ],
        "pathParameters": {
            "parameter1": "value1"
        },
        "isBase64Encoded": True,
        "stageVariables": {
            "stageVariable1": "value1",
            "stageVariable2": "value2"
        }
    }
    event2 = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/path/to/resource",
        "rawQueryString": "pilot=None",
        "cookies": [
            "cookie1",
            "cookie2"
        ],
        "headers": {
            "Header1": "value1",
            "Header2": "value1,value2"
        },
        "queryStringParameters": {
            "pilot": 'none'
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "api-id",
            "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                        "notBefore": "May 28 12:30:02 2019 GMT",
                        "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
            },
            "authorizer": {
                "jwt": {
                    "claims": {
                        "claim1": "value1",
                        "claim2": "value2"
                    },
                    "scopes": [
                        "scope1",
                        "scope2"
                    ]
                }
            },
            "domainName": "id.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "id",
            "http": {
                "method": "POST",
                "path": "/path/to/resource",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1/32",
                "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
        },
        "body": [
            "LFRO",
            "LFRU"
        ],
        "pathParameters": {
            "parameter1": "value1"
        },
        "isBase64Encoded": True,
        "stageVariables": {
            "stageVariable1": "value1",
            "stageVariable2": "value2"
        }
    }
    result1=faster_lambda_handler(event1, context={})
    result2 = faster_lambda_handler(event2, context={})
    #experimental test
    """
    pattern1 = re.compile(
        r'https://pilot-briefer\.s3\.amazonaws\.com/'
        r'([^/]+)\.txt\?AWSAccessKeyId=[A-Za-z0-9]+&Signature=[A-Za-z0-9%]+&Expires=\d+'
    )
    
    pattern2 = re.compile(
        r'https://pilot-briefer\.s3\.amazonaws\.com/[^/]+'
    )
    """
    def test_init(self):
        self.assertNotEquals(self.result1['headers']['Location'], None)
        #experimental#self.assertEquals(self.pattern2.match(self.result1['headers']['Location']), True)
        self.assertEquals(self.result1['statusCode'], 200)
        self.assertEquals(self.result2['body'], '<b>Invalid request query param try a request with the following query parameter pattern /?flightpath=LFRO,LFPX</b>')
        self.assertEquals(self.result2['statusCode'], 400)