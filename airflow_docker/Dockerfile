FROM apache/airflow:2.7.3-python3.9

USER root

LABEL maintainer="ifive"

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow

COPY ./dags /opt/airflow/dags

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# 초기화 스크립트 실행
RUN airflow db init

# 사용자 생성 및 초기 비밀번호 설정
RUN airflow users create \
    --username admin \
    --firstname ifive \
    --lastname data \
    --role Admin \
    --email admin@example.com \
    --password 1234


# 웹 서버 및 스케줄러 시작
CMD ["bash", "-c", "airflow db init && airflow webserver -p 8080 -D & airflow scheduler"]
