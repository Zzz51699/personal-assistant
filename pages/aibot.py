# 女朋友
# 1、ai得知道他是你的朋友 langchain中提示词模块来限定
#    朋友的性格和类型由用户选择
# 2、ai还能能记住用户和它聊天的记录
#    langchain的memory记忆模块来实现
# 3、需要使用langchain的chain链，链把提示词+模型+记忆连接起来
# 构建我们的提示词，通过提示词来给大模型定义规则
import base64
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory # 在内存中保存历史记忆的模块
from langchain.chains import ConversationChain


st.title('我的电子闺蜜❤️❤️💕💕')
st.subheader("找电子闺蜜，享赛博人生")
if "gms" not in st.session_state:
    st.session_state.gms =[]

for gm in st.session_state.gms:
    with st.chat_message(gm["role"]):
        st.write(gm["context"])


# 构建的大模型
llm = ChatOpenAI(
    model="glm-4-0520",
    api_key="4acbcfdec78dd13d0c037ecbb34560af.ZD9q6NLklwT0A1Bp",
    temperature=0.99,
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)
# 构建记忆模块
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
# 通过链把三个模块给连接起来
# ConversationChain链之所以能所以历史记忆存储，主要是因为会做一件事情，会把memory记忆模块中的数据以history参数名的形式
# 封装到链的PromptTemplate提示词模板当中
temp = "现在你要扮演一个闺蜜的角色，你的性格是"+st.session_state.xingge+"，你只需要回答你用户的话即可，不需要重复用户的话，也不需要将你的角色和性格进行展示。你的用户说的话是:{input},你们的以前的对话是{history}"
prompt = PromptTemplate(
    input_variables=["input","history"],
    template=temp
)
chain = ConversationChain(
    prompt=prompt,
    llm=llm,
    memory=st.session_state.memory
)

input = st.chat_input("和你的闺蜜说点话吧")
if input:
    with st.chat_message("user"):
        st.write(input)
    st.session_state.gms.append({"role":"user","context":input})
    # 调用大模型回答我们的问题
    result = chain.invoke(input)
    # 带有记忆的链result中没有content,
    with st.chat_message("assistant"):
        st.write(result["response"])
    st.session_state.gms.append({"role":"assistant","context":result["response"]})

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
main_bg('4.jpg')
