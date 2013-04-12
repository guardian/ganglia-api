import unittest
from ganglia import ganglia_api 

class TestAlert(unittest.TestCase):
	def test_nothing(self):
		self.assertEquals(1,1)

	def test_config(self):
		config = ganglia_api.GangliaConfig("./tests/config")
		self.assertEquals(len(config.env_service_dict), 1)
		key, gmetad = config.env_service_dict.items()[0]
		self.assertEquals(('TEST', 'ME'), key)
		self.assertEquals(gmetad.environment, 'TEST')
		self.assertEquals(gmetad.service, 'ME')
		self.assertEquals(gmetad.xml_port, 12345)
		self.assertEquals(gmetad.interactive_port, 12346)

#	def test_future(self):
#		config = ganglia_api.GangliaConfig("./config")
#		d
#		ganglia_api.GangliaPollThread(config, data)