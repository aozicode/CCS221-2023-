import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

plt.title("Flood Fill")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

two_d_arr = np.array([[1, 0, 1], 
                      [0, 1, 0],
                      [1, 0, 1]])

def change(x, y, ColorVal, MoveDirection):
    global two_d_arr

    if MoveDirection not in ["u", "d", "l", "r"]:
        st.write("Invalid MoveDirection. Try again.")
        return

    if MoveDirection == "u" and x > 0:
        two_d_arr[x][y] = ColorVal
        change(x - 1, y, ColorVal, MoveDirection)
    elif MoveDirection == "d" and x < two_d_arr.shape[0] - 1:
        two_d_arr[x][y] = ColorVal
        change(x + 1, y, ColorVal, MoveDirection)
    elif MoveDirection == "r" and y < two_d_arr.shape[1] - 1:
        two_d_arr[x][y] = ColorVal
        change(x, y + 1, ColorVal, MoveDirection)
    elif MoveDirection == "l" and y > 0:
        two_d_arr[x][y] = ColorVal
        change(x, y - 1, ColorVal, MoveDirection)

    img = plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    img.set_clim([0, 50])
    plt.colorbar()
    st.pyplot(plt.gcf())

def main():
    column = st.number_input("Column (0, 1, 2): ", value=0, min_value=0, max_value=2)
    row = st.number_input("Row (0, 1, 2): ", value=0, min_value=0, max_value=2)
    color = st.number_input("Color: ", value=0)
    direction = st.selectbox("Direction", ["u", "d", "l", "r"])
    
    change(column, row, color, direction)

if __name__ == '__main__':
    main()