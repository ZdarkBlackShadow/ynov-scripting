# CHapitre 6

## Consigne

Créer une mini application avec `argparse`

## Prérequis

```bash
pip install argparse
```

## Script

```python
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-f','--foo', help='Description for foo argument', required=True)
parser.add_argument('-b','--bar', help='Description for bar argument', required=True)
parser.add_argument('-c', '--coo', help='Description for coo argument', required=True)
args = vars(parser.parse_args())

print(args["bar"])
```