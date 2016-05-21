import boto3
import json

def lambda_handler(event, context):
    
    print(event)
    
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName='seagullgameQ')

    queue.send_message(MessageBody=json.dumps(event))
     
    return {"new score passed to sqs queue": event['score']}
