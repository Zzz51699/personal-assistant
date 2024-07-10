import streamlit as st
import re
import data.data as dd
import time
import base64
# 设置修改密码的标签页
st.set_page_config(
    page_title="私人助手修改密码页",
    page_icon="pages/狗.jpg"
)
# 设置页面的标题
st.title("私人助手修改密码页 👏")

# 设置修改密码页面的组件
username = st.text_input("请输入手机号")
password = st.text_input("请输入新密码",type="password")
repass = st.text_input("请再次输入新密码",type="password")
ChangePasswordFlag = st.button("修改密码")
# 登录按钮
loginFlag = st.button("已经修改？点击登录")

# 定义一个修改函数
def ChangePassword(username,newpassword,repass):
    # 1、校验三个信息是否填写
    if username and newpassword and repass:
        #2、校验用户名的长度是否为11位 并且是否为手机号 正则表达式
        if re.match('^(13|15|17|18|19)[0-9]{9}$', username):
            #3、查看两次密码是否一致 并且密码长度必须大于等于8位
            if newpassword == repass and len(password) >=8:

                if dd.query_user_by_username(username):
                    dd.update_data(newpassword,username)
                    st.success("修改成功")
                    time.sleep(2)
                    st.switch_page("login.py")
                else:
                    st.error("用户不存在，请注册！")
            else:
                st.error("两次密码不一致或者密码长度字段不足8位")
        else:
            st.error("手机号格式不正确")

    else:
        st.error("请务必填写相关修改信息")


if ChangePasswordFlag:
    ChangePassword(username, password, repass)


if loginFlag:
    # 如果要跳转到系统的首页，前面不能加pages
    st.switch_page("login.py")









