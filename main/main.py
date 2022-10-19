import json
import sample_pb2
from google.protobuf.json_format import Parse, ParseDict

data = {
  "result": {
    "temp": 10,
    "timestamp": 1666175702
    
  }
}

message = ParseDict(data, sample_pb2.SomeMessage())

print(message)
from google.protobuf.json_format import MessageToDict, MessageToJson

message_as_json_str = MessageToJson(message)

print(message_as_json_str)

