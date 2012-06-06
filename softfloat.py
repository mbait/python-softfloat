class Float(object):
	def __init__(self):
		self._rep = 0x00000000

	def __str__(self):
		return ''

	def __repr__(self):
		return self._rep

	def from_string(self, s):
		return self

	def to_double_bits(self):
		return self._rep
