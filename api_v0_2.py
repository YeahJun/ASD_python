# -*- coding: utf-8 -*-

def folders_create(request,*args,**kwargs):
	"""새로운 폴더를 생성한다.


	:URL: https://api.server.com/api/0/fileops/folder_create/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 새 폴더의 경로.


	:param created: 선택 사항. 클라이언트 앱이 설치된 OS에서 폴더가 생성된 시점에 대한 타임 스탬프 기록.


	:param modified: 선택 사항. 타임 스탬프는 클라이언트 앱이 설치된 OS에서 폴더를 수정한 시점.


	:Return: 새로운 폴더를 위한 메타데이터.


	:Error 403: 주어진 경로의 폴더가 존재하지 않는다.

"""
def folders_or_files_delete(request,*args,**kwargs):
	"""파일이나 폴더를 삭제한다.


	:URL: https://api.server.com/api/0/fileops/delete/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 삭제할 폴더나 파일의 경로.


	:param only_empty: 선택 사항. 기본적으로 False로 설정된다. True이면 비어 있는 경우에만 폴더가 삭제된다. 파일을 삭제할 때 매개 변수가 사용되지는 않는다.


	:param without_trash: 선택 사항. 기본적으로 False로 설정된다. True이면 휴지통으로 옮기는 작업없이 삭제된다.


	:Return: 삭제된 폴더나 파일의 메타데이터.


	:Error 403: 사용자가 폴더를 삭제할 수 없거나, only_empty 변수가 True지만 폴더가 비어 있지 않다.


	:Error 404: 지정한 폴더를 찾을 수 없다.

"""
def folders_or_files_multi_delete(request,*args,**kwargs):
	"""여러 개의 파일이나 폴더를 삭제한다.


	:URL: https://api.server.com/api/0/fileops/multi/delete/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 삭제된 폴더나 파일의 경로 리스트이다. 예시: path=/1/2/3&path=/1/2/4


	:param only_empty: 선택 사항. 기본적으로 False로 설정된다. True이면, 비어 있는 폴더만 삭제된다. 파일을 삭제할 때 매개 변수가 사용되지 않는다.


	:param without_trash: 선택 사항. 기본적으로 False로 설정된다. True이면, 휴지통으로 옮기는 작업없이 삭제된다.


	:Return: 삭제된 파일이나 폴더의 메타데이터 목록.


	:Error 403: 사용자가 폴더를 삭제할 수 없거나, only_empty 변수가 True지만 폴더가 비어 있지 않다.


	:Error 404: 지정한 폴더를 찾을 수 없다.
	"""
def folders_or_files_undelete(request,*args,**kwargs):
	"""삭제된 파일이나 폴더를 복원한다.


	:URL: https://api.server.com/api/0/fileops/undelete/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 복원할 파일 또는 폴더의 경로이다.


	:Return: 복원된 폴더의 메타데이터.


	:Error 403: 사용자가 파일이나 폴더의 복원을 허락하지 않았다. (폴더가 삭제되지 않았거나 일부 삭제된 상위 개체의 일부이다.) 예를 들어, 이 파일보다 나중에 삭제된 폴더에서 삭제한 파일은 복원할 수 없다.


	:Error 404: 지정한 폴더를 찾을 수 없다.

"""
def folders_or_files_multi_undelete(request,*args,**kwargs):
	"""삭제된 파일이나 폴더를 복원한다.


	:URL: https://api.server.com/api/0/fileops/multi/undelete/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 복원된 파일이나 폴더의 경로 리스트이다. 예시: path=/1/2/3&path=/1/2/4


	:Return: 복원된 파일이나 폴더의 메타데이터 리스트.


	:Error 403: 사용자가 파일이나 폴더의 복원을 허락하지 않았다. (폴더가 삭제되지 않았거나, 일부 삭제된 상위 객체의 일부이다.) 예를 들어, 이 파일보다 나중에 삭제된 폴더에서 삭제한 파일은 복원할 수 없다.


	:Error 404: 지정한 폴더를 찾을 수 없다.
	"""
def folder_or_file_rename(request,*args,**kwargs):
	"""파일이나 폴더의 이름을 바꾼다.


	:URL: https://api.server.com/api/0/fileops/rename/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 파일이나 폴더의 경로.


	:param newname: 필수 사항. 새로운 이름.


	:Return: 이름이 수정되는 객체를 위한 메타데이터.


	:Error 404: 지정한 파일 또는 폴더를 찾을 수 없다.


	:Note: 이름을 바꾸면 이전 이름이 있는 폴더(파일)가 삭제되고 새 파일 또는 새 이름이 있는 폴더가 생성된다.

"""
def folders_or_files_move(request,*args,**kwargs):
	"""선택된 파일이나 폴더가 새로운 폴더로 옮겨진다. 파일 버전이 이동되지는 않는다. 즉, 버전 관리 지점에서 새 파일을 생성하고 이전 폴더에서 새 파일을 생성하는 것처럼 작업이 새로 생성되는 것처럼 보인다.


	:URL: https://api.server.com/api/0/fileops/move/


	:Version: 0


	:Method: POST


	:param from_path: 필수 사항. 옮겨질 파일이나 폴더의 초기 경로.


	:param to_path: 필수 사항. 객체가 옮겨갈 폴더.


	:Return: 옮겨지는 객체에 대한 정보 (새로운 경로를 포함한)


	:Error 400: 필수 매개 변수 중 하나가 설정되지 않았다.


	:Error 404: 이동할 경로를 찾을 수 없거나, 이동할 필요가 있는 폴더를 찾을 수 없다.


	:Error 405: 이동할 객체의 경로가 폴더가 아니다.


	:Error 409: 객체와 같은 폴더로 옮기길 시도했다.


	:Error 412: 공동 작업자가 공유 루트 폴더를 다른 사용자의 공용 폴더로 이동하거나, 다른 사용자가 만든 공용 폴더로 만든 공용 폴더로 이동하려고 한다. (이러한 폴더는 일종의 마운트 지점이므로, 공유 루트 폴더임에 유의해야 한다. 이러한 폴더를 이동하면 논리적으로 충돌한다.)


	:Error 424: 폴더를 트리 아래 하위 폴더로 이동하려고 한다. 이동한 폴더는 새 폴더가 이동된 새 폴더의 상위 항목이다. 상위 노드를 하위 노드로 이동하는 것은 금지되어 있다.


	:Error 501: 기능이 구현되지 않았다.


	:Note: 옮기는 것은 파일이나 폴더이지만, 장소는 오직 폴더이다. 이 API method를 사용할 때 고려해야 할 몇 가지 충돌이 있다.


	:Note: 만약 파일이나 폴더가 복사될 때(예를 들어 name) 동일한 폴더에 이름이 같은 객체가 있다면 옮겨가는 객체의 이름은 ‘name(1)’로 바뀌고, 초기 객체와 같은 level에 위치한다. 데스크탑 클라이언트에서 동일한 상황이 발생할 경우 OS가 일반적으로 파일을 조합하거나 교체한다고 가정한다. 이 시나리오는 주어진 API method를 사용하여 실행하기가 어렵다. 이러한 충돌이 발생할 경우 데스크탑 클라이언트에서 대체 방법을 호출하는 것이 좋다. 예를 들어, /files/create + /fileops/delete (이전 위치에서 파일을 삭제하고 새 파일에서 파일을 생성한다.) 한 폴더를 다른 폴더로 이동하면 일부 공동 작업자가 자동적으로 폴더에 대한 접근 권한을 상실한다. 예를 들어, 폴더 /1이 사용자 A에게 공유되어 있을 때, 폴더 /1/2/3/4/5 는 사용자 B에게 공유된다, 그리고 폴더 /1/2/3/6도 같은 사용자 B에게 공유된다. 폴더의 주인인 C(또는 사용자 A)가 폴더 /1/2/3/4를 폴더 1/2/3/6으로 옮겼을 때, 사용자 B는 자동적으로 /1/2/3/4/5에 대한 접근 권한을 상실한다. (사용자 B가 이미 폴더 /1/2/3/6에 대한 접근 권한을 갖고 있기 때문에)


	:Note: API method는 세 가지 현상에 의해 특징 지어진다.


	:Note: 1. Moved


	:Note: 2. Created(공동 작업자가 소스 폴더에 대한 접근이 없을 경우)


	:Note: 3. Deleted(공동 작업자가 목적지 폴더에 접근 권한이 없을 경우)

"""
def folders_or_files_copy(request,*args,**kwargs):
	"""선택된 파일이나 폴더를 새로운 폴더나 같은 폴더에 복사한다. 파일 버전은 복사되지 않는다.


	:URL: https://api.server.com/api/0/fileops/copy/


	:Version: 0


	:Method: POST


	:param from_path: 필수 사항. 파일이나 폴더의 초기 경로.


	:param to_path: 필수 사항. 객체가 복사될 폴더.


	:Return: 새로운 폴더나 파일에 관한 정보


	:Error 400: 필수 매개 변수 중 하나가 설정되지 않았다.


	:Error 404: 복사될 경로를 찾을 수 없거나 객체를 복사해야 하는 폴더를 찾을 수 없다.


	:Error 405: 복사가 실행되는 경로는 폴더가 아니다.


	:Error 424: 폴더를 트리 아래 하위 폴더에 복사하려고 한다. 복사된 폴더는 복사된 새 폴더의 상위 폴더이다. 사우이 폴더를 하위 폴더에 복사할 수 없다.


	:Note: 만약 파일이나 폴더가 복사될 때(예를 들어 name) 동일한 폴더에 이름이 같은 객체가 있다면 옮겨가는 객체의 이름은 ‘name(1)’로 바뀌고, 초기 객체와 같은 level에 위치한다. 데스크탑 클라이언트에서 동일한 상황이 발생할 경우 OS가 일반적으로 파일을 조합하거나 교체한다고 가정한다. 이 시나리오는 주어진 API method를 사용하여 실행하기가 어렵다. 이러한 충돌이 발생할 경우 데스크탑 클라이언트에서 대체 방법을 호출하는 것이 좋다. 예를 들어, /files/create (새로운 장소에서 재작성)
	:Note: 작업 결과는 “파일 생성” 또는 “폴더 생성”이다.

"""