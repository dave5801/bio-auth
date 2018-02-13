from django.test import TestCase

# Create your tests here.
class TestS3BucketProperties(TestCase):

    #def get_list_of_photos_from_local_directory(self):
    #def get_aws_credentials
    #generate_unique_s3_bucket_name
    def setUp(self):
        testfile = "static/test_photos_for_checking_api/nicholas_cage"

        test_s3_props = S3BucketProperties(testfile)

    def test_get_list_of_photos_from_local_directory(self):

        self.assertEqual(True, False)
