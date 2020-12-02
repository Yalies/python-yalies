# yalies [![PyPI version](https://badge.fury.io/py/yalies.svg)](https://badge.fury.io/py/yalies)

> Python library for interfacing with the Yalies API.

[API documentation](https://yalies.io/apidocs)

## Setup
First, install the module:

```sh
pip3 install yalies
```

Then, to use the module, you must import it in your code:

```py
import yalies
```

Then initialize the API, using a token that you may obtain from the [API documentation page](https://yalies.io/apidocs):

```py
api = yalies.API('your token')
# Never hardcode tokens. Use a config file or environment variable instead.
# The name 'api' can be whatever is most appropriate for your program.
```

## Retrieval Functions
There is only one public-facing function in the `API` class:

`API.students([query, filters, page])` allows your program to request a list of students matching certain parameters. You may pass the `query` parameter, a string, specifying a textual query to search by. Alternatively, or in addition, you may pass `filters` a dictionary specifying lists of acceptable properties of the students you wish to retrieve data on. See `example.py` for a complete usage example, and the [API documentation](https://yalies.io/apidocs) for more information about request format.

## Author
[Erik Boesen](https://github.com/ErikBoesen)

## License
[MIT](LICENSE)
