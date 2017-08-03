# -*- coding: utf-8 -*-

def list_albums(request,*args,**kwargs):
	"""사용자 앨범을 나열한다.


	:URL: https://api.server.com/api/1/albums/


	:Version: 1


	:Method: GET


	:Header MountbitAuth: 사용자 인증 토큰.


	:param offset: 리스트의 시작부터 얼만큼 떨어져 있는지를 보여주는 오프셋.


	:param limit: 반환되는 앨범의 수 (최대 2000).


	:Return: 사용자 앨범 리스트.
	"""
def create_album(request,*args,**kwargs):
	"""새로운 앨범을 생성한다.


	:URL: https://api.server.com/api/1/albums/create/


	:Version: 1


	:Method: POST

	:Header MountbitAuth: 사용자 인증 토큰.


	:param name: 선택 사항. 앨범의 이름. 지정된 이름이 없으면 자동으로 이름을 생성해준다.


	:Return: 앨범 정보.


	:Error 403: 동일한 이름의 앨범이 존재한다. 
	"""
def create_album(request,*args,**kwargs):
	"""새로운 앨범을 생성한다.


	:URL: https://api.server.com/api/1/albums/create/


	:Version: 1


	:Method: POST

	:Header MountbitAuth: 사용자 인증 토큰.


	:param name: 선택 사항. 앨범의 이름. 지정된 이름이 없으면 자동으로 이름을 생성해준다. 


	:Return: 앨범 정보.


	:Error 403: 동일한 이름의 앨범이 존재한다. 
	"""
def list_files(request,*args,**kwargs):
	"""앨범의 내용 리스트를 반환한다.


	:URL: https://api.server.com/api/1/albums/<album_id>/


	:Version: 1


	:Method: GET


	:Header MountbitAuth: 사용자 인증 토큰. 만약 공개 앨범이면, 매개 변수는 선택 사항.


	:param offset: 리스트의 처음에서 떨어진 오프셋.


	:param limit: 반환되는 앨범의 개수(최대 2000개).


	:Return: 앨범의 총 파일 수 및 각 파일의 데이터 목록에 대한 정보


	:Error 404: 앨범을 찾을 수 없다.
	"""
def add_files(request,*args,**kwargs):
	"""앨범에 파일을 추가한다.


	:URL: https://api.server.com/api/1/albums/<album_id>/add_files/


	:Version: 1


	:Method: POST


	:Header MountbitAuth: 사용자 인증 토큰. 만약 공개 앨범이면, 매개변수는 선택 사항.


	:param paths: 사용자 홈 디렉토리와 관련된 파일의 경로 목록.


	:Return: 각 파일 경로에 대한 각 추가 상태의 목록.


	:Error 404: 앨범을 찾을 수 없다. 
	"""
def make_public(request,*args,**kwargs):
	"""모든 사용자들에게 앨범을 공유한다.


	:URL: https://api.server.com/api/1/albums/<album_id>/make_public/ 


	:Version: 1


	:Method: POST


	:Header MountbitAuth: 사용자 인증 토큰.


	:param: 없음.


	:Return: 앨범 정보.


	:Error 404: 앨범을 찾을 수 없다. 
	"""
def get_file_url(request,*args,**kwargs):
	"""파일 다운로드 URL 을 받는다.


	:URL: https://api.server.com/api/1/albums/<album_id>/<file_hash>/ 


	:Version: 1


	:Method: GET


	:Header MountbitAuth: 사용자 인증 토큰. 만약 공개 앨범이면, 매개변수는 선택 사항


	:param for_view: 플래그. 1로 설정이 되어있으면, 웹 브라우저에서 볼 수 있는 링크를 반환하고, 그 외의 경우에는 다운로드 받을 수 있는 링크를 반환한다.


	:Return: 파일 다운로드에 필요한 정보.


	:Error 403: 현재 권한으로 앨범에 접근할 수 없다.


	:Error 404: 앨범 또는 파일을 찾을 수 없다.
	"""
def get_file_url(request,*args,**kwargs):
	"""파일 다운로드 URL을 받는다.


	:URL: https://api.server.com/api/1/albums/<album_id>/<file_hash>/ 


	:Version: 1


	:Method: GET


	:Header MountbitAuth: 사용자 인증 토큰. 만약 공개 앨범이면, 매개변수는 선택 사항.


	:param: 없음.


	:Return: 파일 다운로드에 필요한 정보.


	:Error 403: 현재 권한으로 앨범에 접근할 수 없다.


	:Error 404: 앨범 또는 파일을 찾을 수 없다.
	"""
def get_file_info(request,*args,**kwargs):
	"""하나의 파일에 대한 정보를 가져온다.


	:URL: https://api.server.com/api/1/albums/<album_id>/<file_hash>/info/ 


	:Version: 1


	:Method: GET 


	:Header MountbitAuth: 사용자 인증 토큰. 만약 공개 앨범이면, 매개변수는 선택 사항


	:param: 없음.


	:Return: 파일 정보.


	:Error 403: 현재 권한으로 앨범에 접근할 수 없다.


	:Error 404: 앨범 또는 파일을 찾을 수 없다.
	"""
def create_extra(request,*args,**kwargs):
	"""지정된 파일에 대한 강제 기록 생성. 실시간 생성이거나 큐를 통해 딜레이가 있을 수 있다. 특정 유형의 추가 데이터 생성을 담당하는 플러그인 설정에 따라 다르다. 이론적으로, 한 파일에 대해 여러 유형의 추가 데이터가 있으면 모든 유형이 만들어진다. 추가 자료를 만들 플러그인을 선택할 수 있다. 여러 추가 데이터 플러그인이 하나의 파일에 해당하는 상황은 아직 구현 되지 않을 수 있다는 점을 언급해야 한다. 일부 파일에 이미 일부 외부 데이터가 있는 경우 다시 만들어진다.


	:Version: 1


	:Method: POST 


	:Header MountbitAuth: 사용자 인증 토큰. 만약 공개 앨범이면, 매개변수는 선택 사항.


	:param: 없음.


	:Return: Extra data 가 생성을 위해서 큐에 들어가 있으면 true 를 반환한다. 그렇지 않으면 false 를 반환한다


	:Error 403: 현재 권한으로 앨범에 접근할 수 없다.


	:Error 404: 앨범 또는 파일을 찾을 수 없다.

"""