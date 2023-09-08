import json
import boto3
import string
import random

# initialize session client
def lambda_handler(event, context):
    
    N = 10

    newPassword = ''.join(random.choices(string.ascii_uppercase + 
                                string.digits, k=N))

    client = boto3.client('secretsmanager')
 

    getRes = client.get_secret_value(
        SecretId = 'SECRET_NAME'
    )
    current_secrets = json.loads(getRes['SecretString'])
    
    current_secrets.update({
        "KEY_TO_ROTATE" : newPassword
    })
    
    #print(str(json.dumps(current_secrets)))
    
    response = client.put_secret_value(
        SecretId = 'SECRET_NAME',
        SecretString=str(json.dumps(current_secrets))
    )
    #print(response)
