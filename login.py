import streamlit as st
import re
import time
import data.data as dd
import base64

st.set_page_config(
    page_title="登录页面",
    page_icon="🙂"
)
st.title('登录你的账号')
username = st.text_input("请输入你的用户名")
password = st.text_input("请输入你的密码",type="password")
loginFlag = st.button("登录")
ChangePasswordFlag = st.button("修改密码")

def login(username,password):
    if username and password:
        if re.match('^(13|15|17|18|19)[0-9]{9}$', username):
            if len(password) >= 8:
                res = dd.select_user(username)
                if res:
                    if res["password"] == password:
                        st.session_state.user_id = res["user_id"]
                        st.session_state.username = res["username"]
                        st.switch_page("pages/chatbot.py")
                    else:
                        st.error("密码不正确，请重新输入")
                else:
                    st.error("用户名不存在，请先注册")
            else:
                st.error("密码长度不足8位")
        else:
            st.error("手机号格式不正确")
    else:
        st.error("请填写相关信息")


registerFlag = st.button("没有账号，点此注册")
if loginFlag:
    login(username,password)
if registerFlag:
    st.switch_page("pages/register.py")
if ChangePasswordFlag:
    st.switch_page("pages/password.py")

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