# -*- coding: utf-8 -*-

def accounts_delete(request,*args,**kwargs):
	"""사용자 계정을 삭제한다. 


	:URL: https://api.server.com/api/0/admin/accounts_delete/


	:Version: 0


	:Method: POST


	:param user_id: 선택 사항. 사용자 ID. 


	:param immediately: 필수 사항. True 일 경우 사용자의 모든 데이터 제거.


	:param migrate_file: 필수 사항. 계정이 삭제되면 파일들이 다른 사용자로 마이그레이트.


	:param migrate_login: 선택 사항. 마이그레이션을 하는 경우, 사용자가 주어진 파일들을 받게 된다. 


	:Return: 사용자 정보

"""
def accounts_restore(request,*args,**kwargs):
	"""사용자 계정이 완전히 삭제되지 않은 경우에 복구한다.


	:URL: https://api.server.com/api/0/admin/accounts_restore/


	:Version: 0


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID. 


	:Return: 사용자 정보

"""
def admin_accounts_disable(request,*args,**kwargs):
	"""사용자 계정을 비활성화 시킨다. 


	:URL: https://api.server.com/api/1/admin/accounts_disable/


	:Version: 0, 1 


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID. 


	:param reason: 필수 사항. 비밀번호를 변경하는 이유.


	:Return: 사용자 정보

"""
def admin_accounts_enable(request,*args,**kwargs):
	"""사용자 계정을 활성화시킨다.


	:URL: https://api.server.com/api/1/admin/accounts_enable/


	:Version: 1 


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID. 


	:param reason: 필수 사항. 비밀번호를 변경하는 이유.


	:Return: 사용자 정보

"""
def admin_accounts_find_users(request,*args,**kwargs):
	"""주어진 매개변수들과 함께 사용자들의 리스트를 반환한다. 이 메소드는 관리자만 사용할 수 있다.


	:URL: https://api.server.com/api/1/admin/accounts_find_users/


	:Version: 1 


	:Method: POST


	:param user_id: 선택 사항. 찾고자 하는 사용자의 아이디


	:param registration_date_from 과registration_date_to: 선택 사항. 사용자 등록에 대한 기간. 매개변수가 주어지면, 이 메소드는 이 기간 안에 등록한 사용자들을 반환한다. 매개변수는 다같이 또는 하나씩 전송이 될 수 있다. 


	:param login: 선택 사항. 사용자 로그인


	:param name: 선택 사항. 사용자 이름.


	:param last_login_from and last_login_to: 선택 사항. 사용자가 검색되는 기간. 매개변수는 하나씩 또는 다같이 보내질 수 있다. 


	:param storage_size_from and storage_size_to: 선택 사항. 사용자가 검색되는 저장영역의 크기. 매개변수는 하나씩 또는 다같이 보내질 수 있다. 


	:param is_active: 선택 사항. 활성 / 비활성 사용자. 


	:param has_region: 선택 사항. 사용자 계정이 지역(region)을 갖고 있는지 여부 


	:param region: 선택 사항. 지역(region) 이름 


	:param role: 선택 사항. 관리자 또는 사용자.


	:param company_name: 선택 사항.


	:param company_id: 선택 사항.


	:param is_deleted: 선택 사항.


	:param deleted_date: 선택 사항.


	:param block_date: 선택 사항.


	:param limit: 선택 사항. 레코드의 개수 제한. 백엔드 설정에 따라서 이 속성에 대한 최댓값을 설정한다. (기본적으로 2000으로 설정되어 있다.)


	:param offset: 선택 사항. 리스트의 시작에서부터 떨어진 오프셋.


	:param order_field: 선택 사항. 사용자 리스트를 정렬하기 위한 속성


	:param order_direction: 선택 사항. 오름차순, 내림차순


	:Return: 레코드 양 (개수), 레코드 한도 (한도), 사용자 목록 (사용자), 레코드 목록의 오프셋 (오프셋).

	"""
def admin_accounts_generate_login_key(request,*args,**kwargs):
	"""시스템에 액세스하기 위해 임시 키를 생성한다. 시스템에 액세스하기 위해 / accounts / login 메소드로 키를 보낼 수 있다.


	:URL: https://api.server.com/api/0/admin/accounts_generate_login_key/


	:Version: 0


	:Method: POST


	:param user_id: 필수 사항. 사용자의 아이디


	:Return: 사용자 ID, 액세스 키

	"""
def admin_accounts_set_password(request,*args,**kwargs):
	"""사용자 비밀번호 바꾸는 것을 허용한다.


	:URL: https://api.server.com/api/1/admin/accounts_set_password/


	:Version: 1


	:Method: POST


	:param user_id: 필수 사항. 사용자의 아이디


	:param new_password: 선택 사항. 새로운 비밀번호.


	:Return: 사용자 정보

"""
def assign_role(request,*args,**kwargs):
	"""사용자의 역할을 바꾼다.


	:URL: https://api.server.com/api/0/admin/assign_role/


	:Version: 0


	:Method: POST


	:param user_id: 필수 사항. 사용자의 아이디.


	:param role: 필수 사항. 사용자의 새로운 역할.


	:Return: 사용자 정보

"""
def companies_find(request,*args,**kwargs):
	"""회사 리스트를 반환한다.


	:URL: https://api.server.com/api/1/admin/find_companies/


	:Version: 0


	:Method: GET, POST


	:param offset: 오프셋 값.


	:param limit: 아이템의 최대 개수.


	:param order_field: 정렬 속성.


	:param company_id:


	:param status:


	:param name:


	:param owner_id:


	:param domain:


	:param registration_date:


	:param employees_count:


	:param quota_employees_count:


	:param storage_size:


	:param order_direction: 정렬 방향.


	:param ASCENDING: 오름차순.


	:param DESCENDING: 내림차순.


	:param status: 회사의 상태 (활성화, 비활성화) 


	:param company_id_in: 회사의 json 어레이 ID


	:param name_in: 회사의 json 어레이 이름


	:param owner_id_in: 회사의 소유자 ID json 어레이


	:param domain_in: 회사의 도메인의 json 어레이


	:param storage_size_from: 저장공간의 최소 크기 


	:param storage_size_to: 저장공간의 최대 크기


	:Return 회사: 회사 레코드 구성


	:Return company_id: 회사 아이디


	:Return name: 회사 이름


	:Return owner_id: 회사의 소유자 아이디 


	:Return employees_count: 회사 직원 수


	:Return logo: 로고 URL


	:Return domain: 서브 도메인 이름


	:Return storage_size: 저장소 크기 


	:Return quota_size: 할당량 크기 


	:Return quota_employees_count: 할당량 직원 수 


	:Return registration_date: 회사 등록 날짜 


	:Return public_links_allow: 공유 링크 허용 


	:Return status: 회사 상태 


	:Return sharing_outside_allow: 외부 공유 허용 


	:Return company_folder_creation_allow: 폴더 생성 허용


	:Return limit:


	:Return offset:


	:Return count:


	:Error 403: 사용자는 회사의 리스트를 볼 권한이 없다

"""
def company_approve(request,*args,**kwargs):
	"""
	:URL: https://api.server.com/api/1/admin/company/<company id>/approve/


	:Version: 1


	:Method: GET 

"""
def company_cancel_invite_user(request,*args,**kwargs):
	"""사용자 초대 취소 


	:URL: https://api.server.com/api/1/admin/company/<company id>/invite_user/cancel/


	:Version: 1


	:Method: POST 

"""
def company_deny(request,*args,**kwargs):
	"""
	:URL: https://api.server.com/api/1/admin/company/<company id>/deny/


	:Version: 1


	:Method: GET 

"""
def company_edit_user(request,*args,**kwargs):
	"""사용자 초대 취소 


	:URL: https://api.server.com/api/1/admin/company/<company id>/edit_user/


	:Version: 1


	:Method: POST 

"""
def company_invite_user(request,*args,**kwargs):
	"""사용자 초대


	:URL: https://api.server.com/api/1/company/<company id>/invite_user/


	:Version: 1


	:Method: POST 


	:param email: 필수 사항. 초대 받는 사용자의 이메일


	:param invitation: 초대 메시지


	:Return: 사용자 정보.

"""
def company_remove(request,*args,**kwargs):
	"""회사 제거


	:URL: https://api.server.com/api/1/company/<company id>/remove/


	:Method: POST, GET 


	:param company_id: 필수 사항, URL 문자열에서 가져온 회사 아이디


	:Return: 없음


	:Error 403: 사용자가 회사 리스트를 볼 권한 없다


	:Error 404: 주어진 아이디로 회사를 찾을 수 없다


	:Error 400: 회사를 삭제할 수 없다 

"""
def company_status_change(request,*args,**kwargs):
	"""회사의 상태가 활성/비활성에서 변경이 되었는지 확인 또는 변경한다.


	:URL: https://api.server.com/api/1/company/<company id>/status/


	:Method: POST, GET 


	:param company_id: 필수 사항, URL 문자열에서 가져온 회사 아이디


	:param status: 상태 값


	:Return 회사 현재 상태


	:Error 403: 사용자가 회사 설정을 볼 권한 없다


	:Error 404: 주어진 아이디로 회사를 찾을 수 없다

"""
def create_user(request,*args,**kwargs):
	""" """
def create_user(request,*args,**kwargs):
	""" """
def delete_user_feature(request,*args,**kwargs):
	""" """
def edit_user(request,*args,**kwargs):
	"""사용자 데이터를 수정하는 것을 허용한다 


	:URL: https://api.server.com/api/1/admin/edit_user/


	:Method: POST 


	:param user_id: 필수 사항. 사용자 아이디.


	:param hard_quota_size: 선택 사항. 사용자가 주어진 저장 용량 크기를 초과하지 못하도록 하는 크기 (무제한의 경우 :1).


	:param quota_size: 선택 사항. 사용자가 주어진 저장 용량 크기를 초과하도록 하는 크기 (무제한의 경우 :1).


	:param region: 선택 사항. 사용자의 지역(region).


	:Return: 사용자 정보


	:Error 404: 주어진 아이디로 사용자를 찾을 수 없다 

"""
def get_locked_logins(request,*args,**kwargs):
	"""잠긴 로그인 리스트를 가져온다 


	:URL: https://api.server.com/api/1/admin/blocked_logins/


	:Method: POST, GET


	:param: 없음


	:Return: 잠긴 로그인의 리스트


	:Error: 없음

"""
def get_user_by_login(request,*args,**kwargs):
	""" """
def invite_user(request,*args,**kwargs):
	"""초대 이메일을 발송한다.


	:URL: https://api.server.com/api/0/admin/invite_user/


	:Version: 0


	:Method: POST


	:param email: 필수 사항. 초대받은 사용자의 이메일


	:param invitation: 초대 메시지.


	:Return: 사용자 정보

"""
def set_user_feature(request,*args,**kwargs):
	""" """
def get_data(request,*args,**kwargs):
	"""측정항목에 대한 데이터를 반환한다.


	:URL: https://api.server.com/api/0/analytics/get_data/


	:Version: 0


	:Method: POST 


	:param token: 인증 토큰.


	:param date_from: 날짜 범위, 타임스탬프.


	:param date_to: 날짜 범위, 타임스탬프.


	:param metric: 측정 항목.


	:param period: 기간 [일, 주, 월].


	:param region: 데이터가 요청이 된 지역(region) .


	:Return: 측정항목 값


	:Error 404: 키를 찾을 수 없다 


	:Note: 이 메소드는 관리자 권한을 필요로 한다 

	"""
def get_metrics(request,*args,**kwargs):
	"""측정 항목의 리스트를 반환한다.


	:URL: https://api.server.com/api/0/analytics/get_metrics/


	:Version: 0


	:Method: GET 


	:Return: 매개 변수와 측정 항목의 리스트

	:Note: 이 메소드는 관리자 권한을 필요로 한다 
	"""
def get_multiple_data(request,*args,**kwargs):
	"""주어진 측정항목 리스트에 대한 데이터를 반환한다 


	:URL: https://api.server.com/api/0/analytics/get_multiple_data/


	:Version: 0


	:Method: POST 


	:param date_from: 날짜 범위, 타임스탬프.


	:param date_to: 날짜 범위, 타임스탬프.


	:param metric: 측정 항목.


	:Return: 이름으로 그룹화된 측정항목 값의 리스트.


	:Note: 관리자 권한이 필요하다.
	"""
def get_result(request,*args,**kwargs):
	"""비동기 API 메소드의 성능 상태를 수신하는 데 도움을 준다.


	:URL: https://api.server.com/api/0/task/<task_id>/


	:Version: 0


	:Method: GET 


	:param task_id: 필수 사항. 백그라운드 작업의 ID 


	:Return :실행 종료 시 사전에 추가 된 임의의 json 딕셔너리.


	:Error 404 : 작업을 찾을 수 없다


	:Error 400: 작업을 실행하는 중에 에러가 발생함

"""
def check_ws(request,*args,**kwargs):
	"""웹 소켓이 사용가능한지 확인한다.


	:URL: https://api.server.com/api/0/check_ws/


	:Version: 0


	:Method: GET, POST 


	:param: 없음


	:Return: 성공 또는 실패


	:Error: 없음

"""
def events(request,*args,**kwargs):
	"""날짜 내림차순으로 정렬된 사용자 이벤트를 반환한다.


	:URL: https://api.server.com/api/0/events/


	:Version: 0


	:Method: GET 


	:param skip: 선택 사항. 초기 데이터 오프셋. (Page_by_page 디스플레이 구성이 가능하다.)


	:param limit: 선택 사항. 레코드 양의 제한. 최댓값은 100이다. 기본 양은 20으로 설정되어 있다.


	:param type: 선택 사항. 이벤트 유형별 필터링.


	:param person: 선택 사항. 이벤트 생정자에 의해서 필터링. 다음과 같은 값들을 가질 수 있다


	:param me: 이벤트 생성자가 현재 사용자이다.


	:param other: 이벤트 생성자가 현재 사용자가 아니다.


	:param from_timestamp: 선택 사항. 데이터 선택의 처음 날짜


	:param to_timestamp: 선택 사항. 데이터 선택의 마지막 날짜


	:Return: 이벤트 집합


	:Return type: 이벤트 타입. 아래를 볼 것


	:Return timestamp: 이벤트 시간 (UTC, ms).


	:Return path: 파일 또는 폴더에 대한 전체 경로


	:Return deleted: 객체가 제거되었는지 아닌지를 가리키는 플래그


	:Return oldname: 이벤트 이름 재설정에 이 값이 추가된다. 기존 폴더 또는 파일의 이름을 가리킨다. 


	:Return oldpath: 이동 이벤트에 이 값이 추가된다. 기존 폴더 또는 파일의 경로를 가리킨다 


	:Return old: 이동 또는 이름 재설정 이벤트에 추가되는 값이다. 기존 폴더 또는 파일에 대한 정보를 가지고 있다. (내용, 버전) 


	:Return user_id: 이 값은 공동 작업자 추가 또는 삭제 이벤트에 추가된다. 추가되거나 삭제 된 공동 작업자의 ID이다.


	:Return content: 값은 파일 이벤트에 추가된다. 삽입된 필드에 대한 설명을 가리킨다. See /metadata.


	:Return version: 파일 이벤트에 추가되는 값이다. 파일 버전이다.


	:Note: 1. 폴더 이벤트 


	:Note: A. folder_created: 폴더를 생성한다.


	:Note: B. folder_deleted: 폴더를 삭제한다.


	:Note: C. folder_renamed: 폴더 이름을 재설정한다.


	:Note: D. share_invitation_sent: 공유 폴더에 대한 새 공동 작업자가 추가된다. 폴더에 대한 액세스 권한이 있는 모든 사용자와 새 공동 작업자는 해당 알림을 받는다.


	:Note: E. share_invitation_accepted: 공동 작업자는 공유 폴더에 대한 초대를 수락한다. 폴더에 대한 액세스 권한이 있는 모든 사용자와 새 공동 작업자는 해당 알림을 받는다.


	:Note: F. share_invitation_declined: 공동 작업자가 공유 폴더에 대한 초대장을 취소한다. 폴더에 대한 액세스 권한이 있는 모든 사용자와 공동 작업자는 해당 알림을 받는다.


	:Note: G. share_invitation_revoked: 폴더 소유자가 공유 폴더에 대한 초대를 취소한다. 폴더에 대한 액세스 권한이 있는 모든 사용자와 공동 작업자는 해당 알림을 받는다.


	:Note: H. folder_collab_removed: 폴더 공동 작업자가 삭제된다. 모든 공동 작업자에게 알림이 전송된다.


	:Note: I. folder_unshared: 폴더에 대한 액세스가 취소되었다. 모든 공동 작업자에게 알림이 전송된다.


	:Note: J. folder_undeleted: 폴더가 복구된다.


	:Note: K. folder_moved: 폴더가 한 폴더에서 다른 폴더로 이동한다.

	"""
def files_download_extra(request,*args,**kwargs):
	""" """
def files_extra_create(request,*args,**kwargs):
	"""지정된 파일에 대한 추가 데이터를 생성한다. 그것은 실시간 생성이거나 대기열에서의 지연일 수 있다. 그것은 특정 유형의 추가 데이터 생성을 담당하는 플러그인 설정에 따라 다르다. 이론적으로, 한 파일에 대해 여러 유형의 추가 데이터가 있으면 이 모든 유형이 만들어진다. 추가 자료를 만들 플러그인을 선택할 수 없다. 일부 파일에 이미 일부 외부 데이터가 있는 경우 다시 만든다.


	:URL: https://api.server.com/api/0/files/create_extra/


	:Version: 0


	:Method: POST 


	:param path: 필수 사항. 추가 데이터가 생성될 파일의 경로


	:param version: 선택 사항. 파일의 버전 번호


	:Return 시작: 추가 데이터가 생성될 때 대기열에 있으면 (플러그인에 따라 다름) True로 설정한다. 대기중인 작업이 없으면 False로 설정한다.


	:Error 404: 지정한 경로에 파일을 찾을 수 없다. 또는 존재하지 않는 파일 버전이 입력되었다. 

"""
def links_download_extra(request,*args,**kwargs):
	""" """
def links_extra_create(request,*args,**kwargs):
	"""지정된 파일에 대한 추가 기록 생성. 메소드는 API 메소드 / files / create_extra와 유사하지만 공용 파일을 위한 것이라는 차이점이 있다.


	:URL: https://api.server.com/api/0/links/create_extra


	:Version: 0


	:Method: POST


	:param hash: 필수 사항. 게시된 객체의 ID 에 해당하는 해시


	:param path: 선택 사항. 게시된 디렉토리와 관련이 되어있는 파일 또는 폴더의 경로 


	:Return 시작: 추가 데이터가 생성될 때 대기열에 있으면 (플러그인에 따라 다름) True로 설정한다. 대기중인 작업이 없으면 False로 설정한다.


	:Error 404: 객체를 찾을 수 없다. 


	:Error 가능한 이유: 경로가 잘못 입력되었거나 객체가 이동되었거나 삭제되었다.

"""
def shares_create_extra(request,*args,**kwargs):
	"""지정된 파일에 대한 추가 데이터를 생성한다. 그것은 실시간 생성이거나 대기열에서의 지연일 수 있다. 그것은 특정 유형의 추가 데이터 생성을 담당하는 플러그인 설정에 따라 다르다. 이론적으로, 한 파일에 대해 여러 유형의 추가 데이터가 있으면 이 모든 유형이 만들어진다. 추가 자료를 만들 플러그인을 선택할 수 없다. 일부 파일에 이미 일부 외부 데이터가 있는 경우 다시 만든다.


	:URL: https://api.server.com/api/1/shares/create_extra/


	:Version: 1


	:Method: POST 


	:Method: Header


	:Method: 사용자 인증 토큰. 공유된 폴더가 공개되어 있으면, 이 매개 변수는 선택 사항이다.


	:param invite_hash: 필수 사항. 공유 폴더에 사용자를 초대하기 위한 고유한 해시. method /folders/shared/add/ 로부터의 해시 결과. 


	:param path: 필수 사항. 게시된 폴더와 관련된 파일의 경로


	:Return 시작: 추가 데이터가 생성될 때 대기열에 있으면 (플러그인에 따라 다름) True로 설정한다. 대기중인 작업이 없으면 False로 설정한다


	:Error 403: 공유된 폴더에 대한 접근 권한이 충분하지 않다


	:Error 404: 특정 파일이 발견되지 않았다.

"""
def get_set_key(request,*args,**kwargs):
	"""특정 키에 대해 값들의 집합을 반환한다 


	:URL: https://api.server.com/api/0/keyvalue/<key_name>


	:Version: 0


	:Method: GET, POST 


	:param value: POST 요청에 대한 새로운 키 값(문자열 또는 JSON)


	:param rights: 키에 대한 권한


	:Return: GET 요청에 대한 키 값


	:Error 404 : 키를 찾을 수 없다

	"""
def get_storage():
	""" """
def notices(request,*args,**kwargs):
	"""시간의 내림차순으로 필터링 사용자 알림 리스트 


	:URL: https://api.server.com/api/0/notices/


	:Version: 0


	:Method: GET 


	:param type: 선택 사항. 알림 타입에 따라서 필터가 됨.


	:param global: 모든 사용자에게 전송.


	:param personal: 특정 사용자에게 전송.


	:param behavior: 선택 사항. 알림 행동 타입에 따라 필터링 된다.


	:param interactive: 알림은 몇가지 사용자 행동들을 필요로 한다 (확인, 취소)


	:param static: 알림의 목적은 사용자에게 알리는 것이다


	:param status: 선택 사항. 알림 상태에 의해 필터링이 된다


	:param new: 새로운 알림


	:param viewed: 알림을 확인


	:param waiting: 알림이 확인을 기다린다


	:param declined: A notification is declined: 알림이 거부당했다. 


	:param Accepted: A notification is accepted: 알림이 받아들여졌다.


	:Return: 알림 집합

	"""
def get_updates(request,*args,**kwargs):
	"""현재 가능한 업데이트들을 가져온다.

	:URL: https://api.server.com/api/0/soft/get_update/


	:Version: 0


	:Method: GET 


	:param platform: 필수 사항. 플랫폼 타입 (Windows or Mac).


	:Return 주어진 플랫폼에 따라 현재 가능한 업데이트를 설명한다.
	"""
def get_version(request,*args,**kwargs):
	"""특정 플랫폼에 대한 현재 클라이언트 앱 버전을 반환한다.


	:URL: https://api.server.com/api/0/soft/get_version/


	:Version: 0


	:Method: GET 


	:param platform: 필수 사항. 플랫폼 타입 (Windows or Mac). 매개 변수가 설정되면 메서드는 지정된 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 목록이 반환된다


	:Return: 특정 플랫폼에 대해 현재 앱 버전을 설명하는 객체


	:Error 403: A version for a non:existing platform is requested 존재하지 않는 플랫폼에 대해나 버전을 요청 

	"""
def list_updates(request,*args,**kwargs):
	"""모든 플랫폼 또는 특정 플랫폼에 대한 업데이트 목록을 반환한다.


	:URL: https://api.server.com/api/0/soft/list_updates/


	:Version: 0


	:Method: GET 


	:param platform: 선택 사항. 플랫폼 타입. 매개 변수가 설정되면 메서드는 지정된 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 목록이 반환된다.


	:Return 업데이트 리스트 

"""
def list_versions(request,*args,**kwargs):
	"""특정 플랫폼에 대한 현재 클라이언트 앱 버전 리스트를 반환한다. (관리자용)


	:URL: https://api.server.com/api/0/soft/list_version/


	:Version: 0


	:Method: GET 


	:param platform: 선택 사항. 플랫폼 타입. 매개 변수가 설정되면 메서드는 지정된 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 목록이 반환된다.


	:Return: 최신 버전에서 이전 버전으로 정렬 된 버전 리스트 (즉, 리스트는 추가 시간순으로 정렬).

"""
def set_update(request,*args,**kwargs):
	"""특정 플랫폼에 대한 새로운 업데이트를 설치한다. (관리자용)


	:URL: https://api.server.com/api/0/soft/set_update/


	:Version: 0


	:Method: GET 


	:param platform: 필수 사항. 플랫폼 타입


	:param link_base: 필수 사항. 업데이트 할 다운로드 링크.


	:param version_base: 필수 사항. 업데이트 버전.


	:param link_exp: 선택 사항. 실험적 업데이트에 대한 다운로드 링크


	:param version_exp: 선택 사항. 실험적 업데이트 버전.


	:param competition: 필수 사항. 경쟁 인덱스라고도 부른다. 표준 업데이트를 받는 사용자의 수와 실험중인 사용자의 수를 정의한다. 실험 업데이트 가능성은 다음 공식을 사용하여 계산된다.


	:param x = user_id % competition.


	:param x = 0 인 경우 id = user_id를 가진 사용자는 실험적 업데이트를 받는다. (설정된 경우 경쟁 색인! = 0). 다른 경우 사용자는 표준 업데이트를 받는다. 공식 및 인덱싱에 대한 권한이 있는 사용자가 갱신 요청을 사용할 경우에만 사용된다. 사용자가 인증되지 않은 경우 이 알고리즘은 사용되지 않으며 사용자는 표준 업데이트를 받는다.


	:Return: 특정 플랫폼에 대해 현재 앱 버전을 설명하는 객체
	"""
def set_version(request,*args,**kwargs):
	"""지정된 플랫폼에 대해 현재 클라이언트 응용 프로그램 버전을 새로 설정하거나 업데이트한다. (관리자용)


	:URL: https://api.server.com/api/0/soft/set_version/


	:Version: 0


	:Method: GET 


	:param platform: 필수 사항. 플랫폼 타입


	:param link_base: 필수 사항. 업데이트 할 다운로드 링크.


	:param version_base: 필수 사항. 업데이트 버전.


	:param link_exp: 선택 사항. 실험적 업데이트에 대한 다운로드 링크


	:param version_exp: 선택 사항. 실험적 업데이트 버전.


	:param competition: 필수 사항. 경쟁 인덱스라고도 부른다. 표준 업데이트를 받는 사용자의 수와 실험중인 사용자의 수를 정의한다. 실험 업데이트 가능성은 다음 공식을 사용하여 계산된다.


	:param x = user_id % competition.


	:param x = 0 인 경우 id = user_id를 가진 사용자는 실험적 업데이트를 받는다. (설정된 경우 경쟁 색인! = 0). 다른 경우 사용자는 표준 업데이트를 받는다. 공식 및 인덱싱에 대한 권한이 있는 사용자가 갱신 요청을 사용할 경우에만 사용된다. 사용자가 인증되지 않은 경우 이 알고리즘은 사용되지 않으며 사용자는 표준 업데이트를 받는다.


	:Return: 특정 플랫폼에 대해 현재 앱 버전을 설명하는 객체

	"""
def company_folder_add(request,*args,**kwargs):
	"""
	:Version: 0, 1


	:Method: POST 

"""
def company_folder_add(request,*args,**kwargs):
	"""현재 사용자의 회사 공개 공유 목록에 폴더를 추가한다. 현재 사용자를 위한 방법 메소드이다.


	:URL: https://api.server.com/api/1/shares/company/add/


	:Version: 0


	:Method: GET 


	:param path: 필수 사항, 폴더 경로


	:param public_name: 폴더에 대한 공개 이름. 폴더명이 디폴트로 사용.


	:Error 403: 다른 기업의 사용자에게는 폴더 공유가 금지된다.

"""
def company_folder_add(request,*args,**kwargs):
	"""현재 사용자의 회사의 공유 목록에 폴더를 추가한다. 현재 사용자를 위한 메소드이다.


	:URL: https://api.server.com/api/1/shares/company/add/


	:Version: 0


	:Method: GET 


	:param path: 필수 사항, 폴더 경로


	:param public_name: 폴더에 대한 공개 이름. 폴더명이 디폴트로 사용.


	:Error 403: 다른 기업의 사용자에게는 폴더 공유가 금지된다. 

"""
def company_folder_hide(request,*args,**kwargs):
	"""회사의 공유 목록에서 폴더를 제거한다. 현재 사용자를 위한 메소드이다. 


	:URL: https://api.server.com/api/1/shares/company/hide/


	:param: 둘 중 선택


	:param folder_hash: 폴더 공개 해시


	:param path: 폴더경로


	:Return: 없음


	:Error 404: 회사 폴더 리스트에서 폴더를 찾을 수 없다 

"""