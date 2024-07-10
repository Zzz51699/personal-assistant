import streamlit as st
import base64
st.title("闺蜜性格选择页面")
if "xingge" not in st.session_state:
    st.session_state.xingge = ""
bt = st.button("温柔知性")
if bt:
    st.session_state.xingge="温柔知性"
    st.switch_page("pages/aibot.py")
bt1 = st.button("霸道冷漠")
if bt1:
    st.session_state.xingge="霸道冷漠"
    st.switch_page("pages/aibot.py")
bt2 = st.button("活泼可爱")
if bt2:
    st.session_state.xingge="活泼可爱"
    st.switch_page("pages/aibot.py")

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