import boto3
ec2= boto3.resource('ec2')
sns_client=boto3.client('sns')
backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]
snapshot_ids = []
for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot =  vol.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:732910247554:Boto3-trial',
    Subject='Boto3-trial',
    Message = str(snapshot_ids)
)