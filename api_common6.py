# -*- coding: utf-8 -*-

def files_download_extra(request,*args,**kwargs):
	""" """
def files_extra_create(request,*args,**kwargs):
	"""지정된 파일에 대한 extradata을 생성한다. 이는 실시간으로 생성되거나 대기열에서 지연될 수 있다; 이는 특정 유형의 extradata를 생성할 책임이 있는 플러그 인 설정에 따라 달라진다. 이론적으로, 하나의 파일에 대해 여러 종류의 extradata가 있다면, 이러한 모든 유형의 데이터가 생성될 것이다. 당신은 extradata를 생성할 일부 플러그 인을 선택할 수 없다. 만약 어떤 파일들이 이미 extradata를 가지고 있다면, 이들은 한번 더 생성될 것이다.


	:URL: https://api.server.com/api/0/files/create_extra/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. Extradata가 생성된 파일의 경로


	:param version: 선택 사항. 파일 버전 넘버.


	:Return: 시작: extradata가 생성을 위해 대기하고 있을 때 True로 설정한다. (플러그 인에 따라 다름). 대기중인 작업이 없으면 False로 설정한다.


	:Error 404: 지정된 경로의 파일을 찾을 수 없다. 또는 존재하지 않는 파일 버전을 입력했다.

"""
def links_download_extra(request,*args,**kwargs):
	""" """
def links_extra_create(request,*args,**kwargs):
	"""특정 파일에 대한 extradata를 생성한다. 이 method는 API method /files/create_extra와 비슷한 데, 공용 파일을 위한다는 차이점이 있다.


	:URL: https://api.server.com/api/0/links/create_extra


	:Version: 0


	:Method: POST


	:param hash: 필수 사항. 객체를 검색하는 ID의 일종인 게시된 객체의 해시


	:param path: 선택 사항. 게시된 디렉터리와 관련된 파일이나 폴더의 경로


	:Return: 시작: extradata가 생성을 위해 대기하고 있을 때 True로 설정한다. (플러그 인에 따라 다름). 대기중인 작업이 없으면 False로 설정한다.


	:Error 404: 객체를 찾을 수 없다. 예상 이유: 경로가 잘못 입력되었다. 객체가 옮겨졌거나 삭제되었다.

"""
def shares_create_extra(request,*args,**kwargs):
	"""지정된 파일에 대한 extradata을 생성한다. 이는 실시간으로 생성되거나 대기열에서 지연될 수 있다; 이는 특정 유형의 extradata를 생성할 책임이 있는 플러그 인 설정에 따라 달라진다. 이론적으로, 하나의 파일에 대해 여러 종류의 extradata가 있다면, 이러한 모든 유형의 데이터가 생성될 것이다. 당신은 extradata를 생성할 일부 플러그 인을 선택할 수 없다. 만약 어떤 파일들이 이미 extradata를 가지고 있다면, 이들은 한번 더 생성될 것이다.


	:URL: https://api.server.com/api/1/shares/create_extra/


	:Version: 1


	:Method: POST


	:Headers MountbitAuth: 권한이 있는 사용자의 토큰. 공유된 폴더가 공용이면, 이 매개 변수는 선택 사항이다.


	:param invite_hash: 필수 사항. 공유 폴더에 사용자를 초대하는 고유한 해시. 해시 결과는 method /folders/shared/add/에서 얻음.


	:param path: 필수 사항. 게시된 폴더와 관련된 파일의 경로.


	:Return 시작: extradata가 생성을 위해 대기하고 있을 때 True로 설정한다. (플러그 인에 따라 다름). 대기중인 작업이 없으면 False로 설정한다.


	:Error 403: 공유 폴더 액세스 권한이 없다.


	:Error 404: 지정된 폴더를 찾을 수 없다.

"""