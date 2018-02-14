from django.test import TestCase
from bioAuthCredentials.create_and_populate_s3_buckets import S3BucketProperties
# Create your tests here.
class TestS3BucketProperties(TestCase):

    #def get_list_of_photos_from_local_directory(self):
    #def get_aws_credentials
    #generate_unique_s3_bucket_name
   # def setUp(self):
    #    testfileurl = "static/test_photos_for_checking_api/nicholas_cage"

     #   test_s3_props = S3BucketProperties(testfileurl)

    def test_s3BucketProperties_url_exists(self):

        testfileurl = "static/test_photos_for_checking_api/nicholas_cage"
        test_s3_props = S3BucketProperties(testfileurl)

        test_url_from_SS3BucketProperties = test_s3_props.url

        self.assertEqual(testfileurl, test_url_from_SS3BucketProperties)
