import boto3
import json

def lambda_handler(event, context):
    
    print(event)
    
    client = boto3.client('kinesis')
    
    response = client.put_record(
        StreamName='pooh',
        Data=json.dumps({"score": event['score']}),
        PartitionKey='seagull'
    )
     
    return { "action": {"score": event['score']}, "kinesis_response":response }
