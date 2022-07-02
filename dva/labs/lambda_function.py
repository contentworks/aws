import json
import boto3
import numpy as np
import cv2
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        ikey = record['s3']['object']['key']
        img=ikey.split("/")[-1]
        print(img)
        print(ikey)
        print(bucket_name)
        response = s3.get_object(
        Bucket=bucket_name,
        Key=ikey
        )
        content = response['Body'].read()
        # CONVERTING THE IMAGE FROM COLOR TO GREY
        np_array = np.fromstring(content, np.uint8)
        image_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        print("CONVERTED TO GREY")
        cv2.imwrite("/tmp/gray.jpg", gray)
        
        # STORING THE GREYSCALE IMAGE TO CONVERTED FOLDER
        s3.put_object(Bucket=bucket_name, Key="converted/gray.jpg", Body=open("/tmp/gray.jpg", "rb").read())
        print("SAVED IN CONVERTED/")
        