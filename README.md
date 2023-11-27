# code_Data-collect

### Code

> **`Test{}__.ipynb`** : 크롤링을 하기 이전 각종 테스트 과정이 담긴 파일<br/>
> **`Production{}__.ipynb`** : 크롤링 실행 파일


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

### REF

- https://github.com/team-i-Five/code_Data-collect/issues/1 도커 실행 방법 참고 자료

- https://github.com/team-i-Five/code_Data-collect/issues/13 랭킹 데이터 airflow 진행상황 공유

- https://airflow.apache.org/docs/docker-stack/build.html
