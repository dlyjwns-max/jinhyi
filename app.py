import pathlib
import streamlit as st
import streamlit.components.v1 as components

# Streamlit 기본 페이지 설정 (전체 화면 모드 및 브라우저 탭 타이틀)
st.set_page_config(
    page_title="Apex 3D 사격 & 궁술 시뮬레이터",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit 기본 패딩 및 여백을 완전히 제거하여 WebGL 캔버스를 100% 꽉 차게 렌더링
st.markdown(
    """
    <style>
        /* Streamlit 기본 상하좌우 패딩 및 여백 제거 */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        /* 상단 Streamlit 헤더 바 및 하단 푸터 숨기기 */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        footer {
            display: none !important;
        }
        /* Iframe을 뷰포트 전체 크기로 확장 및 스크롤바 제거 */
        iframe {
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }
        body {
            background-color: #05070a;
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 현재 app.py 파일이 위치한 경로를 기준으로 상대 경로 지정
BASE_DIR = pathlib.Path(__file__).parent
HTML_FILE_PATH = BASE_DIR / "htmls" / "index.html"

def render_app():
    """htmls/index.html 파일을 불러와 Streamlit components로 주입하는 함수"""
    if HTML_FILE_PATH.exists():
        try:
            with open(HTML_FILE_PATH, "r", encoding="utf-8") as f:
                html_content = f.read()
            
            # 읽어온 HTML 콘텐츠를 1000px 높이의 캔버스 Iframe으로 출력
            components.html(html_content, height=1000, scrolling=False)
        except Exception as e:
            st.error(f"⚠️ HTML 파일 로딩 중 오류가 발생했습니다: {e}")
    else:
        st.error(f"❌ `{HTML_FILE_PATH}` 경로에서 `index.html` 파일을 찾을 수 없습니다.")
        st.info(
            "GitHub 저장소의 파일/폴더 구조가 아래와 동일하게 구성되었는지 확인해 주세요:\n\n"
            "```text\n"
            "├── app.py\n"
            "├── requirements.txt\n"
            "└── htmls/\n"
            "    └── index.html\n"
            "```"
        )

if __name__ == "__main__":
    render_app()
