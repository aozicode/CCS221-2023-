import numpy as np
import cv2
import streamlit as st

def read_image(file):
    try:
        img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        if img is None:
            st.error("Error: Image file not found or could not be read.")
            return None
        else:
            return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def translate_image(img, tx_new, ty_new):
    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, tx_new], [0, 1, ty_new]])
    translated_img = cv2.warpAffine(img, M, (cols, rows))
    return translated_img

def main():
    st.title("Image Translation")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        img = read_image(uploaded_file)
        if img is not None:
            st.image(img, caption="Original Image")

            # Prompt user for original x and y coordinates
            orig_x = st.text_input("Enter original x coordinate: ")
            orig_y = st.text_input("Enter original y coordinate: ")
            tx, ty = int(orig_x), int(orig_y)

            while True:
                # Show the translated image
                transformed_img = translate_image(img, tx, ty)
                st.image(transformed_img, caption=f"Translated Image")

                tx_new = st.text_input("Enter new x coordinate or press 1 to exit: ")
                if tx_new == "1":
                    st.write("Thank you!")
                    break

                ty_new = st.text_input("Enter new y coordinate: ")
                tx += int(tx_new)
                ty += int(ty_new)

if __name__ == '__main__':
    main()