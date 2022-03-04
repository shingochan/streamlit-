import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit入門')

left, right = st.columns(2)
button = left.button('右からむに文字を表示')
if button:
    right.write('ここは右からむです')
expander = st.expander('問い合わせ')
expander.write('答え')


# text = st.text_nput(
#     'あなたが好きな言葉を教えてください',
 
# )
# 'あなたが好きな言葉', text

# cond = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディションは', cond

# if st.checkbox('show image'):    
#     img = Image.open('sample.jpg')
#     st.image(img,caption='ちさちゃん',use_column_width=True)
