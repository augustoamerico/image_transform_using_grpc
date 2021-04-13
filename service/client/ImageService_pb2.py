# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ImageService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ImageService.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12ImageService.proto\"]\n\x12ImageUploadRequest\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\x0c\x12\n\n\x02Id\x18\x02 \x01(\t\x12*\n\nStatusCode\x18\x03 \x01(\x0e\x32\x16.ImageUploadStatusCode\"o\n\x13ImageUploadResponse\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\x0c\x12\n\n\x02Id\x18\x02 \x01(\t\x12*\n\nStatusCode\x18\x03 \x01(\x0e\x32\x16.ImageUploadStatusCode\x12\x0f\n\x07Message\x18\x04 \x01(\t*H\n\x15ImageUploadStatusCode\x12\x06\n\x02Ok\x10\x00\x12\n\n\x06\x46\x61iled\x10\x01\x12\x0b\n\x07Unknown\x10\x02\x12\x0e\n\nInProgress\x10\x03\x32G\n\x0cImageService\x12\x37\n\x06Upload\x12\x13.ImageUploadRequest\x1a\x14.ImageUploadResponse\"\x00(\x01\x62\x06proto3'
)

_IMAGEUPLOADSTATUSCODE = _descriptor.EnumDescriptor(
  name='ImageUploadStatusCode',
  full_name='ImageUploadStatusCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Ok', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InProgress', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=230,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_IMAGEUPLOADSTATUSCODE)

ImageUploadStatusCode = enum_type_wrapper.EnumTypeWrapper(_IMAGEUPLOADSTATUSCODE)
Ok = 0
Failed = 1
Unknown = 2
InProgress = 3



_IMAGEUPLOADREQUEST = _descriptor.Descriptor(
  name='ImageUploadRequest',
  full_name='ImageUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Content', full_name='ImageUploadRequest.Content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Id', full_name='ImageUploadRequest.Id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StatusCode', full_name='ImageUploadRequest.StatusCode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=115,
)


_IMAGEUPLOADRESPONSE = _descriptor.Descriptor(
  name='ImageUploadResponse',
  full_name='ImageUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Content', full_name='ImageUploadResponse.Content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Id', full_name='ImageUploadResponse.Id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StatusCode', full_name='ImageUploadResponse.StatusCode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Message', full_name='ImageUploadResponse.Message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=228,
)

_IMAGEUPLOADREQUEST.fields_by_name['StatusCode'].enum_type = _IMAGEUPLOADSTATUSCODE
_IMAGEUPLOADRESPONSE.fields_by_name['StatusCode'].enum_type = _IMAGEUPLOADSTATUSCODE
DESCRIPTOR.message_types_by_name['ImageUploadRequest'] = _IMAGEUPLOADREQUEST
DESCRIPTOR.message_types_by_name['ImageUploadResponse'] = _IMAGEUPLOADRESPONSE
DESCRIPTOR.enum_types_by_name['ImageUploadStatusCode'] = _IMAGEUPLOADSTATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageUploadRequest = _reflection.GeneratedProtocolMessageType('ImageUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEUPLOADREQUEST,
  '__module__' : 'ImageService_pb2'
  # @@protoc_insertion_point(class_scope:ImageUploadRequest)
  })
_sym_db.RegisterMessage(ImageUploadRequest)

ImageUploadResponse = _reflection.GeneratedProtocolMessageType('ImageUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEUPLOADRESPONSE,
  '__module__' : 'ImageService_pb2'
  # @@protoc_insertion_point(class_scope:ImageUploadResponse)
  })
_sym_db.RegisterMessage(ImageUploadResponse)



_IMAGESERVICE = _descriptor.ServiceDescriptor(
  name='ImageService',
  full_name='ImageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=304,
  serialized_end=375,
  methods=[
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='ImageService.Upload',
    index=0,
    containing_service=None,
    input_type=_IMAGEUPLOADREQUEST,
    output_type=_IMAGEUPLOADRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGESERVICE)

DESCRIPTOR.services_by_name['ImageService'] = _IMAGESERVICE

# @@protoc_insertion_point(module_scope)
