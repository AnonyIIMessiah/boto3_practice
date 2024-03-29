import boto3
import json
s3_client=boto3.client('s3')
dynamodb=boto3.resource('dynamodb')
def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_filename=event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,Key=json_filename)
    jsonFileReader = json_object['Body'].read()
    jsonDict=json.loads(jsonFileReader)
    table=dynamodb.Table('employees')
    print(table)
    table.put_item(Item=jsonDict)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
