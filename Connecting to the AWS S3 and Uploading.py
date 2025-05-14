##### NOW INSTALLIN THE BOTO3 AND CONNECTING THE DATA TO AWS S3------

!pip install boto3

import boto3

ACCESS_KEY = 'ACCESS_KEY'
SECRET_KEY = 'SECRET_KEY'
BUCKET_NAME = 'upen-food-delivery'

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

# Upload to S3
s3.upload_file("train.csv", BUCKET_NAME, "upen-food-delivery/cleaned_food_data.csv")
print("Uploaded to S3!")
