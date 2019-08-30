# Major Tom API Packages
Python Package for interacting with Major Tom's APIs

major_tom_api folder has the actual package.
Check the README inside it for more info on the package itself.

`$ python3 test.py` checks that it's been imported into the environment properly.

# Building Packages

Run the following in each package directory:

```
python3 setup.py sdist bdist_wheel

python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

[Reference](https://packaging.python.org/tutorials/packaging-projects/)
