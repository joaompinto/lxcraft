# Debugging

Debug messages are by setting the `DEBUG` environment variable to a list of debug categories.

Examples
```sh
    DEBUG=all       # Debug all categories
    DEBUG=action    # Debug resource actions
    DEBUG=command   # Debug command execution
    DEBUG=category1,category2,...   # Debug multiple categories
```


## Debugging Tests

The following example will run the test_apt* tests with "all" debugging enabled.

```sh
DEBUG=all just test-only test_apt
```
