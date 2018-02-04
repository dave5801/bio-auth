import boto
import os
import boto.s3
import sys
from boto.s3.key import Key
import string
import random


'''
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

