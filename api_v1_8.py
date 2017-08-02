# -*- coding: utf-8 -*-

def add_email_view(*args,**kwargs):
	"""새 이메일을 사용자 계정에 추가한다. 사용자는 이메일을 확인한 후 새로운 이메일을 통해 다시 로그인할 수 있다.

	:Class: EmailPasswordAuth(name,messages=None,**kwargs)

	:URL: https://api.server.com/api/1/accounts/add_email/


	:Version: 1


	:Method: POST


	:param email: 필수 사항. 이메일 주소.


	:Return: 로그인 정보(자격)

	"""
def create_view(*args,**kwargs):
	"""새로운 시스템을 등록한다.

	:Class: EmailPasswordAuth(name,messages=None,**kwargs)

	:URL: https://api.server.com/api/1/accounts/create/


	:Version: 1


	:Method: POST


	:param email: 필수 사항. 이메일 주소.


	:param password: 필수 사항. 비밀번호. 최대 256 Bytes.


	:param name: 필수 사항. 이름. 최대 256 Bytes.


	:param invite_hash: 선택 사항. 초대 토큰. 기존 사용자가 아직 등록되지 않은 사용자의 폴더를 공유하면 시스템은 자동으로 새 사용자를 생성하고, ‘invite_hash’를 생성한다. 그러면 시스템이 새 사용자의 이메일로 해시 메시지를 전송한다. 사용자가 해당 링크를 따라가면 자동으로 시스템에 등록된다.


	:Return: 로그인 정보(자격)


	:Error 403: 이미 시스템에 등록되어 있는 이메일 주소이다.
	"""
def kt_get_account(*args,**kwargs):
	"""KT 시스템에서 승인 정보를 반환한다.

	:Class: EmailPasswordAuth(name,messages=None,**kwargs)

	:URL: https://api.server.com/api/1/accounts/kt_get_account/


	:Version: 1


	:Method: GET


	:param email: 필수 사항. 이메일 주소.


	:Return: 사용자 정보.


	:Error 403: 이미 시스템에 등록되어 있는 이메일 주소이다.
	"""
def add_phone_view(*args,**kwargs):
	"""새 전화 번호를 사용자 계정에 추가한다. 사용자는 새 전화 번호를 확인한 후 인증을 받을 수 있다.


	:Class: PhoneAuth(name,messages=None,**kwargs)

	:URL: https://api.server.com/api/1/accounts/add_phone/


	:Version: 1


	:Method: POST


	:param phone: 전화번호.


	:Return: 사용자 정보.


	:Error 403: 이미 시스템에 등록되어 있는 이메일 주소이다.

	"""
def create_view(*args,**kwargs):
	"""새로운 계정을 추가한다.

	:Class: PhoneAuth(name,messages=None,**kwargs)


	:URL: https://api.server.com/api/1/accounts/create_by_phone/


	:Version: 1


	:Method: POST


	:param phone: 필수 사항. 국제 번호 형식의 전화 번호.


	:param password: 필수 사항. 비밀번호. 최대 256 Bytes.


	:param name: 필수 사항. 이름. 최대 256 Bytes.


	:param invite_hash: 선택 사항. 초대 토큰. 기존 사용자가 아직 등록되지 않은 사용자의 폴더를 공유하면 시스템은 자동으로 새 사용자를 생성하고, ‘invite_hash’를 생성한다. 그러면 시스템이 새 사용자의 이메일로 해시 메시지를 전송한다. 사용자가 해당 링크를 따라가면 자동으로 시스템에 등록된다.


	:Return: 사용자 정보.


	:Error 403: 이미 시스템에 등록되어 있는 이메일 주소이다.

"""
def login_view(*args,**kwargs):
	"""인증 토큰은 반환한다.

	:Class: PhoneAuth(name,messages=None,**kwargs)


	:URL: https://api.server.com/api/1/accounts/login_by_phone/


	:Version: 1


	:Method: POST


	:param phone: 필수 사항. 국제 번호 형식의 전화 번호.


	:param password: 필수 사항. 비밀번호. 최대 256 Bytes.


	:param permanent_auth: 선택 사항. 기본적으로 Boolean 값이 False로 설정되어 있다. 즉, 제한된 기간 내에 토큰 요청이 유효하다. True로 설정하면 영구 토큰이 전송된다.


	:param device_description: 선택 사항. 사용자가 로그인하는 디바이스에 대한 설명. 필드가 비어 있고 영구 토큰이 요청된 경우 <로그인 날짜> + <사용자 에이전트>로 값을 반환한다.


	:Return: 인증 토큰. 토큰은 서비스에 대한 모든 요청에서 헤더 Mountbit:Auth로 삽입.


	:Error 403: 이미 시스템에 등록되어 있는 이메일 주소이다.
	"""
def generate_login_key_view(*args,**kwargs):
	"""짧은 기간동안 /etc/ssh/sshd_config를 통해 실시간 인증 토큰을 가져오는 데 도움이 되는 임시 키 토큰을 반환한다.

	:Class: TempKeyAuth(name,**kwargs)

	:URL: https://api.server.com/api/1/accounts/generate_login_key/


	:Version: 0, 1


	:Method: POST


	:param: 없음.


	:Return: 실제 승인 토큰을 수신하는 데 사용되는 임시 키.

	"""
def login_view(*args,**kwargs):
	"""임시 권한 토큰을 반환한다.

	:Class: TempKeyAuth(name,**kwargs)

	:URL: https://api.server.com/api/1/accounts/login_by_key/


	:Version: 1


	:Method: POST


	:param key: Method/accounts/generate_login_key를 통해 수신된 임시 승인 키


	:Return: 실제 승인 토큰을 수신하는 데 사용되는 임시 키.
	"""
def oauth_confirm(*args,**kwargs):
	"""
	인증 토큰을 반환한다. 이 method는 사용자가 백엔드에서 사용자의 인증을 완료할 수 있도록 모바일 운영자 웹 사이트에 성공적으로 인증된 후 호출되어야 한다.
	
	:Class: oAuth(name,service_name,consumer_key,consumer_secret,request_token_url,access_token_url,authorize_url,base_url,host,signature_method='HMAC:SHA1',messages=None,**kwargs)

	:URL: https://api.server.com/api/1/accounts/oauth_confirm/


	:Version: 1


	:Method: POST


	:param Oauth_token: 필수 사항. OAuth 서비스에 대한 첫 번째 요청에 의해 발급된 토큰.


	:param Oauth_verifier: 필수 사항. OAuth 서비스에 대한 완전한 권한 부여 절차 후에 영구적 토큰 수신.


	:Return: 인증 토큰. 서비스에 대한 모든 후속 요청에서 헤더 형식으로 대체.


	:Error 403: 작업을 사용할 수 없다. (예: 첫 번째 성공적인 통화 후에 이 API method를 두 번 째로 호출할 때)


	:Error 424: 화이트 밸런스 기능이 활성화된 경우에만 발생하며, 허용되는 권한 중 하나가 없는 경우에만 오류가 발생한다.


	:Error 503: 셀룰러 연산자 서비스를 사용할 수 없다.
	"""
def oauth_url(*args,**kwargs):
	"""Megafon 서버의 인증 URL을 반환한다.


	:URL: https://api.server.com/api/1/accounts/oauth_url/


	:Version: 0, 1


	:Method: Oauth_callback이 통과되지 않으면 기본 값은 백엔드 설정에서 가져온다.


	:param Clien_id: 선택 사항. 모바일 운영자 사이트에서 성공적으로 인증한 후 다시 연결할 리소스의 URL이 구성에서 선택.


	:param Permanent_auth: 선택 사항. 기본 값은 False이며, 제한된 수명을 가진 토큰 요청. True이면 영구 토큰 발급.


	:param Device_desciption: 선택 사항. 로그인이 발생한 장치에 대한 설명, 필드가 비어 있고 영구 토큰이 요청된 경우, 값은 ‘<로그인 날짜> + <사용자 에이전트>’ 형식으로 표기.


	:Return: Megafon 사이트의 승인 페이지 주소(이후 로그인을 위해 사용자를 리디렉션 해야함.)


	:Error 503: 셀룰러 연산자 서비스를 사용할 수 없다.
	"""
def oauth_confirm(*args,**kwargs):
	"""인증 토큰을 반환한다.

	:Class: GoogleAuth(name,service_name,client_id,client_secret,access_token_url,authorize_url,base_url,messages=None,callback_url=None,**kwargs)

	:URL: https://api.server.com/api/1/accounts/google_confirm/


	:Version: 1


	:Method: POST


	:param code: 선택 사항. oAuth 제공자에 대한 임시 액세스 코드.


	:param state: 필수 사항. 영구 인증에 사용되는 추가 매개 변수가 포함된 문자열. Value는 json dictionary에 보내 진다. Value의 예: {“permanent_auth”:+false,+”device_description”:+null,+”need_to_stop_auth”:+false}


	:param token: 선택 사항. 모바일 장치가 이미 로그인 되어 있는 경우 Google oAuth의 승인 토큰 존재.


	:Note: Google 웹 사이트에서 성공적을 인증한 후 이 방법으로 리디렉션한다.


	:Return: 인증 토큰. (서비스에 대한 모든 향후 요청에서 헤더 Mount:Auth 로 삽입해야 한다.)


	:Error 403: 연산자를 사용할 수 없다. (예를 들어, 이미 성공적으로 호출된 후 이 API method를 호출하려고 할 때).


	:Error 503: 서비스를 사용할 수 없다.
	"""
def oauth_confirm(*args,**kwargs):
	"""구글 서버에 인증 URL을 반환한다.

	:Class: GoogleAuth(name,service_name,client_id,client_secret,access_token_url,authorize_url,base_url,messages=None,callback_url=None,**kwargs):oauth_url(*args,**kwargs)

	:URL: https://api.server.com/api/1/accounts/google_url/


	:Version: 0, 1


	:Method: POST


	:param permanent_auth: 선택 사항. 기본적으로 boolean은 False로 설정, 제한된 기간 내에 토큰 요청이 유효. True로 설정하면 영구 토큰 전송.


	:param device_description: 선택 사항. 사용자가 로그인하는 디바이스에 대한 설명. (필드가 비어 있고 영구 토큰이 요청되면 ‘<로그인 날짜> + <user agent>’로 값 반환.)


	:Return: 다음 로그인 후 사용자가 리디렉션 해야 하는 구글 웹 사이트의 승인 페이지 주소.


	:Error 503: OAuth 제공자 서비스를 사용할 수 없다.
	"""
def create_view(*args,**kwargs):
	"""해시 함수와 로그인 상태를 알고 있는 경우 언제든지 값을 생성할 수 있는 영구 인증 토큰을 수신하는데 사용한다. 이 로그인 method를 사용하여 인증 정보를 생성하고 관련된 영구 토큰은 반환한다. 이 토큰은 method /accounts /permanent_tokens /에서 반환되는 영구 토큰이 아니며, 삭제할 수 있는 유일한 방법은 관련 자격 증명을 삭제하는 것이다. 각 사용자는 이 플러그인 안에서 제공하는 자격 증명을 하나만 가질 수 있다. 이 method를 호출하면 기존 인증 정보가 새 인증서와 함께 인증 토큰과 함께 교환된다.
	:Class: BasicAuth(name,**kwargs)

	:Headers MountbitAuth: 권한 부여 토큰.


	:URL: https://api.server.com/api/1/accounts/create_basic_auth/


	:Version: 1


	:Method: POST


	:param login: 선택 사항. 고유한 로그인. 시스템이 수신되지 않으면 시스템에서 우발적인 영문자 시퀀스(8개 기호)를 생성.


	:param password: 선택 사항. 시스템이 수신되지 않으면 시스템에서 우발적인 영숫자 시퀀스(7개 기호)를 생성.


	:Return: 인증 토큰. 권한이 필요한 모든 서버 요청에서 헤더 Mountbit:Auth로 삽입.


	:Error 403: 다른 사용자가 이미 로그인했다.
	"""
def get_view(*args,**kwargs):
	"""기본 승인을 위해 (로그인 및 암호를 사용하여) 로그인 및 암호를 반환한다.
	:Class: BasicAuth(name,**kwargs)

	:Headers MountbitAuth: 권한 부여 토큰.


	:URL: https://api.server.com/api/1/accounts/get_basic_auth/


	:Version: 1


	:Method: GET


	:param: 없음.


	:Error 404: 사용자 계정에 기본 인증을 위한 로그인 및 암호가 포함되어 있지 않다.
	"""
def login(*args,**kwargs):
	"""새로운 사용자를 추가한다.

	:Class: LDAPAuth(name,server,port,**kwargs)

	:URL: https://api.server.com/api/1/accounts/login_by_ldap/


	:Version: 1


	:Method: POST


	:param name: 필수 사항. 이름. 최대 사이즈는 256 bytes.


	:param password: 필수 사항. 비밀번호. 최대 사이즈는 256 bytes.


	:param permanent_auth: 선택 사항. 기본적으로 Boolean 값은 False로 설정되어 있다. 즉, 토큰 요청은 제한된 기간 내에 가능하다. 만약 True이면, 영구 토큰 생성.


	:param device_description: 선택 사항. 사용자가 로그인하는 디바이스에 대한 설명. (필드가 비어 있고 영구 토큰이 요청되면 ‘<로그인 날짜> + <user agent>’로 값 반환.)


	:Return: 로그인 정보.


	:Error 401: 지정된 name/password의 사용자가 ActiveDirectory 서버에서 인증하지 못 했다.
	"""
def accounts_login(request,*args,**kwargs):
	"""Auth 토큰을 반환한다.


	:URL: https://api.server.com/api/1/accounts/login/


	:Version: 1


	:Method: POST


	:param login: 필수 사항. 준비된 형식의 login.


	:param password: 필수 사항. 사용자 비밀번호.


	:param permanent_auth: 선택 사항. 기본적으로 Boolean 값은 False로 설정되어 있다. 즉, 토큰 요청은 제한된 기간 내에 가능하다. 만약 True이면, 영구 토큰 생성.


	:param device_description: 선택 사항. 사용자가 로그인하는 디바이스에 대한 설명. (필드가 비어 있고 영구 토큰이 요청되면 ‘<로그인 날짜> + <user agent>’로 값 반환.) 


	:Return: 인증 토큰 정보.
	"""
def accounts_logout(request,*args,**kwargs):
	"""초대 토큰에 따라 사용자 로그인을 반환한다.


	:URL: https://api.server.com/api/1/accounts/logout/


	:Version: 0, 1


	:Method: POST


	:param: 매개 변수가 없다. 토큰을 삭제하는 데 승인 헤더가 사용된다.


	:Return 200: 성공.


	:Return 404: 토큰 삭제가 불가능하다.

"""
def get_invited(request,*args,**kwargs):
	"""토큰의 삭제 여부를 반환한다.


	:URL: https://api.server.com/api/1/accounts/getinvited/


	:Version: 1


	:Method: GET


	:param hash: 필수 사항. 초대 토큰.


	:Return: 초대를 보낸 사용자의 로그인.


	:Error 404: 해당 초대 토큰을 가진 사용자를 찾을 수 없다.

"""
def accounts_approve(request,*args,**kwargs):
	"""등록 확인 URL의 일부인 확인 토큰을 통해 등록을 확인한다. 이 URL은 등록 후 사용자 이메일 주소로 보낸 메시지에 나열된다.


	:URL: https://api.server.com/api/1/accounts/approve/


	:Version: 0, 1


	:Method: GET


	:param hash: 필수 사항. 사용자 등록을 확인할 수 있는 토큰.


	:Return: 사용자 정보.


	:Error 404: 해당 초대 토큰을 가진 사용자를 찾을 수 없다.
	"""
def accounts_get(request,*args,**kwargs):
	"""사용자 계정 정보를 반환한다.


	:URL: https://api.server.com/api/1/accounts/get/


	:Version: 1


	:Method: GET


	:param user_id: 선택 사항. 사용자 ID. 매개 변수가 생략되었거나 권한이 위임된 사용자가 아닌 경우 권한이 부여된 사용자에 대한 정보가 반환된다. 매개 변수를 입력하고 관리자가 method를 호출하면 지정된 사용자에 대한 정보가 반환된다.


	:Return: 사용자 계정 정보.


	:Error 404: 해당 초대 토큰을 가진 사용자를 찾을 수 없다.
	"""
def accounts_change_profile_settings(request,*args,**kwargs):
	"""사용자 프로필을 변경한다. (이름, 비밀번호, 기타…)


	:URL: https://api.server.com/api/1/accounts/change_profile/


	:Version: 0, 1


	:Method: POST


	:param name: 선택 사항. 사용자의 새로운 이름.


	:param password: 선택 사항. 사용자의 새로운 비밀번호. (사용자 이메일 주소로 특수 링크가 전송된다. 사용자가 링크를 따라가면 암호가 해커에 의해 바뀐 경우 계정을 반환할 수 있다.)


	:param lang: 선택 사항. 인터페이스 언어. (허용되는 값은 “en”, “ru”, “de”)


	:param timezone: 선택 사항. 사용자 시간대. (“Europe/Moscow”, “America/Los_Angeles” 등. 자세한 내용은 tz 데이터베이스 시간대 목록 참조.)


	:param extra_info: 사용자를 위한 추가적인 정보.


	:Return: 없음.


	:Error 200: 비밀번호가 바뀌지 않았다.


	:Error 400: 시스템에서 사용자를 찾을 수 없거나 매개 변수 중 하나의 유효성이 검사되지 않았다. 모든 매개 변수는 선택사항이지만 매개 변수가 하나 이상 입력되어야 한다.

"""
def accounts_resend_message_for_approve(request,*args,**kwargs):
	"""사용자가 아직 확인하지 않은 경우 등록을 확인하기 위해 두 번째 메시지를 보낸다.


	:URL: https://api.server.com/api/1/accounts/resend_message_for_approve/


	:Version: 1


	:Method: POST


	:param login: 메시지를 재전송하여 확인하길 원하는 로그인.


	:Return: 없음.


	:Error 403: 사용자가 이미 등록을 확인했다.

"""
def accounts_recover_lost_password(request,*args,**kwargs):
	"""이 로그인과 관련된 계정에 임시로 액세스 하는 데 필요한 메시지를 지정된 로그인으로 보낸다.


	:URL: https://api.server.com/api/1/accounts/recover_lost_password/


	:Version: 1


	:Method: POST


	:param login: 암호를 승인한 다음 암호를 변경하는 데 사용되는 메시지가 전송되는 로그인.


	:Return: 없음.


	:Error 400: 사용자를 시스템에서 찾을 수 없다.

"""
def accounts_tokens(request,*args,**kwargs):
	"""현재 사용자의 인증 토큰을 반환한다.


	:URL: https://api.server.com/api/1/accounts/permanent_tokens/


	:URL: https://api.server.com/api/1/accounts/tokens/


	:Version: 0, 1


	:Method: GET


	:param include_not_permanent: 응답할 영구 토큰을 추가하지 않는다.


	:Return: 사용자 토큰이 포함된 목록.

	:Note: 디바이스 설명이 실제 디바이스 버전과 호환되지 않을 수 있다.

"""
def accounts_accept_offer(request,*args,**kwargs):
	"""사용자가 제안을 수락했음을 확인한다.


	:URL: https://api.server.com/api/1/accounts/accept_offer/


	:Version: 0, 1


	:Method: POST


	:param: 없음.


	:Return 200: 확인이 승인되었다.

"""
def accounts_decline_offer(request,*args,**kwargs):
	"""제안을 취소한다.


	:URL: https://api.server.com/api/0/accounts/decline_offer/


	:Version: 0, 1


	:Method: POST


	:param: 없음.


	:Return 200: 수락이 확인되었다.


	:Error 405: 설정에 의해 method가 제한되었다.


	:Note: 이 Method는 can_decline_offer == True 일 때 사용 가능하다.

"""
def accounts_get_offer(request,*args,**kwargs):
	"""제안을 요청한다.


	:URL: https://api.server.com/api/1/accounts/get_offer/


	:Version: 0, 1


	:Method: GET


	:param: 없음.


	:Return HTML: 제안서를 나열하는 페이지.


	:Note: 제안서의 텍스트 키가 존재하지 않거나 비어 있는 경우 키가 비어 있는 상태로 key:value에 저장된다.

"""
def accounts_feedback(request,*args,**kwargs):
	"""앱에 관한 피드백을 보낸다.


	:URL: https://api.server.com/api/1/accounts/feedback/


	:Version: 0, 1


	:Method: POST


	:param name: 선택 사항. 피드백을 보내는 사용자의 이름.


	:param email: 선택 사항. 피드백을 보내는 사용자의 이메일.


	:param comment: 필수 사항. 메시지 텍스트.


	:Return 200: 피드백이 처리된다. URL은 앱 로그가 필요하면 다운받을 수 있는 선택적 매개 변수 “url_upload_logs”와 JSON을 포함하고 있다.
	"""
def accounts_feedback_list(request,*args,**kwargs):
	"""앱 사용에 대한 피드백 목록(관리자만 해당)을 선택한다.


	:URL: https://api.server.com/api/1/accounts/feedback_list/


	:Version: 0, 1


	:Method: GET


	:param limit: 선택 사항. 결과 목록에서 제한되는 값의 양.


	:param offset: 선택 사항. 결과 목록에서의 오프셋 값.


	:param order_field: 선택 사항. 필드에 의해 정렬. (기본적으로 날짜로 설정되어 있다.)


	:param order_direction: 선택 사항. 순서를 정렬. (기본적으로 오름차순.)


	:Return: 피드백 목록.
	"""
def accounts_remove_login(request,*args,*kwargs):
	"""지정된 사용자 로그인을 삭제한다.


	:URL: https://api.server.com/api/1/accounts/remove_login/


	:Version: 1


	:Method: POST


	:Headers MountbitAuth: 권한 부여 토큰.


	:param login: 삭제할 로그인.


	:Return 200: 성공.


	:Return 400: 사용자의 마지막 로그인을 지우는 것이 불가능하다.


	:Return 404: 로그인을 찾을 수 없다.

"""
def accounts_check(request,*args,**kwargs):
	"""사용자 계정의 존재 여부를 확인한다.


	:URL: https://api.server.com/api/1/accounts/check/


	:Version: 1


	:Method: GET


	:param login: 필수 사항. 사용자 로그인


	:Return: 사용자 존재 여부. (존재한다면 {'status': 'ok'}를, 아니라면 {'status': 'not found'}를 반환한다.)


	:Error 404: 이 로그인의 사용자를 찾을 수 없다.
	"""
