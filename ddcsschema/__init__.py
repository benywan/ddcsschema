import os

__version__ = "0.0.15"

BLOCKCHAIN_NAME_ENVVAR = "DDCSSCHEMA_BLOCKCHAIN_NAME"
if BLOCKCHAIN_NAME_ENVVAR in os.environ:
    if os.environ[BLOCKCHAIN_NAME_ENVVAR] in ['ddcscrd_main', 'ddcscrd_regtest',
                                              'ddcscrd_testnet']:
        BLOCKCHAIN_NAME = os.environ[BLOCKCHAIN_NAME_ENVVAR]
    else:
        raise OSError("invalid blockchain name: %s" % os.environ[BLOCKCHAIN_NAME_ENVVAR])
else:
    BLOCKCHAIN_NAME = "ddcscrd_main"
