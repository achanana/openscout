# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscout.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openscout.proto',
  package='openscout',
  syntax='proto3',
  serialized_pb=_b('\n\x0fopenscout.proto\x12\topenscout\"B\n\x0c\x45ngineFields\x12\x15\n\rresult_string\x18\x01 \x01(\t\x1a\x1b\n\nBytesValue\x12\r\n\x05value\x18\x01 \x01(\x0c\x42\x1e\n\x14\x65\x64u.cmu.cs.openscoutB\x06Protosb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENGINEFIELDS_BYTESVALUE = _descriptor.Descriptor(
  name='BytesValue',
  full_name='openscout.EngineFields.BytesValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='openscout.EngineFields.BytesValue.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=96,
)

_ENGINEFIELDS = _descriptor.Descriptor(
  name='EngineFields',
  full_name='openscout.EngineFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result_string', full_name='openscout.EngineFields.result_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENGINEFIELDS_BYTESVALUE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=96,
)

_ENGINEFIELDS_BYTESVALUE.containing_type = _ENGINEFIELDS
DESCRIPTOR.message_types_by_name['EngineFields'] = _ENGINEFIELDS

EngineFields = _reflection.GeneratedProtocolMessageType('EngineFields', (_message.Message,), dict(

  BytesValue = _reflection.GeneratedProtocolMessageType('BytesValue', (_message.Message,), dict(
    DESCRIPTOR = _ENGINEFIELDS_BYTESVALUE,
    __module__ = 'openscout_pb2'
    # @@protoc_insertion_point(class_scope:openscout.EngineFields.BytesValue)
    ))
  ,
  DESCRIPTOR = _ENGINEFIELDS,
  __module__ = 'openscout_pb2'
  # @@protoc_insertion_point(class_scope:openscout.EngineFields)
  ))
_sym_db.RegisterMessage(EngineFields)
_sym_db.RegisterMessage(EngineFields.BytesValue)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\024edu.cmu.cs.openscoutB\006Protos'))
# @@protoc_insertion_point(module_scope)
