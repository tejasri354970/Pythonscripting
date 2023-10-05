import boto3

# Create a Boto3 EC2 client
client = boto3.client('ec2')

# Replace 'instance_id_to_start' with the actual instance IDs you want to start
instance_ids_to_start = ['i-0b9b5b422890687ac', 'i-07cd4fe25fec59d43', 'i-07c8e920108ec4971']

# Start instances
client.start_instances(InstanceIds=instance_ids_to_start)

# Wait for instances to start (optional)
# You might want to wait a bit before fetching instance details

# Loop through instance IDs and print information
for instance_id in instance_ids_to_start:
    instance = client.describe_instances(InstanceIds=[instance_id])

    # Each reservation might contain multiple instances, so let's loop through them
    for reservation in instance['Reservations']:
        for instance_info in reservation['Instances']:
            print('Instance ID: {}'.format(instance_info['InstanceId']))

            if 'Tags' in instance_info:
                for tag in instance_info['Tags']:
                    key = tag['Key']
                    value = tag['Value']
                    print('Tag: Key={}, Value={}'.format(key, value))
