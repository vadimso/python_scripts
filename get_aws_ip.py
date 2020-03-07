import boto3

ec2 = boto3.resource(service_name='ec2',
                     region_name='eu-west-1',
                     aws_access_key_id='xxx',
                     aws_secret_access_key='xxx')

for i in ec2.instances.all():
    print(i.private_ip_address)
    print(i.public_ip_address)
