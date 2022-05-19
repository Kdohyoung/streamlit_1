# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st

# 웹 대시보드 개발 라이브러리인, 스트림릿은 , main 함수가 있어야한다.

def main() :
    st.title('안녕하세요 웹 대시보드 프로젝트') 
    st.title('Hello')



st.subheader('이 영역은 subheader 영역')
st.success('작업이 성공했을때 사용하자.')
st.warning('경고 문구를 보여주고 싶을때 사용하자')
st.info('정보를 보여주고 싶을때')
st.error('a문제가 발생했을때')
