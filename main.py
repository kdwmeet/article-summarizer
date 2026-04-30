import streamlit as st
from app.chain import summarize_article

st.set_page_config(page_title="아티클 요약 비서", layout="wide")

st.title("URL 기반 아티클 핵심 3줄 요약 비서")
st.markdown("길고 복잡한 뉴스 기사나 기술 블로그의 URL 링크를 입력하면, 에이전트가 직접 해당 페이지를 읽고 가장 중요한 3가지 문장으로 요약해 줍니다.")
st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("아티클 링크 입력")
    with st.form("sumary_form"):
        url_input = st.text_input(
            "웹페이지 URL을 붙여넣으십시오.",
            placeholder="https://example.com/long-article-news"
        )
        submit_btn = st.form_submit_button("핵심 3줄 요약하기", use_container_width=True)

with col2:
    st.subheader("핵심 요약 결과")
    if submit_btn and url_input.strip():
        with st.spinner("웹페이지에 접속하여 본문을 추출하고 분석 중입니다."):
            result = summarize_article(url_input)

            st.success("아티클 분석 및 요약이 완료되었습니다.")
        with st.container(border=True):
            st.markdown(result)
    
    elif not submit_btn:
        st.write("좌측에 URL을 입력하고 버튼을 누르십시오.")