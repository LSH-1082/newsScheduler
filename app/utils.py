import requests
import openai
import json
from openai import OpenAI
from config import *
from templates import *
from datetime import date, timedelta


def processCategoryGroup(category_dict, html, fetch_func):
    for emoji, query in category_dict.items():
        raw_news = fetch_func(query)
        if not raw_news:
            continue
        summarized = summarizeWithGPT(query, str(raw_news))
        html += f"<h3>{emoji}</h3>"
        for issue in summarized:
            html += getIssueTemplate(issue)
        html += "<hr>"
    return html

def getNewsFromNaver(query):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {"query": query, "sort": "sim", "display": 20}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        items = resp.json()['items']
        return [{
            "t": item["title"], "l": item["link"],
            "d": item["description"], "p": item["pubDate"]
        } for item in items]
    else:
        print(f"네이버 뉴스 요청 실패: {resp.status_code}")
        return []
    
def getNewsFromWorld(query):
    url = 'https://newsapi.org/v2/everything'
    params = {"q" : query, "from" : date.today() - timedelta(days=2), "sortBy" : "popularity", "apiKey" : NEWS_API_KEY}
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        items = resp.json()['articles']
        return [{
            "t": item["title"], "l": item["url"],
            "d": item["description"], "p": item["publishedAt"]
        } for item in items]
    else:
        print(f"월드 뉴스 요청 실패: {resp.status_code}")
        return []

def summarizeWithGPT(category, articles):
    client = OpenAI(api_key=OPENAI_API_KEY)
    prompt = getPromptTemplate(category, articles)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.3
    )
    data = response.choices[0].message.content.replace("`", "").replace("json", "")
    try:
        return json.loads(data)
    except Exception as e:
        print("GPT 응답 파싱 실패:", e)
        return []

def sendMail(html):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart('alternative')
    msg['Subject'] = '뉴스 요약 보고서'
    msg['From'] = SMTP_EMAIL
    msg['To'] = RECEIVER_EMAIL

    msg.attach(MIMEText(html, 'html'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)
        print("📪 메일 전송 완료")
    except Exception as e:
        print(f"메일 전송 실패: {e}")