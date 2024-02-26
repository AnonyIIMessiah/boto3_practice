import boto3
client = boto3.client('ec2')
resp= client.describe_instances(Filters=[
  {  'Name': 'instance-state-name',
    'Values': ['terminated']
    }
])

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance id is {instance['InstanceId']}")