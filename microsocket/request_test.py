from unittest import TestCase
from .constants import MAX_PAYLOAD_LENGTH
from .request import Request

class RequestTestCase(TestCase):
	def test_new_single_packet_request(self):
		request = Request(method=1, resource=2, payload='ABC')
		self.assertEqual(request.opcode, 0)
		self.assertEqual(request.channel, 0)
		self.assertEqual(request.direction, 0)
		self.assertEqual(request.priority, 1)
		self.assertEqual(request.method, 1)
		self.assertEqual(request.resource, 2)
		self.assertEqual(request.payload, 'ABC')
		self.assertEqual(request.payload_length, 3)
		self.assertEqual(request.total_sequences, 1)

		request = Request(method=1, resource=2, payload='A' * MAX_PAYLOAD_LENGTH)
		self.assertEqual(request.opcode, 0)
		self.assertEqual(request.channel, 0)
		self.assertEqual(request.direction, 0)
		self.assertEqual(request.priority, 1)
		self.assertEqual(request.method, 1)
		self.assertEqual(request.resource, 2)
		self.assertEqual(request.payload, 'A' * MAX_PAYLOAD_LENGTH)
		self.assertEqual(request.payload_length, MAX_PAYLOAD_LENGTH)
		self.assertEqual(request.total_sequences, 1)

	def test_new_multi_packet_request(self):
		request = Request(method=1, resource=2, payload='A' * MAX_PAYLOAD_LENGTH * 2)
		self.assertEqual(request.opcode, 0)
		self.assertEqual(request.channel, 0)
		self.assertEqual(request.direction, 0)
		self.assertEqual(request.priority, 1)
		self.assertEqual(request.method, 1)
		self.assertEqual(request.resource, 2)
		self.assertEqual(request.payload, 'A' * MAX_PAYLOAD_LENGTH * 2)
		self.assertEqual(request.payload_length, MAX_PAYLOAD_LENGTH * 2)
		self.assertEqual(request.total_sequences, 2)