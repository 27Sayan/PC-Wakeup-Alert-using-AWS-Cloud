import json
import boto3

def lambda_handler(event, context):
    sesclient = boto3.client("ses", region_name="your_region_name")
    
    emailResponse = sesclient.send_email(
        Destination = {
            "ToAddresses": [
                "destination/receiver_email_address"
            ],
        },
        Message={
            "Body":{
                "Text":{
                    "Data": "Email from lambda"
                }
            },
            "Subject": {
                "Data": "Email from mes acc"
            },
        },
    Source= "sender_email_address"
    )