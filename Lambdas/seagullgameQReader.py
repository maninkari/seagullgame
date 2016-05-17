
import boto3
import base64
import json

def lambda_handler(event, context):
    
    client = boto3.resource('dynamodb').Table("seagullgame")

    #print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        colleague = json.loads(payload)
        collname = colleague['pooh']
        
        print "Decoded payload: %s" % payload
        print "Decoded colleague name: %s" % collname
        
        rec = {'colleague':collname,'key2':'1'}
        print(rec)
        
        # colleagues must have been setup in dynamoDB first 
                
        response = client.update_item( 
            Key={ 'colleague': collname }, 
            UpdateExpression="SET contador = if_not_exists(contador, :start) + :inc", 
            ExpressionAttributeValues={ ':inc': 1, ':start': 0, }, 
            ReturnValues="UPDATED_NEW"
        )
        
        print(response)  
        
    return 'Successfully processed {} records.'.format(len(event['Records']))
    
    
