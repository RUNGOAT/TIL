# [Git] origin, remote, branch

<br>

# origin, remote

<br>

> ## origin

git을 통해 remote repository에서 프로젝트 코드를 check out 하면 나만의 local repository를 갖게 되고

commit과 push, 그리고 pull 커맨드 등을 통해 remote repository와 협업을 하게 된다.

이 때 remote repository의 URL을 일일이 입력하지 않고

"orgin" 이라고 하는 키워드(alias)를 대신 활용하는 것

즉, "orgin" 은 remote repository URL을 참조하기 위한 **변수명** 

> ## remote

remote repository를 참조해야 하는 작업을 할 때는 항상 "git remote" 라고 하는 키워를 사용해야 한다.

그래서 "remote" 는 origin이 참조하는 remote repository와 특정 커맨드를 수행하기 위해 사용하는 일종의 git 커맨드 정도로 생각



그래서

> git remote

커맨드를 사용하면 remote repository 리스트를 볼 수 있는데, 이 때 repository의 URL이 출력되지 않고 alias인 origin이 대신 출력된다.

URL을  확인하기 위해서는

> git remote -v

커맨드를 활용하면 alias와 URL이 함께 출력되는 것을 확인할 수 있다.

<br>

[출처]([[git\] origin, remote, 그리고 branch 개념 : 네이버 블로그 (naver.com)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hisukdory&logNo=220766885707))

[출처 안의 출처]([[git\] origin, remote, 그리고 branch 개념 : 네이버 블로그 (naver.com)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hisukdory&logNo=220766885707))

<br>



# branch

<br>

> ## 브랜치(branch)란?

​	독립적으로 어떤 작업을 진행하기 위한 개념

​	각각의 브랜치는 독립적이기에, 여러 작업을 동시에 진행할 수 있습니다.

![branch](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup1_1_1.png)

​	또한 이렇게 만들어진 branch는 다른 branch와 병합할 수 있는데,

![branch merge](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup1_1_2.png) 

위 그림과 같이 먼저 메인 브랜치에서 자신의 작접 전용 브랜치를 만들고, 각자 작업을 진행한 후에 메인 브랜치에 자신의 작업 전용 브랜치의 변경 사항을 적용합니다. 이렇게 함으로써 독립적으로 작업을 수행하여 결과를 하나로 모을 수 있고

이런 '작업 단위', 즉 브랜치로 그 작업의 기록을 중간 중간에 남기게 되어 문제가 발생했을 경우 원인이 되는 작업을 찾아내거나 그에 따른 대책을 세우기 쉬워집니다.

<br>

> ## master 브랜치

저장소를 처음 만들면, Git은 바로 **'master or main'** 이라는 이름의 브랜치를 만들어 둡니다. 이 새로운 저장소에 새로운 파일을 추가 한다거나, 추가한 파일의 내용을 변경하여 그 내용을 저장(커밋, Commit)하는 것은 **모두 'master' 라는 이름의 브랜치**를 통해 처리할 수 있는 일이 됩니다.

'master'가 아닌 또 다른 새로운 브랜치를 만들어서 '이제부터 이 브랜치를 사용할거야!'라고 선언(체크아웃, checkout)하지 않는 이상, 이 때의 모든 작업은 'master' 브랜치에서 이루어 집니다.

![master branch](https://backlog.com/git-tutorial/kr/img/post/stepup/capture_stepup1_1_3.png)



[출처]([브랜치란? [브랜치 (Branch)] | 누구나 쉽게 이해할 수 있는 Git 입문~버전 관리를 완벽하게 이용해보자~ | Backlog](https://backlog.com/git-tutorial/kr/stepup/stepup1_1.html))