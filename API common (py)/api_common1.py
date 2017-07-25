def get_data(request, *args, **kwargs):
	"""측정 항목에 대한 정보를 반환한다 


	:URL : https://api.server.com/api/0/analytics/get_data/


	:Version : 0


	:Method : GET


	:param :• token: 인증 토큰


	:Return : 측정 항목 값


	:Error : • 404 – 키를 찾을 수 없다. 


	:Note : • 이 메소드는 사용자가 관리자 권한을 가지는 것을 필요로 한다. 


	"""
	def get_metrics(request, *args, **kwargs):
	"""https://api.server.com/api/0/analytics/get_metrics/ 


	:Version : 0 


	:Method : GET


	:Return : 매개 변수를 포함한 측정 항목 메소드 


	:Note : • 이 메소드는 사용자가 관리자 권한을 가지는 것을 필요로 한다. 


	"""
	def get_multiple_data(request, *args, **kwargs):
	"""주어진 매트릭스 목록을 기준으로 매트릭스 데이터를 반환한다.


	:URL : https://api.server.com/api/0/analytics/get_multiple_data/


	:Version : 0


	:param :• date_from – 타임스탬프 간격


	:Return : 측정 항목으로 그룹이 된 측정 항목의 리스트 


	:Note : 관리자 권한이 필요하다.


	"""