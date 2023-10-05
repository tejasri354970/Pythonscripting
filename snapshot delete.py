import boto3
def delete_ebs_snapshot(snapshot_id):
    ec2 = boto3.client('ec2')  # Create an EC2 client

    response = ec2.delete_snapshot(
        SnapshotId=snapshot_id
    )

    return response

# Replace 'your_snapshot_id' with the actual snapshot ID that you want to delete
snapshot_id = 'snap-009a6c96bd1267443'
response = delete_ebs_snapshot(snapshot_id)
print(f"Snapshot {snapshot_id} deletion response: {response}")
