generate types
```
python -m grpc_tools.protoc --python_out=./src/generated --grpc_python_out=./src/generated/ -I ./src/proto --mypy_out=src/generated ./src/proto/*.proto
```

lint-fix = "pre-commit run --all-files"
start-dev = "python -m src.app"
local-db = "docker-compose up"
local-server = "uvicorn src.app:app --reload"
test-int = "pytest tests/integration/*"
generate-code = "python -m grpc_tools.protoc --python_out=./src/generated --grpc_python_out=./src/generated -I ./src ./src/**/protos/*.proto"
