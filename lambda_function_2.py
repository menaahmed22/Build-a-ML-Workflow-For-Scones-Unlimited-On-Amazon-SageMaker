import json
import boto3
import base64
#from sagemaker.serializers import IdentitySerializer
#import sagemaker.session as session

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-01-23-13-24-30-904'  ## TODO: fill in
runtime = boto3.Session().client('sagemaker-runtime')


def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    
    # Instantiate a Predictor

    # For this model the IdentitySerializer needs to be "image/png"

    # Make a prediction:

    image_data = event['body']['image_data']
    response = runtime.invoke_endpoint(EndpointName = ENDPOINT, ContentType = 'image/png',Body = image)
    predictions = json.loads(response['Body'].read().decode())
    # We return the data back to the Step Function #Create a new key to the event named   "inferences"  
    event['body']["inferences"] = predictions
    #print(json.dumps(event))
    
    return {
        'statusCode': 200,
        'body': event

        }