# encoding: utf-8
from logging import log
from os import close
import streamlit as st
import pandas as pd
import numpy as np
from streamlit.type_util import _NUMPY_ARRAY_TYPE_STR
from pathlib import Path

#df = pd.DataFrame({"Title":[],"Description":[],"UserName":[],"Reward":[],})
#df.to_csv(r"D:\学习\5A\block-chain\data\problems.csv")

st.set_page_config(
    page_title="PiggyBank",
    layout="wide"

)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

sidebar = st.sidebar.radio(
    "Guide Page",
    ("Ask questions", "See the board")
)





if sidebar=="Ask questions":
    path_prob = Path(__file__).parents[0]/"data/problems.csv"
    df_problems = pd.read_csv(path_prob, index_col=0)

    with st.form("key"):
        a = st.text_input("Title","")
        b = st.text_input("Description","")
        c = st.text_input("UserName","")
        d = st.text_input("Reward","")
        submitted = st.form_submit_button('Confirm')

        if submitted:
            df_temp = pd.DataFrame({
                'Title': [a],
                'Description': [b],
                'UserName': [c],
                'Reward': [d]
            })
            df_problems = df_problems.append(df_temp, ignore_index=True)
            df_problems.to_csv(path_prob)

            name_ = "data/Answer_Problem"+str(df_problems.shape[0])+".csv"
            name_ = Path(__file__).parents[0]/name_
            df_ans = pd.DataFrame({"Username":[],"Answer":[]})
            df_ans.to_csv(name_)

            st.success("Submit successfully")

elif sidebar == "See the board":
    st.title('PiggyBankStackFlow')
    path_prob = Path(__file__).parents[0] / "data/problems.csv"
    df_problems = pd.read_csv(path_prob, index_col=0)
    for index,row in df_problems.iterrows():

        name = "Problem"+str(index+1)

        with st.expander("expander_"+name):
            st.title(row["Title"])
            st.write(row["Description"])

            st.write("")
            st.write("--------------------------------------------------------")
            st.write("")


            st.title("Answers:")
            answer_path = "data/Answer_"+name+".csv"
            answer_path = Path(__file__).parents[0] /answer_path
            df_ans = pd.read_csv(answer_path, index_col=0)
            for ind_,row_ in df_ans.iterrows():
                with st.form("ans"+str(index)+str(ind_)):
                    st.write(row_["Username"]+":")
                    st.write(row_["Answer"])
                    award = st.form_submit_button("Award!")
                    if award:
                        st.success("Award successfully!")



            st.write("")
            st.write("--------------------------------------------------------")
            st.write("")
            st.title("Your answer:")

            with st.form(name):
                a = st.text_input("Username","")
                b = st.text_input("Answer","")
                submit = st.form_submit_button('Validate text')

                if submit:
                    df_temp_ = pd.DataFrame({
                        'Username': [a],
                        'Answer': [b]
                    })
                    df_ans_ = pd.read_csv(answer_path, index_col=0)

                    df_ans_ = df_ans_.append(df_temp_, ignore_index=True)
                    df_ans_.to_csv(answer_path)
                    st.success("Submit successfully")

