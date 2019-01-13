# pytest-plugins

## pytest-html:

Under **fixture** directory, run:

```
pytest -v --html=report.html
```

You will see it generates report.html in the root running directory.



## pytest-regression:

This plugin makes it simple to test general data, images, files, and numeric tables by saving *expected* data in a *data directory* (courtesy of [pytest-datadir](https://github.com/gabrielcnr/pytest-datadir)) that can be used to verify that future runs produce the same data.

Under **plugins** directory, run:

```
pytest test_regression.py
```

The first time your run this test, it will *fail* with a message like this:

```
>           pytest.fail(msg)
E           Failed: File not found in data directory, created:
E           - C:\Users\bruno\pytest-regressions\tests\test_grids\test_grids2.yml
```

The fixture will generate a `test_grids.yml` file (same name as the test) in the *data directory* with the contents of data, which should be committed to  version control as baseline.

Run it again, it will pass now! 



## pytest-xdist:

Under **plugins** directory, run:

```
pytest  -v --tb=no -n auto
```



## pytest-bdd:

Under **plugins** directory, run:

```
pytest -v
```

