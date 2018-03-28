from setuptools import setup, find_packages
import os
from ddcsschema import __version__ as version

requires = [
    'protobuf==3.2.0',
    'jsonschema',
    'ecdsa',
]

base_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "ddcsschema")
setup(
    name="ddcsschema",
    description="Protobuf schema for claims on the DDCS blockchain",
    version=version,
    author="jackrobison@ddcs.io",
    install_requires=requires,
    packages=find_packages(exclude=['tests'])
)
