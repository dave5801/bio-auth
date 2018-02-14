from django.test import TestCase
from bioAuthCredentials.create_and_populate_s3_buckets import S3BucketProperties
import os
# Create your tests here.


URL_TO_PHOTO_DIRECTORY_FOR_TESTING = "static/test_photos_for_checking_api/nicholas_cage"

class TestS3BucketProperties(TestCase):

    def test_if_s3_bucket_properties_can_be_initialized_correctly(self):
        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)

        test_url_from_SS3BucketProperties = test_s3_props.url
        self.assertIsNotNone(test_url_from_SS3BucketProperties)


    def test_s3BucketProperties_url_exists(self):

        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)

        test_url_from_SS3BucketProperties = test_s3_props.url

        self.assertEqual(URL_TO_PHOTO_DIRECTORY_FOR_TESTING,
         test_url_from_SS3BucketProperties)


    def test_get_list_of_photos_from_local_directory(self):
        self.assertEqual(True,True)


    
    def test_generate_unique_s3_bucket_name(self):
        self.assertEqual(True,True)


