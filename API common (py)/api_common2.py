def get_updates(request, *args, **kwargs):
	"""현재 가능한 업데이트를 반환한다.


	:URL : https://api.server.com/api/0/soft/get_update/ 


	:Version : 0


	:Method : GET


	:param :• platform: 필수 사항. 플랫폼 타입 (윈도우 또는 맥).


	:Return : 주어진 플랫폼에서 현재 가능한 업데이트에 대한 설명이 반환된다.


	:Error : • 403: 존재하지않는 플랫폼에 대한 업데이트가 요청되었다. 


	:Note : Describes a current available update for the given platform.


	"""
	def get_version(request, *args, **kwargs):
	"""특정 플랫폼에 대한 현재 클라이언트의 앱 버전을 반환한다.


	:URL : https://api.server.com/api/0/soft/get_version/


	:Version : 0 


	:Method : GET


	:param :platform: 선택 사항. 플랫폼 타입. 만약에 파라미터가 설정이 되면, 메소드는 특정 플랫폼에 대한 버전 리스트를 반환한다. 그렇지 않으면 모든 플랫폼에 대한 버전 리스트가 반환된다. 


	:Return : 특정 플랫폼에 대한 버전 리스트 객체 


	:Error : • 403: 존재하지 않는 플랫폼에 대한 버전을 요청한다.


	"""
	def list_updates(request, *args, **kwargs)ㅁ:
	"""모든 플랫폼 또는 특정 플랫폼에 대한 업데이트 리스트를 반환한다. (관리자만 사용할 수 있다.)


	:URL :  https://api.server.com/api/0/soft/list_updates/ 


	:Version : 0


	:param :• platform: 선택 사항. 플랫폼 유형. 매개 변수가 설정되면 메서드는 특정 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 리스트가 반환된다.


	:Return : 업데이트 리스트 

"""
def list_versions(request, *args, **kwargs):
	"""모든 플랫폼 또는 특정 플랫폼에 대한 버전 리스트를 반환한다.


	:URL : https://api.server.com/api/0/soft/list_version/


	:Version : 0 


	:Method : GET


	:param :선택 사항. 플랫폼 유형. 매개 변수가 설정되면 메서드는 특정 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 리스트가 반환된다.


	:Return : 시간에 대한 내림차순으로 된 버전의 리스트

"""
def set_update(request, *args, **kwargs):
	"""특정 플랫폼에 새로운 업데이트를 설치한다.


	:URL : https://api.server.com/api/0/soft/set_update/


	:Version : 0 


	:Method : GET


	:param :• platform: 필수 사항. 플랫폼 타입


	:Return : 특정 플랫폼에 대한 버전 리스트 객체


	:Error : • 403: 존재하지 않는 플랫폼에 대한 버전을 요청한다. 


	"""
	def set_version(request, *args, **kwargs):
	"""지정된 플랫폼에 대해 현재 클라이언트 응용 프로그램 버전을 새로 설정하거나 업데이트한다.


	:URL : https://api.server.com/api/0/soft/set_version/


	:Version : 0 


	:Method : GET


	:param :• platform: 필수 사항. 플랫폼 타입.


	:Error : • 403: 존재하지 않는 플랫폼에 대한 버전을 요청한다. 


	"""