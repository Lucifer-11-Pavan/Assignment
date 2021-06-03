# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:28:19 2021

@author: Lucifer
"""

import logging
import boto3
from botocore.exceptions import ClientError

def uniqueCode(pic_name):
    code = ''
    for character in pic_name:
        if character.isdigit():
            code = code + character
    return code

#uniqueCode('paul-12345.jpg')

def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    
    file_name = uniqueCode(picture_name) + '.jpg'
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

picture_name = 'paul-12345.jpg'