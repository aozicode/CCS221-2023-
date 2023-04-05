import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

def plot_basic_object(points):
    tri = Delaunay(points).convex_hull
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, lw=0.5, color='orange', shade=True)
    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)
    st.pyplot(fig)

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

def main():
    st.title("3D Cube")
    init_cube = cube(side_length=3)
    plot_basic_object(init_cube)

if __name__ == '__main__':
    main()

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

#rectangle
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

def plt_basic_object(points):
    
    tri=Delaunay(points).convex_hull
    
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, shade=True, lw=0.5, color='purple')
    
    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)
    st.pyplot(fig) # Use st.pyplot to display the figure

st.title("Rectangle")    

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

init_rectangle = rectangle(side_lengths=(2, 4, 2)) #here we can customize the rectangle
points = tf.constant(init_rectangle, dtype=tf.float32)

plt_basic_object(points)

#pyramid
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay
import tensorflow as tf
import streamlit as st

def pyramid(side=6, height=8, bottom_lower=(0, 0, -2)):
    side = side / np.sqrt(2)  
    height = height # calculates the tip
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower + [-side, -side, 0], 
        bottom_lower + [side, -side, 0],  
        bottom_lower + [side, side, 0],  
        bottom_lower + [-side, side, 0],  
        bottom_lower + [0, 0, height],     
    ])
    return points

def plt_basic_object(points):
    tri=Delaunay(points).convex_hull
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, lw=0.5, shade=True, color='yellow')
    ax.set_xlim3d(-6,6)
    ax.set_ylim3d(-6,6)
    ax.set_zlim3d(-6,6)
    return fig

st.title("Pyramid")

side = st.sidebar.slider("Side length", 1.0, 10.0, 6.0, 0.1)
height = st.sidebar.slider("Height", 1.0, 10.0, 8.0, 0.1)
bottom_x = st.sidebar.slider("Bottom x-coordinate", -5.0, 5.0, 0.0, 0.1)
bottom_y = st.sidebar.slider("Bottom y-coordinate", -5.0, 5.0, 0.0, 0.1)
bottom_z = st.sidebar.slider("Bottom z-coordinate", -5.0, 5.0, -2.0, 0.1)

points = pyramid(side=side, height=height, bottom_lower=(bottom_x, bottom_y, bottom_z))

fig = plt_basic_object(points)

st.write(fig)