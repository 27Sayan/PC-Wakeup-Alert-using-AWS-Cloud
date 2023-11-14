import keyboard
import boto3
import json
import requests
import sys

# AWS Lambda function configuration
lambda_function_name = 'your_function-name' 
region_name = 'your_region_name'   

# API Gateway endpoint URL
api_gateway_url = 'your_api_url'

# Configure AWS Lambda client
lambda_client = boto3.client('lambda', region_name=region_name)

# Variable to track whether the first key event has been processed
key_processed = False

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
    global key_processed
    
    if event.event_type == keyboard.KEY_DOWN and not key_processed:
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

        # Mark that the key event has been processed
        key_processed = True
        
        # Unhook the keyboard event handler to stop further events
        keyboard.unhook_all()

# Hook the keyboard event handler
keyboard.hook(on_key_event)

try:
    print('Waiting for a key press...')
    keyboard.wait()

except KeyboardInterrupt:
    print('Keyboard event handling stopped.')
    keyboard.unhook_all()
