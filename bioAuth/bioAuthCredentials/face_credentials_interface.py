import boto3
import os
from os import listdir
from os.path import isfile, join

#BUCKET = "amazon-rekognition"
BUCKET = "hackthenowprojectbucket"
KEY = "test.jpg"


class FaceCredentialsAWSInterface(object):
    def __init__(self, url_where_photos_are=None):
        self.url_where_photos_are = url_where_photos_are


    def getListOfPhotoUrlsFromADirectoryofFaces(self):

        if not os.path.isdir(self.url_where_photos_are):
            return "Invalid File Path"

        return os.listdir(self.url_where_photos_are)


if __name__ == '__main__':
    face_credentials_interface = FaceCredentialsAWSInterface("static/test_photos_for_checking_api/nicholas_cage/")

    list_of_face_photos = face_credentials_interface.getListOfPhotoUrlsFromADirectoryofFaces()
    print(list_of_face_photos)


'''
def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="eu-west-1"):
    rekognition = boto3.client("rekognition", region)
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


for label in detect_labels(BUCKET, KEY):
    print("{Name} - {Confidence}%".format(**label))
    '''