도커 이미지 빌드
```
docker build --platform=(운영체제에 맞게) -t news-scheduler .(파일경로)
```

도커 이미지 파일로 저장
```
docker save -o news-scheduler.tar news-scheduler
```

도커 파일 이미지로 업로드
```
docker load -i news-scheduler.tar
```

도커 이미지 실행(-d: 백그라운드)
```
docker run -d --name news-scheduler news-scheduler
```
