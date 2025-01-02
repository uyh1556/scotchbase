FROM python:3.9-slim

# 빌드에 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /scotchbase

# 필요한 패키지 설치
COPY requirements.txt /scotchbase/requirements.txt
RUN pip3 install --no-cache-dir -r /scotchbase/requirements.txt

# 소스 코드 및 기타 필요한 파일 복사
COPY . /scotchbase

# 환경 변수 설정 (예시)
ENV DJANGO_SETTINGS_MODULE=scotchbase.settings

# 포트 설정
EXPOSE 8080

# Django 개발 서버 실행 (생산 환경에서는 WSGI 서버 사용 권장)
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]