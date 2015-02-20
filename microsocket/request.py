from .constants import MAX_PAYLOAD_LENGTH

class Request(object):
	def __init__(self, method, resource, payload, opcode=0, channel=0, direction=0, priority=1):
		self.method = method
		self.resource = resource
		self.payload = payload
		self.payload_length = len(payload or '')
		self.opcode = opcode
		self.channel = channel
		self.direction = direction
		self.priority = priority
		self.total_sequences = int(self.payload_length / MAX_PAYLOAD_LENGTH) + (0 if self.payload_length % MAX_PAYLOAD_LENGTH == 0 else 1)