import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():

    print('Instance id is {} and Instance Type is {}'.format(instance.instance_id, instance.instance_type))

    if instance.tags:
        for tag in instance.tags:
            key = tag['Key']
            value = tag['Value']
            print('Tag: Key={}, Value={}'.format(key, value))
