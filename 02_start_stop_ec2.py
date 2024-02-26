import boto3
client= boto3.client('ec2')
# response = client.stop_instances(
#     InstanceIds=[
#         'i-08d07786086e96549',
#     ],
    
# )

# response = client.start_instances(
#     InstanceIds=[
#         'i-08d07786086e96549',
#     ],
    
# )

# print(response['StartingInstances'][0]['CurrentState']['Name'])
response = client.terminate_instances(
    InstanceIds=[
        'i-08d07786086e96549',
    ],
    
)

print(response['TerminatingInstances'][0]['CurrentState']['Name'])