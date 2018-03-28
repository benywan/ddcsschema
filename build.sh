#!/bin/bash

set -euxo pipefail

echo "Building protobuf files"
rm -rf ./ddcsschema/schema/*_pb2.py
find . -name "*.pyc" -delete
protoc --proto_path=./ddcsschema/proto --python_out=./ddcsschema/schema ./ddcsschema/proto/*.proto
