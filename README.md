# Python Datastuctures & Utilities

Reference Udemy course:
https://www.udemy.com/course/algorithms-and-data-structures-in-python

### Environment management

Python environment based on the currently installed python environment.

```
pip3 install --upgrade virtualenv
virtualenv -p python3 py-learn
source py-learn/bin/activate
pip install -r requirements.txt
```

### Run flake8 linter

Ensure static analysis per rules in root setup.cfg

- Navigate to folder with python files
- Run `flake8`

### To do

#### Hash tables
- add quadratic probing to hash tables
- add rehashing to hash tables
- implement dictionary of dictionary example

#### Trees
- implement avl tree methods (with rotations)
- implement rb tree methods (with recoloring and rotations)

#### Heaps
- implement heaps and associated methods