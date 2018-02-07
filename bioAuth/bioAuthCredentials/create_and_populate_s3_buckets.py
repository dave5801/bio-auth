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

    def get_photo_url_from_local_directory(self):
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

        bucket = conn.create_bucket(bucket_name,location=boto.s3.connection.Location.DEFAULT)
        #conn.create_bucket(bucket_name,location=boto.s3.connection.Location.DEFAULT)

        k = Key(bucket)
        k.key = 'cage1.png'
        k.set_contents_from_filename(testfile,
            cb=None, num_cb=10)


if __name__ == '__main__':
    testfile = "static/test_photos_for_checking_api/nicholas_cage/cage1.png"

    new_s3_bucket = CreateNewS3Bucket("static/test_photos_for_checking_api/nicholas_cage/cage1.png")

