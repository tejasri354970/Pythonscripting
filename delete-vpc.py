import boto3

# Create a boto3 client for EC2
ec2 = boto3.client('ec2')

def delete_vpc(vpc_id):
    try:
        response = ec2.delete_vpc(VpcId=vpc_id)
        print(f"VPC {vpc_id} deletion response: {response}")
    except Exception as e:
        print(f"Error deleting VPC {vpc_id}: {str(e)}")

# List of VPC IDs you want to delete
vpc_ids_to_delete = ['vpc-07c3c9157590854ac']

# Call the function to delete each VPC in the list
for vpc_id in vpc_ids_to_delete:
    delete_vpc(vpc_id)
