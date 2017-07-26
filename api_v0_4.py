# -*- coding: utf-8 -*-

def accounts_create(request,*args,**kwargs):
	"""새로운 시스템을 등록한다.


	:URL: https://api.server.com/api/0/accounts/create/


	:Version: 0


	:Method: POST


	:param email: 필수 사항. 이메일 주소


	:param password: 필수 사항. 최대 256 byte크기의 비밀번호.


	:param name: 필수 사항. 최대 256 byte 크기의 이름.


	:param company_name: 선택 사항. 회사 이름이.


	:param company_plan: 선택 사항. 회사 계획.


	:param invite_hash: 선택 사항. 초대 토큰. 기존 사용자가 아직 등록되지 않은 사용자의 폴더를 공유하면 시스템은 자동으로 새 사용자를 생성하고 ‘invite_hash’를 생성한다. 그러면 시스템이 새 사용자의 이메일로 해시 메시지를 전송한다. 사용자가 해당 링크를 따라가면 사용자가 자동으로 시스템에 등록된다. 사용자는 자신의 이메일 주소를 확인할 필요가 없다.


	:Return: 로그인 정보 (자격증)


	:Error 403: 이 이메일 주소의 사용자가 이미 시스템에 등록되어 있다.

	"""
def accounts_login(request,*args,**kwargs):
	"""인증 토큰은 반환한다.


	:URL: https://api.server.com/api/0/accounts/login/


	:Version: 0


	:Method: POST

	:param email: 선택 사항. 이메일 주소.


	:param password: 선택 사항. 비밀번호.


	:param key: 선택 사항. Technique /account/generate_login_key를 사용한 초기 인증 토큰.


	:param permanent_auth: 선택 사항. 기본적으로, Boolean 값은 false로 설정되어 있다. 토큰 요청은 제한된 기간 내에 유효하다. True로 설정하면 영구 토큰이 전송된다.


	:param device_description: 선택 사항. 사용자가 로그인하는 기계에 대한 설명. 만약 필드가 비어있고 영구 토큰이 요청되면 ‘<로그인 날짜> + <사용자 에이전트>’ 값이 반환된다.


	:Return: 인증 토큰. 이 토큰은 서비스에 대한 모든 향후 요청에서 Mountbit:Auth 헤더로 삽입해야 한다.


	:Error 403: 이 이메일 주소의 사용자가 이미 시스템에 등록되어 있다.
	"""
def get_invited(request,*args,**kwargs):
	"""초대 토큰에 따라 사용자 이메일을 반환한다.


	:URL: https://api.server.com/api/0/accounts/getinvited/


	:Version: 0


	:Method: GET


	:param hash: 필수 사항. 초대 토큰.


	:Return: 초대장을 보낸 사용자 이메일.


	:Error 404: 해당 초대 토큰을 가진 사용자를 찾을 수 없다.

"""
def accounts_get(request,*args,**kwargs):
	"""사용자의 계정 정보를 반환한다.


	:URL: https://api.server.com/api/0/accounts/get/


	:Version: 0


	:Method: GET


	:param user_id: 선택 사항. 사용자의 ID. 매개 변수가 생략되었거나 권한이 위임된 사용자가 아닌 경우 권한이 부여된 사용자에 대한 정보가 반환된다. 매개 변수를 입력하고 관리자가 method를 호출하면 지정된 사용자에 대한 정보가 반환된다.


	:Return: 사용자의 계정 정보.


	:Error 404: 해당 초대 토큰을 가진 사용자를 찾을 수 없다.
	"""
def accounts_recover_lost_password(request,*args,**kwargs):
	"""이 이메일과 관련된 계정에 임시로 접근하는데 필요한 메시지를 이메일로 전송한다. 임시 링크는 24시간 동안 유효하다.


	:URL: https://api.server.com/api/0/accounts/recover_lost_password/


	:Version: 0


	:Method: POST


	:param email: 필수 사항. 암호를 승인한 다음 암호를 변경하는 데 사용되는 메시지.


	:Error 400: 이 이메일을 가진 사용자를 시스템에서 찾을 수 없다.

"""
