# Quantum Wells Explorer

**An interactive computational tool for simulating 1D quantum confinement.**

The Quantum Wells Explorer is a web-based application designed to help physics students and researchers visualize the behavior of a quantum particle in a finite square potential well. By solving the Time-Independent Schrödinger Equation using the Finite Difference Method, this tool allows users to dynamically adjust the width and depth of a well to observe real-time changes in energy eigenvalues and wavefunctions.

## Live Demo
insert link here when deployed to GitHub

## Physics Context
In nanoscience, quantum confinement is a fundamental phenomenon. When the dimensions of a semiconductor structure are reduced to the scale of the exciton Bohr radius, the electronic properties change drastically. This tool provides a visual interface to explore these concepts, serving as a digital laboratory for analyzing how geometry dictates quantum energy states.

## Features
* **Interactive Controls:** Adjust well width and depth using sliders to see instantaneous updates.
* **Eigenstate Visualization:** View the first few energy levels and their corresponding probability wavefunctions ($\psi$).
* **Professional Backend:** Built with a finite difference Hamiltonian matrix solver using `SciPy.linalg.eigh`.
* **Responsive UI:** Interactive plotting with `Plotly` allows users to zoom, hover, and inspect data points.

## Tech Stack
* **Frontend/UI:** [Streamlit](https://streamlit.io/)
* **Numerical Engine:** [NumPy](https://numpy.org/) & [SciPy](https://scipy.org/)
* **Visualization:** [Plotly](https://plotly.com/)
* **Environment:** Python 3.9+

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/quantum-wells-explorer.git](https://github.com/YOUR_USERNAME/quantum-wells-explorer.git)
   cd quantum-wells-explorer

```

2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the application:**
```bash
streamlit run app.py

```



## The Physics Behind the Code

This simulation solves the 1D Time-Independent Schrödinger Equation:

$$-\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} + V(x)\psi = E\psi$$

### Numerical Method

We discretize the spatial coordinate $x$ into a grid of $N$ points. This allows us to convert the differential operator into a matrix form (Finite Difference Method). We then solve the resulting matrix eigenvalue problem ($H\psi = E\psi$) using `scipy.linalg.eigh` to extract the energy eigenvalues and the corresponding wavefunctions.

### Note on Units

This simulation operates in **natural units** (dimensionless) where $\hbar = 1$ and $m = 1$.

* **Energy Scaling:** Physical energies can be recovered by scaling the output by $E_0 = \frac{\hbar^2}{2mL_0^2}$, where $L_0$ is your characteristic length unit.
* **Stability:** This approach is used to prevent floating-point precision errors during matrix diagonalization.

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```

```
