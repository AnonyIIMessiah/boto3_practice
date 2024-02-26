import boto3


# EC2 instance ID
instance_id = 'i-0f455a7442533d077'

# Create EC2 client
ec2 = boto3.client('ec2',region_name="us-east-1")

def lambda_handler(event, context):
    try:
        state = get_instance_state()

        if state == 'stopped':
            start_instance()
        elif state == 'running':
            stop_instance()

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

def get_instance_state():
    response = ec2.describe_instances(InstanceIds=[instance_id])
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    return state

def start_instance():
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} started.")

def stop_instance():
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} stopped.")
