import boto3
import time


# Create EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

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

def main():
    while True:
        try:
            state = get_instance_state()

            if state == 'stopped':
                start_instance()
            elif state == 'running':
                stop_instance()

        except Exception as e:
            print(f"An error occurred: {e}")

        # Adjust the sleep duration based on your preferred interval (in seconds)
        time.sleep(600)  # 10 minutes

if __name__ == "__main__":
    main()
