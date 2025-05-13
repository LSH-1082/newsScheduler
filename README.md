<div align='center'>

# 📰 NewsScheduler
AI 뉴스 요약 및 이메일 자동 전송 시스템

<img src="https://img.shields.io/badge/status-active-brightgreen" alt="Project Status">
<img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
<img src="https://img.shields.io/github/languages/top/LSH-1082/NewsScheduler" alt="Top Language">

</div>

## 📖 목차
1. [📋 프로젝트 소개](#-프로젝트-소개)
2. [✨ 주요 기능](#-주요-기능)
3. [🛠️ 기술 스택](#%EF%B8%8F-기술-스택)
4. [🚀 수행 업무](#-수행-업무)
5. [🧠 회고 및 배운 점](#-회고-및-배운-점)
6. [⚡ 빠른 시작](#-빠른-시작)


## 📋 프로젝트 소개

뉴스 API를 통해 최신 뉴스를 수집하고, OpenAI GPT API를 사용해 뉴스를 자동 요약한 뒤 HTML 형식의 이메일로 전송하는 자동화 시스템입니다. Docker를 활용해 자동 실행 및 배포 편의성을 높였으며, 실사용 가능한 서비스로 발전시켰습니다.

- **기간 / 인원**: 2025.05.10 ~ 2025.05.13 / 1인 프로젝트

## ✨ 주요 기능

1. 뉴스 API를 통한 최신 뉴스 데이터 수집  
2. OpenAI GPT API 기반 뉴스 요약 자동화  
3. HTML 형식의 이메일로 요약 내용 전송  
4. Docker를 통한 정기 자동 실행 및 배포  


## 🛠️ 기술 스택

**백엔드 / 데이터 수집**  
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow" />
<img src="https://img.shields.io/badge/MyBatis-000000?style=for-the-badge&logo=data&logoColor=brown" />
<img src="https://img.shields.io/badge/News%20API-FF9900?style=for-the-badge&logo=rss&logoColor=grey" />
<img src="https://img.shields.io/badge/Naver%20News-03C75A?style=for-the-badge&logo=naver&logoColor=green" />

**AI 요약**  
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />

**프론트 출력 / 포맷팅**  
<img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=red" />
<img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=cyan" />

**인프라**  
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=blue" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />


## 🚀 수행 업무

- Python 기반 백엔드 및 뉴스 수집 스크립트 개발
- OpenAI GPT API를 활용한 요약 로직 구현
- MyBatis를 통한 직접 SQL 작성 및 데이터 처리
- HTML 템플릿을 활용한 이메일 전송 자동화 구현
- Docker 이미지 생성 및 컨테이너 관리, 정기 실행 스케줄링


## 🧠 회고 및 배운 점

- 처음 MUI 같은 프론트엔드 컴포넌트 라이브러리를 다루는 데 익숙하지 않았고, 공식 문서를 참고해 필요한 정보를 찾는 것도 어려웠습니다. 하지만 반복적인 탐색과 실습을 통해 UI 구현에 익숙해졌습니다.

- Docker를 처음 사용하면서 이미지 생성, 컨테이너 실행 및 관리 과정에 어려움을 겪었지만, 이전 프로젝트 경험과 공식 문서를 바탕으로 문제를 해결할 수 있었습니다.

- 실제 서비스 배포를 위해 리눅스 환경 구성, 네트워크 설정, 서버 자동화를 학습하고 직접 적용하며 인프라 운영 경험을 쌓을 수 있었습니다.

- 다음에는 AI 프롬프트를 보다 정교하게 설계하여 요약 정확도를 높이고, 다양한 뉴스 도메인에 맞춤형 요약을 제공하는 방향으로 개선할 계획입니다.


## ⚡ 빠른 시작


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


---

<div align="center">
  
🌟 **Made by LSH | 2025** 🌟

</div>

