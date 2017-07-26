# -*- coding: utf-8 -*-

def get_result(request,*args,**kwargs):
	"""비동기 API 메소드의 성능 상태를 수신하는 데 도움을 준다


	:URL: https://api.server.com/api/0/task/<task_id>/


	:Version: 0


	:Method: GET


	:param task_id: 필수. 백그라운드 작업의 ID


	:Return: 임의의 ‘JSON’ 사전, 즉, 실행이 끝날 때 사전에 추가된 데이터


	:Error 404: 백그라운드 작업을 찾을 수 없다.


	:Error 400: 백그라운드 작업을 작동시키는 중에 에러가 발생한다.

"""