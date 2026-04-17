# PyRoDeEn
Python Rotating Detonation Engines is a project that simplifies computational fluid dynamics, thermochemistry and optimizations as a gateway for studens and indedpendent researchers to understand and simulate pressure gain combustion applications, namely rotating detonation engine configurations.
---
### Installation and usage

Ideally from within a [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) environment and from the root folder of the project, the project can be installed as follows.
```
pip install -r .\requirements.txt
pip install -e .
```
Where -e can be skipped for non-developers.
So far this project only has a command to test numpy nparray instantiation with the following command.
```
pyrodeen test_grid
```