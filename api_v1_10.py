# -*- coding: utf-8 -*-

def company_get(request,*args,**kwargs):
	"""회사 정보를 반환한다.


	:URL: https://api.server.com/api/1/accounts/company/<company id>/


	:Version: 1


	:Method: GET


	:param company_id: URL로부터 받은 회사 ID.


	:Return: 회사 사용자 대상 :


	:Return company_id: 회사 ID.


	:Return name: 회사명.


	:Return owner_id: 회사 소유주의 ID.


	:Return employees_count: 회사 직원 수.


	:Return logo_url: 로고 URL.


	:Return domain: 서브 도메인 이름.


	:Return storage_size: 저장 공간 크기.


	:Return quota_size: 할당 크기.


	:Return registration_date: 회사 등록 날짜.


	:Return 회사 관리자 대상으로 모든 사용자들의 데이터를 보여준다.


	:Return ldap_is_enabled: LDAP 가 사용 가능 여부.


	:Return ldap_address: LDAP 주소.


	:Return ldap_port: LDAP 포트.


	:Return ldap_basedn: LDAP 검색을 위한 LDAP 기반의DN.


	:Return ldap_user_attribute: 사용자의 로그인 이름을 저장하는 LDAP 서버의 속성.


	:Return ldap_user_agent_dn: 풀 사용자 DN 을 포함한LDAP 속성.


	:Return ldap_user_agent_password: 사용자 비밀번호를 포함한 LDAP 속성.


	:Return public_links_allow: 공개 링크 허용 여부 (허용/비허용).


	:Error 403: 사용자는 회사의 데이터를 볼 권한이 없다. 


	:Error 404: 주어진 ID로 회사를 찾을 수 없다.

"""
def company_get_public(request,*args,**kwargs):
	"""도메인 이름에 따른 회사의 공개 정보를 반환한다.


	:param domain: 회사 도메인 값


	:Return: 회사 정보를 포함한 json 딕셔너리.


	:Error 404: 이 도메인으로 회사를 찾을 수 없다

"""
def company_change(request,*args,**kwargs):
	"""회사 설정을 변경하고 회사 또는 시스템 관리자의 접근 한이 필요하다.


	:URL: httsp://api.server.com/api/1/company/<company id>/change/


	:Method: POST


	:param company_id: 필수 사항. URL 문자열로부터의 회사 ID


	:param name: 회사 이름


	:param domain: 회사 도메인


	:param logo_url: 로고 URL


	:param ldap_is_enabled: LDAP 가 사용 가능 여부


	:param ldap_address: LDAP 주소


	:param ldap_port: LDAP 포트


	:param ldap_basedn: LDAP 검색을 위한 LDAP 기반의DN


	:param ldap_user_attribute: 사용자의 로그인 이름을 저장하는 LDAP 서버의 속성


	:param ldap_user_agent_dn: 풀 사용자 DN 을 포함한LDAP 속성


	:param ldap_user_agent_password: 사용자 비밀번호를 포함한 LDAP 속성 


	:param public_links_allow: 공개 링크 허용 여부 (허용/비허용)


	:param wizard_state: 웹 프론트엔드와 마법사:사용자 정의 구성 프로세스에 대한 상태를 저장한다.


	:param notification_email: state 컴퍼니에 대한 알림 이메일. 


	:Return: 기업 공개 정보. accounts/company/<id>/ API 메소드를 참고.


	:Error 403: 사용자는 회사의 설정을 변경할 권한이 없다.


	:Error 404: 이 도메인으로 회사를 찾을 수 없다.

"""
def company_confirm_logo(request,*args,**kwargs):
	"""로고 업로드의 완료를 확인한다.

	:URL: https://api.server.com/api/1/company/<company_id>/logo_confirm/ 


	:Method: POST, GET


	:param company_id: 필수 사항. URL로부터 얻은 회사 ID


	:param temp_name: 임시 파일명


	:param size: 회사 로고의 파일 사이즈, 파일 업로드 확인할 때 사용


	:param checksum: 로고 md5 체크썸, 파일 업로드 확인할 때 사용 


	:Return: 없음.


	:Error 404: 주어진 ID로 회사를 찾을 수 없다.

"""
def company_clear_logo(request,*args,**kwargs):
	"""회사 로고를 제거한다.


	:URL: https://api.server.com/api/1/company/<company_id>/logo_clear/ 


	:Method: POST, GET


	:param company_id: 의무, URL로부터 얻은 회사 ID.


	:Return: 없음.


	:Error 404: 주어진 ID로 회사를 찾을 수 없다

"""
def company_create_logo(request,*args,**kwargs):
	"""회사 로고를 생성한다.


	:URL: https://api.server.com/api/1/company/<company_id>/logo_upload/ 


	:Method: POST, GET


	:param company_id: 필수 사항. URL로부터 얻은 회사 ID.


	:Return: 없음.


	:Error 404: 주어진 ID로 회사를 찾을 수 없다

"""
def company_users_enable(request,*args,**kwargs):
	"""회사에서 사용자를 활성화한다.


	:URL: https://api.server.com/api/1/company/<company id>/users_enable/ 


	:Method: POST


	:param company_id: 필수 사항. URL로부터 얻은 회사 ID


	:param user_id: 필수 사항. 사용자 ID


	:param reason: 활성화 시키는 이유


	:Return: 사용자 공개 정보 (/accounts/get)


	:Error 404: 주어진 ID로 회사/사용자를 찾을 수 없다

"""
def company_users_disable(request,*args,**kwargs):
	"""회사에서 사용자를 비활성화한다.


	:URL: https://api.server.com/api/1/accounts/company/<company id>/users_disable/ 


	:Method: POST


	:param company_id: 필수 사항. URL로부터 받은 회사 ID


	:param user_id: 필수 사항. 사용자 ID 목록


	:param reason: 비활성화 사유


	:param remote_wipe: 모든 기기에서 데이터 삭제


	:Return: 없음.


	:Error 404: 주어진 ID로 회사를 찾을 수 없다

"""
def company_create_user(request,*args,**kwargs):
	"""회사를 생성한다.


	:URL: https://api.server.com/api/1/accounts/company/<company id>/create_user/ 


	:Method: POST, GET


	:param company_id: 필수 사항. URL로부터 받은 회사 ID


	:param login: 필수 사항. 사용자 로그인 


	:param name: 필수 사항. 사용자 이름 


	:param password: 필수 사항. 사용자 패스워드 


	:Return: Account/get 과 같은 사용자 공개 정보.


	:Error 402: 사용자 할당량을 초과했다.


	:Error 403: 사용자에게 회사의 설정을 바꿀 권한이 없다. 


	:Error 404: 주어진 ID로 회사를 찾을 수 없다.

"""
def company_users(request,*args,**kwargs):
	"""회사 직원 리스트를 반환한다.


	:URL: https://api.server.com/api/1/accounts/company/<company id>/users


	:Method: POST, GET


	:param company_id: 필수 사항. URL로부터 받은 회사 ID


	:Return: 회사 직원 리스트


	:Return userid: 직원 


	:Return name: 직원 이름


	:Return position: 직원 위치


	
	:Error 403: 사용자에게 회사의 설정을 바꿀 권한이 없다. 


	:Error 404: 주어진 ID로 회사를 찾을 수 없다.

"""
def company_user_tokens(request,*args,**kwargs):
	"""회사 관리자에게 사용자의 토큰 리스트를 반환한다.


	:URL: https://api.server.com/api/1/company/user_permanent_tokens https://api.server.com/api/1/company/user_tokens/ 


	:Method: POST, GET


	:param userid: 회사의 사용자 ID


	:param include_not_permanent: 비영구적인 토큰 포함


	:Return device_description: 설명 문자열


	:Return id: 토큰 ID


	:Return created: 생성 일자 타임스탬프


	:Return is_synced: PC 또는 MAC 클라이언트의 동기화 상태 여부


	:Return last_action: 가장 최근에 요청한 API에 대한 정보


	:Error 403: 사용자에게 회사 데이터 접근 권한이 없다.


	:Error 404: 사용자를 찾을 수 없다.

"""
def company_user_token_remove(request,*args,**kwargs):
	"""회사 사용자의 토큰을 삭제하거나 토큰을 원격 초기화로 표시한다. 기업 관리자가 사용한다. 


	:URL: https://api.server.com/api/1/company/user_permanent_token/remove 


	:URL: https://api.server.com/api/1/company/user_tokens/remove/ 


	:Method: POST


	:param token_id: 토큰 ID


	:param remote_wipe: 원격 제거 플래그


	:Return: 없음.


	:Error 403: 사용자에게 회사 데이터 접근 권한이 없다.


	:Error 404: 사용자 또는 토큰을 찾을 수 없다.

"""
def company_user_token_cancel_remove(request,*args,**kwargs):
	"""토큰 삭제를 취소한다.


	:URL: https://api.server.com/api/1/company/user_permanent_token/cancel_remove 


	:URL: https://api.server.com/api/1/company/user_tokens/cancel_remove/


	:Method: POST


	:param token_id: 토큰 ID 


	:Return: 없음.


	:Error 403: 사용자에게 회사 데이터 접근 권한이 없다. 


	:Error 404: 사용자 또는 토큰을 찾을 수 없다.

"""
def company_folder_add(request,*args,**kwargs):
	"""현재 사용자의 회사 공개 공유 목록에 폴더를 추가한다. 현재 사용자를 위한 method이다. 


	:URL: https://api.server.com/api/1/shares/company/add/ 


	:Method: POST, GET


	:param path: 필수 사항. 폴더 경로.


	:param public_name: 폴더의 공개 이름, 기본적으로 사용되는 폴더 이름 


	:Return: 구성 요소들의 맵


	:Return owner_id: 소유자 ID 공유


	:Return public_name: 이름 공유


	:Return folder_hash: 다른 사람들에게 폴더 공유를 하기 위한 해시 값


	:Error 403: 다른 회사로부터 온 사용자들이 공유 폴더를 접근하는 것은 금지되어 있다.

"""
def company_folder_hide(request,*args,**kwargs):
	"""회사의 공개 리스트에서 공유 폴더를 제거한다. 현재 사용자를 위한 메소드이다. 


	:URL: https://api.server.com/api/1/shares/company/hide/ 


	:Method: 없음.


	:param folder_hash: 폴더 공개 해시


	:param path: 폴더 경로


	:param: foler_hash나 path 둘 중 하나나

	:Return: 없음.


	:Error 404: 폴더를 찾을 수 없다.

"""
def company_folders_get(request,*args,**kwargs):
	"""현재 작업하고 있는 사용자에게 공유 폴더 리스트를 반환한다.


	:URL: https://api.server.com/api/1/shares/company/get/ 


	:param folder_hash: 게시된 폴더의 해시


	:param offset: 시작부터 건너뛸 레코드의 수


	:param limit: 반환할 레코드의 최대 개수


	:param show_all: 선택 사항. 회사의 모든 폴더를 보여줄 플래그 (회사 관리자를 위한 매개 변수)


	:Return: 맵의 리스트 :


	:Return owner_id: 공유되는 소유주의 ID


	:Return public_name: 이름 공유 


	:Return folder_hash: 다른 사람들과 공유하기 위한 폴더의 해시 값 


	:Return owner_name: 폴더의 소유자 이름


	:Return collaborators_count: 공동 작업자 수 


	:Return modification_time: 마지막 수정 날짜


	:Return status: 폴더 상태:


	:Return waiting: 현재 사용자가 폴더에 초대되었다.


	:Return requested: 현재 사용자가 폴더에 대해 액세스를 요청했다.


	:Return accepted: 현재 사용자는 이 폴더에 액세스할 수 있다.


	:Return path: 폴더 경로. 현재 사용자에게 공유가 되어있거나, 현재 사용자가 소유자일 때 비어있지 않다


	:Error 404: 주어진 ID로 회사를 찾을 수 없다.

"""
def company_folders_get_one(request,*args,**kwargs):
	"""현재 사용자에게 folder_hash에 의해 공유 폴더를 반환한다.


	:URL: https://api.server.com/api/1/shares/company/get/(?P<folder_hash>[a:zA:Z0:9:_!]+)/ 

	:param folder_hash: 다른 사람들과 공유하기 위한 폴더의 해시 값


	:Return: 맵의 리스트 :


	:Return owner_id: 소유주의 ID 공유


	:Return public_name: 이름 공유 


	:Return folder_hash: 다른 사람들과 공유하기 위한 폴더의 해시 값 


	:Return owner_name: 폴더 소유자의 이름


	:Return collaborators_count: 공동 작업자 수


	:Return modification_time: 마지막 수정 날짜


	:Return path: 폴더 경로, 현재 사용자에게 공유가 되어있거나, 현재 사용자가 소유자일 때 비어 있지 않다


	:Return status: 폴더 상태: 


	:Return waiting: 현재 사용자가 폴더에 초대되었다.


	:Return requested: 현재 사용자가 폴더에 대해 액세스를 요청했다.


	:Return accepted: 현재 사용자는 이 폴더에 액세스할 수 있다. 

"""
def company_get_shares(request,*args,**kwargs):
	"""회사 관리자에게만 이미 공유 된 폴더 및 공개 링크 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/company/shared/ 

	:param name: 필터를 위한 사용자 이름. 기본적으로 모든 유저들을 대상으로 한다.


	:Return 맵의 리스트:


	:Return bytes: 파일의 크기 


	:Return creation_time: 생성된 시간 스탬프를 공유


	:Return modification_time: 파일 수정 시간 스탬프


	:Return owner_id: 소유자의 ID를 공유하고 링크


	:Return owner_name: 소유자의 이름을 공유하고 링크


	:Return shared_outside: 게시된 폴더의 경우 공동 작업자 또는 회사의 소유자가 아닌 경우 플래그가 true. 링크는 항상 true.


	:Return src_path: 파일 또는 폴더의 경로


	:Return type: 타입. ‘share’ : 게시된 폴더  and ‘link’ : 링크
	"""
def company_share_access_request(request,*args,**kwargs):
	"""공용 폴더 소유자에게 액세스 요청을 보낸다.


	:URL: https://api.server.com/api/1/shares/company/request/  

	:param folder_hash: 필수 사항. 회사 폴더 리스트에 대한 응답에서 나온 폴더 해시


	:param invitataion: 폴더 소유자에 대한 설명 요청


	:Return: 없음.


	:Error 403: 폴더가 이미 공유되었거나, 현재 사용자에게 허용되지 않는다.


	:Error 404: 폴더 해시 또는 사용자를 찾을 수 없다.


	:Error 409: 폴더 공유가 충돌 나거나, 자기 자신에게 폴더를 공유하지 못한다

"""
def company_share_access_accept(request,*args,**kwargs):
	"""폴더 공유 요청을 받아들인다.


	:URL: https://api.server.com/api/1/shares/company/accept/ 


	:Method: POST, GET


	:param older_hash: 필수 사항. 회사 폴더 리스트에 대한 응답에서 나온 폴더 해시


	:param writer: 폴더에 대한 권한을 쓰고 (True or False) 읽기전용으로 기본 설정되어 있다.


	:Return: 없음.


	:Error 403: 폴더가 이미 공유되었거나, 현재 사용자에게 허용되지 않는다.


	:Error 404: 폴더 해시 또는 사용자를 찾을 수 없다.

"""
def company_share_get_requests(request,*args,**kwargs):
	"""회사 공유 액세스를 나열한다. 


	:URL: https://api.server.com/api/1/shares/company/requests/ 

	:param: 없음.


	:Return: 공유된 정보에 대한 리스트

	:Error 403: 폴더가 이미 공유되었거나, 현재 사용자에게 허용되지 않는다.


	:Error 404: 폴더 해시 또는 사용자를 찾을 수 없다.

"""
def company_shares_collaborators(request,*args,**kwargs):
	"""공유 폴더에 대한 공동 작업자 목록을 반환한다.


	:URL: https://api.server.com/api/1/company/admin/shares/collaborators/



	:Version: 1


	:Method: GET


	:param userid: 필수 사항. 공유 폴더 소유자 ID


	:param path: 필수 사항. 폴더 경로.


	:Return: 공동 작업자에 대한 리스트


	:Error 404: 폴더를 찾을 수 없다. 

	:Note: is_indirect: 공유 폴더의 직접 또는 간접 공동 작업자. False 인 경우 폴더에 대한 액세스 권한을 부여 받은 직접 공동 작업자이다. True이면 부모 폴더에 대한 액세스 권한이 부여된 간접 공동 작업자이다.

"""
def company_shares_remove(request,*args,**kwargs):
	"""공유 폴더에서 사용자를 삭제한다.


	:URL: https://api.server.com/api/1/company/admin/shares/remove/


	:Method: POST


	:param userid: 필수 사항. 공유 폴더 소유자 ID


	:param path: 필수 사항. 폴더 경로


	:param member_login: 필수 사항. 공유 폴더에서 제거되어야 하는 사용자 로그인


	:Return 200: 성공적으로 삭제되었다.


	:Error 403: 사용자가 공유 폴더 공동 작업자가 아니다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def company_shares_unshare(request,*args,**kwargs):
	"""공유 폴더에서 모든 사용자를 삭제한다. 폴더를 모든 공동 작업자로부터 숨긴다.


	:URL: https://api.server.com/api/1/company/admin/shares/unshare/


	:Method: POST


	:param userid: 필수 사항. 공유 폴더 소유자 ID 


	:param path: 필수 사항. 공유 폴더 경로.


	:Return 200: 공유 취소가 성공적이다.


	:Error 404: 지정한 경로가 있는 공유 폴더를 찾을 수 없다.

"""
def company_cancel_invite_user(request,*args,**kwargs):
	"""사용자 초대를 취소한다.


	:URL:  https://api.server.com/api/1/company/<company id>/invite_user/


	:Version: 1


	:Method: POST


	:param email: 필수 사항. 초대하려는 사용자의 이메일 주소


	:param invitation: 초대 메시지

"""
def company_status_change(request,*args,**kwargs):
	"""회사 상태를 변경하거나 확인한다. (활성화 / 비활성화)


	:URL: https://api.server.com/api/1/company/<company id>/status/ 


	:Method: POST, GET


	:param company_id: 필수 사항. URL로부터 가져온 회사 ID


	:param status: 회사 상태 값


	:Return: 회사의 현재 상태.


	:Error 403: 사용자에게 회사 설정을 바꿀 수 있는 권한이 없다.


	:Error 404: 주어진 ID로 회사를 찾을 수 없다.

"""
def company_remove(request,*args,**kwargs):
	"""회사를 제거한다.


	:URL: https://api.server.com/api/1/company/<company id>/remove/ 


	:Method: POST, GET


	:param company_id: 필수 사항. URL 로부터 가져온 회사 ID


	:Return: 없음


	:Error 403: 사용자가 회사 리스트를 볼 권한이 없다.


	:Error 404: 주어진 ID로 회사를 찾을 수 없다. 


	:Error 400: 회사를 제거할 수 없다.

"""
