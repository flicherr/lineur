# lineur - linear neuron (C++)

A lightweight C++ project implementing standalone single-layer neural models for:

- **Binary classification**
- **Nonlinear regression**

The project includes dataset generation, training visualization, and an interactive UI built with ImGui.

---

## Overview

This project focuses on implementing neural models from scratch without external ML frameworks.  
It is designed to clearly demonstrate the behavioral differences between classification and regression while providing real-time visualization of training dynamics.

Two independent neuron implementations are provided:

- `ClNeuron` – binary classification  
- `RegNeuron` – regression  

Each model has its own data structures and training logic.

---

## Features

### Classification
- Linear binary classifier
- Two bias strategies:
  - Explicit bias term (`w0`)
  - Threshold-based decision
- Custom dataset loading
- Interactive visualization of decision boundary

### Regression
- Single-layer regression neuron
- Nonlinear target functions (e.g., parabola-based datasets)
- Optional noise injection in dataset generation
- Real-time prediction curve rendering

### UI
- Built with ImGui
- Toolbar with:
  - Model selector (combo box)
  - Training controls
  - Dataset loading
- Interactive canvas:
  - Zoom
  - Mouse panning
  - Data point rendering
  - Model output rendering

---

## Build

### Requirements

- C++20 or newer
- CMake
- ImGui
- X11 (Linux)

### Build Steps

```bash
mkdir build
cmake -S . -B build
cmake --build build
```

---

## Dataset Format

### Classification
```
x y label
```
Example:
```
 0.5 1.2 1
-0.3 0.8 0
```

### Regression
```
x y
```
Example:
```
-2.0 4.1
 0.5 0.3
```
