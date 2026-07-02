import streamlit as st
import numpy as np
from scipy import linalg
import plotly.graph_objects as go

# --- 1. PHYSICS ENGINE ---
def solve_schrodinger(width, depth, n_points=500):
    """Solves the 1D Schrödinger equation for a finite square well."""
    L = 20.0  # Size of the simulation domain
    x = np.linspace(-L/2, L/2, n_points)
    dx = x[1] - x[0]
    
    # Potential: -depth inside the well, 0 outside
    V = np.zeros_like(x)
    V[np.abs(x) < width/2] = -depth
    
    # Kinetic Energy Matrix (Finite Difference)
    # T = -1/(2*dx^2) * (psi_{i+1} - 2psi_i + psi_{i-1})
    main_diag = 2.0 / dx**2 * np.ones(n_points)
    off_diag = -1.0 / dx**2 * np.ones(n_points - 1)
    T = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
    
    # Hamiltonian = T + V
    H = T + np.diag(V)
    
    # Solve Eigenvalues/vectors
    eigenvalues, eigenvectors = linalg.eigh(H)
    
    return x, V, eigenvalues, eigenvectors

# --- 2. UI CONTROLLER ---
st.set_page_config(page_title="Quantum Wells Explorer", layout="wide")
st.title("⚛️ Quantum Wells Explorer")
st.markdown("Explore how potential wells influence particle energy levels.")

# Sidebar for inputs
with st.sidebar:
    st.header("Parameters")
    width = st.slider("Well Width", 1.0, 10.0, 5.0)
    depth = st.slider("Well Depth", 1.0, 50.0, 20.0)
    num_states = st.slider("Number of States to Plot", 1, 5, 3)

# --- 3. EXECUTION & VISUALIZATION ---
x, V, energies, psi = solve_schrodinger(width, depth)

fig = go.Figure()

# Plot the Potential Well
fig.add_trace(go.Scatter(x=x, y=V, name="Potential V(x)", line=dict(color='black', width=3)))

# Plot the Energy Levels and Wavefunctions
# We add an offset to the wavefunctions so they are visible above the energy level
for i in range(num_states):
    energy = energies[i]
    # Only show bound states (energy < 0)
    if energy < 0:
        # Scale wavefunction for visualization
        y_psi = psi[:, i] * 5 + energy 
        fig.add_trace(go.Scatter(x=x, y=y_psi, name=f"State {i+1} (E={energy:.2f})"))
        # Draw energy level line
        fig.add_hline(y=energy, line_dash="dash", line_color="gray", annotation_text=f"E{i+1}")

fig.update_layout(
    xaxis_title="Position (x)",
    yaxis_title="Energy / Psi",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# Add context
with st.expander("Physics Behind This"):
    st.write("""
    This app solves the Time-Independent Schrödinger Equation: 
    $$-\\frac{\\hbar^2}{2m} \\frac{d^2\\psi}{dx^2} + V(x)\\psi = E\\psi$$
    We use the **Finite Difference Method** to discretize the Hamiltonian into a matrix, 
    allowing us to use `scipy.linalg.eigh` to find the energy eigenvalues and wavefunctions.
    """)