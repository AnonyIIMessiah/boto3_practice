import boto3
client=boto3.client('ec2')

instances=client.describe_instances()
used_amis = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])
# Remove duplicate amis
def remove_duplicates(amis):
    unique_amis=[]
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
    return unique_amis
unique_amis=remove_duplicates(used_amis)
print(unique_amis)
# get custom amis

custom_images=client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        }
    ],
    Owners= ['self']
)

# All amis present for user
custom_amis_list=[]
for image in custom_images['Images']:
    custom_amis_list.append(image['ImageId'])

# delete unused amis
for custom_ami in custom_amis_list:
    if custom_ami not in used_amis:
        print("Deregistering ami "+custom_ami)
        client.deregister_image(ImageId=custom_ami)