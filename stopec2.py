import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

instance_ids_to_stop = ['i-02dd2ae1c9e83d442']
#instance_ids_to_stop = ['i-07c8e920108ec4971', 'i-07cd4fe25fec59d43', 'i-0b9b5b422890687ac']
client.stop_instances(InstanceIds=instance_ids_to_stop)

for instance_id in instance_ids_to_stop:
    instance = ec2.Instance(instance_id)

    print('Instance ID: {}'.format(instance.instance_id))

    if instance.tags:
        for tag in instance.tags:
            key = tag['Key']
            value = tag['Value']
            print('Tag: Key={}, Value={}'.format(key, value))
