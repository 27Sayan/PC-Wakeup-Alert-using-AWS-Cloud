import keyboard
import boto3
import sys
import json
import requests

# AWS Lambda function configuration
lambda_function_name = 'your_function_name' 
region_name = 'your_region_name'  

# API Gateway endpoint URL
api_gateway_url = 'your_api_url'

# Configure AWS Lambda client
lambda_client = boto3.client('lambda', region_name=region_name)

def invoke_lambda_function(payload):
    try:
        response = lambda_client.invoke(
            FunctionName=lambda_function_name,
            InvocationType='Event',     
            Payload=json.dumps(payload)
        )
        print('Lambda function invoked. Response:', response)
    except Exception as e:
        print('Error invoking Lambda function:', str(e))

def send_to_api(payload):
    try:
        response = requests.post(api_gateway_url, json=payload)
        print('API Gateway response:', response.status_code)
    except Exception as e:
        print('Error sending POST request to API Gateway:', str(e))

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        print(f'Key {event.name} was pressed')
        
        # Create JSON payload
        payload = {
            "body-json": {
                "pcName": event.name
            }
        }
        
        # Trigger the Lambda function when a key is pressed
        invoke_lambda_function(payload)

        # Send the payload to API Gateway
        send_to_api(payload)

        # Unhook the keyboard and exit the script
        keyboard.unhook_all()
        sys.exit()

# Hook the keyboard event handler
keyboard.hook(on_key_event)

try:
    print('Waiting for a key press...')
    keyboard.wait()

except KeyboardInterrupt:
    print('Keyboard event handling stopped.')
