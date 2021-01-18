# PyTasky
A package to connect to TsWw Api.

## Installation
You can install the Package using [PyPi](https://pypi.org/project/PyTasky/).
Run `py -m pip install PyTasky`.

## Usage
Simple example to get top groups.

```py
from PyTasky import TaskSystem

client = TaskSystem('API_TOKEN') 

tops = client.topGroups()

for x in tops:
    print(x.name)
```

Replace `API_TOKEN` with you own token.

Read More at [Task System WebStie](https://taskyonline.com/docs.html).
