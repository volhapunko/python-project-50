# GENDIFF
Compares two configuration files (json, yaml) and shows differences in three chosen formats: tylish, plain or json.

### Hexlet tests and linter status: 
[![Actions Status](https://github.com/volhapunko/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/volhapunko/python-project-50/actions)
### Github Actions badge:
[![Python CI](https://github.com/volhapunko/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/volhapunko/python-project-50/actions/workflows/pyci.yml)
### SonarQube badges:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=volhapunko_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=volhapunko_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=volhapunko_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=volhapunko_python-project-50)

## Installation:
git clone https://github.com/volhapunko/python-project-50.git  
cd python-project-50  
make install

## Usage:
#### Stylish format (default)
gendiff file3.json file4.json  
gendiff file3.yml file4.yml
#### Plain format
gendiff -f plain file3.json file4.json  
gendiff -f plain file3.yml file4.yml
#### Json format
gendiff -f json file3.json file4.json  
gendiff -f json file3.yml file4.yml

## Asciinema:
### For plain files (json, yaml)
[![asciicast](https://asciinema.org/a/8L1WYzpo3nIhNNAi.svg)](https://asciinema.org/a/8L1WYzpo3nIhNNAi)
### For nested structures (json, yaml)
#### Stylish
[![asciicast](https://asciinema.org/a/MoRM8VAkhI3ZR9jz.svg)](https://asciinema.org/a/MoRM8VAkhI3ZR9jz)
#### Plain
[![asciicast](https://asciinema.org/a/BVfGRHpd8GciItHI.svg)](https://asciinema.org/a/BVfGRHpd8GciItHI)
#### Json
[![asciicast](https://asciinema.org/a/TLN45QZODOROb5rj.svg)](https://asciinema.org/a/TLN45QZODOROb5rj)

## Testing:
make lint  
make test