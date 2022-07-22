# 1. 개발 도구 선정

## 1.1 인텔리제이(Intelij IDEA) 장점 및 기능

**장점**

-   강력한 추천 기능
-   다양한 리팩토링과 디버깅 기능
-   높은 Git 자유도
-   프로젝트 시작할 때 인덱싱을 하여 파일을 비롯한 자원들에 대한 빠른 검색 속도
-   HTML과 CSS, JS, XML에 대한 강력한 기능 지원
-   자바, 스프링 부트 버전업에 맞춘 빠른 업데이트

**커뮤니티(무료) 기능**

-   자바 개발에 대한 모든 기능 지원
-   Maven, Gradle과 같은 빌드 도구 기능 지원
-   깃 & 깃허브와 같은 VCS(버전 관리 시스템) 기능 지원
-   스프링 부트의 경우 톰캣과 같은 별도의 외장 서버 없이 실행 가능

HTML과 CSS, JS에 대한 지원은 하지 않아 다른 개발 도구 or 얼티메이트(유료) 이용

## 1.2 인텔리제이 설치 방법

1) 인텔리제이를 바로 내려받지 않고 젯브레인 툴박스 이용  
2) 툴박스를 통해 인텔리제이 설치

**툴박스**: 젯브레인의 제품 전체를 관리해 주는 데스크톱 앱

-   모든 제품군의 버전 관리와 JVM 옵션 등 조정할 수 있음
-   새로운 버전이 나오면 툴박스 앱 안에서 업데이트를 바로 확인해서 진행 가능
-   [설정 -> Settings] : Maximun heap size 설정, 인텔리제이를 실행하는데, 어느 만큼의 메모리를 할당할지를 결정

## 1.3 인텔리제이에서 프로젝트 생성 방법

**1) 프로젝트 유형 선택: 그레이들 (Gradle)**

**2) GroupId와 ArtifactId 등록**

-   GroupId: 사용할 도메인를 거꾸로 이용 ex) com.dev-choee.service-a
-   ArtifactId: 프로젝트의 이름 ex) springboot2-webservice

**3) 그레이들 옵션 선택: 인텔리제이의 기본 설정값**

**4) 프로젝트의 디렉토리 위치 선택**

-   기본적으로 ArtifactId가 프로젝트 이름
-   Project location에서 원하는 위치로 수정

## 1.4 그레이들 프로젝트를 스프링부트 프로젝트로 변경하기

build.gradle 파일 열어서 스프링 부트에 필요한 설정 추가

**1) buildscript 코드 작성**

```
buildscript{ 
    ext{ 
        springBoothVersion = '2.1.7.RELEASE' 
    }
    repositories{
        mavenCentral()
        jcenter() 
    }
    dependencies{  
        classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")        
    }
}
```

**_buildscript_**

-   보통 별도의 외부 라이브러리를 가져와야 할 때 사용, repository와 dependencies로 구성

**_ext_**

-   build.gradle에서 사용하는 전역변수를 설정하겠다는 의미
-   여기서springBootVersion 전역변수를 생성하고 그 값을 '2.1.7.RELEASE'로 설정

**_mavenCentral_**

-   기본적으로 많이 사용
-   단점: 본인이 만든 라이브러리를 업로드하기 위해 많은 과정과 설정 필요하여 공유가 안 되는 상황 발생

**_jcencer_**

-   라이브러리 업로드를 간단하게 한 저장소
-   인터넷의 jcenter 레파지토리 사용 ([https://bintray.com/bintray/jcenter](https://bintray.com/bintray/jcenter))
-   jcenter에 라이브러리를 업로드하면 mavenCentral에도 업로드될 수 있도록 자동화 가능

**_dependencies_**

-   플러그인의 의존성을 받겠다는 의미
-   spring-boot-gradle-plugin라는 스프링 부트 그레이들 플러그인의 2.1.7.RELEASE를 의존성으로 받도록 설정

**2) buildscript 이외 코드 작성**

-   앞서 선언한 플러그인 의존성들을 적용할 것인지를 결정하는 코드

```
apply plugin: 'java' 
apply plugin: 'eclipse' 
apply plugin: 'org.springframework.boot' 
apply plugin: 'io.spring.dependency-management' // !!필수!! 스프링 부트의 의존성들을 관리해 주는 플러그인
```

-   repositories : 각종 의존성(라이브러리)들을 어떤 원격 저장소에서 받을지를 결정

```
repositories { 
	mavenCentral() 
}
```

-   프로젝트 개발에 필요한 의존성들을 선언하는 곳

```
dependencies { 
	implementation('org.springframework.boot:spring-boot-starter-web') 
	testImplementation('org.springframework.boot:spring-boot-starter-test') 
}
```

-   인텔리제이에서는 메이븐 저장소의 데이터를 인덱싱해서 관리하기 때문에 의존성 자동완성 가능(ctrl+space)
-   버전을 명시하지 않아야만 위에서 작성한 "org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}"의 버전을 따라간다.
-   책에서는 compile(), testCompile을 사용하지만, implementation을 사용.

**_Gradle 의존성 옵션: Compile vs implemaetation_**

-   참조: [https://bluayer.com/13](https://bluayer.com/13)

 [\[Gradle\] implementation vs compile

서론 Gradle dependency 관련해서 검색을 하다보면, 어떤 글에서는 implementation을 사용하고 어떤 글에서는 compile을 사용하는 경우가 있다. 사실 어떻게 사용해도 돌아가긴 해서, 음... 무슨 차이지?하고

bluayer.com](https://bluayer.com/13)

**3) build.gradle 변경 반영**  
인텔리제이 오른쪽 하단 알럿의 Enable Auto-import 클릭하여build.gradle 변경이 있을 때 마다 자동 반영되도록 설정

**4) 의존성 확인**  
오른쪽 Gradle 탭을 클릭하여 의존성들이 잘 받아졌는지 확인

## 1.5 인텔리제이에서 깃과 깃허브 사용하는 방법

-   VCS(버전 관리 시스템) 선택: Git
-   Git의 원격 저장소 서비스 선택: Github

**인텔리제이에서 깃허브 연동**

1) Ctrl + Shift + A : Action 검색창 열기  
2) share project on github 검색  
3) 깃허브 로그인  
4) Repository name 설정 후 등록 ( 최초 git ingnore 설정 No)  
5) 첫 커밋 팝업창에서 .idea 디렉토리 제외한 후 커밋 ( 실행시 자동으로 생성되는 파일들이므로 깃허브 올릴 필요 없음 )  
6) .gitignore파일을 사용하여 .idea 폴더를 앞으로의 모든 커밋 대상에서 제외 처리

-   인텔리제이에서는 .gitignore 파일에 대한 기본적인 지원이 없음
-   플러그인에서 .gitignore 지원

**.ignore 플러그인  
_지원 기능_**

-   파일 위치 자동완성
-   이그노어 처리 여부 확인
-   다양한 이그노어 파일 지원(.gitignore, .npmignore, .dockerignore 등)

_**설치 방법**_

1) Ctrl + Shift + A : Action 검색창 열기  
2) plugins 검색  
3) Marketplace 에서 .ignore 설치  
4) 인텔리제이를 다시 시작해서 설치한 플러그인 적용 ( 반드시 재시작해야만 함)  
5) .gitignore 파일 생성: 프로젝트 이름을 선택한 뒤, 마우스 오른쪽 or Alt + Insert로 New(생성목록) 확인하여 .gitignore 파일 생성  
6) 이그노어 처리 후 깃허브에 .gitignore 파일을 푸시하여 반영

**_이그노어 처리_**

-   인텔리제이에서 자동으로 생성되는 파일들을 모두 이그노어 처리
-   .gradle .idea