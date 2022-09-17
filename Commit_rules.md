# COMMMIT RULE
## 이 문서는 팀 내 커밋 룰을 지정하기 위한 문서로, 배포 브랜치에는 포함되지 않아야 하고, 2022년 12월 이후 강제력을 가집니다. 팀 구성원 전원의 동의 없이 임의 배포 및 수정, 사용을 금지합니다.  
  
## 1. 작성 및 수정  
* 이 문서의 최초 내용 중 일부는 2022/09/17 팀 회의를 통해 구성원 전원의 동의를 받은 내용입니다.  
* 1.2 수정 및 이의제기는 전원이 참석한 온/오프라인 회의(권장) 혹은 전원의 메신저 내 동의 하에서만 가능합니다.  
* 1.3 합의 없는 개인적인 수정 및 사용은 금지합니다.  


## 2. 메인 개발 룰   
### 2.1 브랜치 관리
* main(deploy 전용), nightly branch로 분할합니다.  
* nightly 브랜치에 최대한 머지합니다.  
* nightly branch에서는 제한 없이 파생 브랜치를 만들 수 있습니다.  
* main branch에서도 파생 브랜치를 만들 수 있으나, 최대한 지양합니다.  

### 2.2 머지 관리 
* 팀 구성원 전원에게 review를 요청한다.  
* nightly, main 브랜치의 ***모든*** 머지는 팀 구성원 한 명 이상의 approve을 받은 후 진행합니다.  
* merge pull request는 code 작성자와 approver를 제외한 인원 중 한 명이 진행합니다.  
* 모든 변경점은 우선적으로 nightly에 머지합니다. 충분한 검증이 된 이후 main에 머지를 진행합니다.  
* 필요한 경우 merge와 같이 혹은 merge 이후 6시간 이내에 문서화를 진행합니다.
* merge 사항이 잘못되었을 경우 ***merge pull request를 진행한 사람***이 책임지고 revert 및 rebase 진행합니다.  

### 2.3 테스트 및 액션 관리(필요 시 git action 테스트 프로세스로 대체한다.)
* main branch에 머지할 경우 아래 사항을 수행한다  
	+  신규 추가한 사항이 python class/function이며 testcase가 없을 경우
		* pull request 제안자는 이를 테스트할 수 있는 test code를 unit test 용도로 별도 폴더에 작성한다. 경로는 추후 협의한다.  
		* pull request 시 본문 맨 마지막에 testcode 실행 결과 로그를 첨부한다.  
		* assignee 중 한명이 직접 testcode를 실행하여 테스트하고(이하 manual unit test) 그 기록을 comment로 기입한다.
		* 최소 2명 이상의 assignee를 걸고 confirm 받는다.  
		* assignee가 approve 시에는 testcode 실행 결과 로그를 첨부하고 . 단 github action 도입 이후에는 action으로 대체한다.
	+ 수정사항이 python class/function이며 testcase가 있을 경우
		* pull request 제안자는 request 본문 맨 마지막에 test code 실행 결과 로그를 첨부한다.  

* nightly 브랜치에 머지할 경우 test code 추가 및 pull request 제안자의 실행 결과만 본문에 추가합니다.
* 추가한 사항이 위와 달라 테스트가 어려울 경우 문서화를 먼저 진행하고 실행 로그/데이터 버젼/conda env 환경 및 필요하다고 생각되는 사항을 pull request 본문 마지막에 기입한다.

### 2.4 code 관리 
> <https://google.github.io/styleguide/pyguide.html>
* 모든 함수와 클래스에는 docstring을 google style로 작성한다.
* 기타 린팅 및 코드 스타일은 google style을 따른다.
