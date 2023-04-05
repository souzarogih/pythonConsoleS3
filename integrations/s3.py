import boto3
import pprint
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

load_dotenv()


def create_bucket(bucket_name, region):
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        pprint.pprint(s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)) #Usamos o pprint para uma saída mais amigável do resultado.
    except ClientError as e:
        print(e)

# create_bucket("hello-bucket-python", "sa-east-1")


def list_buckets():

    s3_client = boto3.client('s3',
                             aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                             aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
    try:
        response = s3_client.list_buckets()
    except ClientError as ce:
        print(f"Ocorreu um erro ao listar os buckets: {ce}")

    for bucket in response['Buckets']: # Para cada bucket, fazemos um looping para exibir os dados.
        pprint.pprint(bucket) # Usamos o pprint para uma saída mais amigável do resultado.

# list_buckets()


def delete_bucket(bucket_name):
    try:
        s3_client = boto3.resource('s3',
                                   aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                                    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
        bucket = s3_client.Bucket(bucket_name)
        pprint.pprint(bucket.delete()) # Usamos o pprint para uma saída mais amigável do resultado.
    except ClientError as e:
        print(e)

# delete_bucket("hello-bucket-python")


def upload_object(bucket_name, keyname, file_to_upload):
    try:
        s3_client = boto3.client('s3')
        response = s3_client.upload_file(
            Filename=file_to_upload,
            Bucket=bucket_name,
            Key=keyname,
            ExtraArgs={"Tagging": "Project=ZZZ&Area=AAA"}
        )
    except ClientError as e:
        print(e)

# Passamos por parametro o nome do bucket, nome da chave e path do arquivo local
# upload_object("hello-bucket-python", "exemplo.txt", "exemplo.txt")


def list_objects(bucket_name):
    try:
        s3_client = boto3.resource('s3',
                                   aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                                    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
        bucket = s3_client.Bucket(bucket_name)
                # Para cada objeto encontrado, vamos mostraro nome/keyname
        for obj in bucket.objects.all():
            pprint.pprint(obj.key) #Usamos o pprint para uma saída mais amigável do resultado.
    except ClientError as e:
        print(e)

# list_objects("hello-bucket-python")


# def view_object(bucket_name, object_name):
#     try:
#         s3_client = boto3.client('s3')
#         response = s3_client.get_object(Bucket=bucket_name,Key=object_name)
                # pprint.pprint(response) #Usamos o pprint para uma saída mais amigável do resultado.
    # except ClientError as er:
    #     print(er)

# view_object("hello-bucket-python", "exemplo.txt")


def download_object(bucket_name, keyname, download_name):
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                          aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
        s3.download_file(bucket_name, keyname, download_name)
    except ClientError as e:
        print(e)

# download_object("hello-bucket-python", "exemplo.txt", "exemplo_download.txt")


def delete_objects(bucket_name, keyname):
    try:
        s3_client = boto3.client('s3')
        response = s3_client.delete_object(Bucket=bucket_name,Key=keyname)
        print(response)
    except ClientError as e:
        print(e)

# delete_objects("hello-bucket-python", "exemplo.txt")
