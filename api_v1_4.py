# -*- coding: utf-8 -*-

def trash_content(request,*args,**kwargs):
	"""현재 휴지통에 있는 파일 및 폴더에 대한 정보 목록을 반환한다


	:URL: https://api.server.com/api/1/trash/


	:Version: 1


	:Method: GET


	:param dirs_only: 선택 사항. 기본적으로 0으로 설정되어 있다. 1이면 디렉토리들이 리스트에 포함되어 있다.


	:param extra: 선택 사항. 기본적으로 true 로 설정되어 있다. 메타데이터와 함께 몇 가지 추가 정보 (추가 데이터라고 함)를 반환한다. 추가 정보라 함은 mp3 태그 (파일에 mp3 형식 인 경우), 미리보기 정보 (파일이 문서 인 경우), 축소판에 대한 정보 (파일이 이미지인 경우) 등. 형식 CL:1558을 참조.


	:param offset: 선택 사항. 기본적으로 0으로 설정되어 있다. 휴지통 내용물 리스트의 시작점으로부터 얼마나 떨어져 있는지를 가리키는 오프셋.


	:param limit: 선택 사항. 기본적으로 0으로 설정되어 있다. 휴지통 내용물 리스트에 요청을 할 때 가져올 수 있는 최대 객체 개수.


	:Return: 휴지통에 있는 각 객체의 메타 데이터 목록. 더 나아가 휴지통 해시는 헤더 Etag에 포함되어 반환된다. 이 해시는 If:None:Match 헤더에 넣어서 서버로 보낼 때 클라이언트 쪽의 캐시에 사용할 수 있다. 서버의 휴지통 내용이 변경되지 않은 경우 코드 304가 반환된다.


	:Return: 응답 형식은 API method / metadata가 반환하는 것과 유사하다. 그러나 객체 정보의 필드 경로 대신 필드 이름이 반환된다. 이 필드는 객체 ID로 사용되어 휴지통에서 복원된다. 삭제되기 전에 오브젝트가 있었던 위치를 가리키는 restore_path 필드도 추가된다.


	:Error 304: 마지막 요청과 변화한 것이 없다 (If:None:Match 헤더에 의해서 결정된다).


	:Error 404: 휴지통 또는 그 안에 있는 객체를 찾을 수 없다. 예를 들어, 요청이 수행되는 동안에 삭제되어 버린 경우. 

"""
def trash_restore(request,*args,**kwargs):
	"""휴지통으로부터 객체를 복원한다.


	:URL: https://api.server.com/api/1/trash/restore/<name>


	:Version: 1


	:Method: POST


	:param name: 필수 사항. 휴지통에 있는 객체의 이름.


	:param overwrite: 선택 사항 (기본적으로 1로 설정되어 있다.) 복원할 폴더 또는 파일이 사용자 파일 저장소에 이미 존재하고 이 파라미터가 0으로 설정되어 있으면 http exception에 의해 코드 403이 표시된다. 


	:Note: 이 메소드는 동시에 존재하지 않는다.

"""
def trash_clear(request,*args,**kwargs):
	"""휴지통 내용물을 모두 제거한다


	:URL: https://api.server.com/api/1/trash/clear/


	:Version: 1


	:Method: POST


	:param paths: 선택 사항. 휴지통에서 제거될 파일 또는 폴더의 경로 리스트.


	:Note: 이 메소드는 동시에 존재하지 않는다.

"""
def trash_shared_content(request,*args,**kwargs):
	"""공유 폴더에 있었고 현재는 휴지통에 있는 파일 및 폴더에 대한 데이터 목록을 반환한다.


	:URL: https://api.server.com/api/1/trash/from_shared/<path>


	:Version: 1


	:Method: GET


	:param path: 필수 사항. 공유 폴더에 대한 경로.


	:param dirs_only: 선택 사항. 기본적으로 0으로 설정되어 있다. 1이면 디렉토리들이 리스트에 추가가 된다.


	:param extra: 선택 사항. 기본적으로 true 로 설정되어 있다. 메타 데이터와 함께 몇 가지 추가 정보 (추가 데이터라고 함)를 반환한다. 추가 정보라 함은 mp3 태그 (파일에 mp3 형식 인 경우), 미리보기 정보 (파일이 문서 인 경우), 축소판에 대한 정보 (파일이 이미지인 경우) 등. 형식 CL:1558 참조.


	:param offset: 선택 사항. 기본적으로 0으로 설정되어 있다. 휴지통 내용물 리스트의 시작점으로부터 얼마나 떨어져 있는지를 가리키는 오프셋.


	:param limit: 선택 사항. 기본적으로 0으로 설정되어 있다. 휴지통 내용물 리스트에 요청을 할 때 가져올 수 있는 최대 객체 개수.


	:Return: 휴지통에 있는 각 객체의 메타 데이터 목록. 더 나아가 휴지통 해시는 헤더 Etag에 포함되어 반환된다. 이 해시는 If:None:Match 헤더에 넣어서 서버로 보낼 때 클라이언트 쪽의 캐시에 사용할 수 있다. 서버의 휴지통 내용이 변경되지 않은 경우 코드 304가 반환된다.


	:Return: 응답 형식은 API method / metadata가 반환하는 것과 유사하다. 그러나 객체 정보의 필드 경로 대신 필드 이름이 반환된다. 이 필드는 객체 ID로 사용되어 휴지통에서 복원된다. 삭제되기 전에 객체가 있었던 위치를 가리키는 restore_path 필드도 추가된다.


	:Error 304: 마지막 요청과 변화한 것이 없다 (If:None:Match 헤더에 의해서 결정된다).


	:Error 404: 휴지통 또는 그 안에 있는 객체를 찾을 수 없다. 예를 들어, 요청이 수행되는 동안에 삭제되어 버린 경우.


	:Error 400: 폴더 (공유된 접근)가 더 이상 이 사용자에게 속하지 않는다

"""
def trash_shared_restore(request,*args,**kwargs):
	"""공유 폴더에 있는 객체를 휴지통에서 복원한다.


	:URL: https://api.server.com/api/1/trash/restore/<name>/from_shared/<path>


	:Version: 1


	:Method: POST


	:param name: 필수 사항. 휴지통 안에 있는 파일의 이름


	:param path: 필수 사항. 공유된 폴더의 경로.


	:param overwrite: 선택 사항 (기본적으로 1로 설정되어 있다.) 복원할 폴더 또는 파일이 사용자 파일 저장소에 이미 존재하고 이 파라미터가 0으로 설정되어 있으면 http Exception에 의해 코드 403이 보여진다.


	:Note: 이 메소드는 동시에 일어날 수 없다.

"""