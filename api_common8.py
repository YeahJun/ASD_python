# -*- coding: utf-8 -*-

def get_set_key(request,*args,**kwargs):
	"""지정된 key 값을 설정한다.


	:URL: https://api.server.com/api/0/keyvalue/<key_name>


	:Version: 0


	:Method: GET/POST


	:param value: POST 요청에 대한 새로운 key 값 (문자열이나 JSON).


	:param rights: key에 대한 권한.


	:Return: GET 요청에 대한 key 값


	:Error 404: key를 찾을 수 없다.

	"""