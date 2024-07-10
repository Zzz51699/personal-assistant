import streamlit as st
import base64
st.title('山泉AI产品网')

col,col1,col2 = st.columns(3)
with col:
    st.image("http://gips1.baidu.com/it/u=3679066767,3429623176&fm=3042&app=3042&f=JPEG&wm=1,huayi,0,0,13,9&wmo=0,0")
    bt = st.button("小白助手")
    if bt:
        st.switch_page("pages/xiaobaibot.py")
with col1:
    st.image("历史.jpg")
    bt1 = st.button("历史知识助手")
    if bt1:
        st.switch_page("pages/dfswbot.py")
with col2:
    st.image("闺蜜.jpg")
    bt2 = st.button("赛博闺蜜")
    if bt2:
        st.switch_page("pages/friend.py")

def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
# 调用
main_bg('3.jpg')