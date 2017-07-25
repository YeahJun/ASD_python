def check_ws(request, *args, **kwargs):
	"""WebSocket을 확인한다.


	:URL : https://api.server.com/api/0/check_ws/


	:Version : 0


	:Method : GET, POST


	:param :없음.


	:Return : 성공 또는 실패


	:Error : 없음.

"""
def events(request, *args, **kwargs):
	"""날짜별로 내림차순으로 정렬된 사용자 이벤트 목록을 반환한다.


	:URL : https://api.server.com/api/0/events/


	:Version : 0


	:Method : GET


	:param :• skip: 선택 사항. 초기 데이터 오프셋. 이 method는 page-by-page 디스플레이를 구성한다.


	:Return : 이벤트 집합.


	:Return : • type: 이벤트 유형. See below.


	"""
	def notices(request, *args, **kwargs):
	"""시간별로 필터링 된 사용자 알림 목록을 내림차순으로 반환한다.


	:URL : https://api.server.com/api/0/notices/


	:Version : 0


	:Method : GET


	:param :• type: 선택 사항. 알림 유형으로 필터링.


	:Return : 알림 집합.


	:Error :

"""