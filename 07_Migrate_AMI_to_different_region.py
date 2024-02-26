import boto3

##Part-1 Create Images

source_region = 'ap-south-1'
ec2 = boto3.resource('ec2',region_name = source_region)

instances=ec2.instance.filter(InstanceIds=['i-0c701cbfe12538107'])

image_ids=[]

for instance in instances:
    image = instance.create_image(Name='Demo Boto - '+instance.id, Description='Demo Boto'+instance.id)
    image_ids.append(image.id)
print("Images to be copied "+image_ids)

##Part-2 Wait for images to be available
#Get waiter for image_available

client =boto3.client('ec2',region_name=source_region)
waiter=client.get_waiter('image_available')

#wait for images to be ready
waiter.wait(Filters=[{
    'Name': 'image_id',
    'Values': images_ids
}])



# Part-3 Copy images to other regions

destination_region = 'us-east-1'
client = boto3.client('ec2',region_name=destination_region)
for image_id in image_ids:
    client.copy_image(Name='Boto3 Copy'+image_id, SourceImageId=image_id, SourceRegion='ap-south-1')
