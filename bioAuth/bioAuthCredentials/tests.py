from django.test import TestCase
from bioAuthCredentials.create_and_populate_s3_buckets import S3BucketProperties
import os.path
# Create your tests here.


URL_TO_PHOTO_DIRECTORY_FOR_TESTING = "bioAuthCredentials/static/test_photos_for_checking_api/nicholas_cage"

class TestS3BucketProperties(TestCase):

    def test_if_s3_bucket_properties_can_be_initialized_correctly(self):
        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)

        test_url_from_SS3BucketProperties = test_s3_props.url
        self.assertIsNotNone(test_url_from_SS3BucketProperties)


    def test_s3BucketProperties_url_is_valid_directory(self):

        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)
        assert os.path.exists(test_s3_props.url)


        '''
    def test_get_list_of_photos_from_local_directory(self):
        print("TESTING")
        test_s3_props = S3BucketProperties(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)
        print(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)

        test_get_photos_from_a_directory = os.listdir(URL_TO_PHOTO_DIRECTORY_FOR_TESTING)
        print(os.listdir(URL_TO_PHOTO_DIRECTORY_FOR_TESTING))


        test_s3_properties_has_directory_of_photos = test_s3_props.get_list_of_photos_from_local_directory()
        print(test_s3_properties_has_directory_of_photos)
        self.assertEqual(True,True)
        '''


    
    #def test_generate_unique_s3_bucket_name(self):
    #    self.assertEqual(True,True)


