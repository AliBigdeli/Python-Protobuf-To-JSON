<h1 align="center">Protobuf to Json and Opposite with Python</h1>
<h3 align="center">Simple demonstration of how you can change json to probuf google and opposite</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://www.freecodecamp.org/news/content/images/size/w2000/2020/05/unnamed-1.png" alt="git" width="100" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a>
</p>


# Goal
The whole goal and purpose of this repository is to make a sample and step by step coding and setup for creating .proto file and converting to json.

# Create a json Sample
i will be using the below json example as a sample:

```js
{
  "result": {
    "temp": 10,
    "timestamp": 1666175702
  }
}
```
# Convert json to .proto file

there are a lot of ways to this part but one of the easiest way is to use this web page which can convert your json data into .proto file in a matter of second. after that just copy the content and put it in a file and name it correctly as FILENAME.proto.

link to website: https://json-to-proto.github.io/


# Download bin files and add to environments
base on you os you can choose what source you want to download. this particular directory will help you use protoc commands in command line to generate the module for using in python code as translate for your data.

link to files: https://github.com/protocolbuffers/protobuf/releases

<strong>note:</strong> I am using windows at the moment so i will choose: ```protoc-21.8-win64.zip```
now all you have to do is to add this directory to your windows environments path: ```path-to-folder/bin``` just like ```c:\protobuf\bin```

# Generate the module
First you need to install the dependency of the generator which can be handled by installing a module through pip:
```shell
pip install protobuf
```
Then you can generate the module based on the proto file that you created by the website. with following the structure of the command bellow:
```shell
protoc -I=. --python_out=./output ./sample.proto  
```
For more information check this reference:
https://developers.google.com/protocol-buffers/docs/pythontutorial

# Use the Generated module in code
now that you have created the module you can use it to create and parse data with it. for simplicity i created and example for you in main directory which will help you turn a json into and protobuf string and then reverse it to json again.

```python
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
```

Output:
```js
result {
  temp: 10
  timestamp: 1666175702
}

json:
 {
  "result": {
    "temp": 10,
    "timestamp": 1666175702
  }
}
dict:
 {
  "result": {
    "temp": 10,
    "timestamp": 1666175702
  }
}
result {
  temp: 10
  timestamp: 1666175702
}

json: 
 {
  "result": {
    "temp": 10,
    "timestamp": 1666175702
  }
}
dict:
 {'result': {'temp': 10, 'timestamp': 1666175702}}

```