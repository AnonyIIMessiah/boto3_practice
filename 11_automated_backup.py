import boto3
import datetime

# EC2 instance ID
instance_id = 'YOUR_INSTANCE_ID'

# AMI tags
ami_name = 'Automated Backup - ' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# Create EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

def lambda_handler(event, context):
    try:
        # Create AMI
        response = ec2.create_image(
            InstanceId=instance_id,
            Name=ami_name,
            Description='Automated backup created by Lambda',
            NoReboot=True  # You can set NoReboot to False if you want to reboot the instance during the AMI creation process
        )

        # Add tags to the AMI (optional)
        ami_id = response['ImageId']
        ec2.create_tags(Resources=[ami_id], Tags=[{'Key': 'Backup', 'Value': 'AutomatedBackup'}])

        print(f"AMI {ami_id} created successfully.")

        return {
            'statusCode': 200,
            'body': 'Success'
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return {
            'statusCode': 500,
            'body': f"Error: {e}"
        }
