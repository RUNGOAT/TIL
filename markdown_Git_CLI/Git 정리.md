### [1] Git 초기 설정

> ​	최초에 한번만 진행
```bash
$ git config --global user.name "hanoogi2"
$ git config --global user.email "hanoogi@gmail.com"
```

```bash
$ git config --global -l
$ git config --global --list
```

### [2] Git 기본 명령어

#### (0) 로컬저장소

- Working Direcotory : 사용자의 일반적인 작업이 일어나는 곳

- Staging Area : 커밋을 위한 파일 및 폴더가 추가 되는 곳

- 로컬 Respository : staging Area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 곳

  ![image-20220113102616279](C:\Users\hanoo\AppData\Roaming\Typora\typora-user-images\image-20220113102616279.png)

#### (1) git init

```
$ git init
Initialized empty Git repository in D:/ssafy-7th_test/git-test/.git/

```

- 현재 작업 중인 디렉토리를 Git 으로 관리
- `.git` 이라는 숨김 파일, 터미널에 `(master)`라고 표기
- **git 저장소를 중첩해서 만들지 마세요**

#### (2) git status

- Working Directory와 Stating Area에 있는 파일의 현재 상태

- 상태

  1. `Untracked` : Git관리 하지 않은 파일(한번도 Staging Area에 올린적이 없는 파일)
  2. `Tracked` : Git이 관리하는 파일
     1. `Unmodified` : 최신상태
     2. `Modified` : 수정되었지만, 아직 Stage Area에는 반영하지 않은 상태
     3. `Staged` :  Stage Area에 올라간 상태

  ```bash
  $ git status
  $ git status -s
  ```

  

#### (3) git add

- Working Directory -> Staging Area 올리는 명령어

- `Untracked`/`Modified` -> `Staged`

  ```
  $ git add a.txt
  $ git add .
  ```

  

#### (4) git commit

- Staging Area에 올라온 파일의 변경사항을 하나의 버전(커밋)을 저장
- `커밋메세지` 현재 변경사항 의미있게 표현

```bash
$ git commit -m 'first commit'
```

#### (5) git log

- 커밋 내역(ID, 작성자, 시간 ,메세지)을 조회

  ```bash
  $ git log
  $ git log --oneline
  ```

---

### [3] 원격 저장소에 업로드

#### (1) git remote

- 로컬 저장소에 원격 저장소를 `등록, 삭제, 조회` 하는 명령어

  1. 원격저장소 등록

     - `git remote add <이름> <주소>` 작성

       ```
       $ git remote add origin https://github.com/hanoogi2/TIL.git
       ```

  2. 원격저장소 조회

     - `git remote -v`

       ```bash
       $ git remote -v
       origin  https://github.com/hanoogi2/TIL.git (fetch)
       origin  https://github.com/hanoogi2/TIL.git (push)
       
       ```

       

  3. 원격저장소 **연결** 삭제

     - `git remote rm <이름>`

       ```bash
       $ git remote rm origin
       ```

       

#### (2) git push

- 로컬저장소의 커밋을 원격저장소에 업로드하는 명령어

- `git push <저장소 이름> <브랜치>`

  ```
  $ git push origin master
  
  ```

  ```
  $ git push -u origin master
  $ git push 
  ```

  

---

 #### README.md

> 원격저장소의 소개나 설명이 담겨있는 대문 역할

#### .gitignore

> 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하다도록 지정

(1) .gitignore

- 민감한 개인 정보 가 담긴 파일
- OS 에서 활용되는 파일
- IDE(pycharm), Text editor(vscode) 등에서 활용되는 파일
  - pycharm : `.idea`
  - vscode : `.vscode`
- 개발언어(python) 혹은 프레임워크(django)에서 사용하는 파일
  - 가상환경 : `venv/`
  - `__pycache__/`

(2) .gitignore 주의사항

	- 반드시 이름을 `.gitignore` 로 작성
	- `.gitignore`파일은 `.git`폴더와 동일한 위치에 생성
	- 제외 하고 싶은 파일은 반드시 `git add`전에 `.gitignore`에 작성

(3) 쉽게 만들기

 - gitignore.io

---

### [4]  원격 저장소 가져오기

### (1) git clone

- 원격저장소의 커밋내용을 모두 가져와서, 로컬저장소에 생성

- git clone 명령어를 사용하면 원격저장소 통째로 복재해서 내컴퓨터에 복사한다.

- 초기에 한번만 진행

- `git clone <원격 저장소 주소>`

- 폴더 단위 가져옴

  ```
  $ git clone https://github.com/hanoogi2/TIL.git
  ```

- 로컬저장소에 `git inti`과 `git remote add`가 이미 수행된 상태

  

#### (2) git pull

- 원격저장소의 변경사항을 업데이트하는 명령어

  ```
  $ cd TIL
  $ git pull origin master 
  ```

  

---

(1) 집에서 작성

```
$ git init
$ touch day1.md
$ git add .
$ git commit -m '집에서 day1 작성'
$ git remote add origin https://github.com/hanoogi2/TIL-remote.git
$ git push origin master

```

(2) 강의실에서 작성

```
$ git clone https://github.com/hanoogi2/TIL-remote.git TIL-class
$ cd TIL-class
$ touch day2.md
$ git add .
$ git commit -m '강의장에서 day2 작성'
$ git push origin master
```

(3) 집에서 강의실에 올린 것 받기

```
$ git pull origin master
```























