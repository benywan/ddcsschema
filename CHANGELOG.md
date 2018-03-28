# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/).
This project was forked from Electrum v2.7.1 thus the first release is
labeled as 2.7.1. Subsequent releases will follow
[Semantic Versioning](http://semver.org/).

## [Unreleased]
### Security
  *
  *

### Fixed
  *
  *

### Deprecated
  *
  *

### Changed
  *
  *

### Added
  *
  *

### Removed
  *
  *


## [0.0.15] - 2018-03-20
### Changed
 * Added address prefixes for regtest and testnet blockchains


## [0.0.14] - 2017-11-08
### Added
 * Added `ClaimDict.validate_private_key` helper method to check a private key is for a certificate claim


## [0.0.13] - 2017-10-25
### Changed
 * Bumped jsonschema requirement to 2.6.0


## [0.0.12] - 2017-10-12
### Fixed
 * Verify that a Certificate keyType matches that in the der encoded public key


## [0.0.11] - 2017-09-18
### Fixed
 * Validate the prefix and checksum for lbrycrd addresses


## [0.0.10] - 2017-08-22
### Fixed
 * Fix uncaught decode error migrating 0.0.3 claims with a non-dictionary fee.

### Changed
 * Changed minimum length for channel name from 4 to 1


## [0.0.9] - 2017-07-24
### Fixed
 * Fix https://github.com/lbryio/lbryschema/issues/8

### Added
 * Add support for ISO-639-alpha2 language prefixes in claim metadata


## [0.0.8] - 2017-07-11
### Added
 * Added changelog


