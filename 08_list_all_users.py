import boto3

client=boto3.client('iam')

response = client.list_users()
# print(response)
for users in response['Users']:
    print(users['UserName'])