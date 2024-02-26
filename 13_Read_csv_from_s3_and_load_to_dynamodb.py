import boto3
import json
s3_client=boto3.client("s3")
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3_filename=event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket,Key=s3_filename)
    data = resp['Body'].read().decode("utf-8")
    employees=data.split("\n")
    for emp in employees:
        print(emp)
        emp_data = emp.split(",")
        try:
            # TODO: write code...
            table.put_item(
                Item = {
                    "id":emp_data[0],
                    "name":emp_data[1],
                    "location":emp_data[2]
                })
        except Exception as e:
            print("EOF")
        # add it tii dynamodb
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
