import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="major-tom-script-api",
    version="0.0.1",
    author="Jesse Coffey",
    author_email="jcoffey@kubos.com",
    description="A package for interacting with Major Tom's Script API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kubos/major-tom-api-packages",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    python_requires='>=3.7',
)
