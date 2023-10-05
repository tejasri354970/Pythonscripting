import boto3

# Create a boto3 client for EC2
ec2 = boto3.client('ec2')

def create_vpc(cidr_block, vpc_name):
    try:
        response = ec2.create_vpc(
            CidrBlock=cidr_block,
            TagSpecifications=[
                {
                    'ResourceType': 'vpc',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': vpc_name
                        },
                    ]
                },
            ]
        )
        vpc_id = response['Vpc']['VpcId']
        print(f"VPC created: {vpc_id}")
        return vpc_id
    except Exception as e:
        print(f"Error creating VPC: {str(e)}")
        return None

# Call the function to create a VPC with desired CIDR block and name
created_vpc_id = create_vpc(cidr_block='173.0.0.0/16', vpc_name='MyVPC')
