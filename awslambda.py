import json
import boto3

def lambda_handler(event, context):
    sesclient = boto3.client("ses", region_name="ap-south-1")
    
    try:
        emailResponse = sesclient.send_email(
            Destination = {
                "ToAddresses": [
                    "Destination/ Reciever email address"
                ],
            },
            Message={
                "Body":{
                    "Text":{
                        "Data": "Email from lambda"
                    }
                },
                "Subject": {
                    "Data": "Your PC has been activated."
                },
            },
            Source= "Source/ Sender email address."
        )
        response = {
            "statusCode": 200,
            "body": json.dumps("Email sent successfully!")
        }
    except Exception as e:
        print(e)
        response = {
            "statusCode": 500,
            "body": json.dumps("Failed to send email.")
        }

    return response
