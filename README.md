# Check IP

Simple wrapper around AWS check ip https://checkip.amazonaws.com

## Installation

```bash
🌈  ~ $ pip install checkip-0.1.0-py3-none-any.whl 
Defaulting to user installation because normal site-packages is not writeable
Processing ./checkip-0.1.0-py3-none-any.whl
Collecting click<9.0.0,>=8.0.1
  Using cached click-8.0.1-py3-none-any.whl (97 kB)
Collecting requests<3.0.0,>=2.26.0
  Using cached requests-2.26.0-py2.py3-none-any.whl (62 kB)
Collecting charset-normalizer~=2.0.0
  Using cached charset_normalizer-2.0.6-py3-none-any.whl (37 kB)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests<3.0.0,>=2.26.0->checkip==0.1.0) (2.10)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/lib/python3/dist-packages (from requests<3.0.0,>=2.26.0->checkip==0.1.0) (1.26.2)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests<3.0.0,>=2.26.0->checkip==0.1.0) (2020.6.20)
Installing collected packages: charset-normalizer, requests, click, checkip
Successfully installed charset-normalizer-2.0.6 checkip-0.1.0 click-8.0.1 requests-2.26.0
```

## Usage
```bash
🌈  ~ $ checkip
64.233.191.119
```

## Build

```bash
poetry build
```

## Run

```bash
poetry run checkip
```

## Test

```bash
pytest
```

## Develop

Before you begin, ensure you have a virual environment created

```bash
poetry shell
```
