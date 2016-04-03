# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: automation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='automation.proto',
  package='automation',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x61utomation.proto\x12\nautomation\"\x90\x01\n\x10\x43lusterOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x0cserial_tasks\x18\x02 \x03(\x0b\x32\x19.automation.TaskContainer\x12\x30\n\x05state\x18\x03 \x01(\x0e\x32!.automation.ClusterOperationState\x12\r\n\x05\x65rror\x18\x04 \x01(\t\"N\n\rTaskContainer\x12(\n\x0eparallel_tasks\x18\x01 \x03(\x0b\x32\x10.automation.Task\x12\x13\n\x0b\x63oncurrency\x18\x02 \x01(\x05\"\xce\x01\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\nparameters\x18\x02 \x03(\x0b\x32 .automation.Task.ParametersEntry\x12\n\n\x02id\x18\x03 \x01(\t\x12$\n\x05state\x18\x04 \x01(\x0e\x32\x15.automation.TaskState\x12\x0e\n\x06output\x18\x05 \x01(\t\x12\r\n\x05\x65rror\x18\x06 \x01(\t\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb1\x01\n\x1e\x45nqueueClusterOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\nparameters\x18\x02 \x03(\x0b\x32:.automation.EnqueueClusterOperationRequest.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\x1f\x45nqueueClusterOperationResponse\x12\n\n\x02id\x18\x01 \x01(\t\"-\n\x1fGetClusterOperationStateRequest\x12\n\n\x02id\x18\x01 \x01(\t\"T\n GetClusterOperationStateResponse\x12\x30\n\x05state\x18\x01 \x01(\x0e\x32!.automation.ClusterOperationState\"/\n!GetClusterOperationDetailsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"V\n\"GetClusterOperationDetailsResponse\x12\x30\n\ncluster_op\x18\x02 \x01(\x0b\x32\x1c.automation.ClusterOperation*\x9a\x01\n\x15\x43lusterOperationState\x12#\n\x1fUNKNOWN_CLUSTER_OPERATION_STATE\x10\x00\x12!\n\x1d\x43LUSTER_OPERATION_NOT_STARTED\x10\x01\x12\x1d\n\x19\x43LUSTER_OPERATION_RUNNING\x10\x02\x12\x1a\n\x16\x43LUSTER_OPERATION_DONE\x10\x03*K\n\tTaskState\x12\x16\n\x12UNKNOWN_TASK_STATE\x10\x00\x12\x0f\n\x0bNOT_STARTED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CLUSTEROPERATIONSTATE = _descriptor.EnumDescriptor(
  name='ClusterOperationState',
  full_name='automation.ClusterOperationState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CLUSTER_OPERATION_STATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUSTER_OPERATION_NOT_STARTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUSTER_OPERATION_RUNNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLUSTER_OPERATION_DONE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=966,
  serialized_end=1120,
)
_sym_db.RegisterEnumDescriptor(_CLUSTEROPERATIONSTATE)

ClusterOperationState = enum_type_wrapper.EnumTypeWrapper(_CLUSTEROPERATIONSTATE)
_TASKSTATE = _descriptor.EnumDescriptor(
  name='TaskState',
  full_name='automation.TaskState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TASK_STATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_STARTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1122,
  serialized_end=1197,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE)

TaskState = enum_type_wrapper.EnumTypeWrapper(_TASKSTATE)
UNKNOWN_CLUSTER_OPERATION_STATE = 0
CLUSTER_OPERATION_NOT_STARTED = 1
CLUSTER_OPERATION_RUNNING = 2
CLUSTER_OPERATION_DONE = 3
UNKNOWN_TASK_STATE = 0
NOT_STARTED = 1
RUNNING = 2
DONE = 3



_CLUSTEROPERATION = _descriptor.Descriptor(
  name='ClusterOperation',
  full_name='automation.ClusterOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='automation.ClusterOperation.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_tasks', full_name='automation.ClusterOperation.serial_tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='automation.ClusterOperation.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='automation.ClusterOperation.error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=33,
  serialized_end=177,
)


_TASKCONTAINER = _descriptor.Descriptor(
  name='TaskContainer',
  full_name='automation.TaskContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parallel_tasks', full_name='automation.TaskContainer.parallel_tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='concurrency', full_name='automation.TaskContainer.concurrency', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=179,
  serialized_end=257,
)


_TASK_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='automation.Task.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='automation.Task.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='automation.Task.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=466,
)

_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='automation.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='automation.Task.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='automation.Task.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='automation.Task.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='automation.Task.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='automation.Task.output', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='automation.Task.error', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TASK_PARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=466,
)


_ENQUEUECLUSTEROPERATIONREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='automation.EnqueueClusterOperationRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='automation.EnqueueClusterOperationRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='automation.EnqueueClusterOperationRequest.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=466,
)

_ENQUEUECLUSTEROPERATIONREQUEST = _descriptor.Descriptor(
  name='EnqueueClusterOperationRequest',
  full_name='automation.EnqueueClusterOperationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='automation.EnqueueClusterOperationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='automation.EnqueueClusterOperationRequest.parameters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ENQUEUECLUSTEROPERATIONREQUEST_PARAMETERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=469,
  serialized_end=646,
)


_ENQUEUECLUSTEROPERATIONRESPONSE = _descriptor.Descriptor(
  name='EnqueueClusterOperationResponse',
  full_name='automation.EnqueueClusterOperationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='automation.EnqueueClusterOperationResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=648,
  serialized_end=693,
)


_GETCLUSTEROPERATIONSTATEREQUEST = _descriptor.Descriptor(
  name='GetClusterOperationStateRequest',
  full_name='automation.GetClusterOperationStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='automation.GetClusterOperationStateRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=695,
  serialized_end=740,
)


_GETCLUSTEROPERATIONSTATERESPONSE = _descriptor.Descriptor(
  name='GetClusterOperationStateResponse',
  full_name='automation.GetClusterOperationStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='automation.GetClusterOperationStateResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=742,
  serialized_end=826,
)


_GETCLUSTEROPERATIONDETAILSREQUEST = _descriptor.Descriptor(
  name='GetClusterOperationDetailsRequest',
  full_name='automation.GetClusterOperationDetailsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='automation.GetClusterOperationDetailsRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=828,
  serialized_end=875,
)


_GETCLUSTEROPERATIONDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetClusterOperationDetailsResponse',
  full_name='automation.GetClusterOperationDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_op', full_name='automation.GetClusterOperationDetailsResponse.cluster_op', index=0,
      number=2, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=877,
  serialized_end=963,
)

_CLUSTEROPERATION.fields_by_name['serial_tasks'].message_type = _TASKCONTAINER
_CLUSTEROPERATION.fields_by_name['state'].enum_type = _CLUSTEROPERATIONSTATE
_TASKCONTAINER.fields_by_name['parallel_tasks'].message_type = _TASK
_TASK_PARAMETERSENTRY.containing_type = _TASK
_TASK.fields_by_name['parameters'].message_type = _TASK_PARAMETERSENTRY
_TASK.fields_by_name['state'].enum_type = _TASKSTATE
_ENQUEUECLUSTEROPERATIONREQUEST_PARAMETERSENTRY.containing_type = _ENQUEUECLUSTEROPERATIONREQUEST
_ENQUEUECLUSTEROPERATIONREQUEST.fields_by_name['parameters'].message_type = _ENQUEUECLUSTEROPERATIONREQUEST_PARAMETERSENTRY
_GETCLUSTEROPERATIONSTATERESPONSE.fields_by_name['state'].enum_type = _CLUSTEROPERATIONSTATE
_GETCLUSTEROPERATIONDETAILSRESPONSE.fields_by_name['cluster_op'].message_type = _CLUSTEROPERATION
DESCRIPTOR.message_types_by_name['ClusterOperation'] = _CLUSTEROPERATION
DESCRIPTOR.message_types_by_name['TaskContainer'] = _TASKCONTAINER
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['EnqueueClusterOperationRequest'] = _ENQUEUECLUSTEROPERATIONREQUEST
DESCRIPTOR.message_types_by_name['EnqueueClusterOperationResponse'] = _ENQUEUECLUSTEROPERATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetClusterOperationStateRequest'] = _GETCLUSTEROPERATIONSTATEREQUEST
DESCRIPTOR.message_types_by_name['GetClusterOperationStateResponse'] = _GETCLUSTEROPERATIONSTATERESPONSE
DESCRIPTOR.message_types_by_name['GetClusterOperationDetailsRequest'] = _GETCLUSTEROPERATIONDETAILSREQUEST
DESCRIPTOR.message_types_by_name['GetClusterOperationDetailsResponse'] = _GETCLUSTEROPERATIONDETAILSRESPONSE
DESCRIPTOR.enum_types_by_name['ClusterOperationState'] = _CLUSTEROPERATIONSTATE
DESCRIPTOR.enum_types_by_name['TaskState'] = _TASKSTATE

ClusterOperation = _reflection.GeneratedProtocolMessageType('ClusterOperation', (_message.Message,), dict(
  DESCRIPTOR = _CLUSTEROPERATION,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.ClusterOperation)
  ))
_sym_db.RegisterMessage(ClusterOperation)

TaskContainer = _reflection.GeneratedProtocolMessageType('TaskContainer', (_message.Message,), dict(
  DESCRIPTOR = _TASKCONTAINER,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.TaskContainer)
  ))
_sym_db.RegisterMessage(TaskContainer)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _TASK_PARAMETERSENTRY,
    __module__ = 'automation_pb2'
    # @@protoc_insertion_point(class_scope:automation.Task.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _TASK,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.Task)
  ))
_sym_db.RegisterMessage(Task)
_sym_db.RegisterMessage(Task.ParametersEntry)

EnqueueClusterOperationRequest = _reflection.GeneratedProtocolMessageType('EnqueueClusterOperationRequest', (_message.Message,), dict(

  ParametersEntry = _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), dict(
    DESCRIPTOR = _ENQUEUECLUSTEROPERATIONREQUEST_PARAMETERSENTRY,
    __module__ = 'automation_pb2'
    # @@protoc_insertion_point(class_scope:automation.EnqueueClusterOperationRequest.ParametersEntry)
    ))
  ,
  DESCRIPTOR = _ENQUEUECLUSTEROPERATIONREQUEST,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.EnqueueClusterOperationRequest)
  ))
_sym_db.RegisterMessage(EnqueueClusterOperationRequest)
_sym_db.RegisterMessage(EnqueueClusterOperationRequest.ParametersEntry)

EnqueueClusterOperationResponse = _reflection.GeneratedProtocolMessageType('EnqueueClusterOperationResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENQUEUECLUSTEROPERATIONRESPONSE,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.EnqueueClusterOperationResponse)
  ))
_sym_db.RegisterMessage(EnqueueClusterOperationResponse)

GetClusterOperationStateRequest = _reflection.GeneratedProtocolMessageType('GetClusterOperationStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTEROPERATIONSTATEREQUEST,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.GetClusterOperationStateRequest)
  ))
_sym_db.RegisterMessage(GetClusterOperationStateRequest)

GetClusterOperationStateResponse = _reflection.GeneratedProtocolMessageType('GetClusterOperationStateResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTEROPERATIONSTATERESPONSE,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.GetClusterOperationStateResponse)
  ))
_sym_db.RegisterMessage(GetClusterOperationStateResponse)

GetClusterOperationDetailsRequest = _reflection.GeneratedProtocolMessageType('GetClusterOperationDetailsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTEROPERATIONDETAILSREQUEST,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.GetClusterOperationDetailsRequest)
  ))
_sym_db.RegisterMessage(GetClusterOperationDetailsRequest)

GetClusterOperationDetailsResponse = _reflection.GeneratedProtocolMessageType('GetClusterOperationDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCLUSTEROPERATIONDETAILSRESPONSE,
  __module__ = 'automation_pb2'
  # @@protoc_insertion_point(class_scope:automation.GetClusterOperationDetailsResponse)
  ))
_sym_db.RegisterMessage(GetClusterOperationDetailsResponse)


_TASK_PARAMETERSENTRY.has_options = True
_TASK_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ENQUEUECLUSTEROPERATIONREQUEST_PARAMETERSENTRY.has_options = True
_ENQUEUECLUSTEROPERATIONREQUEST_PARAMETERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
