import unittest
from . import data
from thrift_cli import ThriftStruct, ThriftCLIException

class TestThriftStruct(unittest.TestCase):

	def test_init_field_required_and_optional(self):
		field1 = ThriftStruct.Field(1, 'void', 'someField1', required=True)
		field2 = ThriftStruct.Field(2, 'void', 'someField2', required=False)
		field3 = ThriftStruct.Field(3, 'void', 'someField3', optional=True)
		field4 = ThriftStruct.Field(4, 'void', 'someField4', optional=False)
		field5 = ThriftStruct.Field(5, 'void', 'someField7', required=True, optional=False)
		field6 = ThriftStruct.Field(6, 'void', 'someField8', required=False, optional=True)
		self.assertTrue(field1.required and not field1.optional)
		self.assertTrue(not field2.required and field2.optional)
		self.assertTrue(not field3.required and field3.optional)
		self.assertTrue(field4.required and not field4.optional)
		self.assertTrue(field5.required and not field5.optional)
		self.assertTrue(not field6.required and field6.optional)
		with self.assertRaises(ThriftCLIException):
			field7 = ThriftStruct.Field(7, 'void', 'someField5', required=True, optional=True)
		with self.assertRaises(ThriftCLIException):
			field8 = ThriftStruct.Field(8, 'void', 'someField6', required=False, optional=False)