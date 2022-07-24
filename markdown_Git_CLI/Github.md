# git 이란

- 버전 : 컴퓨터 소프트웨어의 특정 상태

- 관리 : 어떤 일의 사무, 시설이나 물건의 유지 . 개량

- 프로그램 : 컴퓨터에서 실행될 때 특정 작업을 수행하는 일련의 명령어들의 모음

  

  - 버전관리 - 컴퓨터 소프트웨어의 특정 상태들을 관리하는 것



# GUI 와 CLI

- GUI (Graphic User Interface)

그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식

- CLI ()

명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식



- **Why CLI**

GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모

수 많은 서버/개발 시스템이 CLI를 통한 조작 환경을 제공



- linux shell

커널과 사용자 간의 다리역할



- 절대 경로

루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것

윈도우 바탕 화면의 절대 경로 - C:/Users/ssafy/Desktop



- 상대 경로

현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것

현재 작업하고 있는 디렉토리가 C:/Users 일 때

./ 현재 작업하고 있는 폴더				../ 현재 작업하고 있는 폴더의 부모 폴더


CLI
---

## README.md

프로젝트에 대한 설명 문서

Github 프로젝트에서 가장 먼저 보는 문서

일반적으로 소프트웨어와 함께 배포



## Repository

특정 디렉토리를 버전 관리하는 저장소

__git init__ 명령어로 로컬 저장소를 생성

.git 디렉토리에 **버전 관리에 필요한 모든 것**이 들어있음



#### README.md 생성하기

- Working Directory - 내가 작업하고 있는 **실제 디렉토리**

- Staging Area - **커밋**으로 남기고 싶은, **특정 버전**으로 관리하고 싶은 파일이 있는 곳

- Repository - 커밋들이 저장되는 곳

**커밋(commit)**은 이 3가지 영역을 바탕으로 동작



Working Directory						git add 로 -> Area

Staging Area								  git commit 으로 -> Repository

Repository										**committed**



git status

현재 git으로 관리되고 있는 파일들의 상태

---



git clone {remote_repo}		- remote repo를 local로 복사한다.

git push origin master   local repo의 최신 커밋을 remote repo로 push한다



매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것

신입 개발자에게 요구되는 가장 큰 능력, 꾸준히 학습할 수 있나요?

Github 관리
