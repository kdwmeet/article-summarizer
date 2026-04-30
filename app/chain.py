from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

def summarize_article(url: str) -> str:
    """URL에서 웹페이지 본문을 추출하고 3줄로 요약"""
    
    # 웹 페이지 내용 로드 (Retrieval)
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()

        if not docs:
            return "해당 URL에서 텍스트를 추출할 수 없습니다. 보안 설정이 되어 있거나 잘못된 링크 일 수 있습니다."
        
        article_content = docs[0].page_content
    except Exception as e:
        return f"웹 페이지를 불러오는 중 오류가 발생했습니다: {str(e)}"
    
    # 토큰 한도 초과 방지를 위해 본문 텍스트 길이를 안전하게 자름
    if len(article_content) > 15000:
        article_content = article_content[:15000]
    
    # 요약 생성
    # 단순 요약이므로 reasoning_effort를 낮게 설정하여 응답 속도를 높임.
    llm = ChatOpenAI(model="gpt-5.4-nano", reasoning_effort="low")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 전문 요약가입니다. 제공된 아티클 본문을 분석하여 가장 핵심이 되는 내용을 정확히 3줄의 글머리 기호(Bullet points)로 요약하십시오. 각 줄은 명확하고 간결한 한국어로 작성해야 합니다."),
        ("user", "아티클 본문:\n{article_content}")
    ])

    # f-string 배제 및 딕셔너리 주입 원칙 준수
    chain = prompt | llm
    response = chain.invoke({"article_content": article_content})

    return response.content