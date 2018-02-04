import boto3
import os
from os import listdir
from os.path import isfile, join


#Key.set(os.environ.get('AWS_ACCESS_KEY_ID', ''))
#BaseUrl.set(os.environ.get('AWS_SECRET_ACCESS_KEY', ''))

class FaceCredentialsAWSInterface(object):
    def __init__(self, url_where_photos_are=None):
        self.url_where_photos_are = url_where_photos_are


    def getListOfPhotoUrlsFromADirectoryofFaces(self):

        if not os.path.isdir(self.url_where_photos_are):
            return "Invalid File Path"

        return os.listdir(self.url_where_photos_are)

    def detect_labels(self, bucket, key, max_labels=10, min_confidence=90, region="eu-west-1"):
        
        '''
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID', ''),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY',
        '''
        #rekognition = boto3.client('rekognition', region)
        rekognition = boto3.client(
            'rekognition',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            )
        print(type(rekognition))
        print(key)
        return ''
        '''
        
        response = rekognition.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": key,
                }
            },
            MaxLabels=max_labels,
            MinConfidence=min_confidence,
        )
        return response['Labels']
        '''
        


if __name__ == '__main__':

    face_credentials_interface = FaceCredentialsAWSInterface("static/test_photos_for_checking_api/nicholas_cage/")

    list_of_face_photos = face_credentials_interface.getListOfPhotoUrlsFromADirectoryofFaces()
    print(list_of_face_photos)

    #BUCKET = "amazon-rekognition"
    BUCKET = "hackthenowprojectbucket"
    KEY = list_of_face_photos[0]

    x = face_credentials_interface.detect_labels(BUCKET, KEY)
    print(x)
        
