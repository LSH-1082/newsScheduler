도커 이미지 빌드
```
docker build -t news-scheduler .(파일경로)
```

도커 이미지 실행(-d: 백그라운드)
```
docker run -d --name news-scheduler news-scheduler
```