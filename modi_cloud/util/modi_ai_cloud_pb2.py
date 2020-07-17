# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modi_ai_cloud.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='modi_ai_cloud.proto',
  package='modi_cloud',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13modi_ai_cloud.proto\x12\nmodi_cloud\"F\n\x0bObjectsSend\x12\x13\n\x0btrain_array\x18\x01 \x01(\x0c\x12\x13\n\x0blabel_array\x18\x02 \x01(\x0c\x12\r\n\x05model\x18\x03 \x01(\x0c\" \n\nStdoutSend\x12\x12\n\nask_stdout\x18\x01 \x01(\x05\"#\n\x0bStdoutReply\x12\x14\n\x0creply_stdout\x18\x01 \x01(\t\",\n\x14TransferCompleteSend\x12\x14\n\x0c\x61sk_transfer\x18\x01 \x01(\x05\",\n\x14LearningCompleteSend\x12\x14\n\x0c\x61sk_learning\x18\x01 \x01(\x05\"/\n\x15TransferCompleteReply\x12\x16\n\x0ereply_transfer\x18\x01 \x01(\x05\"/\n\x15LearningCompleteReply\x12\x16\n\x0ereply_learning\x18\x01 \x01(\x05\"#\n\nModelReply\x12\x15\n\rtrained_model\x18\x01 \x01(\x0c\x32\x91\x03\n\x12\x44\x61ta_Model_Handler\x12>\n\x0bSendObjects\x12\x17.modi_cloud.ObjectsSend\x1a\x16.modi_cloud.ModelReply\x12\x43\n\x10SendObjectsAgain\x12\x17.modi_cloud.ObjectsSend\x1a\x16.modi_cloud.ModelReply\x12W\n\x10TransferComplete\x12 .modi_cloud.TransferCompleteSend\x1a!.modi_cloud.TransferCompleteReply\x12W\n\x10LearningComplete\x12 .modi_cloud.LearningCompleteSend\x1a!.modi_cloud.LearningCompleteReply\x12\x44\n\x0fMonitorLearning\x12\x16.modi_cloud.StdoutSend\x1a\x17.modi_cloud.StdoutReply0\x01\x62\x06proto3'
)




_OBJECTSSEND = _descriptor.Descriptor(
  name='ObjectsSend',
  full_name='modi_cloud.ObjectsSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_array', full_name='modi_cloud.ObjectsSend.train_array', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_array', full_name='modi_cloud.ObjectsSend.label_array', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model', full_name='modi_cloud.ObjectsSend.model', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=35,
  serialized_end=105,
)


_STDOUTSEND = _descriptor.Descriptor(
  name='StdoutSend',
  full_name='modi_cloud.StdoutSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ask_stdout', full_name='modi_cloud.StdoutSend.ask_stdout', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=107,
  serialized_end=139,
)


_STDOUTREPLY = _descriptor.Descriptor(
  name='StdoutReply',
  full_name='modi_cloud.StdoutReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_stdout', full_name='modi_cloud.StdoutReply.reply_stdout', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=141,
  serialized_end=176,
)


_TRANSFERCOMPLETESEND = _descriptor.Descriptor(
  name='TransferCompleteSend',
  full_name='modi_cloud.TransferCompleteSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ask_transfer', full_name='modi_cloud.TransferCompleteSend.ask_transfer', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=178,
  serialized_end=222,
)


_LEARNINGCOMPLETESEND = _descriptor.Descriptor(
  name='LearningCompleteSend',
  full_name='modi_cloud.LearningCompleteSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ask_learning', full_name='modi_cloud.LearningCompleteSend.ask_learning', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=224,
  serialized_end=268,
)


_TRANSFERCOMPLETEREPLY = _descriptor.Descriptor(
  name='TransferCompleteReply',
  full_name='modi_cloud.TransferCompleteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_transfer', full_name='modi_cloud.TransferCompleteReply.reply_transfer', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=270,
  serialized_end=317,
)


_LEARNINGCOMPLETEREPLY = _descriptor.Descriptor(
  name='LearningCompleteReply',
  full_name='modi_cloud.LearningCompleteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_learning', full_name='modi_cloud.LearningCompleteReply.reply_learning', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=319,
  serialized_end=366,
)


_MODELREPLY = _descriptor.Descriptor(
  name='ModelReply',
  full_name='modi_cloud.ModelReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trained_model', full_name='modi_cloud.ModelReply.trained_model', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=368,
  serialized_end=403,
)

DESCRIPTOR.message_types_by_name['ObjectsSend'] = _OBJECTSSEND
DESCRIPTOR.message_types_by_name['StdoutSend'] = _STDOUTSEND
DESCRIPTOR.message_types_by_name['StdoutReply'] = _STDOUTREPLY
DESCRIPTOR.message_types_by_name['TransferCompleteSend'] = _TRANSFERCOMPLETESEND
DESCRIPTOR.message_types_by_name['LearningCompleteSend'] = _LEARNINGCOMPLETESEND
DESCRIPTOR.message_types_by_name['TransferCompleteReply'] = _TRANSFERCOMPLETEREPLY
DESCRIPTOR.message_types_by_name['LearningCompleteReply'] = _LEARNINGCOMPLETEREPLY
DESCRIPTOR.message_types_by_name['ModelReply'] = _MODELREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectsSend = _reflection.GeneratedProtocolMessageType('ObjectsSend', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSSEND,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.ObjectsSend)
  })
_sym_db.RegisterMessage(ObjectsSend)

StdoutSend = _reflection.GeneratedProtocolMessageType('StdoutSend', (_message.Message,), {
  'DESCRIPTOR' : _STDOUTSEND,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.StdoutSend)
  })
_sym_db.RegisterMessage(StdoutSend)

StdoutReply = _reflection.GeneratedProtocolMessageType('StdoutReply', (_message.Message,), {
  'DESCRIPTOR' : _STDOUTREPLY,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.StdoutReply)
  })
_sym_db.RegisterMessage(StdoutReply)

TransferCompleteSend = _reflection.GeneratedProtocolMessageType('TransferCompleteSend', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERCOMPLETESEND,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.TransferCompleteSend)
  })
_sym_db.RegisterMessage(TransferCompleteSend)

LearningCompleteSend = _reflection.GeneratedProtocolMessageType('LearningCompleteSend', (_message.Message,), {
  'DESCRIPTOR' : _LEARNINGCOMPLETESEND,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.LearningCompleteSend)
  })
_sym_db.RegisterMessage(LearningCompleteSend)

TransferCompleteReply = _reflection.GeneratedProtocolMessageType('TransferCompleteReply', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERCOMPLETEREPLY,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.TransferCompleteReply)
  })
_sym_db.RegisterMessage(TransferCompleteReply)

LearningCompleteReply = _reflection.GeneratedProtocolMessageType('LearningCompleteReply', (_message.Message,), {
  'DESCRIPTOR' : _LEARNINGCOMPLETEREPLY,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.LearningCompleteReply)
  })
_sym_db.RegisterMessage(LearningCompleteReply)

ModelReply = _reflection.GeneratedProtocolMessageType('ModelReply', (_message.Message,), {
  'DESCRIPTOR' : _MODELREPLY,
  '__module__' : 'modi_ai_cloud_pb2'
  # @@protoc_insertion_point(class_scope:modi_cloud.ModelReply)
  })
_sym_db.RegisterMessage(ModelReply)



_DATA_MODEL_HANDLER = _descriptor.ServiceDescriptor(
  name='Data_Model_Handler',
  full_name='modi_cloud.Data_Model_Handler',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=406,
  serialized_end=807,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendObjects',
    full_name='modi_cloud.Data_Model_Handler.SendObjects',
    index=0,
    containing_service=None,
    input_type=_OBJECTSSEND,
    output_type=_MODELREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendObjectsAgain',
    full_name='modi_cloud.Data_Model_Handler.SendObjectsAgain',
    index=1,
    containing_service=None,
    input_type=_OBJECTSSEND,
    output_type=_MODELREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TransferComplete',
    full_name='modi_cloud.Data_Model_Handler.TransferComplete',
    index=2,
    containing_service=None,
    input_type=_TRANSFERCOMPLETESEND,
    output_type=_TRANSFERCOMPLETEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='LearningComplete',
    full_name='modi_cloud.Data_Model_Handler.LearningComplete',
    index=3,
    containing_service=None,
    input_type=_LEARNINGCOMPLETESEND,
    output_type=_LEARNINGCOMPLETEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MonitorLearning',
    full_name='modi_cloud.Data_Model_Handler.MonitorLearning',
    index=4,
    containing_service=None,
    input_type=_STDOUTSEND,
    output_type=_STDOUTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATA_MODEL_HANDLER)

DESCRIPTOR.services_by_name['Data_Model_Handler'] = _DATA_MODEL_HANDLER

# @@protoc_insertion_point(module_scope)
