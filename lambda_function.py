import json
import boto3
import string
import random

# initialize session client
def lambda_handler(event, context):
    
    N = 10

    newPassword = ''.join(random.choices(string.ascii_uppercase + 
                                string.digit, k=N))

    client = boto3.client('secretsmanager')
 

    getRes = client.get_secret_value(
        SecretId = 'sample-secret'
    )
    current_secrets = json.loads(getRes['SecretString'])
    
    current_secrets.update({
        "password" : newPassword
    })
    
    #print(str(json.dumps(current_secrets)))
    
    response = client.put_secret_value(
        SecretId = 'sample-secret'
        SecretString=str(json.dumps(current_secrets))
    )
    #print(response)
