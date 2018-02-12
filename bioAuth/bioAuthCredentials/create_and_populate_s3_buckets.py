import boto
import os
import boto.s3
import sys
from boto.s3.key import Key
import string
import random


class S3BucketProperties(object):
    def __init__(self,url=None):
        self.url=url

    def get_list_of_photos_from_local_directory(self):
        if not os.path.isdir(self.url):
            print("not Directory")
        else:
            x = os.listdir(self.url)
            print("dir contents", x)

        return self.url

    def get_aws_credentials(self):
        return [os.environ.get('AWS_ACCESS_KEY_ID'), os.environ.get('AWS_SECRET_ACCESS_KEY')]

    def generate_unique_s3_bucket_name(self, size=20, chars=string.ascii_uppercase + string.digits):
        random_str = ''.join(random.choice(chars) for _ in range(size))
        return random_str.lower() + "-bucket"


class CreateNewS3Bucket(object):

    def display_output_complete(self,complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()

    def __init__(self,url=None):
        self.url = url
        self.properties = S3BucketProperties(self.url)

        credentials = self.properties.get_aws_credentials()

        AWS_ACCESS_KEY_ID = credentials[0]
        AWS_SECRET_ACCESS_KEY = credentials[1]

        conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)

        bucket_name = self.properties.generate_unique_s3_bucket_name()

        bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

        list_of_photos = self.properties.get_list_of_photos_from_local_directory()
        print(list_of_photos)

        '''
        k = Key(bucket)
        k.key = 'cage1.png'
        print("TEST", k)
        k.set_contents_from_filename(testfile,cb=None, num_cb=10)
        '''


if __name__ == '__main__':
    testfile = "static/test_photos_for_checking_api/nicholas_cage"

    test_s3_props = S3BucketProperties(testfile)

    #x = test_s3_props.get_list_of_photos_from_local_directory()
    new_s3_bucket = CreateNewS3Bucket(testfile)
