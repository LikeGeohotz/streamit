import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit')

st.write('Progress Bar')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

"Done"

left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに表示")

if button:
    right_column.write("これは右カラム")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2の回答")


text = st.text_input("Which color dou you like?")
"あなたの好きな色は: ", text

number = st.selectbox(
    "Which number do you like?",
    list(range(1, 11))
)
"あなたの好きな数字は ", number, " です"

condition = st.slider("あなたの今の調子は？", 0, 100, 70)
"Condition: ", condition


if st.checkbox('Show Image'):
    img = Image.open('test.jpg')
    st.image(img, caption='Burst', use_column_width=True)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [31.58, 130.54],
    columns=['lat', 'lon']
)
st.map(df)

st.dataframe(df.style.highlight_max())
