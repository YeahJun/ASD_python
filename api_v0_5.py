# -*- coding: utf-8 -*-

def admin_account_generate_login_key(request,*args,**kwargs):
	"""시스템에 접근하기 위한 임시 키를 생성한다. 키는 /accounts/login method를 통해 시스템에 접근하기 위해 전송된다.


	:URL: https://api.server.com/api/0/admin/accounts_generate_login_key/


	:Version: 0


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID.


	:Return: 사용자 ID, 접근 키.
	"""
def admin_set_effective_userid(request,*args,**kwargs):
	"""토큰에 대해 효율적인 user_id를 설정한다.


	:URL: https://api.server.com/api/0/admin/set_effective_userid/


	:Version: 0


	:Method: POST


	:param euser_id: 필수 사항. 사용자 ID.


	:param token: 필수 사항. user_id를 변경해야 하는 사용자의 토큰.


	:Return: 사용자 정보.

"""
def assign_role(request,*args,**kwargs):
	"""사용자의 역할을 변경한다.


	:URL: https://api.server.com/api/0/admin/assign_role/


	:Version: 0


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID.


	:param role: 필수 사항. 사용자의 새로운 역할.


	:Return: 사용자 정보.

"""
def accounts_delete(request,*args,**kwargs):
	"""사용자 계정을 삭제한다.


	:URL: https://api.server.com/api/0/admin/accounts_delete/


	:Version: 0


	:Method: POST


	:param user_id: 선택 사항. 사용자 ID.


	:param immediately: 필수 사항. 실제 전송 시 모든 사용자 데이터를 완전히 삭제한다.


	:param migrate_file: 필수 사항. 사용자가 삭제될 경우, 파일이 다른 사용자에게 이동한다.


	:param migrate_login: 선택 사항. 마이그레이션할 때, 해당 사용자가 파일을 받게 된다.


	:Return: 사용자 정보.

"""
def accounts_restore(request,*args,**kwargs):
	"""완전히 제거되지 않은 계정을 복원한다.


	:URL: https://api.server.com/api/0/admin/accounts_restore/


	:Version: 0


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID.


	:Return: 사용자 정보.

"""
def invite_user(request,*args,**kwargs):
	"""초대 이메일을 전송한다.


	:URL: https://api.server.com/api/0/admin/invite_user/


	:Version: 0


	:Method: POST


	:param email: 필수 사항. 초대될 사용자의 이메일.


	:param invitation: 초대 텍스트.


	:Return: 사용자 정보.

"""