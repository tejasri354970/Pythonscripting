import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Specify the existing key pair name, VPC ID, and security group ID as variables
key_pair_name = 'priya'
vpc_id = 'vpc-08ed4915b3cf826b6'
security_group_id = 'sg-01b7ad51f9b3501b5'
subnet_id = 'subnet-013cb27cc9619f6fc'  # Replace with your actual subnet ID

# Specify the tag key and value
tag_key = 'Name'
tag_value = 'Swetha'  # Replace with the desired name

# Launch an EC2 instance with a tag
resp = ec2_client.run_instances(
    ImageId='ami-0f5ee92e2d63afc18',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName=key_pair_name,
    SecurityGroupIds=[security_group_id],
    SubnetId=subnet_id,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': tag_key,
                    'Value': tag_value
                },
            ]
        },
    ]
)

# Print the instance IDs
for instance in resp['Instances']:
    print(instance['InstanceId'])
