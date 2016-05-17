import boto3
import json

def lambda_handler(event, context):
    
    print(event)
     
    client = boto3.client('kinesis')
    
    response = client.put_record(
        StreamName='pooh',
        Data=json.dumps({"pooh": event['colleague']}),
        PartitionKey='seagull'
    )
     
    return { "action": {"pooh": event['colleague']}, "kinesis_response":response }
