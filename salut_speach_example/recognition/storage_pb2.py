# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\x16smartspeech.storage.v1\"#\n\rUploadRequest\x12\x12\n\nfile_chunk\x18\x01 \x01(\x0c\")\n\x0eUploadResponse\x12\x17\n\x0frequest_file_id\x18\x01 \x01(\t\"+\n\x0f\x44ownloadRequest\x12\x18\n\x10response_file_id\x18\x01 \x01(\t\"&\n\x10\x44ownloadResponse\x12\x12\n\nfile_chunk\x18\x01 \x01(\x0c\x32\xcd\x01\n\x0bSmartSpeech\x12[\n\x06Upload\x12%.smartspeech.storage.v1.UploadRequest\x1a&.smartspeech.storage.v1.UploadResponse\"\x00(\x01\x12\x61\n\x08\x44ownload\x12\'.smartspeech.storage.v1.DownloadRequest\x1a(.smartspeech.storage.v1.DownloadResponse\"\x00\x30\x01\x42\x62\n)ru.sberdevices.smartspeech.recognition.v1Z5github.com/sberdevices/smartspeech/storage/v1;storageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)ru.sberdevices.smartspeech.recognition.v1Z5github.com/sberdevices/smartspeech/storage/v1;storage'
  _globals['_UPLOADREQUEST']._serialized_start=41
  _globals['_UPLOADREQUEST']._serialized_end=76
  _globals['_UPLOADRESPONSE']._serialized_start=78
  _globals['_UPLOADRESPONSE']._serialized_end=119
  _globals['_DOWNLOADREQUEST']._serialized_start=121
  _globals['_DOWNLOADREQUEST']._serialized_end=164
  _globals['_DOWNLOADRESPONSE']._serialized_start=166
  _globals['_DOWNLOADRESPONSE']._serialized_end=204
  _globals['_SMARTSPEECH']._serialized_start=207
  _globals['_SMARTSPEECH']._serialized_end=412
# @@protoc_insertion_point(module_scope)
