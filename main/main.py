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


# creating a binary file as and output
output_file = open("./main/proto_string", "wb")
output_file.write(message.SerializeToString())
output_file.close()


# reading the file and decoding to json
output_file = open("./main/proto_string", "rb")
message2 = sample_pb2.SomeMessage()
message2.ParseFromString(output_file.read())
print(message2)



# creating protobuf object from serialized protobuf data
#  and converting to json object
string_data = '''result {
  temp: 10
  timestamp: 1666175702
}'''

from google.protobuf.text_format import Parse
message_obj = sample_pb2.SomeMessage()
message_obj_data = Parse(string_data,message_obj)
message_dict = MessageToDict(message_obj_data)
message_json = MessageToJson(message_obj_data)
print(message_dict)