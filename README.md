# Pig-Py

Pig-py is a python console application that creates icon and splash images for android and ios platforms

## Instalation
```
pip install pig-py
```

## Usage
```
pig [platform] [options]
```

> For more experience use 1024x1024 images for icons and 2732x2732 for splash

#### Platform types
* ionic
* android `to do`
* ios `to do`

#### Options
See options too using `pig --help`

| Command | Required | Description |
| ------- | -------- | ----------- |
| `-f` `--file` | true | file name |
| `-o` `--output` | false | destination folder of images |

#### Example
```
pig ionic -n file.png
```