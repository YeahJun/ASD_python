# -*- coding: utf-8 -*-

def folders_create(request,*args,**kwargs):
	"""새 폴더를 만든다.


	:URL: https://api.server.com/api/1/fileops/folder_create


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 새로운 폴더의 경로.


	:param created: 선택 사항. 클라이언트 앱이 설치된 OS에서 폴더가 생성된 시간을 기록하는 타임스탬프.


	:param modified: 선택 사항. 클라이언트 앱이 설치된 OS에서 폴더가 수정된 시간을 기록하는 타임스탬프.


	:Return: 새로운 폴더에 대한 metadata.


	:Error 403: 주어진 폴더의 경로가 존재하지 않는다.

"""
def folders_or_files_delete(request,*args,**kwargs):
	"""파일이나 폴더를 삭제한다.


	:URL: https://api.server.com/api/1/fileops/delete/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 삭제할 파일이나 폴더의 경로.


	:param only_empty: 선택 사항. 기본적으로 False. True라면, 오직 폴더가 비어 있을 때만 삭제. 이 매개 변수는 파일이 삭제될 때 사용되지 않음.


	:param without_trash: 선택 사항. 기본적으로 False. 만약 True라면, 객체는 휴지통으로 이동하지 않고 삭제.


	:Return: 복구된 폴더의 메타데이터


	:Error 403: 사용자가 폴더를 삭제하도록 허용하지 않았거나, only_empty가 True이기에 폴더가 비어 있다.


	:Error 404: 지정된 폴더를 찾을 수 없다.

"""
def folders_or_files_multi_delete(request,*args,**kwargs):
	"""여러 개의 파일과 폴더를 삭제한다.


	:URL: https://api.server.com/api/1/fileops/multi/delete/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 삭제할 파일들과 폴더들의 경로 리스트. Example: path=/1/2/3&path=/1/2/4


	:param only_empty: 선택 사항. 기본적으로 False. 만약 True라면, 만약 True라면, 오직 폴더가 비어 있을 때만 삭제. 이 매개 변수는 파일이 삭제될 때 사용되지 않음.


	:param without_trash: 선택 사항. 기본적으로 False. 만약 True라면, 객체들은 휴지통으로 이동하지 않고 삭제.


	:Return: 삭제된 파일들과 폴더들의 메타데이터.


	:Error 403: 사용자가 폴더를 삭제하도록 허용하지 않았거나, only_empty가 True이기에 폴더가 비어 있다.


	:Error 404: 지정된 폴더를 찾을 수 없다.
	"""
def folders_or_files_undelete(request,*args,**kwargs):
	"""삭제된 파일이나 폴더를 복구한다.


	:URL: https://api.server.com/api/1/fileops/undelete/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 복구될 파일이나 폴더의 경로.


	:Return: 복구된 파일이나 폴더의 메타데이터.


	:Error 403: 사용자가 파일이나 폴더를 복구하는 것이 허락되지 않았다. (폴더가 삭제되지 않았거나 이것이 삭제된 상위 객체의 일부이다.). 예를 들어, 해당 파일보다 나중에 삭제된 폴더에서 삭제한 파일을 복원할 수 없다.


	:Error 404: 지정된 폴더를 찾을 수 없다.

"""
def folders_or_files_multi_undelete(request,*args,**kwargs):
	"""삭제된 파일이나 폴더를 복구한다.


	:URL: https://api.server.com/api/1/fileops/multi/undelete/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 복구할 파일이나 폴더들의 경로 리스트. 예시: path=/1/2/3&path=/1/2/4


	:Return: 복구될 파일이나 폴더의 메타데이터.


	:Error 403: 사용자가 파일이나 폴더를 복구하는 것이 허락되지 않았다. (폴더가 삭제되지 않았거나 삭제된 상위 객체의 일부이다.). 예를 들어, 해당 파일보다 나중에 삭제된 폴더에서 삭제한 파일은 복원할 수 없다.


	:Error 404: 지정된 폴더를 찾을 수 없다.
	"""
def folders_or_files_rename(request,*args,**kwargs):
	"""파일이나 폴더의 이름을 바꾼다.


	:URL: https://api.server.com/api/1/fileops/rename/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 파일이나 폴더의 경로.


	:param newname: 필수 사항. 새로운 이름.


	:Return: 이름이 바뀐 객체에 대한 메타데이터.


	:Error 404: 지정된 파일이나 폴더들의 경로를 찾을 수 없다.


	:Note: Renaming은 이전 이름을 가진 폴더(파일)가 삭제되고 새로운 이름을 가진 새 파일이나 새 폴더가 생성됨을 의미한다.

"""
def folders_or_files_purge(request,*args,**kwargs):
	"""삭제된 모든 파일 및 파일 버전을 지운다.


	:URL: https://api.server.com/api/1/fileops/purge/


	:Version: 1


	:Method: POST


	:param: 없음.


	:Return 200: 파일 및 폴더를 지우는 작업이 대기열에 있다.

"""
def folders_or_files_purge_status(request,*args,**kwargs):
	"""사용자 파일들의 삭제에 대한 작업 상태를 반환한다.


	:URL: https://api.server.com/api/1/fileops/purgestatus/


	:Version: 0, 1


	:Method: POST


	:Return: 사용자 파일들의 삭제에 대한 작업 상태

	"""
def folders_or_files_move(request,*args,**kwargs):
	"""선택된 파일이나 폴더를 새 폴더에 옮긴다. 파일 버전은 이동되지 않는다. 즉, 버전 관리 관점에서 보면, 이 작업은 이전 폴더를 삭제하고 새로운 경로에 새로운 파일을 생성하는 것과 비슷하다.


	:URL: https://api.server.com/api/1/fileops/move/


	:Version: 1


	:Method: POST


	:param from_path: 필수 사항. 이동시킬 파일이나 폴더의 초기 경로.


	:param to_path: 필수 사항. 객체가 이동될 폴더.


	:param overwrite: 선택 사항(기본적으로 True). 폴더나 파일이 이미 to_path에 존재하는 폴더에 옮겨졌고, overwrite 매개 변수가 False라면, http exception에 의해 에러 코드 403이 표시된다.


	:Return: 이동한 객체에 대한 정보 (새로운 경로 포함)


	:Error 400: 필수적인 매개 변수 중 하나가 설정되지 않았다.


	:Error 403: overwrite 매개 변수가 False이고 to_path폴더 안에 옮겨질 폴더나 파일이 이미 존재한다.


	:Error 404: 이동할 경로를 찾을 수 없다. 또는 움직여질 객체의 폴더를 찾을 수 없다.


	:Error 405: 옮겨질 경로가 폴더가 아니다.


	:Error 409: 같은 폴더에 옮겨질 작업이 실행되었다.


	:Error 412: 공동 작업자가 공유된 루트 폴더를 다른 사용자의 공용 폴더에 옮기려고 하거나, 다른 사용자가 생성한 공용 위치에 생성하려 한다. (이러한 폴더들은 일종의 마운트 지점이고, 논리상 충돌이 있을 수 있기 때문에 공유된 루트 폴더라는 것을 유의해야 한다).


	:Error 424: 폴더를 트리 아래 하위 폴더로 이동하려 한다. 이동한 폴더는 이것이 옮겨진 새 폴더의 상위 항목이다. 상위 노드에서 하위 노드로 옮기는 것은 금지되어 있다.


	:Error 501: 해당 기능이 구현되지 않았다.


	:Note: 우리가 움직일 수 있는 것은 파일이나 폴더 둘 다 이지만, 우리가 옮기는 위치는 폴더라는 것에 유의해야한다. 이 API method를 이용할 때에는 고려해야할 몇 가지의 충돌이 있다. 만약 어떤 폴더에 파일이나 폴더가(예를 들어, /a/b/c/something의 이름을 가진) 복사 되었을 때, 이미 그 곳에 같은 이름(something)을 지닌 폴더가 있는 경우, 객체가 해당 이름으로 바뀌고 초기 객체와 같은 레벨에 위치할 경우이다. 만약 데스크탑 클라이언트에서 동일한 상황이 발생할 경우, OS가 일반적으로 파일들을 조합하거나 교체한다는 사실을 고려해야 한다. 이 시나리오는 주어진 API method의 도움만으로는 실현하기 어렵다. 어떤 충돌의 상황에서, 데스크탑 클라이언트는 일련의 대체 method들을 호출 하는 것이 좋은데, 예를 들어, /files/create + /fileops/delete (이전 위치의 파일을 지우고 해당 경로에 새로운 파일을 만든다)가 있다.


	:Note: 한 폴더를 다른 곳으로 옮길 때, 일부 작업자들은 자동으로 해당 폴더에 대한 접근 권한을 잃는다. 예를 들어, 폴더 /1 이 사용자 A에게 공유되어 있고, 폴더 /1/2/3/4/5 이 사용자 B에게 공유되어 있고, 폴더 /1/2/3/6 이 같은 사용자 B에게 공유되어 있다. 폴더 주인인 C(또는 사용자 A)가 폴더 /1/2/3/4를 폴더 /1/2/3/6으로 옮기려고 할 때, 사용자 B는 자동으로 폴더 /1/2/3/4/5에 대한 접근 권한을 잃는다. (사용자 B가 이미 폴더 /1/2/3/6에 대한 접근을 하고 있었기 때문에).


	:Note: 이 API method(이동)는 세 가지 이벤트로 특정 지어진다: 1. 이동, 2. 생성 (공동 작업자가 소스 폴더에 접근 할 수 없는 경우), 3. 삭제 (공동 작업자가 대상 폴더에 대한 접근 권한이 없는 경우).

"""
def folders_or_files_copy(request,*args,**kwargs):
	"""선택한 파일이나 폴더를 새 폴더나 같은 폴더에 복사한다. 파일 버전은 복사되지 않는다.


	:URL: https://api.server.com/api/1/fileops/copy/


	:Version: 1


	:Method: POST


	:param from_path: 필수 사항. 복사될 파일이나 폴더의 초기 경로.


	:param to_path: 필수 사항. 객체가 복사될 폴더 위치.


	:param overwrite: 선택 사항(기본적으로 True). 폴더나 파일이 이미 to_path에 존재하는 폴더에 복사되어 졌고, overwrite 매개 변수가 False라면, http exception에 의해 에러 코드 403이 표시된다.


	:Return: 새로운 파일이나 폴더에 대한 정보.


	:Error 400: 필수적인 매개 변수가 설정되어 있지 않다.


	:Error 403: overwrite 매개 변수가 False이고 to_path폴더에 복사된 파일이나 폴더가 이미 존재한다.


	:Error 404: 복사될 경로나 복사를 하게 될 폴더의 경로를 찾을 수 없다.


	:Error 405: 복사가 실행될 경로가 폴더가 아니다.


	:Error 424: 트리 아래 하위 폴더에 복사를 실행하려 한다. 복사될 폴더는 그것이 복사된 위치의 상위 폴더이다. 상위 노드에서 하위 노드로 복사하는 것은 금지되어 있다.


	:Note: 만약 어떤 폴더에 파일이나 폴더가(예를 들어, /a/b/c/something의 이름을 가진) 복사 되었을 때, 이미 그 곳에 같은 이름(something)을 지닌 폴더가 있는 경우, 객체가 해당 이름으로 바뀌고 초기 객체와 같은 레벨에 위치할 경우이다. 만약 데스크탑 클라이언트에서 동일한 상황이 발생할 경우, OS가 일반적으로 파일들을 조합하거나 교체한다는 사실을 고려해야 한다. 이 시나리오는 주어진 API method의 도움만으로는 실현하기 어렵다. 어떤 충돌의 경우에서는, 어떤 충돌의 상황에서, 데스크탑 클라이언트는 일련의 대체 method들을 호출 하는 것이 좋은데, 예를 들어, /files/create (새로운 위치에다가 파일 다시 쓰기).


	:Note: 작업의 결과는 오직 “파일 생성”과 “폴더 생성”이다.

"""