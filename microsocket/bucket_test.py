from unittest import TestCase
from .bucket import Bucket

class BucketTestCase(TestCase):
	def test_new_bucket(self):
		bucket = Bucket()
		self.assertEqual(bucket.requests, [])