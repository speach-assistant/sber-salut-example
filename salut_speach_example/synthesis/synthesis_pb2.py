# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: synthesis.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import task_pb2 as task__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsynthesis.proto\x12\x18smartspeech.synthesis.v1\x1a\ntask.proto\x1a\x1egoogle/protobuf/duration.proto\"\xee\x02\n\x10SynthesisRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12P\n\x0e\x61udio_encoding\x18\x02 \x01(\x0e\x32\x38.smartspeech.synthesis.v1.SynthesisRequest.AudioEncoding\x12\x10\n\x08language\x18\x03 \x01(\t\x12L\n\x0c\x63ontent_type\x18\x04 \x01(\x0e\x32\x36.smartspeech.synthesis.v1.SynthesisRequest.ContentType\x12\r\n\x05voice\x18\x05 \x01(\t\x12\x15\n\rrebuild_cache\x18\x06 \x01(\x08\"Q\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\r\n\tPCM_S16LE\x10\x01\x12\x08\n\x04OPUS\x10\x02\x12\x07\n\x03WAV\x10\x03\"!\n\x0b\x43ontentType\x12\x08\n\x04TEXT\x10\x00\x12\x08\n\x04SSML\x10\x01\"T\n\x11SynthesisResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x31\n\x0e\x61udio_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"\x91\x01\n\x15\x41syncSynthesisRequest\x12\x17\n\x0frequest_file_id\x18\x01 \x01(\t\x12P\n\x0e\x61udio_encoding\x18\x02 \x01(\x0e\x32\x38.smartspeech.synthesis.v1.SynthesisRequest.AudioEncoding\x12\r\n\x05voice\x18\x03 \x01(\t2\xd5\x01\n\x0bSmartSpeech\x12g\n\nSynthesize\x12*.smartspeech.synthesis.v1.SynthesisRequest\x1a+.smartspeech.synthesis.v1.SynthesisResponse0\x01\x12]\n\x0f\x41syncSynthesize\x12/.smartspeech.synthesis.v1.AsyncSynthesisRequest\x1a\x19.smartspeech.task.v1.TaskB\x13\n\x04TODOZ\x0b./;protocolb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'synthesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\004TODOZ\013./;protocol'
  _globals['_SYNTHESISREQUEST']._serialized_start=90
  _globals['_SYNTHESISREQUEST']._serialized_end=456
  _globals['_SYNTHESISREQUEST_AUDIOENCODING']._serialized_start=340
  _globals['_SYNTHESISREQUEST_AUDIOENCODING']._serialized_end=421
  _globals['_SYNTHESISREQUEST_CONTENTTYPE']._serialized_start=423
  _globals['_SYNTHESISREQUEST_CONTENTTYPE']._serialized_end=456
  _globals['_SYNTHESISRESPONSE']._serialized_start=458
  _globals['_SYNTHESISRESPONSE']._serialized_end=542
  _globals['_ASYNCSYNTHESISREQUEST']._serialized_start=545
  _globals['_ASYNCSYNTHESISREQUEST']._serialized_end=690
  _globals['_SMARTSPEECH']._serialized_start=693
  _globals['_SMARTSPEECH']._serialized_end=906
# @@protoc_insertion_point(module_scope)
