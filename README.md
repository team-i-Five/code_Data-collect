# code_Data-collect

### Docker

- http://localhost:8888/

```bash

$ docker build -t my-python .

# 주피터노트북 컨테이너를 실행 및 로컬 code 저장소 공유
## 해당 주피터노트북에서 실행한 파일을 저장하면 로컬의 code에 저장됨.
$ docker run -v {본인파일위치}/code_Data-collect/code:/app -p 8888:8888 my-python

# {본인파일위치} -> ex) /home/user1/project/code_Data-collect/code

```

### REF

- https://github.com/team-i-Five/code_Data-collect/issues/1

