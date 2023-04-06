import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf


def plt_basic_object_(points):
    tri=Delaunay(points).convex_hull
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, shade=True, lw=0.5, color='orange')
    ax.set_xlim3d(-6,6)
    ax.set_ylim3d(-6,6)
    ax.set_zlim3d(-6,6)
    st.pyplot(fig)


def octahedron_(side=8, bottom_lower=(0, 0,-2)):
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


init_octahedron = octahedron_(side=8)

st.title("Octahedron")

points = tf.constant(init_octahedron, dtype=tf.float32)

plt_basic_object_(init_octahedron)