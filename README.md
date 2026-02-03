# Light-GG

DOI: 10.5281/zenodo.18467222 (all versions)

[![DOI](https://zenodo.org/badge/1115256387.svg)](https://doi.org/10.5281/zenodo.18467222)

Author: Maria Babakhanyan Stone

This project is exploratory and intentionally minimal.

**Light-GG** is a lightweight, unit-agnostic Python utility for constructing
2D coordinate grids using only 1D axes and NumPy broadcasting.

The goal is to define large, regular grids using **human-intuitive inputs**
(reference point, extent, resolution) while avoiding the memory cost of
explicit 2D meshgrids.

Light-GG is intentionally minimal and domain-neutral.

**Name** The "GG" in the Light-GG grid generator stands for the word "griglia" from Italian, which means a 'grid'.

---


## Core idea

A 2D grid is defined mathematically as:

* x = x0 + i · dx

* y = y0 + j · dy

```yml
where:
- `(x0, y0)` is a reference point (origin),
- `dx` and `dy` are grid spacings,
- `i` and `j` are grid indices.
```


Light-GG stores only the **1D axes** and relies on NumPy broadcasting to
perform 2D computations efficiently.

---

## Features

- Unit-agnostic (degrees, meters, pixels, etc.)
- Memory-efficient grid construction
- Simple, explicit API
- Suitable for prototyping in astronomy, geospatial analysis,
  radar, agriculture, and general image processing

---

## Installation (development)

From the repository root:

```bash
python -m pip install -e .
```

## Basic usage

```python
from lightgg import make_axes_from_reference

vector_x, vector_y = make_axes_from_reference(
    x_reference=0.0,
    y_reference=0.0,
    span_x=600.0,
    span_y=400.0,
    step=10.0,
)

# Broadcasted coordinate views
X = vector_x[None, :]
Y = vector_y[:, None]

```

## Tutorials
The tutorials/ directory contains Jupyter notebooks that demonstrate
practical usage:

* 01_toy_field.ipynb — basic grid construction and visualization

* 02_fake_flight_lines.ipynb — simulated flight lines and swath coverage

These notebooks are intended as educational examples rather than
domain-specific implementations.

## Scope
Light-GG focuses only on grid construction.

Coordinate reference systems (CRS), projections, file formats, and
domain-specific logic are intentionally out of scope and can be layered
on top if needed.

## License
MIT License
