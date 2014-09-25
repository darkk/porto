# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='rpc',
  serialized_pb='\n\trpc.proto\x12\x03rpc\"\'\n\x17TContainerCreateRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"(\n\x18TContainerDestroyRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x17\n\x15TContainerListRequest\">\n\x1cTContainerGetPropertyRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08property\x18\x02 \x02(\t\"M\n\x1cTContainerSetPropertyRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08property\x18\x02 \x02(\t\x12\r\n\x05value\x18\x03 \x02(\t\"6\n\x18TContainerGetDataRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\t\"&\n\x16TContainerStartRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"%\n\x15TContainerStopRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"&\n\x16TContainerPauseRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\'\n\x17TContainerResumeRequest\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1f\n\x1dTContainerPropertyListRequest\"\x1b\n\x19TContainerDataListRequest\"\xd7\x04\n\x11TContainerRequest\x12,\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x1c.rpc.TContainerCreateRequest\x12.\n\x07\x64\x65stroy\x18\x02 \x01(\x0b\x32\x1d.rpc.TContainerDestroyRequest\x12(\n\x04list\x18\x03 \x01(\x0b\x32\x1a.rpc.TContainerListRequest\x12\x36\n\x0bgetProperty\x18\x04 \x01(\x0b\x32!.rpc.TContainerGetPropertyRequest\x12\x36\n\x0bsetProperty\x18\x05 \x01(\x0b\x32!.rpc.TContainerSetPropertyRequest\x12.\n\x07getData\x18\x06 \x01(\x0b\x32\x1d.rpc.TContainerGetDataRequest\x12*\n\x05start\x18\x07 \x01(\x0b\x32\x1b.rpc.TContainerStartRequest\x12(\n\x04stop\x18\x08 \x01(\x0b\x32\x1a.rpc.TContainerStopRequest\x12*\n\x05pause\x18\t \x01(\x0b\x32\x1b.rpc.TContainerPauseRequest\x12,\n\x06resume\x18\n \x01(\x0b\x32\x1c.rpc.TContainerResumeRequest\x12\x38\n\x0cpropertyList\x18\x0b \x01(\x0b\x32\".rpc.TContainerPropertyListRequest\x12\x30\n\x08\x64\x61taList\x18\x0c \x01(\x0b\x32\x1e.rpc.TContainerDataListRequest\"&\n\x16TContainerListResponse\x12\x0c\n\x04name\x18\x01 \x03(\t\".\n\x1dTContainerGetPropertyResponse\x12\r\n\x05value\x18\x01 \x02(\t\"*\n\x19TContainerGetDataResponse\x12\r\n\x05value\x18\x01 \x02(\t\"\xaa\x01\n\x1eTContainerPropertyListResponse\x12M\n\x04list\x18\x01 \x03(\x0b\x32?.rpc.TContainerPropertyListResponse.TContainerPropertyListEntry\x1a\x39\n\x1bTContainerPropertyListEntry\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x02(\t\"\x9a\x01\n\x1aTContainerDataListResponse\x12\x45\n\x04list\x18\x01 \x03(\x0b\x32\x37.rpc.TContainerDataListResponse.TContainerDataListEntry\x1a\x35\n\x17TContainerDataListEntry\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x02(\t\"\xc5\x02\n\x12TContainerResponse\x12\x1a\n\x05\x65rror\x18\x01 \x02(\x0e\x32\x0b.rpc.EError\x12\x10\n\x08\x65rrorMsg\x18\x02 \x01(\t\x12)\n\x04list\x18\x03 \x01(\x0b\x32\x1b.rpc.TContainerListResponse\x12\x37\n\x0bgetProperty\x18\x04 \x01(\x0b\x32\".rpc.TContainerGetPropertyResponse\x12/\n\x07getData\x18\x05 \x01(\x0b\x32\x1e.rpc.TContainerGetDataResponse\x12\x39\n\x0cpropertyList\x18\x06 \x01(\x0b\x32#.rpc.TContainerPropertyListResponse\x12\x31\n\x08\x64\x61taList\x18\x07 \x01(\x0b\x32\x1f.rpc.TContainerDataListResponse*\xe2\x01\n\x06\x45\x45rror\x12\x0b\n\x07Success\x10\x00\x12\x0b\n\x07Unknown\x10\x01\x12\x11\n\rInvalidMethod\x10\x02\x12\x1a\n\x16\x43ontainerAlreadyExists\x10\x03\x12\x19\n\x15\x43ontainerDoesNotExist\x10\x04\x12\x13\n\x0fInvalidProperty\x10\x05\x12\x0f\n\x0bInvalidData\x10\x06\x12\x10\n\x0cInvalidValue\x10\x07\x12\x10\n\x0cInvalidState\x10\x08\x12\x10\n\x0cNotSupported\x10\t\x12\x18\n\x14ResourceNotAvailable\x10\n')

_EERROR = _descriptor.EnumDescriptor(
  name='EError',
  full_name='rpc.EError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Success', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidMethod', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ContainerAlreadyExists', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ContainerDoesNotExist', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidProperty', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidData', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidValue', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidState', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NotSupported', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ResourceNotAvailable', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1940,
  serialized_end=2166,
)

EError = enum_type_wrapper.EnumTypeWrapper(_EERROR)
Success = 0
Unknown = 1
InvalidMethod = 2
ContainerAlreadyExists = 3
ContainerDoesNotExist = 4
InvalidProperty = 5
InvalidData = 6
InvalidValue = 7
InvalidState = 8
NotSupported = 9
ResourceNotAvailable = 10



_TCONTAINERCREATEREQUEST = _descriptor.Descriptor(
  name='TContainerCreateRequest',
  full_name='rpc.TContainerCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerCreateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=18,
  serialized_end=57,
)


_TCONTAINERDESTROYREQUEST = _descriptor.Descriptor(
  name='TContainerDestroyRequest',
  full_name='rpc.TContainerDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerDestroyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=59,
  serialized_end=99,
)


_TCONTAINERLISTREQUEST = _descriptor.Descriptor(
  name='TContainerListRequest',
  full_name='rpc.TContainerListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=101,
  serialized_end=124,
)


_TCONTAINERGETPROPERTYREQUEST = _descriptor.Descriptor(
  name='TContainerGetPropertyRequest',
  full_name='rpc.TContainerGetPropertyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerGetPropertyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='rpc.TContainerGetPropertyRequest.property', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=126,
  serialized_end=188,
)


_TCONTAINERSETPROPERTYREQUEST = _descriptor.Descriptor(
  name='TContainerSetPropertyRequest',
  full_name='rpc.TContainerSetPropertyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerSetPropertyRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='rpc.TContainerSetPropertyRequest.property', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='rpc.TContainerSetPropertyRequest.value', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=190,
  serialized_end=267,
)


_TCONTAINERGETDATAREQUEST = _descriptor.Descriptor(
  name='TContainerGetDataRequest',
  full_name='rpc.TContainerGetDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerGetDataRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='rpc.TContainerGetDataRequest.data', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=269,
  serialized_end=323,
)


_TCONTAINERSTARTREQUEST = _descriptor.Descriptor(
  name='TContainerStartRequest',
  full_name='rpc.TContainerStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerStartRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=325,
  serialized_end=363,
)


_TCONTAINERSTOPREQUEST = _descriptor.Descriptor(
  name='TContainerStopRequest',
  full_name='rpc.TContainerStopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerStopRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=365,
  serialized_end=402,
)


_TCONTAINERPAUSEREQUEST = _descriptor.Descriptor(
  name='TContainerPauseRequest',
  full_name='rpc.TContainerPauseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerPauseRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=404,
  serialized_end=442,
)


_TCONTAINERRESUMEREQUEST = _descriptor.Descriptor(
  name='TContainerResumeRequest',
  full_name='rpc.TContainerResumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerResumeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=444,
  serialized_end=483,
)


_TCONTAINERPROPERTYLISTREQUEST = _descriptor.Descriptor(
  name='TContainerPropertyListRequest',
  full_name='rpc.TContainerPropertyListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=485,
  serialized_end=516,
)


_TCONTAINERDATALISTREQUEST = _descriptor.Descriptor(
  name='TContainerDataListRequest',
  full_name='rpc.TContainerDataListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=518,
  serialized_end=545,
)


_TCONTAINERREQUEST = _descriptor.Descriptor(
  name='TContainerRequest',
  full_name='rpc.TContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='rpc.TContainerRequest.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destroy', full_name='rpc.TContainerRequest.destroy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list', full_name='rpc.TContainerRequest.list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getProperty', full_name='rpc.TContainerRequest.getProperty', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='setProperty', full_name='rpc.TContainerRequest.setProperty', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getData', full_name='rpc.TContainerRequest.getData', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='rpc.TContainerRequest.start', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stop', full_name='rpc.TContainerRequest.stop', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pause', full_name='rpc.TContainerRequest.pause', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resume', full_name='rpc.TContainerRequest.resume', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='propertyList', full_name='rpc.TContainerRequest.propertyList', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataList', full_name='rpc.TContainerRequest.dataList', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=548,
  serialized_end=1147,
)


_TCONTAINERLISTRESPONSE = _descriptor.Descriptor(
  name='TContainerListResponse',
  full_name='rpc.TContainerListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerListResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=1149,
  serialized_end=1187,
)


_TCONTAINERGETPROPERTYRESPONSE = _descriptor.Descriptor(
  name='TContainerGetPropertyResponse',
  full_name='rpc.TContainerGetPropertyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='rpc.TContainerGetPropertyResponse.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=1189,
  serialized_end=1235,
)


_TCONTAINERGETDATARESPONSE = _descriptor.Descriptor(
  name='TContainerGetDataResponse',
  full_name='rpc.TContainerGetDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='rpc.TContainerGetDataResponse.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=1237,
  serialized_end=1279,
)


_TCONTAINERPROPERTYLISTRESPONSE_TCONTAINERPROPERTYLISTENTRY = _descriptor.Descriptor(
  name='TContainerPropertyListEntry',
  full_name='rpc.TContainerPropertyListResponse.TContainerPropertyListEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerPropertyListResponse.TContainerPropertyListEntry.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='rpc.TContainerPropertyListResponse.TContainerPropertyListEntry.desc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=1395,
  serialized_end=1452,
)

_TCONTAINERPROPERTYLISTRESPONSE = _descriptor.Descriptor(
  name='TContainerPropertyListResponse',
  full_name='rpc.TContainerPropertyListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='rpc.TContainerPropertyListResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TCONTAINERPROPERTYLISTRESPONSE_TCONTAINERPROPERTYLISTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1282,
  serialized_end=1452,
)


_TCONTAINERDATALISTRESPONSE_TCONTAINERDATALISTENTRY = _descriptor.Descriptor(
  name='TContainerDataListEntry',
  full_name='rpc.TContainerDataListResponse.TContainerDataListEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rpc.TContainerDataListResponse.TContainerDataListEntry.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='desc', full_name='rpc.TContainerDataListResponse.TContainerDataListEntry.desc', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=1556,
  serialized_end=1609,
)

_TCONTAINERDATALISTRESPONSE = _descriptor.Descriptor(
  name='TContainerDataListResponse',
  full_name='rpc.TContainerDataListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='rpc.TContainerDataListResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TCONTAINERDATALISTRESPONSE_TCONTAINERDATALISTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1455,
  serialized_end=1609,
)


_TCONTAINERRESPONSE = _descriptor.Descriptor(
  name='TContainerResponse',
  full_name='rpc.TContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='rpc.TContainerResponse.error', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errorMsg', full_name='rpc.TContainerResponse.errorMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list', full_name='rpc.TContainerResponse.list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getProperty', full_name='rpc.TContainerResponse.getProperty', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='getData', full_name='rpc.TContainerResponse.getData', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='propertyList', full_name='rpc.TContainerResponse.propertyList', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataList', full_name='rpc.TContainerResponse.dataList', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=1612,
  serialized_end=1937,
)

_TCONTAINERREQUEST.fields_by_name['create'].message_type = _TCONTAINERCREATEREQUEST
_TCONTAINERREQUEST.fields_by_name['destroy'].message_type = _TCONTAINERDESTROYREQUEST
_TCONTAINERREQUEST.fields_by_name['list'].message_type = _TCONTAINERLISTREQUEST
_TCONTAINERREQUEST.fields_by_name['getProperty'].message_type = _TCONTAINERGETPROPERTYREQUEST
_TCONTAINERREQUEST.fields_by_name['setProperty'].message_type = _TCONTAINERSETPROPERTYREQUEST
_TCONTAINERREQUEST.fields_by_name['getData'].message_type = _TCONTAINERGETDATAREQUEST
_TCONTAINERREQUEST.fields_by_name['start'].message_type = _TCONTAINERSTARTREQUEST
_TCONTAINERREQUEST.fields_by_name['stop'].message_type = _TCONTAINERSTOPREQUEST
_TCONTAINERREQUEST.fields_by_name['pause'].message_type = _TCONTAINERPAUSEREQUEST
_TCONTAINERREQUEST.fields_by_name['resume'].message_type = _TCONTAINERRESUMEREQUEST
_TCONTAINERREQUEST.fields_by_name['propertyList'].message_type = _TCONTAINERPROPERTYLISTREQUEST
_TCONTAINERREQUEST.fields_by_name['dataList'].message_type = _TCONTAINERDATALISTREQUEST
_TCONTAINERPROPERTYLISTRESPONSE_TCONTAINERPROPERTYLISTENTRY.containing_type = _TCONTAINERPROPERTYLISTRESPONSE;
_TCONTAINERPROPERTYLISTRESPONSE.fields_by_name['list'].message_type = _TCONTAINERPROPERTYLISTRESPONSE_TCONTAINERPROPERTYLISTENTRY
_TCONTAINERDATALISTRESPONSE_TCONTAINERDATALISTENTRY.containing_type = _TCONTAINERDATALISTRESPONSE;
_TCONTAINERDATALISTRESPONSE.fields_by_name['list'].message_type = _TCONTAINERDATALISTRESPONSE_TCONTAINERDATALISTENTRY
_TCONTAINERRESPONSE.fields_by_name['error'].enum_type = _EERROR
_TCONTAINERRESPONSE.fields_by_name['list'].message_type = _TCONTAINERLISTRESPONSE
_TCONTAINERRESPONSE.fields_by_name['getProperty'].message_type = _TCONTAINERGETPROPERTYRESPONSE
_TCONTAINERRESPONSE.fields_by_name['getData'].message_type = _TCONTAINERGETDATARESPONSE
_TCONTAINERRESPONSE.fields_by_name['propertyList'].message_type = _TCONTAINERPROPERTYLISTRESPONSE
_TCONTAINERRESPONSE.fields_by_name['dataList'].message_type = _TCONTAINERDATALISTRESPONSE
DESCRIPTOR.message_types_by_name['TContainerCreateRequest'] = _TCONTAINERCREATEREQUEST
DESCRIPTOR.message_types_by_name['TContainerDestroyRequest'] = _TCONTAINERDESTROYREQUEST
DESCRIPTOR.message_types_by_name['TContainerListRequest'] = _TCONTAINERLISTREQUEST
DESCRIPTOR.message_types_by_name['TContainerGetPropertyRequest'] = _TCONTAINERGETPROPERTYREQUEST
DESCRIPTOR.message_types_by_name['TContainerSetPropertyRequest'] = _TCONTAINERSETPROPERTYREQUEST
DESCRIPTOR.message_types_by_name['TContainerGetDataRequest'] = _TCONTAINERGETDATAREQUEST
DESCRIPTOR.message_types_by_name['TContainerStartRequest'] = _TCONTAINERSTARTREQUEST
DESCRIPTOR.message_types_by_name['TContainerStopRequest'] = _TCONTAINERSTOPREQUEST
DESCRIPTOR.message_types_by_name['TContainerPauseRequest'] = _TCONTAINERPAUSEREQUEST
DESCRIPTOR.message_types_by_name['TContainerResumeRequest'] = _TCONTAINERRESUMEREQUEST
DESCRIPTOR.message_types_by_name['TContainerPropertyListRequest'] = _TCONTAINERPROPERTYLISTREQUEST
DESCRIPTOR.message_types_by_name['TContainerDataListRequest'] = _TCONTAINERDATALISTREQUEST
DESCRIPTOR.message_types_by_name['TContainerRequest'] = _TCONTAINERREQUEST
DESCRIPTOR.message_types_by_name['TContainerListResponse'] = _TCONTAINERLISTRESPONSE
DESCRIPTOR.message_types_by_name['TContainerGetPropertyResponse'] = _TCONTAINERGETPROPERTYRESPONSE
DESCRIPTOR.message_types_by_name['TContainerGetDataResponse'] = _TCONTAINERGETDATARESPONSE
DESCRIPTOR.message_types_by_name['TContainerPropertyListResponse'] = _TCONTAINERPROPERTYLISTRESPONSE
DESCRIPTOR.message_types_by_name['TContainerDataListResponse'] = _TCONTAINERDATALISTRESPONSE
DESCRIPTOR.message_types_by_name['TContainerResponse'] = _TCONTAINERRESPONSE

class TContainerCreateRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERCREATEREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerCreateRequest)

class TContainerDestroyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERDESTROYREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerDestroyRequest)

class TContainerListRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERLISTREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerListRequest)

class TContainerGetPropertyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERGETPROPERTYREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerGetPropertyRequest)

class TContainerSetPropertyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERSETPROPERTYREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerSetPropertyRequest)

class TContainerGetDataRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERGETDATAREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerGetDataRequest)

class TContainerStartRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERSTARTREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerStartRequest)

class TContainerStopRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERSTOPREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerStopRequest)

class TContainerPauseRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERPAUSEREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerPauseRequest)

class TContainerResumeRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERRESUMEREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerResumeRequest)

class TContainerPropertyListRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERPROPERTYLISTREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerPropertyListRequest)

class TContainerDataListRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERDATALISTREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerDataListRequest)

class TContainerRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERREQUEST

  # @@protoc_insertion_point(class_scope:rpc.TContainerRequest)

class TContainerListResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERLISTRESPONSE

  # @@protoc_insertion_point(class_scope:rpc.TContainerListResponse)

class TContainerGetPropertyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERGETPROPERTYRESPONSE

  # @@protoc_insertion_point(class_scope:rpc.TContainerGetPropertyResponse)

class TContainerGetDataResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERGETDATARESPONSE

  # @@protoc_insertion_point(class_scope:rpc.TContainerGetDataResponse)

class TContainerPropertyListResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class TContainerPropertyListEntry(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _TCONTAINERPROPERTYLISTRESPONSE_TCONTAINERPROPERTYLISTENTRY

    # @@protoc_insertion_point(class_scope:rpc.TContainerPropertyListResponse.TContainerPropertyListEntry)
  DESCRIPTOR = _TCONTAINERPROPERTYLISTRESPONSE

  # @@protoc_insertion_point(class_scope:rpc.TContainerPropertyListResponse)

class TContainerDataListResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class TContainerDataListEntry(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _TCONTAINERDATALISTRESPONSE_TCONTAINERDATALISTENTRY

    # @@protoc_insertion_point(class_scope:rpc.TContainerDataListResponse.TContainerDataListEntry)
  DESCRIPTOR = _TCONTAINERDATALISTRESPONSE

  # @@protoc_insertion_point(class_scope:rpc.TContainerDataListResponse)

class TContainerResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCONTAINERRESPONSE

  # @@protoc_insertion_point(class_scope:rpc.TContainerResponse)


# @@protoc_insertion_point(module_scope)