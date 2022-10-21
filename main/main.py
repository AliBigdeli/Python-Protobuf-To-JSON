# Simple example to create protobuf object out of dict
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


# Converting from protobuf object to json and dict
from google.protobuf.json_format import MessageToDict, MessageToJson
message_as_json = MessageToJson(message)
message_as_dict = MessageToJson(message)
print("json: \n",message_as_json)
print("dict: \n",message_as_dict)


# creating a binary file as and output
output_file = open("./main/proto_string", "wb")
output_file.write(message.SerializeToString())
output_file.close()


# reading the file and decoding to json
input_file = open("./main/proto_string", "rb")
message_obj = sample_pb2.SomeMessage()
message_obj.ParseFromString(input_file.read())
print(message_obj)



# creating protobuf object from serialized protobuf data
#  and converting to json object
string_data = '''result {
  temp: 10
  timestamp: 1666175702
}'''

from google.protobuf.text_format import Parse
message_obj_2 = sample_pb2.SomeMessage()
message_obj_data = Parse(string_data,message_obj_2)
message_dict = MessageToDict(message_obj_data)
message_json = MessageToJson(message_obj_data)
print("json: \n",message_json)
print("dict: \n",message_dict)