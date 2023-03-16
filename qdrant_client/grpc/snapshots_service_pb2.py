# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: snapshots_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17snapshots_service.proto\x12\x06qdrant\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1b\n\x19\x43reateFullSnapshotRequest\"\x1a\n\x18ListFullSnapshotsRequest\"2\n\x19\x44\x65leteFullSnapshotRequest\x12\x15\n\rsnapshot_name\x18\x01 \x01(\t\"0\n\x15\x43reateSnapshotRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"/\n\x14ListSnapshotsRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"G\n\x15\x44\x65leteSnapshotRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x15\n\rsnapshot_name\x18\x02 \x01(\t\"d\n\x13SnapshotDescription\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\rcreation_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04size\x18\x03 \x01(\x03\"a\n\x16\x43reateSnapshotResponse\x12\x39\n\x14snapshot_description\x18\x01 \x01(\x0b\x32\x1b.qdrant.SnapshotDescription\x12\x0c\n\x04time\x18\x02 \x01(\x01\"a\n\x15ListSnapshotsResponse\x12:\n\x15snapshot_descriptions\x18\x01 \x03(\x0b\x32\x1b.qdrant.SnapshotDescription\x12\x0c\n\x04time\x18\x02 \x01(\x01\"&\n\x16\x44\x65leteSnapshotResponse\x12\x0c\n\x04time\x18\x01 \x01(\x01\x32\xdd\x03\n\tSnapshots\x12I\n\x06\x43reate\x12\x1d.qdrant.CreateSnapshotRequest\x1a\x1e.qdrant.CreateSnapshotResponse\"\x00\x12\x45\n\x04List\x12\x1c.qdrant.ListSnapshotsRequest\x1a\x1d.qdrant.ListSnapshotsResponse\"\x00\x12I\n\x06\x44\x65lete\x12\x1d.qdrant.DeleteSnapshotRequest\x1a\x1e.qdrant.DeleteSnapshotResponse\"\x00\x12Q\n\nCreateFull\x12!.qdrant.CreateFullSnapshotRequest\x1a\x1e.qdrant.CreateSnapshotResponse\"\x00\x12M\n\x08ListFull\x12 .qdrant.ListFullSnapshotsRequest\x1a\x1d.qdrant.ListSnapshotsResponse\"\x00\x12Q\n\nDeleteFull\x12!.qdrant.DeleteFullSnapshotRequest\x1a\x1e.qdrant.DeleteSnapshotResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'snapshots_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEFULLSNAPSHOTREQUEST._serialized_start=98
  _CREATEFULLSNAPSHOTREQUEST._serialized_end=125
  _LISTFULLSNAPSHOTSREQUEST._serialized_start=127
  _LISTFULLSNAPSHOTSREQUEST._serialized_end=153
  _DELETEFULLSNAPSHOTREQUEST._serialized_start=155
  _DELETEFULLSNAPSHOTREQUEST._serialized_end=205
  _CREATESNAPSHOTREQUEST._serialized_start=207
  _CREATESNAPSHOTREQUEST._serialized_end=255
  _LISTSNAPSHOTSREQUEST._serialized_start=257
  _LISTSNAPSHOTSREQUEST._serialized_end=304
  _DELETESNAPSHOTREQUEST._serialized_start=306
  _DELETESNAPSHOTREQUEST._serialized_end=377
  _SNAPSHOTDESCRIPTION._serialized_start=379
  _SNAPSHOTDESCRIPTION._serialized_end=479
  _CREATESNAPSHOTRESPONSE._serialized_start=481
  _CREATESNAPSHOTRESPONSE._serialized_end=578
  _LISTSNAPSHOTSRESPONSE._serialized_start=580
  _LISTSNAPSHOTSRESPONSE._serialized_end=677
  _DELETESNAPSHOTRESPONSE._serialized_start=679
  _DELETESNAPSHOTRESPONSE._serialized_end=717
  _SNAPSHOTS._serialized_start=720
  _SNAPSHOTS._serialized_end=1197
# @@protoc_insertion_point(module_scope)
