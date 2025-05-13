⚙️ 시작 전 설정

이 프로젝트를 실행하기 전에 config.py 파일에 아래 정보를 입력해야 합니다:
```
NAVER_CLIENT_ID = "input naver api id"         # 뉴스 수집용 뉴스 API ID
NAVER_CLIENT_SECRET = "input naver api secret" # 네이버 뉴스 수집용 뉴스 API SECRET
OPENAI_API_KEY = "input openai api key"        # OpenAI GPT 요약 기능용 
NEWS_API_KEY = "input news api key"            # 뉴스 수집용 뉴스 API 키  
SMTP_EMAIL = "input sender email"              # 이메일 발신 주소
SMTP_PASSWORD = "input sender password"        # 이메일 비밀번호 또는 앱 비밀번호 
RECEIVER_EMAIL = "input receive email"         # 이메일 수신 주소
```
🔐 키 값은 외부에 노출되지 않도록 주의해주세요.

---

🐳 Docker 사용법

아래는 Docker를 통해 이미지를 빌드하고 실행하는 과정입니다:

1. 🏗️ 도커 이미지 빌드  
   `docker build --platform=(운영체제에 맞게) -t news-scheduler .`

2. 📦 도커 이미지 파일로 저장  
   `docker save -o news-scheduler.tar news-scheduler`

3. 🗃️ 도커 이미지 파일에서 불러오기  
   `docker load -i news-scheduler.tar`

4. 🚀 도커 컨테이너 실행  
   `docker run -d --name news-scheduler news-scheduler`

📝 -d 옵션은 백그라운드 실행을 의미합니다.
