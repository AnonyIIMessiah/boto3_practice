import boto3
ec2 = boto3.resource('ec2')
# print(ec2.instances.all)
for instance in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1d']
    }
]):
    print('Instance id is '+instance.instance_id+" type is "+instance.instance_type)