# Pandora

This repository collects research notebooks exploring dynamic system modelling, parameter estimation, and simulation-based inference techniques. All examples are implemented in Python using Jupyter notebooks and rely on libraries such as NumPy, PyTorch and the `sbi` package.

## Notebooks

The `notebooks` directory is organised into several subfolders:

- **LSTM** – recurrent neural network models and training experiments.
- **online_parameter_estimation** – adaptive Kalman filters, observer design and related methods.
- **simulation_based_inference** – experiments using the `sbi` library for systems such as mass–spring–damper and multiphase flow.
- **genetic_algorithms** – basic optimisation experiments with genetic algorithms.
- **results** – images generated from the notebooks.

## Getting Started

1. Install Python 3.10 or later.
2. Install dependencies using the requirements file:
   ```
   pip install -r requirements.txt
   ```
3. Launch Jupyter and open any notebook from the `notebooks` directory.

The repository is intended as a sandbox for different modelling and inference strategies. Feel free to explore and adapt the notebooks for your own experiments.
