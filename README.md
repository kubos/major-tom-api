# Major Tom API Packages
Python Package for interacting with Major Tom's APIs

major_tom_api folder has the actual package.
Check the README inside it for more info on the package itself.

`$ python3 test.py` checks that it's been imported into the environment properly.

# Building Packages

1. Make sure you have the appropriate tools installed (setuptools and wheel):

```
python3 -m pip install --user --upgrade setuptools wheel
```

2. Run the following in each package directory to upload to the test PyPi:

```
python3 setup.py sdist bdist_wheel

python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

3. Verify they uploaded correctly by installing from the test PyPi and verifying version number:

```
pip3 install -i https://test.pypi.org/simple/ major-tom-gateway-api
```
or
```
pip3 install -i https://test.pypi.org/simple/ major-tom-script-api
```

4. Now that it's testedFor the official release, upload to the official PyPi:

```
python3 -m twine upload dist/*
```

[Reference](https://packaging.python.org/tutorials/packaging-projects/)
