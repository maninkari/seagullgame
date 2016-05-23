import boto3
from botocore.exceptions import ClientError
import base64
import json
import datetime

def lambda_handler(event, context):
    
    dynamoPooh = boto3.resource('dynamodb').Table("seagullgame")
    dynamoScore = boto3.resource('dynamodb').Table("seagullgameScore")

    for record in event['Records']:
        
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        
        colleagueFlag = True if "pooh" in data else False
        print(colleagueFlag)
        
        if colleagueFlag:
            collname = data['pooh']
            
            print "Decoded payload: %s" % payload
            print "Decoded colleague name: %s" % collname
            
            rec = {'colleague':collname,'key2':'1'}
            print(rec)
            
            response = dynamoPooh.update_item( 
                Key={ 'colleague': collname }, 
                UpdateExpression="SET contador = if_not_exists(contador, :start) + :inc", 
                ExpressionAttributeValues={ ':inc': 1, ':start': 0, }, 
                ReturnValues="UPDATED_NEW"
            )
            
            print(response)  
            return response
        
        else:    
            tempscore = data['score']
            scoredate = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
            
            print "Decoded payload: %s" % payload
            print "Decoded score: %s" % tempscore
            print "Score date: %s" % scoredate
            
            response = 'inicio';
            
            try:
                # if it's a new record, update score, date and number of games played
                response = dynamoScore.update_item( 
                    Key={ 'id': 1 }, 
                    UpdateExpression="SET score = :newscore, scoredate = :scoredate, games = games + :inc", 
                    ConditionExpression="score < :newscore", 
                    ExpressionAttributeValues={ ':newscore': tempscore, ':scoredate': scoredate, ':inc': 1}, 
                    ReturnValues="UPDATED_NEW"
                )
            except ClientError as e:
                if e.response['Error']['Code'] == "ConditionalCheckFailedException":
                    
                    print(e.response['Error']['Message'])
                    
                    # if it's not a new record just increase the number of games
                    response = dynamoScore.update_item( 
                        Key={ 'id': 1 }, 
                        UpdateExpression="SET games = games + :inc",
                        ExpressionAttributeValues={ ':inc': 1},
                        ReturnValues="UPDATED_NEW"
                    )
                    
                    print("UpdateItem succeeded: ")
                    print(response)
                else:
                    raise
            else:
                print("UpdateItem succeeded: ")
                print(response)
            
            return response
    
