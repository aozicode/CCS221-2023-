import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

def plot_basic_object(points, color='orange'):
    tri = Delaunay(points).convex_hull
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, lw=0.5, color=color, shade=True)
    ax.set_xlim3d(-10,10)
    ax.set_ylim3d(-10,10)
    ax.set_zlim3d(-10,10)
    st.write(fig)

def cube(bottom_lower=(-2,-1,-2), side_length=5):
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
    ])
    return points

def octahedron(side=8, bottom_lower=(0, 0,-2)):
    side = side / np.sqrt(2)  
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower + [-side, 0, 0],  # bottom left
        bottom_lower + [0, -side, 0],  # bottom right
        bottom_lower + [side, 0, 0],   # top left
        bottom_lower + [0, side, 0],   # top right
        bottom_lower + [0, 0, side],   # front top
        bottom_lower + [0, 0, -side]   # back bottom
    ])
    return points

def rectangle(bottom_lower=(-2,-1,-2), side_lengths=(5, 3, 4)):
    bottom_lower=np.array(bottom_lower)
    side_lengths = np.array(side_lengths)
    points=np.vstack([
        bottom_lower,
        bottom_lower + [0, side_lengths[1], 0],
        bottom_lower + [side_lengths[0], side_lengths[1], 0],
        bottom_lower + [side_lengths[0], 0, 0],
        bottom_lower + [0, 0, side_lengths[2]],
        bottom_lower + [0, side_lengths[1], side_lengths[2]],
        bottom_lower + [side_lengths[0], side_lengths[1], side_lengths[2]],
        bottom_lower + [side_lengths[0], 0, side_lengths[2]],
        ])
    return points

def pyramid(side_length=5, height=6, bottom_center=(0,0,0)):
    bottom_center = np.array(bottom_center)
    half_side = side_length/2
    points = np.vstack([
        bottom_center + [-half_side, -half_side, 0],
        bottom_center + [half_side, -half_side, 0],
        bottom_center + [half_side, half_side, 0],
        bottom_center + [-half_side, half_side, 0],
        bottom_center + [0, 0, height]
])
    return points

def create_shape():
    st.sidebar.markdown("## Select a shape to display")
    cube_checked = st.sidebar.checkbox("Cube")
    octahedron_checked = st.sidebar.checkbox("Octahedron")
    rectangle_checked = st.sidebar.checkbox("Rectangle")
    pyramid_checked = st.sidebar.checkbox("Pyramid")

    if cube_checked:
        points = cube()
        plot_basic_object(points)
    if octahedron_checked:
        points = octahedron()
        plot_basic_object(points)
    if rectangle_checked:
        points = rectangle()
        plot_basic_object(points)
    if pyramid_checked:
        points = pyramid()
        plot_basic_object(points)
    
if __name__ == "__main__":
    st.title("3D Shapes")
    create_shape()