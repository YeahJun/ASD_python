# -*- coding: utf-8 -*-

def admin_accounts_find_users(request,*args,**kwargs):
	"""지정된 매개 변수가 있는 사용자 목록을 반환한다. (관리자만 사용 가능.)


	:URL: https://api.server.com/api/1/admin/accounts_find_users/


	:Version: 1


	:Method: POST


	:param user_id: 선택 사항. 정보를 찾아야 하는 사용자의 ID.


	:param registration_date_from and registration_date_to: 선택 사항. 사용자 등록 기간. 매개 변수가 주어진 경우 등록된 사용자 목록을 반환한다. 매개 변수를 하나 또는 둘로 전송할 수 있다.


	:param login: 선택 사항. 사용자 로그인.


	:param name: 선택 사항. 사용자 이름.


	:param last_login_from and last_login_to: 선택 사항. 사용자를 검색하는 기간. 매개 변수를 하나 또는 둘로 전송할 수 있다.


	:param storage_size_from and storage_size_to: 선택 사항. 사용자가 검색하는 저장소의 크기. 매개 변수를 하나 또는 둘로 전송할 수 있다.


	:param is_active: 선택 사항. Active/inactive 사용자.


	:param has_region: 선택 사항. 사용자 계정이 영역(region)을 갖고 있는 경우 True/False로 표시.


	:param region: 선택 사항. 영역 이름.


	:param role: 선택 사항. 사용자 역할. (관리자/사용자)


	:param company_name: 선택 사항. 회사 이름.


	:param company_id: 선택 사항. 회사 ID.


	:param is_deleted: 선택 사항.


	:param deleted_date: 선택 사항.


	:param block_date: 선택 사항.


	:param limit: 선택 사항. Record의 양 제한. 최대값은 백엔드 구성에 의해 제한된다(기본값은 2000).


	:param offset: 선택 사항. 목록의 처음부터 오프셋.


	:param order_field: 선택 사항. 사용자 목록(속성에서 선택한 항목)을 정렬한다. (사용자 특징에 따라 선택된다.)


	:param order_direction: 선택 사항. 정렬 순서(오름차순/내림차순).


	:Return: 레코드 양(합계), 레코드 제한(제한), 사용자 목록(사용자들), 레코드 목록(오프셋)
	"""
def admin_accounts_disable(request,*args,**kwargs):
	"""사용자 계정 비활성에 도움을 준다.


	:URL: https://api.server.com/api/1/admin/accounts_disable/


	:Version: 0, 1


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID.


	:param reason: 필수 사항. 비밀번호 변경 이유.


	:Return: 사용자 정보.

"""
def admin_accounts_enable(request,*args,**kwargs):
	"""사용자 계정 활성에 도움을 준다.


	:URL: https://api.server.com/api/1/admin/accounts_enable/


	:Version: 1


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID.


	:param reason: 필수 사항. 비밀번호 변경 이유.


	:Return: 사용자 정보.

"""
def admin_accounts_set_password(request,*args,**kwargs):
	"""사용자 암호를 변경한다.


	:URL: https://api.server.com/api/1/admin/accounts_set_password/


	:Version: 1


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID.


	:param new_password: 선택. 새로운 비밀번호.


	:Return: 사용자 정보.

"""