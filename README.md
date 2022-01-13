generate types
```
python -m grpc_tools.protoc --python_out=./src/generated --grpc_python_out=./src/generated -I ./src --mypy_out=src/generated ./src/**/protos/*.proto
```