from django.test import TestCase
from bioAuthFaceVerificationLogin.create_and_populate_s3_buckets import S3BucketProperties
import os.path
import os
import boto

URL_TO_PHOTO_DIRECTORY_FOR_TESTING = "bioAuthCredentials/static/test_photos_for_checking_api/nicholas_cage"

TEST_PHOTOS_IN_DIRECTORY = os.listdir(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)

TEST_OBJECT_FOR_S3_BUCKET_PROPERTIES = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)


class TestS3BucketProperties(TestCase):

    def test_if_s3_bucket_properties_can_be_initialized_correctly(self):
        test_url_from_SS3BucketProperties = TEST_OBJECT_FOR_S3_BUCKET_PROPERTIES.url
        self.assertIsNotNone(test_url_from_SS3BucketProperties)

    def test_s3BucketProperties_url_is_valid_directory(self):
        assert os.path.exists(TEST_OBJECT_FOR_S3_BUCKET_PROPERTIES.url)

    def test_photos_in_directory_exist(self):
        self.assertEqual(TEST_PHOTOS_IN_DIRECTORY, 
            TEST_OBJECT_FOR_S3_BUCKET_PROPERTIES.get_list_of_photos_from_local_directory())

    def test_unique_s3_bucket_name_is_formated_correctly(self):
        mock_random_string_for_bucket_name = "xxxxxxxxxxxxxxxxxxxx"
        mock_bucket_name_extension = "photo-keyset-bucket"
        mock_created_bucket_name = mock_random_string_for_bucket_name + mock_bucket_name_extension

        test_bucket_name = TEST_OBJECT_FOR_S3_BUCKET_PROPERTIES.generate_unique_s3_bucket_name()
        self.assertEqual(len(mock_created_bucket_name),len(test_bucket_name))


class TestS3Connection(TestCase):
    
    def test_if_basic_connection_works(self):
        self.assertIsNotNone(boto.connect_s3())


class TestS3BucketCreation(TestCase):
    def setUp(self):
        self.connection = boto.connect_s3()

    def test_bucket_can_be_created(self):
        bucket = self.create_bucket()
        self.assertIsNotNone(bucket)
        self.assertEqual(len(bucket.get_all_keys()), 0)

