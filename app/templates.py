def getPromptTemplate(category, articles):
    return f"""역할: 뉴스 요약 도우미.
    아래 기사 목록에서 **{category}**와 가장 관련성 높고 파급력 큰 뉴스 5건을 추려주세요.
    출력 형식:
    {{l: 뉴스링크, h: 제목(20자 내외), s: 본질적 파급효과 요약(1문장)}}
    조건:
    - 뉴스는 최신성·파급력·카테고리 적합성 기준으로 선정
    - 출력은 위 JSON 구조 그대로
    - 다른 출력은 필요 없이 JSON만
    - 내용 변경 없이 토큰 최소화
    - 내용이 영어라면 한글로 해석해서 요약
    입력:
    {articles}"""

def getIssueTemplate(issueData):
    return f"""
    <div class="news-block">
      <b>
        <a href="{issueData["l"]}" style="color:#000000; text-decoration:none;">{issueData["h"]}</a>
      </b><br>
      <span style="color:#666666;">⚡️{issueData["s"]}</span><br>
    </div>
    """

def getHtmlTemplate():
    return f"""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>뉴스 요약</title>
  <style>
    body {{
      font-family: 'Segoe UI', sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
      background-color: #f9f9f9;
      color: #000000;
      max-width: 800px;
      margin: auto;
    }}

    h2 {{
      text-align: center;
    }}

    p.center-desc {{
      text-align: center;
      color: #666666;
    }}

    .news-block {{
      background-color: #ffffff;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
      margin-bottom: 20px;
    }}

    .news-block b a {{
      font-size: 1.05em;
      color: #000000;
      text-decoration: none;
    }}

    .news-block span {{
      color: #666666;
    }}

    h3 {{
      margin-top: 40px;
    }}

    hr {{
      margin: 40px 0;
      border: none;
      border-top: 1px solid #ccc;
    }}

    .footer-note {{
      text-align: center;
      color: #888888;
      font-size: 0.9em;
    }}

    @media screen and (max-width: 600px) {{
      body {{
        padding: 15px;
      }}

      .news-block {{
        padding: 12px;
      }}

      .news-block b a {{
        font-size: 1em;
      }}

      .footer-note {{
        font-size: 0.85em;
      }}
    }}
  </style>
</head>
<body>

  <h2>📰 최근 뉴스 요약</h2>
  <p class="center-desc">카테고리별로 주요 뉴스를 선별했습니다.</p>

  <hr>
"""

def appendHtmlTail(html):
  return html + """
  <p class="footer-note">이 요약은 최근 뉴스 데이터를 기반으로 자동 생성되었습니다.</p>
</body>
</html>
"""