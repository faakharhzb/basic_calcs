# basic_calcs

`basic_calcs` is a python library for basic calculations. It has no dependencies, just the standard library. It can run on almost any OS or python version.

> [!WARNING]
> `basic_calcs` is still in alpha and has many missing features. 

## Installation 

Install using this command:
```sh
pip install basic_calcs
```

## Build from source

To build from source, first fork this repository and clone it. Then, install the developer dependencies:
```sh
pip install build setuptools
```
It is recommended to run this in a virtual environment. After this, run `python -m build` to build the wheels and tarball. Then, to install it, run `pip install .`

> [!NOTE]
> While developing, you might need to build it multiple times. For that, instead of `pip install .`, run `pip install -e .`. This installs 
> `basic_calcs` in editable mode, meaning that you don't have to install it every time and it will automatically update when you edit a file.

## Usage

Usage is very simple. Currently, there are only 4 functions. Their usage is as follows:
```py
from basic_calcs import add, subtract, multiply, divide

add(10, 5)
# 15

subtract(10, 5)
# 5

multiply(10, 5)
# 50

divide(10, 5)
# 2
```
Every function also has a `verbose` parameter which provides a more verbose answer. it defaults to `False`. Use it as follows:
```py
from basic_calcs import add

add(5, 5, True) # it works the same for the rest of the functions
# 5 + 5 = 10
```
