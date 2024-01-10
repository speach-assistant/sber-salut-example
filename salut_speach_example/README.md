# Installation
```
$ pip3 install grpcio-tools
$ cd /salute_speach_example/synthesis
$ python -m grpc_tools.protoc -I . -I .. --python_out=. --grpc_python_out=. synthesis.proto ../storage.proto ../task.proto
$ cd /salute_speach_example/recognition
$ python -m grpc_tools.protoc -I . -I .. --python_out=. --grpc_python_out=. recognition.proto ../storage.proto ../task.proto
```
# Usage synthesis
```
$ python synthesize_example.py --file "test.wav" --text "Тестовый синтез Петровича."
$ python synthesize_example_no_file.py
```
# Usage recognition
```
$ 
$ 
```