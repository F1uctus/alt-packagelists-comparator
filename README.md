# ALT Package lists comparator

basealt binary package lists comparator.
Built for the https://rdb.altlinux.org/api REST API.

### Installing the library

Dependencies:

- Python 3.6+
- (Testing) Pytest
- (Optional) Poetry

Full dependency list is specified in [pyproject.toml](/pyproject.toml)

Here and below, `.` points to the repository root directory.

Install with pip (requires pip >= 20.3.4 and setuptools >= 52):

```bash
$ pip install .
# Use "pip install -e ." for editable install
````

Install with Poetry:

```bash
$ poetry install
```

### Testing the library

With Pytest:

```shell
$ pytest ./tests
```

With Poetry:

```shell
$ poetry test
```

Test lists are cached by default (in [cached_lists](/tests/cached_lists)),
and limited to aarch64 only. To disable caching, change `USE_CACHED_LISTS`
in [conftest.py](/tests/conftest.py) to `False`.

### Usage

The Unix-compatible CLI is located in [bin/altpacom](/bin/altpacom).

Arguments:

```
-a, --arch      ARCHITECTURE  Filter all packages to specified architecture only.
-x, --exclusive PLATFORM      List packages found only in specified platform.
-n, --newest    PLATFORM      List packages with newest version found in specified platform.
-v, --verbosity LEVEL         Show logs of specified level only (and above).
-h, --help                    Show more descriptive CLI help.
```

Example of output for command
`altpacom -x sisyphus -x p10 -n sisyphus`:

```json
{
  "exclusives": {
    "sisyphus": {
      "aarch64": [
        {
          "name": "...",
          "version": "..."
        }
      ],
      "...": []
    },
    "p10": {
      "aarch64": [
        {
          "name": "...",
          "version": "..."
        }
      ],
      "...": []
    }
  },
  "newest": {
    "sisyphus": {
      "aarch64": [
        {
          "name": "...",
          "version": "..."
        }
      ],
      "...": []
    }
  }
}
```
