from .constants import MAX_PAYLOAD_LENGTH

class Packet(object):
	def __init__(self, request, sequence):
		self.request = request
		self.sequence = sequence
		self.payload = request.payload[sequence*MAX_PAYLOAD_LENGTH:(sequence+1)*MAX_PAYLOAD_LENGTH]
		self.payload_length = len(self.payload)