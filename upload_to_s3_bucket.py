import boto3
import awssecretsmanager

# AWS Secrets Manager secret name containing your AWS credentials
secret_name = 'your-secret-name'
# The name of the key that stores the AWS access key ID in the secret
access_key_id_key = 'access_key_id'
# The name of the key that stores the AWS secret access key in the secret
secret_access_key_key = 'secret_access_key'
# AWS S3 bucket information
bucket_name = 'your-bucket-name'
object_name = 'destination/path/filename.ext'  # The object key in S3

# Initialize AWS Secrets Manager client
secrets_client = awssecretsmanager.Client(region_name='us-east-1')  # Specify the appropriate AWS region

# Retrieve the secret values
secret_values = secrets_client.get_secret_string(secret_name=secret_name)

# Parse the secret JSON to get AWS credentials
secret_data = json.loads(secret_values)
aws_access_key_id = secret_data[access_key_id_key]
aws_secret_access_key = secret_data[secret_access_key_key]

# Create an S3 client using the retrieved credentials
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Local file to upload
local_file_path = 'path/to/your/file/filename.ext'

try:
    # Upload a file to S3
    s3.upload_file(local_file_path, bucket_name, object_name)

    print(f'Successfully uploaded {local_file_path} to {bucket_name}/{object_name}')
except Exception as e:
    print(f'Error uploading {local_file_path} to {bucket_name}/{object_name}: {str(e)}')

