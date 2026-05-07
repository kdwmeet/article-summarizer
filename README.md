# Web Article Summarizer (URL 기반 아티클 핵심 3줄 요약 비서)

## 1. 프로젝트 개요

이 프로젝트는 길고 복잡한 뉴스 기사나 기술 블로그의 URL 링크만 제공하면, AI 에이전트가 직접 웹페이지에 접속하여 본문을 추출하고 가장 중요한 핵심 내용 3가지를 한국어로 요약해 주는 실용적인 정보 필터링 도구입니다.

외부 세계의 데이터(웹사이트)를 가져와(Retrieval) LLM의 언어 처리 능력(Generation)과 결합하는 RAG(검색 증강 생성)의 가장 기초적이고 직관적인 형태를 구현합니다.

## 2. 주요 기능

* URL 기반 본문 추출: 복잡한 크롤링 스크립트 작성 없이 LangChain의 WebBaseLoader를 활용하여 웹페이지의 HTML에서 순수 텍스트 본문만 빠르고 정확하게 추출합니다.
* 다국어 자동 번역 및 요약: 해외 영문 기사나 블로그의 URL을 입력하더라도, 모델이 이를 분석하여 명확하고 간결한 한국어 3줄 요약으로 반환합니다.
* 컨텍스트 길이 보호: 토큰 한도 초과(Context Window Overflow) 오류를 방지하기 위해 추출된 텍스트의 길이를 안전하게 제한(15,000자)하는 방어 로직이 적용되어 있습니다.

## 3. 기술 스택

* Language: Python 3.10+
* Package Manager: uv
* LLM: OpenAI gpt-5.4-nano (사실 기반의 요약을 위해 reasoning_effort="low" 파라미터 적용)
* Orchestration: LangChain (ChatPromptTemplate 및 WebBaseLoader)
* Web Scraping: BeautifulSoup4 (html 파싱)
* Web Framework: Streamlit (사용자 인터페이스)

## 4. 프로젝트 구조
```
article-summarizer/
├── .env                  
├── requirements.txt      
├── main.py               
└── app/
    ├── __init__.py
    └── chain.py          
```

## 6. 설치 및 실행 가이드

### 6.1 환경 변수 설정
프로젝트 루트 경로에 .env 파일을 생성하고 OpenAI API 키를 입력하십시오.
OPENAI_API_KEY=sk-your-api-key-here

### 6.2 의존성 설치 및 실행
uv venv
uv pip install -r requirements.txt
uv run streamlit run main.py

## 7. 활용 예시

* 입력: "https://example.com/very-long-tech-news-article" (특정 기술 발표에 관한 장문의 영문 기사)
* 출력:
  - 새로운 AI 모델은 이전 버전 대비 추론 속도가 30% 향상되었습니다.
  - 전력 소비를 줄이기 위한 새로운 아키텍처가 도입되어 모바일 기기에 적합합니다.
  - 해당 모델은 다음 달부터 오픈 소스로 전면 공개될 예정입니다.

## 8. 실행 화면

<img width="1539" height="602" alt="스크린샷 2026-04-30 095147" src="https://github.com/user-attachments/assets/aff33f00-56eb-4d99-8f6b-9ff293c8a524" />
