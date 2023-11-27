# code_Data-collect

### Code

> **`Test{}__.ipynb`** : 각종 테스트 파일 <br/>
> **`Production{}__.ipynb`** : 최종 실행 파일 <br/>

> `Production1_get_all_detail.ipynb` ML 학습용 뮤지컬 상영 데이터 수집 코드 : 과거 상영작 20,499건, 현재 상영작 85건, 상영 예정작 389건 (2023.11.14. 기준) <br/>
> `Production2_insert_ranking_db.ipynb` 수집한 데이터 AWS RDB 적재 코드  <br/>
> `Production3_get_rank.py` 매일 갱신되는 뮤지컬 랭킹 Top 10 수집 airflow dag 파일


### Docker

- [`./Dockerfile`](https://github.com/team-i-Five/code_Data-collect/blob/main/Dockerfile)

```bash

$ docker build -t my-python .

# 주피터노트북 컨테이너를 실행 및 로컬 code 저장소 공유
## 해당 주피터노트북에서 실행한 파일을 저장하면 로컬의 code에 저장됨.
$ docker run -v {본인파일위치}/code_Data-collect/code:/app -p 8888:8888 my-python

# {본인파일위치} -> ex) /home/user1/project/code_Data-collect/code

```
<br>

- [`./airflow_docker/Dockerfile`](https://github.com/team-i-Five/code_Data-collect/blob/main/airflow_docker/Dockerfile)

```bash
$ cd airflow_docker
$ docker build -t airflow-i .
$ docker run --name airflow-c -p 8080:8080 airflow-i

# 이후 실행된 환경의 url로 접속 포트=8080
## ex) localhost:8080
### id=admin, password=1234
```

### DEPLOY
```bash
# AWS ec2 원격접속
## 각종 권한 설정
### 도커 설치 및 이미지 빌드, 컨테이너 실행
$ sudo apt install docker.io
$ git clone ...
$ cd airflow_docker
$ docker build -t airflow-i .
$ nohup docker run --name airflow-c -p 8080:8080 airflow-i &

# AWS ip주소:8080
## id=admin, password=1234
```

### REF

- https://github.com/team-i-Five/code_Data-collect/issues/1 도커 실행 방법 참고 자료

- https://github.com/team-i-Five/code_Data-collect/issues/13 랭킹 데이터 airflow 진행상황 공유

- https://airflow.apache.org/docs/docker-stack/build.html
