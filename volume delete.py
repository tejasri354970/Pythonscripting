import boto3

# Create a boto3 client for EC2
ec2 = boto3.client('ec2')

def delete_volume(volume_id):
    try:
        response = ec2.delete_volume(VolumeId=volume_id)
        print(f"Volume {volume_id} deletion response: {response}")
    except Exception as e:
        print(f"Error deleting volume {volume_id}: {str(e)}")

# Call the function with the Volume ID you want to delete
delete_volume('vol-025884d9bd9a17e07')
