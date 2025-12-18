# Chapitre 7

## Consigne

Utiliser sgnal pour intercepter le `CRTL-C`

## Script

```python
import signal
import sys
import time

def handler(signum, frame):
    print('\nSignal received, exiting gracefully...')
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

print('Press Ctrl+C to trigger signal')

while True:
    time.sleep(1)
```