import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("")

two_d_arr = np.array([[1, 0, 1], 
                      [0, 1, 0],
                      [1, 0, 1]])

def flood_fill(x, y, ColorVal, directions):
    global two_d_arr

    if two_d_arr[x][y] == ColorVal:
        return

    old_color = two_d_arr[x][y]
    two_d_arr[x][y] = ColorVal

    # Flood fill in the specified directions
    if "up" in directions and x > 0 and two_d_arr[x-1][y] == old_color:
        flood_fill(x-1, y, ColorVal, directions) # up
    if "down" in directions and x < two_d_arr.shape[0]-1 and two_d_arr[x+1][y] == old_color:
        flood_fill(x+1, y, ColorVal, directions) # down
    if "left" in directions and y > 0 and two_d_arr[x][y-1] == old_color:
        flood_fill(x, y-1, ColorVal, directions) # left
    if "right" in directions and y < two_d_arr.shape[1]-1 and two_d_arr[x][y+1] == old_color:
        flood_fill(x, y+1, ColorVal, directions) # right

def boundary_fill(x, y, ColorVal):
    global two_d_arr

    if two_d_arr[x][y] == ColorVal:
        return

    old_color = two_d_arr[x][y]
    two_d_arr[x][y] = ColorVal

    if x > 0 and two_d_arr[x-1][y] != old_color:
        boundary_fill(x-1, y, ColorVal)
    if x < two_d_arr.shape[0]-1 and two_d_arr[x+1][y] != old_color:
        boundary_fill(x+1, y, ColorVal)
    if y > 0 and two_d_arr[x][y-1] != old_color:
        boundary_fill(x, y-1, ColorVal)
    if y < two_d_arr.shape[1]-1 and two_d_arr[x][y+1] != old_color:
        boundary_fill(x, y+1, ColorVal)

def change(x, y, ColorVal, Algorithm, directions):
    global two_d_arr

    if Algorithm == "Flood Fill":
        flood_fill(x, y, ColorVal, directions)
    elif Algorithm == "Boundary Fill":
        boundary_fill(x, y, ColorVal)
    else:
        st.write("Invalid algorithm. Try again.")
        return

    img = plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    img.set_clim([0, 50])
    plt.colorbar()
    st.pyplot()

def main():
    column = st.number_input("Column (0, 1, 2): ", min_value=0, max_value=2)
    row = st.number_input("Row (0, 1, 2): ", min_value=0, max_value=2)
    color = st.number_input("Color: ")
    algorithm = st.selectbox("Algorithm: ", ["Flood Fill", "Boundary Fill"])
    directions = st.multiselect("Directions: ", ["up", "down", "left", "right"])

    if st.button("Update"):
        change(column, row, color, algorithm, directions)


if __name__ == '__main__':
    main()