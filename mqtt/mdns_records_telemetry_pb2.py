# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mdns_records_telemetry.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cmdns_records_telemetry.proto\x12!interfaces.mdns_records_telemetry\"\xc4\x01\n\nMdnsRecord\x12\x12\n\nowner_name\x18\x01 \x01(\t\x12?\n\x04type\x18\x02 \x01(\x0e\x32\x31.interfaces.mdns_records_telemetry.MdnsRecordType\x12\x13\n\x0b\x64omain_name\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x10\n\x08res_desc\x18\x05 \x01(\x0c\x12\x10\n\x08priority\x18\x06 \x01(\r\x12\x0e\n\x06weight\x18\x07 \x01(\r\x12\x0c\n\x04port\x18\x08 \x01(\r\"j\n\nMdnsClient\x12\x0b\n\x03mac\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x43\n\x0cmdns_records\x18\x03 \x03(\x0b\x32-.interfaces.mdns_records_telemetry.MdnsRecord\"8\n\x10ObservationPoint\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\x13\n\x0blocation_id\x18\x02 \x01(\t\"9\n\x11ObservationWindow\x12\x12\n\nstarted_at\x18\x01 \x01(\x04\x12\x10\n\x08\x65nded_at\x18\x02 \x01(\x04\"\xf5\x01\n\x11MdnsRecordsReport\x12N\n\x11observation_point\x18\x01 \x01(\x0b\x32\x33.interfaces.mdns_records_telemetry.ObservationPoint\x12P\n\x12observation_window\x18\x02 \x01(\x0b\x32\x34.interfaces.mdns_records_telemetry.ObservationWindow\x12>\n\x07\x63lients\x18\x03 \x03(\x0b\x32-.interfaces.mdns_records_telemetry.MdnsClient*\xcd\x01\n\x0eMdnsRecordType\x12 \n\x1cMDNS_RECORD_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12MDNS_RECORD_TYPE_A\x10\x01\x12\x17\n\x13MDNS_RECORD_TYPE_NS\x10\x02\x12\x1a\n\x16MDNS_RECORD_TYPE_CNAME\x10\x03\x12\x18\n\x14MDNS_RECORD_TYPE_PTR\x10\x04\x12\x18\n\x14MDNS_RECORD_TYPE_TXT\x10\x05\x12\x18\n\x14MDNS_RECORD_TYPE_SRV\x10\x06')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mdns_records_telemetry_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MDNSRECORDTYPE._serialized_start=740
  _MDNSRECORDTYPE._serialized_end=945
  _MDNSRECORD._serialized_start=68
  _MDNSRECORD._serialized_end=264
  _MDNSCLIENT._serialized_start=266
  _MDNSCLIENT._serialized_end=372
  _OBSERVATIONPOINT._serialized_start=374
  _OBSERVATIONPOINT._serialized_end=430
  _OBSERVATIONWINDOW._serialized_start=432
  _OBSERVATIONWINDOW._serialized_end=489
  _MDNSRECORDSREPORT._serialized_start=492
  _MDNSRECORDSREPORT._serialized_end=737
# @@protoc_insertion_point(module_scope)
