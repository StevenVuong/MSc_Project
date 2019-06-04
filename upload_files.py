import boto3
import os
 
def upload_files(path):
    session = boto3.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='LOC'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('ppmi')
 

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
 
if __name__ == "__main__":
    upload_files('\path\to\my\folder')


upload_files("C:\Users\steve\Downloads\T1_SAG_SIEMEN_3T_CLEAN")