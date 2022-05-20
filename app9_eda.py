import streamlit as st
import pandas as pd

def run_eda() :
    st.subheader('EDA 화면')
    df = pd.read_csv('data2/iris.csv')
    # 컬럼이름을 보여주시고, 여러 컬럼들만 선택 가능토록 하여,
    # 선택한 컬럼들만 화면에 보여줍니다.
    column_list = df.columns
    choice_list = st.multiselect('컬럼을 선택하세요',column_list)
    if len(choice_list) != 0  :
        st.dataframe(df[choice_list])

    # 상관 계수를 구하여 화면에 보여줍니다.
        st.dataframe(df[choice_list].corr())