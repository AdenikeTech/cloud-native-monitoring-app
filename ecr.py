import boto3

region_name = 'ca-central-1'

ecr_client = boto3.client('ecr', region_name=region_name)

repository_name = "cloud_native_monitoring_app_image"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)