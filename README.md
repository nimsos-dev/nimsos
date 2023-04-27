# nimsos

NIMS-OS (NIMS Orchestration System) is a Python library to realize a closed loop of robotic experiments and artificial intelligence without human intervention for automated materials exploration. NIMS-OS can perform automated materials exploration in various combinations by considering artificial intelligence and robotic experiments as modules (see the figure below). As artificial intelligence technique for materials science, Bayesian optimization method (PHYSBO), boundLess objective-free exploration method (BLOX), phase diagram construction method (PDC), and random exploration (RE) can be used. NIMS Automated Robotic Electrochemical Experiments (NAREE) system is available as robotic experiments. Visualization tools for the results are also included, allowing users to check optimization results in real time. Newly created modules for artificial intelligence and robotic experiments can be added and used. More modules will be added in the future.

<img src="https://user-images.githubusercontent.com/125417779/234746422-245339fa-9902-41b6-8d0c-13c748ad839b.png" width="600px">


# Document

- [English](https://nimsos-dev.github.io/nimsos/docs/en/index.html)
- [日本語](https://nimsos-dev.github.io/nimsos/docs/jp/index.html)

# Required Packages

- Python >= 3.6
- Cython
- matplotlib
- numpy
- physbo
- scikit-learn
- scipy

# Install

* From PyPI (recommended)

  ```bash
  pip install nimsos
  ```

* From source

  1. Download or clone the github repository

  ```
  git clone https://github.com/nimsos-dev/nimsos
  ```

  2. Install via pip in the nimsos-main folder

  ```bash
  pip install .
  ```

# Uninstall

```bash
pip uninstall nimsos
```

# License

The program package and the complete source code of this software are distributed under the MIT License.
