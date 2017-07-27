# -*- coding: utf-8 -*-

def group_create(request,*args,**kwargs):
	"""새 그룹 생성을 생성한다. 회사 관리자 권한이 필요하다.


	:URL: https://api.server.com/api/1/groups/create/


	:Version: 1


	:Method: POST


	:param name: 새로운 그룹의 이름


	:Return 200: 그룹 생성을 완료했다.


	:Return 403: 그룹이 이미 존재한다.


	:Return 404: 회사를 찾을 수 없다.

"""
def group_delete(request,*args,**kwargs):
	"""이름과 회사로 그룹을 삭제한다. 회사 관리자 권한이 필요하다.


	:URL: https://api.server.com/api/1/groups/delete/


	:Version: 1


	:Method: POST


	:param name: 새로운 그룹의 이름


	:Return 200: 그룹 생성을 완료했다.


	:Return 403: 그룹이 이미 존재한다.


	:Return 404: 회사를 찾을 수 없다.

"""
def group_list(request,*args,**kwargs):
	"""회사의 그룹 목록을 보여준다.


	:URL: https://api.server.com/api/1/groups/list/


	:Version: 1


	:Method: POST, GET


	:param offset: 선택 사항. 오프셋 값


	:param limit: 선택 사항. 제한된 아이템의 수


	:param order_by: 선택 사항. 기본 값: ‘name’. 정렬 필드와 순서, 역 방향 정렬 순서에 대한 음수 값 설정. 예상 값: ‘name’, ‘:name’, ‘members_count’, ‘:members_count’


	:Return groups: 회사 그룹 목록, 각 레코드는


	:Return group_id: 그룹의 ID


	:Return name: 그룹의 이름


	:Return company_id: 회사 ID


	:Return members_count: 그룹 멤버의 수


	:Return limit: 목록 제한


	:Return offset: 목록 오프셋


	:Return count: 모든 그룹의 수

	:Error 404: 회사를 찾을 수 없다.

"""
def group_change(request,*args,**kwargs):
	"""그룹의 설정을 변경한다. 회사 관리자 권한이 필요하다.


	:URL: https://api.server.com/api/1/groups/<group_id>/change/


	:Method: POST


	:param group_id: 필수 사항. URL 로부터 가져온 그룹 ID


	:param name: 필수 사항. 그룹 이름


	:Return group_id: 그룹 식별자


	:Return name: 그룹 이름


	:Return company_id: 그룹 회사 식별자


	:Return members_count: 그룹 멤버의 수

	:Error 403: 사용자에게 그룹을 변경할 권한이 없다.


	:Error 403: 그룹이 이미 존재한다.


	:Error 404: 주어진 ID로 그룹을 찾을 수 없다.

"""
def group_add_user(request,*args,**kwargs):
	"""그룹에 사용자를 추가한다.


	:URL: https://api.server.com/api/1/groups/<group_id>/add_user/


	:Version: 1


	:Method: POST


	:param group_id: 필수 사항. 그룹 ID (URL로부터 가져온 그룹 ID)


	:param user_ids: 필수 사항. 사용자 ID 목록


	:Return: 정보와 함께 추가된 사용자 목록, 또는 실패 코드

	:Error 403: 다른 회사 소속이다.


	:Error 404: 그룹을 찾을 수 없다.

"""
def group_remove_user(request,*args,**kwargs):
	"""그룹에서 사용자를 삭제한다.


	:URL: https://api.server.com/api/1/groups/<group_id>/remove_user/


	:Version: 1


	:Method: POST


	:param group_id: 필수 사항. 그룹 ID (URL로부터 가져온 그룹 ID)


	:param user_ids: 필수 사항. 사용자 ID 목록


	:Return: 정보와 함께 제거된 사용자의 목록 또는 실패 코드


	:Error 403: 다른 회사 소속이다.


	:Error 404: 그룹을 찾을 수 없다.

"""
def group_users(request,*args,**kwargs):
	"""그룹 멤버의 목록을 보여준다.


	:URL: https://api.server.com/api/1/groups/<group_id>/users/


	:Version: 1


	:Method: POST, GET


	:param group_id: 필수 사항. 그룹 ID (URL로부터 가져온 그룹 ID)


	:param offset: 선택 사항. 오프셋 값


	:param limit: 선택 사항. 제한된 아이템 수


	:Return users: 사용자들 목록


	:Return limit: 제한된 목록 수


	:Return offset: 목록 오프셋


	:Return count: 모든 그룹의 수


	:Error 403: 다른 회사 소속이다.


	:Error 404: 그룹을 찾을 수 없다.
	"""
