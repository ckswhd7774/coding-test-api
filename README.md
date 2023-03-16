# coding-test-api
넘블 코딩 테스트 플랫폼 API

# numble Django Challenge [![](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/django-4.2-green.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/drf-3.14-red.svg)](https://www.python.org/downloads/)  

## Root Directory Structure
```
├── .github              # github action directory
├── .idea                # pycharm config directory
└── backend              # django project root directory
```

## Backend Directory Structure
```
└── backend
    ├── api              # django api directory
    ├── app              # django app directory
    ├── config           # django config directory
```

## Package
- [requirements.txt](./backend/requirements.txt)

## Install Virtual Environment & Dependency
```
# __PROJECT_ROOT__/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Server
```
python manage.py runserver 0:8000
```

## Test
```
python manage.py test api
```

## API Document
- http://localhost:8000/swagger/

## API List
- question(문제)
```
- 문제 목록 조회, 생성, 수정, 삭제
```
- answer(답)
```
- 해당 문제의 답 목록 조회, 생성, 수정, 삭제 
```
- explanation(해설)
```
- 해당 문제의 해설 목록 조회, 생성, 수정, 삭제
```
- submit_answer(답 제출)
```
- 제출한 답안 제출 목록 조회
- 답안 제출 생성 및 채점
```
- bookmark(북마크)
```
- 문제 북마크 목록 조회, 생성, 삭제
```
- user(유저)
```
- 로그인
- 유저 정보 조회
- 유저 회원가입
```

## ERD
![스크린샷 2023-03-16 오후 9.51.56.png](..%2F..%2FDesktop%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202023-03-16%20%EC%98%A4%ED%9B%84%209.51.56.png)

## 기술적으로 고민한 부분들
```
- api까지 완성하진 않았지만 모의고사 DB 설계 및 api 설계에 대한 부분들.
- 해당 데이터를 만든 유저가 본인임을 인증할 때 serializer.py에서 validation 체크를 진행해야 할지? 
  아니면 permissions.py에서 체크를 해야 할지? 에 대한 부분들
```