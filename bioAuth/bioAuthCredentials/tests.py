from django.test import TestCase
from bioAuthCredentials.create_and_populate_s3_buckets import S3BucketProperties
import os.path
import os
# Create your tests here.


URL_TO_PHOTO_DIRECTORY_FOR_TESTING = "bioAuthCredentials/static/test_photos_for_checking_api/nicholas_cage"

TEST_PHOTOS_IN_DIRECTORY = os.listdir(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)

class TestS3BucketProperties(TestCase):

    def test_if_s3_bucket_properties_can_be_initialized_correctly(self):
        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)

        test_url_from_SS3BucketProperties = test_s3_props.url
        self.assertIsNotNone(test_url_from_SS3BucketProperties)


    def test_s3BucketProperties_url_is_valid_directory(self):

        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)
        assert os.path.exists(test_s3_props.url)


    def test_photos_in_directory_exist(self):
        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)
        self.assertEqual(TEST_PHOTOS_IN_DIRECTORY, test_s3_props.get_list_of_photos_from_local_directory())

    
    #def test_generate_unique_s3_bucket_name(self):
    #    self.assertEqual(True,True)


