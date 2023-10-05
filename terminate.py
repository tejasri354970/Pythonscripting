import boto3

# List of instance IDs to terminate
instance_ids_to_terminate = ['i-00335849988e11d12', 'i-00240ebc363759e19', 'i-03874f8169bf0eff5']

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Terminate instances
response = ec2_client.terminate_instances(InstanceIds=instance_ids_to_terminate)

# Print the termination results
for instance in response['TerminatingInstances']:
    print(f"Instance ID: {instance['InstanceId']}, Current State: {instance['CurrentState']['Name']}")
