import boto3
ec2 = boto3.resource('ec2')
#sns_client = boto3.client('sns')

backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]
def create_ebs_snapshot(volume_id, description):
    ec2 = boto3.client('ec2')  # Create an EC2 client

    response = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=description
    )

    return response['SnapshotId']

# Replace 'your_volume_id' with the actual volume ID and provide a suitable description
volume_id = 'vol-0776076559bda1e78'
snapshot_description = 'Snapshot created by Python script'

snapshot_id = create_ebs_snapshot(volume_id, snapshot_description)
print(f"Snapshot created with ID: {snapshot_id}")

'''
 sns_client.publish(
     TopicArn = '',
     Subject = 'EBS Snapshots',
     Message = str(snapshot_ids)
 )
'''