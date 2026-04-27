# PyRoDeEn
Python Rotating Detonation Engines is a project that simplifies computational fluid dynamics, thermochemistry, and optimizations as a gateway for students and independent researchers to understand and simulate pressure gain combustion applications, namely rotating detonation engine configurations.
## Installation
Clone this repository via git and cd into its folder.
```
git clone https://github.com/gbonetgarcia/pyrodeen.git
cd pyrodeen
```
Optional: It is recommended to install this module in a conda environment to simplify dependency management.
```
conda create -n pyrodeen python=3.11
```
```
conda activate pyrodeen
```
Use pip to install project and its dependencies. Non-developers can skip the `-e` flag.
```
pip install -e .
```
## Usage
A simple command prints a NumPy matrix representative of a discretized physical space.
```
pyrodeen --test_grid
```
## Contribution
Feel free to read through the code so far. The `pyrodeen` command is defined in pyproject.toml and made accessible through the pip installation; it points at the cli module in src, which then calls other defined objects, most of them being templates.
```
pyproject.toml -> src/pyrodeen/cli.py -> src/pyrodeen/grid.py
```