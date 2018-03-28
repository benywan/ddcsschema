## Protobuf schema for [DDCS](https://github.com/benywan/ddcs) claims and spec for ddcs:// URIs

ddcsschema is a [protobuf](https://github.com/google/protobuf) schema that defines how claims are structured and validated in the LBRY blockchain.
There is also code to construct, parse, and validate ddcs:// URIs.

### Use

Add `git+https://github.com/benywan/ddcsschema.git#egg=ddcsschema` to `requirements.txt`

### Protobuf Schema

See [docs/schema.md](https://github.com/benywan/ddcsschema/blob/master/docs/schema.md).

### Development

To install in development mode, run `pip install -r requirements.txt; pip install -e .` from the repo directory.

To run the tests, run `./run_tests_and_pylint.sh` from the repo directory.

#### Compile .proto files

There are compiled protobuf files in `ddcsschema/schema` (see the files that end in `_pb2.py`), so compiling fresh is not necessary for most.

If you want to compile the protobuf files yourself, install `protoc`:

- macOS: `brew install protobuf`
- Ubuntu: `sudo apt-get install protobuf-compiler python-protobuf`
 
Once protobuf is installed, run `./build.sh` to compile the .proto files.

