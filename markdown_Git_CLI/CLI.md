1. CLI(Command Line Interface) : 터미널을 통해 사용자와 컴퓨터가 상호작용하는 방식
2. GUI(Graphic User Interface) : 그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식
* Interface : 사용자와 컴퓨터가 서로 소통하는 접점



### 터미널 종류

1. 윈도우즈 : 명령프롬프트, Powershell

2. UNIX : bash, ...
   
   1. Mac OS
   
   2. Linux
   
   
   화면 지우기 (윈도우:cls, Unix:ctrl+l)
   

  

### 경로

1. 루트 디렉토리(/)

     - 모든 파일과 폴더를 담고 있는 최상위 폴더
     - windows의 보통 c: 드라이브 
2. 홈 디렉토리(~)

    - 현재 로그인 된 사용자의 홈 폴더

    - windows의 `c:/사용자(users)/ 현재사용자계정`

3. 폴더 vs 디렉토리

     - 거의 같은 의미

     - 윈도우 탐색기 특수 폴더(ex, 네트워크 환경, 내컴퓨터)은 폴더이지만 디렉토리는 아님

     - 폴더가 디렉토리보다 넓은 개념

   

### 절대 경로와 상대 경로

1. 절대 경로: 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것

     - c:/users/사용자이름/Desktop
     - d:/ssafy-7th-gm3/00_startcamp/0112/CLI.md
2. 상대경로 : 현재 작업하는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것

     - `./`  : 현재 작업하고 있는 폴더를 의미

     - `../` : 현재 작업하고 있는 폴더의 부모폴더 의미

   

### 터미널 명령어

1. touch
   - 파일을 생성하는 명령어
     ```
     $ touch test.txt (빈파일 생성)
     $ echo hello world > test2.txt (덮어쓰기)
     $ echo hello world >> test2.txt (추가)
     ```

2. cat 

     - 파일 내용보기
       ```
       $ cat text2.txt
       ```

3. pwd
    
- 현재 작업 디렉토리
    
4. mkdir

     - 새 폴더를 생셩하는 명령어
       ``` 
       $ mkdir hwkim
       $ mkdir "hello world"
       ```
     ```
     
     ```

5. ls

    - 현재 작업중인 디렉토리의 폴더/파일 목록 보여주는 명령어

    - `-a` : all옵션, 숨김파일 보여줌

    - `-l' :  long옵션, 자세히
    
    ```bash
    $ ls -al
    ```

 6. mv

     - 폴더/파일을 다른 폴더 내로 이동하거나 이름 변경하는 명령어

     - 단, 다른 폴더로 이동할때는 작성한 폴더가 반드시 있어함.
       없으면 이름이 바뀝니다.
      ```
      $ mv test.txt hello  (옮기기)
      $ mv test.txt text.txt (이름변경)
      ```

7. cd 

     - 작업디렉토리 변경
       ``` $ cd ~ (홈디렉토리)
       $ cd - (바로 전디렉토리)
       $ cd ..(부모 디렉토리)
       $ cd ../new2/hello (한번에 가기)```
       ```

8. rm 

    - 지우기(휴지통에 안감)

     ```$ rm text.txt
     $ rm -r hello
     ```

