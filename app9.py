import streamlit as st
from app9_home import run_home
from app9_eda import run_eda
from app9_ml import run_ml
from app9_About import run_about
def main():
    st.title('파일 분리 앱')
    menu = ['Home','EDA','ML','About']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()
    elif choice == menu[3] :
        run_about()














if __name__ == '__main__':
    main()