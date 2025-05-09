import schedule
import time
from utils import getNewsFromNaver, getNewsFromWorld, processCategoryGroup, sendMail
from templates import getHtmlTemplate, appendHtmlTail

naverCategory = {
    "🏛️ 정치": "정치",
    "📰 시사": "시사",
    "💰 경제": "경제",
    "🪙 암호화폐" : "암호화폐",
}

worldCategory = {
    "🤖 인공지능" : "artificail intelligence",
    "🛠️ 소프트웨어 개발" : "software development",
    "🔐 소프트웨어 보안" : "software security"
}

def main():
    print("⏰ 오전 9시 뉴스 요약 시작")
    html = getHtmlTemplate()
    html = processCategoryGroup(naverCategory, html, getNewsFromNaver)
    html = processCategoryGroup(worldCategory, html, getNewsFromWorld)

    html = appendHtmlTail(html)
    sendMail(html)

if __name__ == "__main__":
    schedule.every().day.at("09:00").do(main)
    print("⏳ 스케줄러가 실행 중입니다... 매일 09:00에 뉴스 요약 메일이 전송됩니다.")
    while True:
        schedule.run_pending()
        time.sleep(60)