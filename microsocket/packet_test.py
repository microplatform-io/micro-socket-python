from unittest import TestCase
from .packet import Packet
from .request import Request

class PacketTestCase(TestCase):
	def test_new_packet(self):
		request = Request(method=1, resource=2, payload='ABC')

		packet = Packet(request, sequence=0)
		self.assertEqual(packet.request, request)
		self.assertEqual(packet.sequence, 0)
		self.assertEqual(packet.payload, 'ABC')
		self.assertEqual(packet.payload_length, 3)