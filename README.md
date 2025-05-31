# basic_calcs 0.0.3 dev

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

Usage is very simple. Currently, there are only a few functions. Their usage is as follows:
```py
from basic_calcs import add, subtract, multiply, divide, floor, power, root, area_quad, area_triangle

add([10, 5])
# 15. add all the numbers you want to add in the list

subtract([10, 5])
# 5. add all the numbers you want to subtract in the list

multiply([10, 5])
# 50. add all the numbers you want to multiply in the list

divide(10, 5)
# 2

floor(10, 4)
# usually this would be 2.5 but in floor its rounded to 3

power(10, 2)
# 100

root(9, 2)
# 3

area_triangle(10, 2)
# 10

area_quad(10, 2)
# 20
```
Every function also has a `verbose` parameter which provides a more verbose answer. it defaults to `False`. Use it as follows:
```py
from basic_calcs import add

add(5, 5, True) # it works the same for the rest of the functions
# 5 + 5 = 10
```
