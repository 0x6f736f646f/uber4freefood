# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delivery.proto

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
  name='delivery.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x64\x65livery.proto\"C\n\x15\x43\x61ncelDeliveryRequest\x12\x10\n\x08order_no\x18\x01 \x01(\t\x12\x18\n\x10request_token_id\x18\x02 \x01(\t\"P\n\x16\x43\x61ncelDeliveryResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x18\n\x10request_token_id\x18\x03 \x01(\t\"\xf4\x05\n\x16RequestDeliveryRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\x13\n\x0bvendor_type\x18\x02 \x01(\t\x12\x13\n\x0brider_phone\x18\x03 \x01(\t\x12\x11\n\tfrom_name\x18\x04 \x01(\t\x12\x10\n\x08\x66rom_lat\x18\x05 \x01(\t\x12\x11\n\tfrom_long\x18\x06 \x01(\t\x12\x18\n\x10\x66rom_description\x18\x07 \x01(\t\x12\x0f\n\x07to_name\x18\x08 \x01(\t\x12\x0e\n\x06to_lat\x18\t \x01(\t\x12\x0f\n\x07to_long\x18\n \x01(\t\x12\x16\n\x0eto_description\x18\x0b \x01(\t\x12\x16\n\x0erecepient_name\x18\x0c \x01(\t\x12\x17\n\x0frecepient_phone\x18\r \x01(\t\x12\x17\n\x0frecepient_email\x18\x0e \x01(\t\x12\x17\n\x0frecepient_notes\x18\x0f \x01(\t\x12\x13\n\x0bsender_name\x18\x10 \x01(\t\x12\x14\n\x0csender_phone\x18\x11 \x01(\t\x12\x14\n\x0csender_email\x18\x12 \x01(\t\x12\x14\n\x0csender_notes\x18\x13 \x01(\t\x12\x14\n\x0cpick_up_date\x18\x14 \x01(\t\x12\x0e\n\x06status\x18\x15 \x01(\t\x12\x12\n\npay_method\x18\x16 \x01(\t\x12\x0e\n\x06\x61mount\x18\x17 \x01(\t\x12\x0e\n\x06return\x18\x18 \x01(\t\x12\x0c\n\x04note\x18\x19 \x01(\t\x12\x13\n\x0bnote_status\x18\x1a \x01(\t\x12\x14\n\x0crequest_type\x18\x1b \x01(\t\x12\x12\n\norder_type\x18\x1c \x01(\t\x12\x17\n\x0f\x65\x63ommerce_order\x18\x1d \x01(\t\x12\x0f\n\x07\x65xpress\x18\x1e \x01(\t\x12\x0c\n\x04skew\x18\x1f \x01(\t\x12\x0e\n\x06weight\x18  \x01(\t\x12\x0e\n\x06height\x18! \x01(\t\x12\r\n\x05width\x18\" \x01(\t\x12\x0e\n\x06length\x18# \x01(\t\x12\x11\n\titem_name\x18$ \x01(\t\x12\x18\n\x10request_token_id\x18% \x01(\t\"Q\n\x17RequestDeliveryResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x18\n\x10request_token_id\x18\x03 \x01(\t\"B\n\x14TrackDeliveryRequest\x12\x10\n\x08order_no\x18\x01 \x01(\t\x12\x18\n\x10request_token_id\x18\x02 \x01(\t\"\xe9\x01\n\x15TrackDeliveryResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x10\n\x08order_no\x18\x02 \x01(\t\x12\x14\n\x0corder_status\x18\x03 \x01(\t\x12\x12\n\nrider_name\x18\x04 \x01(\t\x12\x13\n\x0brider_phone\x18\x05 \x01(\t\x12\x11\n\trider_pic\x18\x06 \x01(\t\x12\x16\n\x0erider_tracking\x18\x07 \x01(\t\x12\x14\n\x0cnumber_plate\x18\x08 \x01(\t\x12\x14\n\x0cvehicle_make\x18\t \x01(\t\x12\x18\n\x10request_token_id\x18\n \x01(\t2\xd4\x01\n\x05Users\x12\x41\n\x0e\x43\x61ncelDelivery\x12\x16.CancelDeliveryRequest\x1a\x17.CancelDeliveryResponse\x12\x46\n\x0fRequestDelivery\x12\x17.RequestDeliveryRequest\x1a\x18.RequestDeliveryResponse0\x01\x12@\n\rTrackDelivery\x12\x15.TrackDeliveryRequest\x1a\x16.TrackDeliveryResponse0\x01\x62\x06proto3')
)




_CANCELDELIVERYREQUEST = _descriptor.Descriptor(
  name='CancelDeliveryRequest',
  full_name='CancelDeliveryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_no', full_name='CancelDeliveryRequest.order_no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_token_id', full_name='CancelDeliveryRequest.request_token_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=85,
)


_CANCELDELIVERYRESPONSE = _descriptor.Descriptor(
  name='CancelDeliveryResponse',
  full_name='CancelDeliveryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='CancelDeliveryResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='CancelDeliveryResponse.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_token_id', full_name='CancelDeliveryResponse.request_token_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=87,
  serialized_end=167,
)


_REQUESTDELIVERYREQUEST = _descriptor.Descriptor(
  name='RequestDeliveryRequest',
  full_name='RequestDeliveryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='RequestDeliveryRequest.command', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vendor_type', full_name='RequestDeliveryRequest.vendor_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rider_phone', full_name='RequestDeliveryRequest.rider_phone', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_name', full_name='RequestDeliveryRequest.from_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_lat', full_name='RequestDeliveryRequest.from_lat', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_long', full_name='RequestDeliveryRequest.from_long', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_description', full_name='RequestDeliveryRequest.from_description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_name', full_name='RequestDeliveryRequest.to_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_lat', full_name='RequestDeliveryRequest.to_lat', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_long', full_name='RequestDeliveryRequest.to_long', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_description', full_name='RequestDeliveryRequest.to_description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recepient_name', full_name='RequestDeliveryRequest.recepient_name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recepient_phone', full_name='RequestDeliveryRequest.recepient_phone', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recepient_email', full_name='RequestDeliveryRequest.recepient_email', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recepient_notes', full_name='RequestDeliveryRequest.recepient_notes', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_name', full_name='RequestDeliveryRequest.sender_name', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_phone', full_name='RequestDeliveryRequest.sender_phone', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_email', full_name='RequestDeliveryRequest.sender_email', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_notes', full_name='RequestDeliveryRequest.sender_notes', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pick_up_date', full_name='RequestDeliveryRequest.pick_up_date', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='RequestDeliveryRequest.status', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pay_method', full_name='RequestDeliveryRequest.pay_method', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='RequestDeliveryRequest.amount', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='return', full_name='RequestDeliveryRequest.return', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='RequestDeliveryRequest.note', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note_status', full_name='RequestDeliveryRequest.note_status', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_type', full_name='RequestDeliveryRequest.request_type', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_type', full_name='RequestDeliveryRequest.order_type', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ecommerce_order', full_name='RequestDeliveryRequest.ecommerce_order', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='express', full_name='RequestDeliveryRequest.express', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skew', full_name='RequestDeliveryRequest.skew', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='RequestDeliveryRequest.weight', index=31,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='RequestDeliveryRequest.height', index=32,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='RequestDeliveryRequest.width', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='RequestDeliveryRequest.length', index=34,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_name', full_name='RequestDeliveryRequest.item_name', index=35,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_token_id', full_name='RequestDeliveryRequest.request_token_id', index=36,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=170,
  serialized_end=926,
)


_REQUESTDELIVERYRESPONSE = _descriptor.Descriptor(
  name='RequestDeliveryResponse',
  full_name='RequestDeliveryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RequestDeliveryResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='RequestDeliveryResponse.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_token_id', full_name='RequestDeliveryResponse.request_token_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=928,
  serialized_end=1009,
)


_TRACKDELIVERYREQUEST = _descriptor.Descriptor(
  name='TrackDeliveryRequest',
  full_name='TrackDeliveryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_no', full_name='TrackDeliveryRequest.order_no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_token_id', full_name='TrackDeliveryRequest.request_token_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1011,
  serialized_end=1077,
)


_TRACKDELIVERYRESPONSE = _descriptor.Descriptor(
  name='TrackDeliveryResponse',
  full_name='TrackDeliveryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='TrackDeliveryResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_no', full_name='TrackDeliveryResponse.order_no', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_status', full_name='TrackDeliveryResponse.order_status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rider_name', full_name='TrackDeliveryResponse.rider_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rider_phone', full_name='TrackDeliveryResponse.rider_phone', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rider_pic', full_name='TrackDeliveryResponse.rider_pic', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rider_tracking', full_name='TrackDeliveryResponse.rider_tracking', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_plate', full_name='TrackDeliveryResponse.number_plate', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_make', full_name='TrackDeliveryResponse.vehicle_make', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_token_id', full_name='TrackDeliveryResponse.request_token_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1080,
  serialized_end=1313,
)

DESCRIPTOR.message_types_by_name['CancelDeliveryRequest'] = _CANCELDELIVERYREQUEST
DESCRIPTOR.message_types_by_name['CancelDeliveryResponse'] = _CANCELDELIVERYRESPONSE
DESCRIPTOR.message_types_by_name['RequestDeliveryRequest'] = _REQUESTDELIVERYREQUEST
DESCRIPTOR.message_types_by_name['RequestDeliveryResponse'] = _REQUESTDELIVERYRESPONSE
DESCRIPTOR.message_types_by_name['TrackDeliveryRequest'] = _TRACKDELIVERYREQUEST
DESCRIPTOR.message_types_by_name['TrackDeliveryResponse'] = _TRACKDELIVERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CancelDeliveryRequest = _reflection.GeneratedProtocolMessageType('CancelDeliveryRequest', (_message.Message,), dict(
  DESCRIPTOR = _CANCELDELIVERYREQUEST,
  __module__ = 'delivery_pb2'
  # @@protoc_insertion_point(class_scope:CancelDeliveryRequest)
  ))
_sym_db.RegisterMessage(CancelDeliveryRequest)

CancelDeliveryResponse = _reflection.GeneratedProtocolMessageType('CancelDeliveryResponse', (_message.Message,), dict(
  DESCRIPTOR = _CANCELDELIVERYRESPONSE,
  __module__ = 'delivery_pb2'
  # @@protoc_insertion_point(class_scope:CancelDeliveryResponse)
  ))
_sym_db.RegisterMessage(CancelDeliveryResponse)

RequestDeliveryRequest = _reflection.GeneratedProtocolMessageType('RequestDeliveryRequest', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDELIVERYREQUEST,
  __module__ = 'delivery_pb2'
  # @@protoc_insertion_point(class_scope:RequestDeliveryRequest)
  ))
_sym_db.RegisterMessage(RequestDeliveryRequest)

RequestDeliveryResponse = _reflection.GeneratedProtocolMessageType('RequestDeliveryResponse', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDELIVERYRESPONSE,
  __module__ = 'delivery_pb2'
  # @@protoc_insertion_point(class_scope:RequestDeliveryResponse)
  ))
_sym_db.RegisterMessage(RequestDeliveryResponse)

TrackDeliveryRequest = _reflection.GeneratedProtocolMessageType('TrackDeliveryRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRACKDELIVERYREQUEST,
  __module__ = 'delivery_pb2'
  # @@protoc_insertion_point(class_scope:TrackDeliveryRequest)
  ))
_sym_db.RegisterMessage(TrackDeliveryRequest)

TrackDeliveryResponse = _reflection.GeneratedProtocolMessageType('TrackDeliveryResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRACKDELIVERYRESPONSE,
  __module__ = 'delivery_pb2'
  # @@protoc_insertion_point(class_scope:TrackDeliveryResponse)
  ))
_sym_db.RegisterMessage(TrackDeliveryResponse)



_USERS = _descriptor.ServiceDescriptor(
  name='Users',
  full_name='Users',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1316,
  serialized_end=1528,
  methods=[
  _descriptor.MethodDescriptor(
    name='CancelDelivery',
    full_name='Users.CancelDelivery',
    index=0,
    containing_service=None,
    input_type=_CANCELDELIVERYREQUEST,
    output_type=_CANCELDELIVERYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RequestDelivery',
    full_name='Users.RequestDelivery',
    index=1,
    containing_service=None,
    input_type=_REQUESTDELIVERYREQUEST,
    output_type=_REQUESTDELIVERYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TrackDelivery',
    full_name='Users.TrackDelivery',
    index=2,
    containing_service=None,
    input_type=_TRACKDELIVERYREQUEST,
    output_type=_TRACKDELIVERYRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERS)

DESCRIPTOR.services_by_name['Users'] = _USERS

# @@protoc_insertion_point(module_scope)
