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


if __name__ == '__main__':
    testfile = "static/test_photos_for_checking_api/nicholas_cage/cage1.png"

    props = S3BucketProperties(testfile)
    print(props.get_photo_url_from_local_directory())
    print(props.get_aws_credentials())

    print(props.generate_unique_s3_bucket_name())


'''
def generate_unique_s3_id(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

bucket_name = generate_unique_s3_id().lower() + "-bucket"
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "static/test_photos_for_checking_api/nicholas_cage/cage1.png"

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = 'cage1.png'
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)

'''