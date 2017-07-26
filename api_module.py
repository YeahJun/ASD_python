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

def company_folders_get(request,*args,**kwargs):
	"""공유 폴더 목록을 반환한다. 현재 사용자를 위한 method다.


	:URL: https://api.server.com/api/1/shares/company/get/


	:param folder_hash: 공유된 폴더의 해시.


	:param offset: 생략할 레코드의 양을 설정.


	:param limit: 레코드의 최대 반환 양.


	:param show_all: 선택 사항. 모든 회사 폴더를 표시하는 플래그(회사 관리자만 해당) 


	:Return list of maps:


	:Return owner_id: 공유 소유 ID


	:Return public_name: 공유 이름


	:Return folder_hash: 다른 사람에게 폴더를 공유하기 위한 해시 값


	:Return owner_name: 폴더 주인의 이름


	:Return collaborators_count: 공동 작업자 수


	:Return modification_time: 최종 수정 시간


	:Return status: 폴더 상태:


	:Return waiting: 현재 폴더에 초대된 사용자


	:Return requested: 현재 사용자가 요청한 폴더에 대한 액세스


	:Return accepted: 현재 사용자가 이 폴더에 접근 가능


	:Return path: 폴더 경로. (현재 사용자가 소유자이거나 폴더가 공유되는 경우에만 비어 있음.)

"""
def company_folders_get_one(request,*args,**kwargs):
	"""공유 폴더 정보를 folder_hash로 반환한다. 현재 사용자를 위한 method다.


	:URL: https://api.server.com/api/1/shares/company/get/(?P<folder_hash>[a:zA:Z0:9:_!]+)/


	:param folder_hash: 공유된 폴더의 해시. 


	:Return a map of:


	:Return owner_id: 공유 소유 ID


	:Return public_name: 공유 이름


	:Return folder_hash: 다른 사람에게 폴더를 공유하기 위한 해시 값


	:Return owner_name: 폴더 주인의 이름


	:Return collaborators_count: 공동 작업자 수


	:Return modification_time: 최종 수정 시간


	:Return status: 폴더 상태:


	:Return waiting: 현재 폴더에 초대된 사용자


	:Return requested: 현재 사용자가 요청한 폴더에 대한 액세스


	:Return accepted: 현재 사용자가 이 폴더에 액세스 가능


	:Return path: 폴더 경로. (현재 사용자가 소유자이거나 폴더가 공유되는 경우에만 비어 있음.)

"""
def company_get_shares(request,*args,**kwargs):
	"""회사 관리자에게만 이미 공유되는 공유 폴더 및 공용 링크 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/company/shared/


	:param name: 필터의 사용자 이름. 기본적으로 모든 사용자를 위한 method다.


	:Return  지도 목록. 각 지도 요소에는 다음 항목들이 포함된다:


	:Return bytes: 파일의 크기


	:Return creation_time: 공유 생성 타임 스탬프


	:Return modification_time: 파일 수정 타임 스탬프


	:Return owner_id: 공유 또는 연결 소유 ID


	:Return owner_name: 공유 또는 연결 소유 이름


	:Return shared_outside : 게시된 폴더에 대해 공동 작업자 또는 소유자가 회사 소속이 아니면 플래그가 True 로 설정 된다. 링크는 항상 True이다.


	:Return src_path: 파일이나 폴더의 경로


	:Return type: 어떤 종류인가. ‘공유’ : 공유된 폴더 / ‘링크’ : 링크
	"""
def company_share_access_accept(request,*args,**kwargs):
	"""폴더 공유 요청을 수락한다.


	:URL: https://api.server.com/api/1/shares/company/accept/


	:param folder_hash: 의무 사항. 회사 폴더 목록 응답의 폴더 해시.


	:param writer: 폴더에 대한 쓰기 권한(True or False), 기본 값만 읽음.


	:Return: 없음.


	:Error 403: 폴더가 공유되지 않았거나 현재 사용자에 대해 공유되지 않았다.


	:Error 404: 폴더 해시 또는 사용자를 찾을 수 없다.

"""
def company_share_access_request(request,*args,**kwargs):
	"""공유 폴더 소유자에게 액세스를 요청한다.


	:URL: https://api.server.com/api/1/shares/company/request/


	:param folder_hash: 의무 사항. 회사 폴더 목록 응답의 폴더 해시.


	:param invitataion: 폴더 소유자에 대한 설명.


	:Return: 없음.


	:Error 403: 현재 사용자에 대해 이미 공유가 되어 있거나 공유가 불가능하다.


	:Error 404: 폴더 해시 또는 사용자를 찾을 수 없다.


	:Error 409: 사용자가 자신의 폴더를 공유할 수 없다.

"""
def company_share_get_requests(request,*args,**kwargs):
	"""회사의 공유 액세스 요청을 반환한다.


	:URL: https://api.server.com/api/1/shares/company/requests/


	:param: 없음.


	:Return: 공유된 정보 목록.

	:Error 403: 현재 사용자에 대해 공유되지 않거나 공유가 허락되지 않았다.

	:Error 404: 폴더 해시 또는 사용자를 찾을 수 없다.

"""
def company_shares_collaborators(request,*args,**kwargs):
	"""공유 폴더의 공동 작업자 목록을 반환한다.


	:URL: https://api.server.com/api/1/company/admin/shares/collaborators/


	:Version: 1


	:Method: GET


	:param userid: 의무 사항. 공유된 폴더 주인의 ID.


	:param path: 의무 사항. 폴더 경로.


	:Return: 공동 작업자 목록.

	:Error 404: 폴더가 존재하지 않는다.


	:Note: is_indirect: 공유 폴더의 직접적이거나 간접적인 공동 작업자. 만약 False이면, 이것은 폴더에 대한 접근 권한을 부여 받은 직접적인 공동 작업자이다. 만약 True이면, 이것은 상위 폴더에 대한 액세스 권한을 부여 받은 간접적인 공동 작업자이다.

"""
def company_shares_remove(request,*args,**kwargs):
	"""공유 폴더에서 사용자를 삭제한다.


	:URL: https://api.server.com/api/1/company/admin/shares/remove/


	:Method: POST


	:param userid: 의무 사항. 공유된 폴더 주인의 ID.


	:param path: 의무 사항. 폴더 경로.


	:param member_login: 의무 사항. 공유 폴더에서 삭제해야 할 로그인.


	:Return 200: 공유 폴더에서 사용자가 삭제되었다.


	:Error 403: 사용자가 공동 작업자가 아니다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def company_shares_unshare(request,*args,**kwargs):
	"""폴더 공유를 멈추거나 폴더에서 모든 사용자를 삭제한다. 모든 공동 작업자로부터 폴더들이 숨어 있다.


	:URL: https://api.server.com/api/1/company/admin/shares/unshare/


	:Method: POST


	:param userid: 의무 사항. 공유된 폴더 주인의 ID.


	:param path: 의무 사항. 폴더 경로.


	:Return 200: 성공적으로 취소되었다.


	:Error 404: 지정된 경로에서 공유 폴더를 찾을 수 없다.

"""
def diff_confirm(request,*args,**kwargs):
	"""AmazonS3에서 차이를 성공적으로 확인한다.


	:URL: https://api.server.com/api/1/files/confirm_from_diff/<path>


	:Version: 1


	:Method: POST


	:param Version: 의무 사항. 클라이언트에 있는 현재 파일의 버전.

	:param Key: ‘method / files / create_from_diff /’에서 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새 버전의 파일을 생성할 것을 확인 가능.


	:Return: 새로운 파일을 위한 메타데이터. See /metadata


	:Error 403: 클라이언트의 파일 버전이 매우 낮다.


	:Error 409: 파일의 새로운 버전을 생성한 후, 새로 생성된 파일의 체크섬이 ‘etc /hosts’ 폴더에 전송된 체크섬과 일치하지 않는다.

"""
def diff_create(request,*args,**kwargs):
	"""새로운 버전의 파일을 생성하기 위해 diff를 로드한다.


	:URL: https://api.server.com/api/1/files/create_from_diff/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 파일의 경로.


	:param checksum: 의무 사항. 새로운 버전의 파일의 체크섬. (파일의 체크섬을 알기 위한 알고리즘으로 CRC32 사용.)


	:param autoconfirm_upload: 선택 사항. Boolean으로 표시. 만약 Ture이면, Amazon의 클라이언트가 diff를 로드한 후 응답 코드 200 대신 코드 303을 받을 것이다. 그리고 응답 헤더 중 하나는 Location 헤더가 될 것이다. 만약 False이면, 클라이언트는 코드 200을 받고 URL을 통해 자체적으로 다운로드하려 한다.


	:param created: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자의 운영 체제에서 파일이 생성되었을 때의 유닉스 타임 스탬프.


	:param modified: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자의 운영 체제에서 파일을 수정할 때의 유닉스 타임 스탬프.


	:param device_id: 선택 사항. 파일이 업로드 되는 파일의 기기ID.


	:param device_reference: 선택 사항. API initiator 로컬 기기의 저장소 안에 링크를 저장하는 보조 필드.


	:Return: Amazon S3에서 diff를 로드하는 데 필요한 데이터. (반환되는 값 중 하나는 나중에 ‘ /files /confirm_from_diff /method’ 를 통해 다운로드가 성공적이었는 지 확인하는 데 중요한 변수이다. 이 매개 변수를 통해 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새 버전의 파일을 생성하는 것을 확인 할 수 있게 한다.)


	:Error 403: 클라이언트의 파일 버전이 매우 낮다.


	:Error 409: 파일의 새로운 버전을 생성한 후, 새로 생성된 파일의 체크섬이 ‘etc /hosts’ 폴더에 전송된 체크섬과 일치하지 않는다.


	:Error 410: 서버에서 diff를 사용하여 파일을 생성할 때 에러가 발생했다.

"""
def download_entire_folder(request,*args,**kwargs):
	"""아카이브의 폴더와 파일이다. 작업 지속 시간은 추가된 파일 수에 따라 달라지며, 결과에 따라 API method를 정기적으로 요청해야 한다. 테스크 준비는 https://api.server.com/api/1/task/<taskid>/ 에서 확인할 수 있다.


	:URL: https://api.server.com/api/1/files/download_as_archive/


	:Version: 0, 1


	:Method: GET


	:param path: 의무 사항. 아카이브에 추가될 폴더 및 파일로 설정된 경로. 


	:param 예: path=/1/2/3&path=/1/2/4


	:param parent_folder: 선택 사항. 아카이브 생성 요청이 수신된 시점에 열려 있는 사용자의 폴더


	:Return: 테스크 식별자

	"""
def download_entire_public_folder(request,*args,**kwargs):
	"""전체 공유 폴더 또는 일부 선택된 항목을 아카이브로 다운로드한다. 작업 지속 시간은 추가된 파일 수에 따라 달라지며, 결과에 대한 API method를 정기적을 요청해야 한다. 테스크 준비는 https://api.server.com/api/1/task/<taskid>/에서 확인할 수 있다.


	:URL: https://api.server.com/api/1/links/download_as_archive/<hash>/


	:Version: 0, 1


	:Method: GET


	:param hash: 의무 사항. 공개된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:param path: 의무 사항. 아카이브에 추가될 파일 및 폴더에 대해 설정된 경로 예: path=/1/2/3&path=/1/2/4


	:param parent_folder: 선택 사항. 아카이브 생성 요청이 수신된 시점에 열려 있는 사용자의 폴더. 예: parent_folder=/1/2


	:Return: 테스크 식별자


	:Error 403: 저작권 침해로 인해 링크가 차단되었다.

	"""
def file_confirm(request,*args,**kwargs):
	"""Amazon S3에 파일을 성공적으로 업로드했는지 확인한다.


	:URL: https://api.server.com/api/1/files/confirm/<path>


	:Version: 1


	:Method: POST


	:param user_id: 의무 사항. 사용자 ID.


	:param temp_name: 의무 사항. 일시적 파일 이름.


	:param overwrite: 선택 사항. 기본적으로 False로 설정 되어있다. 매개 변수가 True로 설정되어 있고 서버에 유사한 이름의 파일이 있는 경우 기존 파일을 덮어쓴다.


	:param size: 선택 사항. 파일의 크기. (매개 변수는 파일 업로드 여부를 확인하는 데 사용)


	:param checksum: 선택 사항. 파일 업로드가 올바른 지 확인하는 데 사용되는 파일 내용의 체크섬.


	:Return: 업로드 되는 파일의 메타데이터. See /metadata.


	:Error 403: 파일 버전이 다르다.


	:Error 404: 명시된 파일을 찾을 수 없다.


	:Error 409: 요청된 경로에 이미 존재한다. (객체가 폴더 또는 파일이거나 매개 변수를 덮어쓰는 경우에만 해당)

"""
def file_create(request,*args,**kwargs):
	"""파일을 서버에 업로드하는 데 필요한 매개 변수를 반환한다.


	:URL: https://api.server.com/api/1/files/create/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 파일의 경로.


	:param overwrite: 선택 사항. 기본적으로 False로 설정. 매개 변수가 True로 설정되어 있고 서버에 유사한 이름의 파일이 있는 경우 기존 파일을 덮어쓴다. 만약 False로 설정되어 있거나 서버에 비슷한 이름의 파일이 있다면, method는 에러 코드 409를 반환한다. 매개 변수는 항상 PC:client에 대해 False로 설정되며, web:client에 대해선 True로 설정된다.

	:param version: 선택 사항. 이전 파일의 버전 숫자. 파일 버전의 올바른 갱신을 보장하는 데 사용한다. 서버의 현재 파일 버전이 지정된 버전과 일치하지 않으면 에러를 반환한다.

	:param create_dirs: 선택 사항. 기본적으로 True로 설정되어 있다. 만약 매개 변수가 False로 설정되면 파일을 생성할 때 시스템이 없는 폴더를 생성하지 않는다.


	:param created: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자의 운영 체제에서 파일을 생성한 시점(miliseconds).


	:param modified: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자의 운영 체제에서 파일을 수정할 때 시간동안 발생한 타임 스탬프.


	:param device_id: 선택 사항. 파일이 업로드 된 기기의 ID.


	:param device_reference: 선택 사항. API initiator 로컬 디바이스 저장소에 파일에 대한 링크를 저장하는 보조 필드.


	:param size: 선택 사항. 파일의 크기. (중복 제거를 사용하여 파일 업로드가 올바른 지 확인)


	:param checksum: 선택 사항. 파일 업로드가 올바른 지 확인. (파일을 중복 제거하는 데 사용되는 파일 내용의 체크섬)


	:param multipart: 선택 사항. 기본적으로 False로 설정. 만약 True이면, multipart 업로드 시작. Multipart 업로드는 추가 헤더를 표시할 수 있는 URL을 사용하여 URL에 대한 PUT method를 실행. Post 요청과 같이 매개 변수는 사용되지 않는다.


	:return headers: 추가적인 HTTP 헤더들. (POST 요청이 사용되는 경우, 이러한 헤더는 매개 변수 사전에 추가됨)


	:return confirm_url: 파일 업로드가 완료되었음을 확인하기 위한 링크.


	:return temp_path: multipart 업로드가 사용되는 경우에만 반환. 다른 파일 파트의 업로드 매개 변수를 수신하는 데 사용.


	:return: 중복 제거가 실행된 경우 ‘method /metadata/<path>’와 동일한 값을 반환.


	:Error 201: 중복 제거로 인해 파일이 생성되었다, 즉, 동일한 크기의 파일과 체크섬이 이미 서버에 존재한다. 응답 텍스트는 ‘method /metadata /<path>’와 동일한 값을 갖는다.


	:Error 400: 파일 버전이 존재하지 않는다.


	:Error 403: 존재하지 않는 폴더에 파일을 업로드하려고 시도하거나 파일을 덮어 쓰려고 할 때, 파일 버전이 일치하지 않는다.


	:Error 404: 파일을 존재하지 않는 폴더에 업로드하려고 시도했거나 create_dirs가 False이다.


	:Error 409: 파일 이름과 덮어 쓰려는 곳에 존재하는 기존 객체의 이름이 충돌한다.

"""
def file_create_part(request,*args,**kwargs):
	"""Multipart 업로드가 사용될 때 파일 부분을 서버에 업로드하는 데 필요한 매개 변수를 반환한다.


	:URL: https://api.server.com/api/1/files/create_part/


	:Version: 0, 1


	:Method: POST


	:param temp_path: 의무 사항. Multipart 업로드가 시작되었을 때 ‘method/ files/ create/’가 반환되는 경로


	:param part_num: 의무 사항. 업로드 된 파일 part의 수.


	:Return url: PUT method를 사용하여 파일을 전송해야 하는 링크.


	:param headers: 추가적인 HTTP 헤더들.


	:Error 404: 지정한 temp_path가 존재하지 않는다.

"""
def file_resolve_link(request,*args,**kwargs):
	"""게시된 파일에 대한 정보를 표시한다. (다운로드 URL 포함)


	:URL: https://api.server.com/api/1/links/get/<hash>/<path>


	:Version: 0, 1


	:Method: GET


	:param hash: 의무 사항. 공개된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:param path: 선택 사항. 게시된 디렉토리와 관련된 파일경로 (즉, 파일이 위치한 폴더가 아닌 다른 폴더가 게시됨)


	:param for_view: 선택 사항. 다운로드 링크가 필요한 용도를 지정: viewing (streaming) : True (the value Content:Type is set), or download : False (the value Content:Disposition is set). 기본적으로 False로 설정.


	:Return: 다운로드한 파일에 대한 정보가 들어 있는 객체


	:Error 404: 노드가 존재하지 않는다. (이유: 잘못된 경로 입력, 노드가 더 이상 공용이 아니거나 노드의 삭제 등)


	:Error 403: 저작권 침해로 인해 링크가 차단되었다.

"""
def file_versions_to_update(request,*args,**kwargs):
	"""클라이언트 앱의 최신 버전으로 특정 파일을 갱신하기 위해 오름차순으로 정렬된 파일 버전 목록을 반환한다. 


	:URL: https://api.server.com/api/1/files/versions_to_update/


	:Version: 0, 1


	:Method: GET


	:param path: 의무 사항. 파일의 경로.


	:Return: 파일 버전을 설명하는 객체 배열.


	:Error 404: 노드가 존재하지 않는다.

	"""
def files_get(request,*args,**kwargs):
	"""파일 내용을 수신할 매개 변수를 반환한다.


	:URL: https://api.server.com/api/1/files/get/<path>


	:Version: 1


	:Method: GET


	:param version: 의무 사항. 클라이언트 앱 현재 파일의 버전 숫자. 기본적으로 대부분의 현재 버전을 사용.

	:param for_view: 선택 사항. 다운로드 링크의 목적: viewing (streaming) : True (the Content:Type valude is set up), download : False (Content:Disposition value is set up). 기본적으로 False로 설정.


	:param deleted: 선택 사항. True일 때 다운로드 링크 제공. 요청된 파일이 삭제된 경우 파일이 삭제되고 404가 나타남.


	:Return: 다운로드한 파일에 관한 정보를 포함한 객체.


	:Error 404: 노드가 존재하지 않는다.
	"""
def files_get_diff(request,*args,**kwargs):
	"""Diff 파일을 로드 할 컨텐츠를 제공한다.


	:URL: https://api.server.com/api/1/files/get_diff/<path>


	:Version: 0, 1


	:Method: GET


	:Return: 다운로드 중인 diff에 대한 정보를 포함하는 객체.


	:Error 404: 노드가 존재하지 않는다.

	"""
def files_restore_version(request,*args,**kwargs):
	"""지정된 파일 버전을 복원한다. (파일이 새 버전을 가져온다.)


	:URL: https://api.server.com/api/1/files/restore/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 파일의 경로.


	:Return: 복원된 버전 파일의 메타데이터.


	:Error 404: 지정된 파일이나 버전을 찾을 수 없다.

"""
def files_search(request,*args,**kwargs):
	"""쿼리 문을 이용해 파일 시스템에서 파일이나 디렉토리를 찾는다.


	:URL: https://api.server.com/api/1/files/search/


	:Version: 1


	:Method: POST


	:param query: 의무 사항. 검색 쿼리.


	:param offset: 선택 사항. 기본값은 0. 찾는 값의 시작.


	:param limit: 선택 사항. 기본값은 0. 찾는 값의 양.

"""
def files_versions(request,*args,**kwargs):
	"""파일 버전의 목록을 반환한다. 생성 날짜 순으로 재귀적으로 정렬되며, 첫 번째 버전은 현재 버전이다.


	:URL: https://api.server.com/api/1/files/versions/<path>


	:Version: 1


	:Method: GET


	:param skip: 선택 사항. 페이지별로 디스플레이를 활성화.


	:param limit: 선택 사항. 제한된 레코드의 양.


	:param extra: 선택 사항. 각 파일 버전에 대한 정보에 추가 데이터를 추가.


	:Return: 파일 버전을 설명하는 객체 배열.


	:Error 404: 지정된 파일이나 버전을 찾을 수 없다.

	"""
def folder_or_file_link(request,*args,**kwargs):
	"""공용 링크를 생성한다.


	:URL: https://api.server.com/api/1/links/create/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 파일이나 폴더의 경로.


	:param ttl: 선택 사항. 링크 작업 시간, 이 시간 이후에는 링크가 유효하지 않다. 간격의 초 단위 값 [0, 31536000]


	:param download_max: 선택 사항. 링크에 대한 참조 수 제한.


	:param password: 선택 사항. 암호를 지정하여 링크의 데이터에 액세스 가능.


	:param notify: 선택 사항.


	:param upload_folder: 서버에 파일을 업로드하기 위해 링크가 생성되었음을 표시.


	:Return: 파일이나 폴더의 메타데이터. See /metadata


	:Error 400: 파일의 다운로드 폴더에 대한 링크를 생성하려고 시도한다.


	:Error 403: 존재하지 않는 파일에 대한 링크를 생성하려고 시도한다.


	:Error 404: 파일이나 폴더를 찾을 수 없다.

"""
def folder_or_file_purge(request,*args,**kwargs):
	"""삭제된 모든 파일(파일 버전 포함)을 지운다.


	:URL: https://api.server.com/api/1/fileops/purge/


	:Version: 1


	:Method: POST


	:param: 없음.


	:Return 200: 파일 및 폴더 제거 작업이 대기 열에 있다.

"""
def folder_or_file_purge_status(request,*args,**kwargs):
	"""사용자 파일 삭제 테스크 상태를 반환한다.


	:URL: https://api.server.com/api/1/fileops/purgestatus/


	:Version: 0, 1


	:Method: POST


	:param: 없음.


	:Return: 사용자의 파일 삭제 테스크 상태.


	"""
def folder_or_file_rename(request,*args,**kwargs):
	"""파일이나 폴더의 이름을 수정한다.


	:URL: https://api.server.com/api/1/fileops/rename/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 파일이나 폴더의 경로.


	:param newname: 의무 사항. 새로운 이름.


	:Return: 이름이 수정된 객체를 위한 메타데이터. See /metadata.


	:Error 404: 지정된 파일이나 폴더를 찾을 수 없다.


	:Note: 이름을 바꾸면 이전 이름이 있는 폴더(파일)가 삭제되고 새 파일 또는 새 이름의 폴더가 생성됨.

"""
def folder_or_file_unlink(request,*args,**kwargs):
	"""공용 링크를 삭제한다.


	:URL: https://api.server.com/api/1/links/delete/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 파일이나 폴더의 경로.


	:Return: 이름이 수정된 객체를 위한 메타데이터. See /metadata.


	:Error 404: 공용 링크를 찾을 수 없다.

"""
def folders_create(request,*args,**kwargs):
	"""새로운 폴더를 생성한다.


	:URL: https://api.server.com/api/1/fileops/folder_create


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 새로운 폴더의 경로.


	:param created: 선택 사항. 클라이언트 앱이 설치된 OS에서 폴더가 생성된 시점.


	:param modified: 선택 사항. 클라이언트 앱이 설치된 OS에서 폴더를 수정한 시점.


	:Return: 새로운 폴더를 위한 메타데이터. See /metadata.


	:Error 403: 주어진 경로의 폴더가 존재하지 않는다.

"""
def folders_or_files_copy(request,*args,**kwargs):
	"""선택한 파일이나 폴더를 새 폴더 또는 동일한 폴더에 복사한다. 파일 버전은 복사되지 않는다.


	:URL: https://api.server.com/api/1/fileops/copy/


	:Version: 1


	:Method: POST


	:param from_path: 의무 사항. 복사할 파일이나 폴더의 초기 경로.


	:param to_path: 의무 사항. 객체가 복사되어야 하는 폴더의 경로.


	:param overwrite: 선택 (기본적으로 True로 설정). 만약 복사될 파일이나 폴더가 이미 존재할 때 덮어쓰려 하고 False로 설정되어 있을 때, http exception에 의해 코드 403을 보여준다.


	:Return: 새로운 파일이나 폴더를 위한 메타데이터.


	:Error 400: 필수 매개 변수 중 하나가 설정되지 않았다.


	:Error 403: 매개 변수 하나가 False로 설정되어 있고 복사된 파일 또는 폴더가 ‘to_path’에 이미 존재한다.


	:Error 404: 복사할 경로를 찾을 수 없거나 객체를 복사해야 하는 폴더를 찾을 수 없다.


	:Error 405: 복사가 실행되는 경로가 폴더가 아니다.


	:Error 424: 폴더를 트리 아래 하위 폴더에 복사하려고 한다. 복사된 폴더는 복사된 새 폴더의 상위 폴더이다. 상위 노드를 하위 노드에 복사하는 것은 금지되어 있다.


	:Note: 파일이나 폴더를 복사하려고 한다. 한 객체(예를 들어, /something)가 복사하려는 폴더에 동일한 이름으로 존재할 때, 그 객체는 something(1)이라는 이름으로 변경되며 위치하게 된다.

"""
def folders_or_files_delete(request,*args,**kwargs):
	"""파일이나 폴더를 삭제한다.


	:URL: https://api.server.com/api/1/fileops/delete/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 삭제될 파일이나 폴더의 경로.


	:param only_empty: 선택 사항. 기본적으로 False로 설정된다. 만약 True이면, 폴더가 비어 있는 상태에서만 삭제된다. 파일을 삭제할 때 매개 변수가 사용되지 않는다.


	:param without_trash: 선택 사항. 기본적으로 False로 설정된다. 만약 True이면, 휴지통으로 이동되지 않고 바로 삭제된다.


	:Return: 복원된 폴더의 메타데이터. See /metadata.


	:Error 403: 사용자가 폴더의 삭제를 허용하지 않거나 매개 변수 ‘only_empty’가 True이기에 폴더가 비어 있다. 


	:Error 404: 지정된 폴더를 찾을 수 없다.

"""
def folders_or_files_move(request,*args,**kwargs):
	"""선택된 파일이나 폴더를 새로운 폴더로 옮긴다. 파일 버전은 옮겨지지 않는다. 즉, 버전 관리 지점에서 새 파일을 생성하고 이전 폴더에서 삭제하는 것처럼 보인다.


	:URL: https://api.server.com/api/1/fileops/move/


	:Version: 1


	:Method: POST


	:param from_path: 의무 사항. 옮겨져야 하는 파일이나 폴더의 초기 경로.


	:param to_path: 의무 사항. 객체가 옮겨질 폴더의 경로.


	:param overwrite: 선택 (기본적으로 True로 설정). 만약 복사될 파일이나 폴더가 이미 존재할 때 덮어쓰려 하고 False로 설정되어 있을 때, http exception에 의해 코드 403을 보여준다.


	:Return: 옮겨지는 객체에 대한 정보 (새로운 경로를 포함)


	:Error 400: 필수 매개 변수 중 하나가 입력되지 않았다.


	:Error 403: 매개 변수가 False로 설정되어 있고 이동할 폴더나 파일이 이미 ‘to_path’에 존재한다.


	:Error 404: 이동할 경로를 찾을 수 없다. 혹은 객체가 필요로 하는 폴더가 발견되지 않았다.


	:Error 405: 객체를 이동하는 경로가 폴더가 아니다.


	:Error 409: 객체를 기존과 같은 폴더로 이동하려 한다.


	:Error 412: 공동 작업자가 공유 루트 폴더를 다른 사용자의 공용 폴더로 이동하거나 다른 사용자의 공동 작업자가 만든 공용 폴더로 이동하려고 시도한다. (몇몇 폴더는 일종의 마운트 지점이기 때문에 공유 루트 폴더이다. 몇몇 폴더를 이동하는 것은 논리와 맞지 않다.)


	:Error 424: 폴더를 트리 아래 하위 폴더에 복사하려고 한다. 복사된 폴더는 복사된 새 폴더의 상위 폴더이다. 상위 노드를 하위 노드에 복사하는 것은 금지되어 있다.


	:Error 501: 기능이 구현되지 않았다.


	:Note: 이동하는 것이 파일이나 폴더라는 것도 중요하지만, 이동하는 장소는 폴더라는 것도 중요하다. 이 API method를 사용할 때 고려해야 할 몇 가지 유의 사항이 있다.


	:Note: 파일이나 폴더를 복사하려고 한다. 한 객체(예를 들어, /something)가 복사하려는 폴더에 동일한 이름으로 존재할 때, 그 객체는 something(1)이라는 이름으로 변경되며 위치하게 된다. 한 폴더가 이동하면, 다른 공동 작업자들은 자동적으로 접근 권한을 잃는다. 이것은 1. 이동하거나, 2. 생성하거나, 3. 삭제될 때 발생한다는 특징이 있다.

"""
def folders_or_files_multi_delete(request,*args,**kwargs):
	"""여러 파일이나 폴더를 삭제한다.


	:URL: https://api.server.com/api/1/fileops/multi/delete/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 삭제될 파일들이나 폴더들의 경로. 예: path=/1/2/3 & path=/1/2/4


	:param only_empty: 선택 사항. 기본적으로 False로 설정된다. 만약 True이면, 폴더가 비어 있는 상태에서만 삭제된다. 파일을 삭제할 때 매개 변수가 사용되지 않는다.


	:param without_trash: 선택 사항. 기본적으로 False로 설정된다. 만약 True이면, 휴지통으로 이동되지 않고 바로 삭제될 것이다.


	:Return: 삭제될 파일들이나 폴더들의 메타데이터. See /metadata.


	:Error 403: 사용자가 폴더의 삭제를 허용하지 않았거나 매개 변수 ‘only_empty’가 True이기에 폴더가 비어 있다. 


	:Error 404: 지정된 폴더를 찾을 수 없다.
	"""
def folders_or_files_multi_undelete(request,*args,**kwargs):
	"""삭제된 파일이나 폴더를 복원한다.


	:URL: https://api.server.com/api/1/fileops/multi/undelete/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 복원될 파일들이나 폴더들의 경로. 예: path=/1/2/3 & path=/1/2/4


	:Return: 응답 텍스트의 필드 error_code에 있는 각 경로.


	:Error 403: 사용자가 파일이나 폴더의 복원을 허용하지 않았다. (상위 폴더에서 삭제했을 수도 있다.)


	:Error 404: 지정된 폴더를 찾을 수 없다.

	"""
def folders_or_files_undelete(request,*args,**kwargs):
	"""삭제된 파일이나 폴더를 복원한다.


	:URL: https://api.server.com/api/1/fileops/undelete/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 복원될 파일이나 폴더의 경로.


	:Return: 복원될 파일이나 폴더의 메타데이터. See /metadata.


	:Error 403: 사용자가 파일이나 폴더의 복원을 허용하지 않았다. (상위 폴더에서 삭제했을 수도 있다.)


	:Error 404: 지정된 폴더를 찾을 수 없다.

"""
def get_encoded_file_name(request,file_name):
	"""Content:Disposition 헤더에 대해 인코딩된 파일 이름을 반환한다.

"""
def get_file_for_download(request,path,version=None,for_view=False,deleted=True):
	"""
	:Version: 0, 1
\
	:Method: POST

"""
def handover(request,*args,**kwargs):
	"""공동 작업자 중 하나에 공유 폴더를 할당한다. 다음과 같은 작업이 수행된다: 공동 작업자의 스토리지에 파일을 복사한다. 공유 폴더에 대한 액세스를 다시 시도한다. 이전 소유자의 폴더에서 새 소유자의 폴더로 모든 공동 작업자를 이동한다. 이전 소유자는 파일 복사를 보존한다.


	:URL: https://api.server.com/api/1/fileops/handover/


	:Version: 0, 1


	:Method: POST


	:param path: 의무 사항. 새 공동 작업자에게 전달될 폴더의 경로.


	:param member_id: 의무 사항. 소유권자 권한이 부여된 공동 작업자 ID.


	:Return: 없음.


	:Error 400: 주요 매개 변수가 입력이 안 됐다.


	:Error 403: 지정된 공동 작업자가 폴더에 접근할 수 없거나, 공동 작업자가 초대를 받아들이지 않았다.


	:Error 404: 새 공동 작업자에게 할당해야 하는 폴더를 찾을 수 없거나 지정된 사용자가 존재하지 않는다.


	:Note: 폴더 공유는 백그라운드에서 수행된다. 공동 작업자는 접미사가 공유 폴더에 추가되고 이 폴더의 파일이 공유 폴더와 동일한 이름을 가진 새 폴더로 복사되는 것을 본다.

"""
def link_metadata(request,*args,**kwargs):
	"""공유 노드에 대한 정보를 반환한다. 노드가 분리되어 별도의 항목으로 공유되는 경우에는 실행되지 않는다.


	:URL:  https://api.server.com/api/1/links/metadata/<hash>/<path>


	:Version: 1


	:Method: GET


	:param hash: 의무 사항. 공유된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:param path: 선택 사항. 게시된 폴더와 관련된 파일 또는 폴더의 경로.


	:param dirs_only: 선택 사항. 기본적으로 False로 설정되어 있다. 만약 true이면, 폴더가 listing=true일 때 목록을 포함한다.


	:param extra: 선택 사항. 기본적으로 True로 설정. 메타데이터와 함께 추가 정보를 반환한다. MP3(파일이 있는 경우), 미리 보기 정보(파일이 있는 경우) 등이 있을 수 있다.


	:param offset: 선택 사항. 기본적으로 0으로 설정되어 있다. 폴더 내용 목록의 처음부터 오프셋. MP3(파일이 있는 경우), 미리 보기 정보(파일이 있는 경우) 등이 있을 수 있다.


	:param limit: 선택 사항. 기본적으로 0으로 설정. 폴더 목록을 나열할 때 반환되는 객체의 최대 이름 수.


	:Return: 파일이나 폴더를 위한 메타데이터, 결과는 API method 메타데이터에 의해 생성되는 것과 유사하다. 유일한 차이점은 게시된 폴더와 관련하여 모든 경로가 입력된다는 점이다. 공유 루트 폴더에 대한 정보가 표시되면, JSON 결과에도 게시된 루트 폴더의 이름이 포함된 매개 변수가 존재한다.


	:Error 403: 저작권 침해로 인해 링크가 차단되었다.


	:Error 404: 노드를 찾을 수 없다. 경로를 잘못 입력했거나, 노드가 공유되어 있지 않거나, 삭제 되었을 경우이다. 

"""
def links_get(request,*args,**kwargs):
	"""사용자가 생성한 공용 링크 목록을 반환한다.


	:URL: https://api.server.com/api/1/links/


	:Version: 1


	:Method: GET


	:param: 없음.


	:Return: 공용 링크가 생성된 일련의 메타데이터이다.

	"""
def metadata(request,*args,**kwargs):
	"""파일이나 폴더의 메타데이터를 반환한다.


	:URL: https://api.server.com/api/1/metadata/<path>


	:Version: 1


	:Method: GET


	:param Hash: 선택 사항. 각 요청에 대한 각 요청은 텍스트에서 해시 매개 변수를 반환한다. 각 /metadata요청은 이 값을 포함해야 한다. 파일 또는 폴더의 메타데이터가 마지막 요청에서 변경되지 않을 경우 응답은 전체 응답 텍스트가 아닌 304 상태를 포함한다. 이 매개 변수는 경로가 파일이나 listing=false일 때 무시된다. 공유 폴더에 대한 해시는 모든 공동 작업자에게 동일하다.


	:param Listing: 선택 사항. 기본적으로 true로 설정. 만약 true이면, 폴더 메타 데이터 뿐만 아니라 컨텐츠 목록도 반환된다. 목록에는 각 목록 항목에 대한 메타데이터가 포함된다. 만약 false이면, 컨텐츠는 반환되지 않는다.


	:param dirs_only: 선택 사항. 기본적으로 false로 설정. 만약 true이면, listing = true일 때 목록에 포함된다.


	:param deleted: 선택 사항. 기본적으로 false로 설정. 만약 true이고, 삭제된 객체가 목록에 포함되어 있으면, 해당 객체는 목록에 포함되지 않는다.


	:param version: 선택 사항. 메타데이터를 제공해야 하는 특정 파일 버전이다. 디렉터리에 대해 버전 관리가 지원되지 않으면 매개 변수는 무시된다. 매개 변수가 제공되지 않으면 최신 파일 버전이 사용된다.

	:param extra: 선택 사항. 기본적으로 true로 설정. 추가 정보를 메타데이터와 함께 반환. MP3(파일이 있는 경우), 미리 보기 정보(파일이 있는 경우) 등이 있을 수 있다. CL:1558 형식 참조.


	:param offset: 선택 사항. 기본적으로 0으로 설정. 폴더 내용 목록의 처음부터 오프셋.


	:param Limit: 선택 사항. 기본적으로 0으로 설정. 폴더 목록에 대해 반환되는 최대 객체 수.


	:param order_by: 선택 사항. 기본적으로 ‘이름. 지정된 필드를 기준으로 결과를 정렬할 필요가 있음을 나타냄. 가능한 값은 ‘name’, ‘:name’, ‘modified_time’, ‘:modified_time’ 등이 있다.


	:Return: 매개 변수 경로에 따라 파일 또는 폴더의 메타데이터. 폴더의 경로이며 목록 매개 변수가 True이면, 메타데이터는 폴더 목록 뿐만 아니라 목록의 각 객체에 대한 메타데이터도 포함한다. 게다가 헤더 ETag에는 객체 해시가 포함되어 있다. 이 해시는 if:None:Match 헤더의 서버로 전송할 때 클라이언트 측에서 캐시에 사용할 수 있다. 서버의 객체가 변경되지 않은 경우, 응답은 304 코드가 포함된 빈 메시지를 포함한다.


	:Return size: 파일 크기. 폴더에는 항상 0바이트가 있다.


	:Return bytes: 파일 크기를 바이트 단위로 설정. 폴더에는 항상 0이 있다.


	:Return checksum: 파일 체크섬 (md5).


	:Return folder: 폴더인지 파일인지의 여부 표현.


	:Return path: 파일이나 폴더의 경로, с /로 시작. 루트 폴더 메타데이터가 요청된 경우 값은 “/”.


	:Return shared: 폴더의 공유 여부 표현.


	:Return shared_hash: 폴더 해시. 익명 사용자에 대해 폴더를 공유하는 경우에 중요.


	:Return public_link: 폴더 또는 파일에 대한 공용 링크가 없는 경우 해당 값은 False.


	:Return deleted: 객체의 삭제 여부 표현.


	:Return version: 현재 파일의 버전. 폴더에는 항상 0이 있다.


	:Return hash: /metadata를 부르는 데 사용되는 폴더 해시. 파일에 대해 반환되지 않는다.


	:Return thumbnail: 파일에 미리 생성된 썸네일이 있는 경우, 그 썸네일의 경로. 미리 보기가 잘못된 것이 아니면 False.


	:Return icon: 특정 파일 형식의 아이콘(미리 보기를 지원하지 않는 파일)


	:Return modified: 파일이나 폴더가 최종 수정된 날짜.


	:Return owner: 파일이나 폴더 소유자의 사용자 ID.


	:Return owner_name: 파일이나 폴더 소유자의 이름.


	:Return author: 파일(또는 지정된 파일 버전) 작성자 또는 폴더 작성자


	:Return author_name: 파일(또는 지정된 파일 버전) 작성자의 이름 또는 폴더 작성자의 이름


	:Return client_data: 클라이언트 앱 중 하나에 의해 설치된 데이터를 다른 클라이언트로 전송.


	:Return fs_type: 폴더와 관련된 파일 시스템 유형. 객체가 폴더 또는 마운트 지점이 아닌 경우 이 필드가 표시되지 않는다.


	:Return is_last_page: 만약 True이면, 폴더 목록의 마지막 결과 페이지이며, 틀린 페이지가 있다면 더 많은 페이지가 있다는 의미.


	:Error 304: 폴더 내용이 마지막 요청에서 변경되지 않았다. (If:None:Match 헤더에 의해 결정됨)


	:Error 404: 파일이나 폴더를 찾을 수 없다.
	"""
def metadata_full_listing(request,*args,**kwargs):
	"""테스크를 생성하거나 준비된 파일 트리 구조를 다운로드하는 URL을 반환한다.


	:URL: https://api.server.com/api/1/metadata_full_listing/


	:Version: 1


	:Method: GET


	:param listing_request_id: 테스크 식별자. 선택 사항. 빈 값을 전송하거나 보내지 않으면 서버가 사용자의 파일 구조 전체 목록을 생성하고 이 테스크의 식별자를 반환하는 테스크를 생성한다. 테스크 ID를 전달하면 작업 결과로 파일을 다운로드할 URL을 반환한다.


	:Return Listing_request_id: 테스크ID, 만약 매개 변수 listing_request_id 가 지정되지 않았거나 비어 있다면???


	:Return Url: 매개 변수 listing_request_id가 지정된 경우 결과에 대한 참조.


	:Error 404: 요청 ID가 잘못 되었거나 데이터가 아직 준비되지 않았다. (테스크가 이미 시작된 경우, 응답 본문에는 진행 상황에 대한 정보가 포함된다.)

	:Note: 서버의 목록을 작성하는 작업이 완료되면 클라이언트는 알림 시스템을 통해 이에 대한 통지를 받게 된다. 이 통지문은 metadata_full_listing의 형식을 가지고 있으며 비슷하게 보인다.
	:Note: Listing_reuest_id 필드가 이전에 API/ metadata_full_listing/ 에서 얻은 listing_request_id와 일치해야 한다는 것에 유의해야 한다. 이후에 클라이언트는 API method /metadata_full_listing 에 파일 트리 목록을 사용할 수 있는 URL을 요청한다.
	"""
def migration_contents_accept(request,*args,**kwargs):
	"""컨텐츠 마이그레이션 요청 수락


	:URL: https://api.server.com/api/1/migration_contents/accept/


	:Version: 1


	:Method: POST


	:param Hash: 의무 사항. 거부를 위한 해시 코드.


	:Return: 마이그레이션에 대한 정보

	"""
def migration_contents_add(request,*args,**kwargs):
	"""한 사용자에서 다른 사용자로 컨텐츠 마이그레이션 요청을 생성한다.


	:URL: https://api.server.com/api/1/migration_contents/add/


	:Version: 1


	:Method: POST


	:param member_login: 의무 사항. 사용자를 위한 로그인.


	:param path: 선택 사항. 파일 경로. (기본적으로 모든 사용자의 파일을 마이그레이션.)


	:param invitation: 컨텐츠 리시버를 위한 초대 메시지.


	:param cleanup: 마이그레이션 후 폴더 정리.


	:Return: 수락을 위한 해시 코드.

	"""
def migration_contents_get(request,*args,**kwargs):
	"""마이그레이션 요청에 대한 정보를 반환한다. 현재 사용자를 위한 method이다.


	:param path: 선택 사항. 파일 경로.


	:param whoose: 가능한 값:


	:param my: 소유자의 폴더만 반환.


	:param others: 다른 사용자가 마이그레이션한 폴더 반환.


	:param nvalue: 마이그레이션 된 모든 폴더 반환. 


	:param status: 선택 사항. 상태 목록. 가능한 값: ‘수락, ‘요청’. 기본값은 모든 상태를 반환.


	:Return: 마이그레이션 정보 목록.

"""
def migration_contents_reject(request,*args,**kwargs):
	"""컨텐츠 마이그레이션 요청을 거절한다.


	:URL: https://api.server.com/api/1/migration_contents/reject/


	:Version: 1


	:Method: POST


	:param hash: 의무 사항. 거절을 위한 해시 코드.


	:Return: 없음.

"""
def migration_contents_remove(request,*args,**kwargs):
	"""컨텐츠 마이그레이션 요청을 제거한다.


	:URL: https://api.server.com/api/1/migration_contents/remove/


	:Version: 1


	:Method: POST


	:param hash: 의무 사항. 삭제를 위한 해시 코드.


	:Return: 없음.

"""
def shared_collaborators(request,*args,**kwargs):
	"""공유된 폴더를 위한 공동 작업자 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/collaborators/


	:Version: 1


	:Method: GET


	:param path: 의무 사항. 폴더의 경로.


	:Return: 공동 작업자 집합.


	:Error 404: 폴더를 찾을 수 없다.

	:Note is_indirect: 공유 폴더의 직접적이거나 간접적인 공동 작업자. 만약 False이면, 폴더에 대한 접근 권한을 부여 받은 직접적인 공동 작업자이다. 만약 True이면, 상위 폴더에 대한 접근 권한을 부여 받은 간접적인 공동 작업자이다.

"""
def shared_folder_accept(request,*args,**kwargs):
	"""공유 폴더에 대한 초대를 수락한다. 새 폴더가 사용자 루트 폴더에 나타난다. 공동 작업자가 이미 이름이 비슷한 폴더를 가지고 있는 경우, 시퀀스 번호가 폴더 이름에 추가된다. 최대 시퀀스 번호는 10이다. 공동 작업자가 폴더의 이름을 바꿀 수 있다. 이름 변경은 다른 공동 작업자의 시스템에 있는 폴더의 이름에 영향을 주진 않는다.


	:URL: https://api.server.com/api/1/shares/accept/


	:Version: 1


	:Method: POST


	:param hash: 의무 사항. 공유된 폴더에 대한 고유한 초대 해시. 해시는 method /folders /shared /add /에서 수신된다.


	:Return 200: 사용자가 공유 폴더에서 삭제되었다.


	:Error 403: 해시가 특정 사용자의 공유 폴더를 지정하지 않았다.

"""
def shared_folder_add(request,*args,**kwargs):
	"""
	:URL: https://api.server.com/api/1/shares/add/


	:Version: 1


	:Method: POST


	:param path: 의무 사항. 폴더의 경로.


	:param member_login: 선택 사항. 폴더에 대한 액세스 권한이 필요한 사용자의 로그인. (매개 변수를 지정하지 않으면 모든 사용자가 초대를 수락할 수 있도록 액세스 권한이 부여된다.)


	:param writer: 선택 사항. 사용자가 폴더에 객체를 생성할 권한이 있는 경우. 기본적으로 False로 설정.


	:param invitation: 선택 사항. 사용자에게 보낼 초대장.


	:param public_view: 선택 사항. 초대 해시를 통해 모든 사용자에게 읽기 권한을 부여. 기본적으로 False로 설정. (초대를 수락하거나 거부한 후 모든 읽기 권한이 소멸.)


	:param group_id: 선택 사항. 폴더를 공유한 그룹의 식별자. Group_id가 지정된 경우 member_id는 무시된다.


	:Return: 공유된 폴더를 위한 고유한 초대 토큰.


	:Error 403: 폴더에 대한 액세스 권한을 부여할 수 없다.


	:Error 404: 폴더를 찾을 수 없다.


	:Error 409: 사용자가 자신을 위해 폴더에 대한 액세스 권한을 부여하려고 한다.


	:Error 424: 다른 사용자가 공유하는 루트 폴더가 있는 폴더에 대한 액세스 권한을 부여하려고 한다. (이러한 폴더에 액세스 권한을 부여할 순 없다.) 예를 들어, 사용자 A가 사용자 B에게 폴더에 대한 액세스를 허용했다. 사용자 B는 루트 폴더를 폴더 트리의 일부 폴더로 이동하고 사용자 C 폴더에 대한 액세스 권한을 부여했다. 이러한 방법으로, 사용자 C는 사용자 A에서 공유되는 파일 및 폴더에 액세스 할 수 있으며 사용자 A는 이에 대해 알지 못한다.


	:Note: 공동 작업자가 이미 폴더에 대한 액세스 권한을 부여 받은 경우, 이 method는 빈 텍스트 메시지에서 코드 200을 반환한다.

	"""

def shared_folder_decline(request,*args,**kwargs):
	"""공유된 폴더에 대한 초대를 거부한다.


	:URL: https://api.server.com/api/1/shares/decline/


	:Version: 0, 1


	:Method: POST


	:param hash: 필수 사항. 사용자를 공유된 폴더에 초대하는 고유한 초대 해시. 이 해시는 /folders/shared/add/ method의 결과.


	:Return 200: 사용자가 공유된 폴더로부터 삭제되었다.


	:Error 403: 해시가 폴더 접근 권한이 부여된 특정 사용자의 공유 폴더를 지정하지 않았다.

"""
def shared_folder_remove(request,*args,**kwargs):
	"""공유된 폴더로부터 사용자를 제거한다.


	:URL: https://api.server.com/api/1/shares/remove/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 폴더 경로.


	:param member_login: 필수 사항. 공유된 폴더로부터 삭제될 사용자의 로그인


	:Return 200: 사용자가 공유된 폴더로부터 삭제되었다.


	:Error 403: 사용자가 폴더에 대한 공동 작업자가 아니다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def shared_folder_uninvite(request,*args,**kwargs):
	"""공동 작업자 또는 그룹과 함께 공유 폴더에 초대한다. 그룹을 지정하면, member_login 매개 변수는 무시된다.


	:URL: https://api.server.com/api/1/shares/uninvite/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 폴더의 경로.


	:param member_login: 선택 사항. 초대를 받을 사용자의 고유 ID. 만약 매개 변수를 지정하지 않으면, 모든 사용자로부터 접근이 반환된다.


	:param group_id: 선택 사항. 그룹 ID, 그룹 ID가 지정된 경우, member_login 매개 변수는 무시.


	:Return 200: 초대가 성공적으로 취소되었다.


	:Error 403: 초대가 취소되지 않았다. (예를 들어, 이미 수락되었을 경우).

"""
def shared_folder_unshare(request,*args,**kwargs):
	"""폴더에 대한 접근을 취소하고, 모든 공동 작업자를 삭제한다. 모든 공동 작업자의 계정에서 폴더가 사라진다.


	:URL: https://api.server.com/api/1/shares/unshare/


	:Version: 0, 1


	:Method: POST


	:param path: 필수 사항. 공유된 폴더의 경로.


	:Return 200: 취소가 성공적으로 실행된 경우.


	:Error 404: 지정된 경로를 가진 폴더를 찾을 수 없다.

"""
def shared_update_collaborator(request,*args,**kwargs):
	"""일부 디렉토리에 접근 권한을 부여 받은 일부 공동 작업자의 접근 권한을 갱신한다.


	:URL: https://api.server.com/api/1/shares/update_collaborator/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 폴더의 경로.


	:param member_login: 필수 사항. 공유된 폴더에 접근 권한을 부여 받은 사용자의 로그인.


	:param writer: 필수 사항. True나 False가 될 수 있음. 쓰기 권한을 제공하거나 주지 않음.


	:param group_id: 선택 사항. 공유 디렉터리에 대한 접근 권한이 부여된 사용자들의 그룹 ID. 만약 member_login이 지정됐다면, 이 매개 변수는 무시된다.


	:Return 200: 업데이트 성공.


	:Error 403: 폴더에 대한 접근이 허락되지 않았다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def shared_get(request,*args,**kwargs):
	"""공유된 폴더들의 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/


	:Version: 1


	:Method: GET


	:param whose: 선택 사항. 공유된 폴더의 유형을 정의. 예상 값:


	:param my: 오직 소유자의 폴더들만 반환


	:param others: 다른 사용자가 공유한 폴더를 내 공동 작업으로 반환


	:param company: 사용자 회사에서 공유 및 게시된 폴더를 반환


	:param: 기본적으로 해당 method는 모든 유형의 폴더를 반환.


	:Return 200: 각 폴더에 대한 metadata 목록.

"""
def shared_get_invites(request,*args,**kwargs):
	"""공동 작업자에 대해 활성화된 초대 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/invites/


	:Version: 1


	:Method: GET


	:param: 없음


	:Return 200: 아직 수락되지 않은 초대장의 목록
	"""
def trash_clear(request,*args,**kwargs):
	"""휴지통을 비운다.


	:URL: https://api.server.com/api/1/trash/clear/


	:Version: 1


	:Method: POST


	:param paths: 선택 사항. 휴지통에서 삭제할 파일이나 폴더 경로의 목록


	:Note: 이 method는 동시에 존재하지 않는다.

"""
def trash_content(request,*args,**kwargs):
	"""현재 휴지통에 있는 파일 및 폴더들에 대한 정보를 가진 목록을 반환한다.


	:URL: https://api.server.com/api/1/trash/ 


	:Version: 1


	:Method: GET


	:param dirs_only: 선택 사항. 기본적으로 0. 만약 1이라면, 디렉터리는 목록에 포함.


	:param extra: 선택 사항. 기본적으로 True. extradata라고 불리는 추가적인 정보를 메타데이터와 함께 반환. 이는 mp3태그(파일이 mp3 형태일 경우), 미리보기 정보(파일이 문서인 경우) 또는 썸네일 정보(파일이 이미지인 경우) 등.


	:param offset: 선택 사항. 기본적으로 0. 휴지통 내용 목록의 처음부터 오프셋


	:param limit: 선택 사항. 기본적으로 0. 휴지통 내용 목록을 요청하는 동안 반환되는 객체의 최대 개수.


	:Return: 휴지통안에 있는 각 객체에 대한 metadata 목록. 게다가, 휴지통 해시는 Etag 헤더에 반환된다. 이 해시는 If:None:Match 헤더의 서버로 전송될 때 클라이언트 측에서 캐시로 사용할 수 있다. 서버의 휴지통 내용이 변경되지 않을 경우, 304 코드를 반환한다.


	:Return: 응답의 형태는 API method/metadata의 반환 값과 유사하다. 하지만 객체 정보의 필드 경로 대신, 필드 이름이 반환된다. 이 필드는 이것을 휴지통으로부터 복원할 때 객체 ID로 사용된다. 또한 객체가 삭제되기 전에 객체가 위치한 경로를 나타내는 필드인 restore_path도 추가된다.


	:Error 304: 휴지통 내용이 마지막 요청에 의해 변경되지 않았다. (이는If:None:Match에 의해 결정).


	:Error 404: 휴지통이나 휴지통 안에 있는 객체를 찾을 수 없다. (예를 들어, 요청이 수행되는 동안 삭제되는 경우.)

"""
def trash_restore(request,*args,**kwargs):
	"""휴지통으로부터 객체를 복원한다.


	:URL: https://api.server.com/api/1/trash/restore/<name>


	:Version: 1


	:Method: POST


	:param name: 필수 사항. 휴지통 안에 있는 객체 이름.


	:param overwrite: 선택 (기본적으로 1). 폴더나 파일이 사용자 파일 공간에 이미 복원되어 있고 매개 변수 overwrite가 0이라면, http:exception 403 코드를 띄워준다.


	:Return: 이 method는 동시에 존재하지 않는다.

"""
def trash_shared_content(request,*args,**kwargs):
	"""공유된 폴더에 위치하고 있고 현재 휴지통에 있는 파일이나 폴더에 대한 정보 목록을 반환한다.


	:URL: https://api.server.com/api/1/trash/from_shared/<path>


	:Version: 1


	:Method: GET


	:param dirs_only: 선택 사항. 기본적으로 0. 만약 1이라면, 디렉터리는 목록에 포함.


	:param extra: 선택 사항. 기본적으로 True. extradata라고 불리는 추가적인 정보를 메타데이터와 함께 반환. 이는 mp3태그(파일이 mp3 형태일 경우), 미리보기 정보(파일이 문서인 경우) 또는 썸네일 정보(파일이 이미지인 경우) 등.


	:param offset: 선택 사항. 기본적으로 0. 휴지통 내용 목록의 처음부터 오프셋


	:param limit: 선택 사항. 기본적으로 0. 휴지통 내용 목록을 요청하는 동안 반환되는 객체의 최대 개수.


	:Return: 현재 휴지통에 있는 공유 폴더의 각 객체에 대한 metadata 목록. 게다가, Etag 헤더는 공유된 폴더 소유자의 휴지통에 대한 해시를 가지고 있다. 이 해시는 If:None:Match 헤더의 서버로 전송될 때 클라이언트 측에서 캐시로 사용할 수 있다. 서버의 휴지통 내용이 변경되지 않을 경우, 304 코드를 반환한다.


	:Return: 응답의 형태는 API method/metadata의 반환 값과 유사하다. 하지만 객체 정보의 필드 경로 대신, 필드 이름이 반환된다. 이 필드는 이것을 휴지통으로부터 복원할 때 객체 ID로 사용된다. 또한 객체가 삭제되기 전에 객체가 위치한 경로를 나타내는 필드인 restore_path도 추가된다.


	:Error 304: 휴지통 내용이 마지막 요청에 의해 변경되지 않았다. (이는If:None:Match에 의해 결정).


	:Error 400: 해당 폴더 (공유된 접근이 가능한) 가 이 사용자에게 허락되지 않았다.


	:Error 404: 휴지통이나 휴지통 안에 있는 객체를 찾을 수 없다. (예를 들어, 요청이 수행되는 동안 삭제되는 경우.)

"""
def trash_shared_restore(request,*args,**kwargs):
	"""휴지통으로부터 공유된 폴더에 위치해 있는 객체를 복원한다.


	:URL: https://api.server.com/api/1/trash/restore/<name>/from_shared/<path>


	:Version: 1


	:Method: POST


	:param name: 필수 사항. 휴지통 안에 있는 파일 이름.


	:param path: 필수 사항. 공유된 폴더의 경로.


	:param overwrite: 선택 (기본적으로 1). 폴더나 파일이 사용자 파일 공간에 이미 복원되어 있고 매개 변수 overwrite가 0이라면, http:exception 403 코드를 띄워준다.


	:Note: 이 method는 동시에 존재하지 않는다.

"""
def upload_folder_file_create(request,*args,**kwargs):
	"""서버로 파일을 업로드하는데 필요한 매개 변수들을 반환한다.


	:URL: https://api.server.com/api/1/links/upload_folders/file_create/<hash>


	:Version: 1


	:Method: POST


	:param hash: 필수 사항. 파일 업로드를 위한 공용 해시로, links/create/에 의해 생성.


	:param created: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 생성된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param modified: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 수정된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param device_id: 선택 사항. 파일에 업로드 된 디바이스 ID.


	:param device_reference: 선택 사항. API initiator의 로컬 디바이스 스토리지에 파일에 대한 링크를 저장하는 보조 필드.


	:param size: 선택 사항. 생성할 파일의 크기. 매개 변수는 중복을 제거하고 파일 업로드가 제대로 되었는지 확인하는데 쓰임.


	:param checksum: 선택 사항. 파일 중복 제거와 파일 업로드가 제대로 이루어 졌는지 확인하는 checksum(md5).


	:param password: 선택 사항. 생성된 링크에 접근하기 위해 암호가 필요할 경우, 이 매개 변수를 통해 전달.


	:Return url: multipart 업로드가 사용되는 경우 파일에 전송해야 하는 파일에 대한 링크


	:Return parameters: POST 요청의 추가적 매개 변수 (이는 multipart 업로드에서 PUT method가 적용되는 경우 사용되지 않음).


	:Return headers: 추가적인 HTTP 헤더. POST 요청이 사용될 때, 이러한 헤더들은 매개 변수 딕셔너리에 추가.


	:Return confirm_url: 파일 업로드가 완료되었음을 확인하기 위한 주소 링크.


	:Return temp_path: 오직 multipart 업로드가 사용될 때 반환; 이 매개 변수는 다른 파일 파트의 업로드 매개 변수를 받아오는데 사용.


	:Return: 중복 제거가 수행된 경우 method는 /metadata/<path> method와 동일한 값을 반환한다.


	:Error 201: 중복 제거의 결과로 파일이 생성되었다. 즉, 동일한 크기의 파일과 checksum이 이미 서버에 있다. 응답 텍스트는 /metadata/<path> method의 반환 값을 갖는다.


	:Error 400: 효력 없는 요청이 실행되었다.


	:Error 402: 저장하기에 공간이 충분하지 않다.


	:Error 403: 파일을 업로드하기 위한 권한이 부족하다. 사용된 해시는 오직 다운로드에 대해 활성화 되며, 해시 등을 사용해 파일을 불러오는 것은 제한된다.


	:Error 404: 존재하지 않는 폴더에 파일 업로드를 시도했다.

"""
def accounts_accept_offer(request,*args,**kwargs):
	"""사용자가 제안을 수락했음을 확인한다.


	:URL: https://api.server.com/api/1/accounts/accept_offer/


	:Version: 0, 1


	:Method: POST


	:param: 없음


	:Return 200: 수락되었다.

"""
def accounts_approve(request,*args,**kwargs):
	"""등록 확인 URL의 일부인 확인 토큰을 통해 등록을 확인한다. 이 URL은 등록 후 사용자 이메일 주소로 전송되는 메시지에 나열된다.


	:URL: https://api.server.com/api/1/accounts/approve/


	:Version: 0, 1


	:Method: GET


	:param hash: 필수 사항. 사용자의 등록을 확인할 수 있는 토큰


	:Return: 사용자 정보


	:Error 404: 해당 토큰을 가진 사용자를 찾을 수 없다.
	"""
def accounts_cancel_token_remote_wipe(request,*args,**kwargs):
	"""auth_token에 대해 remote_wipe 플래그를을 취소한다.


	:URL: https://api.server.com/api/1/accounts/cancel_token_remote_wipe


	:Method: POST


	:param token_id: auth_token ID


	:Error 404: AuthToken을 찾을 수 없다.

"""
def accounts_change_profile_settings(request,*args,**kwargs):
	"""사용자 프로파일의 매개 변수들을 수정한다(이름, 비밀번호 등).


	:URL: https://api.server.com/api/1/accounts/change_profile/


	:Version: 0, 1


	:Method: POST


	:param name: 선택 사항. 새 사용자 이름.


	:param password: 선택 사항. 새 사용자 비밀번호. 사용자 이메일 주소로 특수 링크가 전송. 사용자가 링크를 따라가면, 해커에 의해 비밀번호가 바뀐 경우 사용자가 계정 반환 가능.


	:param lang: 선택 사항. 인터페이스 언어 (가능한 값은 “en”, “ru”, “de”).


	:param timezone: 선택 사항. 사용자의 타임 존 (다음과 같은 시간 가능 “Europe/Moscow”, “America/Los_Angeles” etc. 더 다양한 정보는, see List of tz database time zones).


	:param extra_info: 사용자에 대한 추가 정보.


	:Return: 없음.


	:Error 200: 비밀번호가 바뀌지 않았다.


	:Error 400: 시스템에서 사용자를 찾을 수 없거나 매개 변수 중 하나가 유효하지 않다. 모든 매개 변수들은 선택사항이지만, 적어도 하나는 입력되어야 한다.

"""
def accounts_check(request,*args,**kwargs):
	"""사용자의 계정이 존재하는지 확인한다.


	:URL: https://api.server.com/api/1/accounts/check/


	:Version: 1


	:Method: GET


	:param login: 필수 사항. 사용자 로그인.


	:Return: 사용자의 존재확인, 있으면 {‘status’: ‘ok’} 없으면 {‘status’: ‘not found’}


	:Error 404: 로그인한 사용자를 찾을 수 없다.

"""
def accounts_decline_offer(request,*args,**kwargs):
	"""제안 확인을 취소한다.


	:URL: https://api.server.com/api/0/accounts/decline_offer/


	:Version: 0, 1


	:Method: POST


	:param: 없음


	:Return 200: 확인이 허락되었다.


	:Error 405: 해당 method는 설정에 의해 제한되었다.


	:Note: 이 method는 설정 옵션 can_decline_off가 True여야 활성화된다.

"""
def accounts_feedback(request,*args,**kwargs):
	"""앱에 대한 피드백을 보낸다.


	:URL: https://api.server.com/api/1/accounts/feedback/


	:Version: 0, 1


	:Method: POST


	:param name: 선택 사항. 피드백을 보낸 사용자의 이름.


	:param email: 선택 사항. 피드백을 보낸 사용자의 이메일.


	:param comment: 필수 사항. 메시지 텍스트.


	:Return 200: 피드백이 전송되었다. 이 응답은 사용자가 앱 로그(필요한 경우)를 다운로드 할 수 있는 선택적인 매개 변수인 “url_upload_logs”를 가진 JSON을 포함한다. URL에 데이터를 업로드하기위해 POST method가 사용된다. 파일 자체가 “log”key와 함께 전송된다. 


	:Return 예: curl :F “log=@/home/strannik/Temp/MountBit:v10.pdf” 


	:Return: –header “User:Agent: desktop:client:win” –progress:bar

"""
def accounts_feedback_list(request,*args,**kwargs):
	"""앱 사용에 대한 피드백들의 목록을 받아온다. (이 method는 관리자에 한해서 활성화된다.)


	:URL: https://api.server.com/api/1/accounts/feedback_list/


	:Version: 0, 1


	:Method: GET


	:param limit: 선택 사항. 결과 목록에서 값의 양을 제한


	:param offset: 선택 사항. 결과 목록에서의 값 오프셋.


	:param order_field: 선택 사항. 필드로 정렬 (기본적으로 날짜).


	:param order_direction: 선택 사항. 정렬 순서 (기본적으로 오름차순).


	:Return: 피드백 목록
	"""
def accounts_get(request,*args,**kwargs):
	"""사용자 계정 정보에 대해 반환한다.


	:URL: https://api.server.com/api/1/accounts/get/


	:Version: 1


	:Method: GET


	:param user_id: 선택 사항. 사용자 ID. 매개 변수가 생략되었거나 권한이 위임된 사용자가 아닌 경우, 권한이 있는 사용자에 대한 정보가 반환된다. 매개 변수가 입력되었고 관리자가 method를 호출하는 경우, 지정된 사용자에 대한 정보가 반환된다.


	:Return: 사용자 계정 정보

	"""
def accounts_get_offer(request,*args,**kwargs):
	"""제안 텍스트를 요청한다.


	:URL: https://api.server.com/api/1/accounts/get_offer/ 


	:Version: 0, 1


	:Method: GET


	:param: 없음


	:Return HTML: 제안 문서


	:Note: 제안 텍스트는 key offer를 가진 key 값에 저장되고, 만약 key가 존재하지 않거나 비어 있으면 결과는 비어 있다.

"""
def accounts_login(request,*args,**kwargs):
	"""auth token을 반환한다.


	:URL: https://api.server.com/api/1/accounts/login/


	:Version: 1


	:Method: POST


	:param login: 필수 사항. 준비된 형식으로의 사용자 로그인.


	:param password: 필수 사항. 사용자 비밀번호.


	:param permanent_auth: 선택 사항. 기본적으로 boolean 필드는 False. 즉, 토큰 요청은 제한된 기간 내에 유효. True로 설정되면, 영구적인 토큰이 전송.


	:param device_description: 선택 사항. 사용자가 로그인하는 디바이스에 대한 설명. 이 필드가 비어 있고 영구적인 토큰이 요청되면, 이 값은 <로그인 날짜> + <사용자 에이전트>로 반환.


	:Return: Auth token 정보 dict. 반환

	"""
def accounts_logout(request,*args,**kwargs):
	"""Token의 삭제 여부를 반환한다.


	:URL: https://api.server.com/api/1/accounts/logout/


	:Version: 0, 1


	:Method: POST


	:param: 매개 없음, authorization 헤더는 토큰을 삭제할 때 사용


	:Return: 실행 상태에 대한 응답 코드:


	:Return 200: 성공


	:Return 404: 토큰을 삭제하는 것이 불가능하다.

"""
def accounts_recover_lost_password(request,*args,**kwargs):
	"""이 로그인과 관련된 계정에 임시로 접근하는 데 필요한 메시지를 주어진 로그인으로 전송한다.


	:URL: https://api.server.com/api/1/accounts/recover_lost_password/


	:Version: 1


	:Method: POST


	:param login: 필수 사항. 암호를 승인한 다음, 암호를 변경하는 데 사용되는 메시지 전송


	:Return: 없음.


	:Error 400: 해당 시스템에서 로그인한 사용자를 찾을 수 없다.

"""
def accounts_remove(request,*args,**kwargs):
	""" """
def accounts_remove_login(request,*args,**kwargs):
	"""특정 사용자의 로그인을 삭제한다.


	:URL: https://api.server.com/api/1/accounts/remove_login/


	:Version: 1


	:Method: POST


	:Method: Headers


	:Method: Mountbit:Auth: authorization 토큰.


	:param login: 삭제될 로그인.


	:Return 200: 성공


	:Return 400: 사용자의 마지막 로그인을 삭제할 수 없다.


	:Return 404: 로그인을 찾을 수 없다.

"""
def accounts_remove_token(request,*args,**kwargs):
	"""사용 가능한 영구 토큰 중 하나를 제거한다.


	:URL: https://api.server.com/api/1/accounts/remove_token/


	:URL: https://api.server.com/api/1/accounts/remove_permanent_token/ (deprecated)


	:Version: 0, 1


	:Method: POST


	:param token_id: 필수 사항. 삭제될 토큰의 ID.


	:Return 200: 토큰이 삭제되었다.


	:Return 404: 토큰을 찾을 수 없다.

"""
def accounts_resend_message_for_approve(request,*args,**kwargs):
	"""사용자가 아직 확인하지 않은 경우 등록 확인을 위해 두번째 메시지를 전송한다.


	:URL: https://api.server.com/api/1/accounts/resend_message_for_approve/


	:Version: 1


	:Method: POST


	:param login: 로그인하여 메시지를 재전송할 것인지 확인.


	:Return: 없음


	:Error 403: 사용자가 이미 등록을 확인했다.

"""
def accounts_token_wiped(request,*args,**kwargs):
	"""remote_wipe 플래그가 있는 auth_token을 제거한다.


	:URL: https://api.server.com/api/1/accounts/token_wiped


	:Method: POST


	:Error 404: remote_wipe플래그가 있는 auth_token을 찾을 수 없다.

"""
def accounts_tokens(request,*args,**kwargs):
	"""현재 사용자에 대한 auth 토큰을 반환한다.


	:URL: https://api.server.com/api/1/accounts/permanent_tokens/


	:URL: https://api.server.com/api/1/accounts/tokens/


	:Version: 0, 1


	:Method: GET


	:param include_not_permanent: 응답할 영구 토큰을 추가하지 않는다.


	:Return: 사용자 토큰 목록

	:Note: 디바이스 설명은 실제 디바이스 버전과 호환되지 않을 수 있다.

"""
def company_change(request,*args,**kwargs):
	"""회사 설정을 변경한다. 이는 회사나 시스템 관리자의 접근 권한을 필요로 한다.


	:URL: https://api.server.com/api/1/company/<compnay id>/change/


	:Method: POST


	:param company_id: 필수 사항. URL 문자열로부터 가져온 회사 ID.


	:param name: 회사 이름.


	:param domain: 회사 도메인.


	:param logo_url : 로고 URL.


	:param ldap_is_enabled: LDAP 활성화 여부 (true | false)


	:param ldap_address: LDAP 주소.


	:param ldap_port: LDAP 포트.


	:param ldap_basedn: LDAP 검색을 수행하기 위한 LDAP 기본 DN.


	:param ldap_user_attribute: 사용자의 로그인 이름을 저장하는 LDAP 서버의 속성


	:param ldap_user_agent_dn: 전체 사용자 에이전트 DN이 있는 LDAP 속성


	:param ldap_user_agent_password: 사용자 에이전트 암호가 있는 LDAP 속성


	:param public_links_allow: 공용 링크 허용 여부


	:param wizard_state: 웹 프론트 엔드에 대한 마법사 상태를 저장, 마법사 : 유용한 구성 프로세스


	:param notification_email: 주(state) 회사에 대한 알림을 위한 이메일.


	:Return: 공용 회사 정보, please see accounts/company/<id>/ API method.


	:Error 403: 사용자가 회사의 설정을 바꿀 수 있는 권한이 없다.


	:Error 404: 주어진 ID를 가진 회사를 찾을 수 없다.

"""
def company_change_users_quota(request,*args,**kwargs):
	"""사용자에 대한 quota_size와 hard_quota_size를 변경한다.


	:URL: https://api.server.com/api/1/accounts/company/change_users_quota


	:Method: POST


	:param company_id: 필수, URL 문자열로부터 가져온 회사 ID


	:param users_id: 필수, 사용자 ID 목록


	:param quota_size: 필수, 사용자들에 대한 할당량


	:Return: 에러 정보와 성공과 실패에 대한 정보를 가진 사용자들의 공용 정보

	:Error 403: 사용자가 회사의 데이터를 열람할 수 있는 권한이 없다.

	:Error 404: 사용자나 회사를 찾을 수 없다.
"""
def company_claer_logo(request,*args,**kwargs):
	"""회사 로고를 지운다.


	:URL: https://api.server.com/api/1/company/<company_id>/logo_clear/


	:Method: POST, GET


	:param company_id: 필수 사항. URL 문자열로부터 가져온 회사 ID


	:Return: 응답 데이터 없음.


	:Error 404: 주어진 ID로 회사를 찾을 수 없다.

"""
def company_confirm_logo(request,*args,**kwargs):
	"""로고가 업로드 되었는지 확인한다.


	:URL: https://api.server.com/api/1/company/<company_id>/logo_confirm/


	:Method: POST, GET


	:param company_id: 필수, URL 문자열로부터 가져온 회사 ID


	:param temp_name: 임시 파일 이름


	:param size: 회사 로고 파일 크기, 파일 업로드 확인을 위해 사용


	:param checksum: 로고 md5 checksum, 파일 업로드 확인을 위해 사용


	:Return: 없음.


	:Error 404: 주어진 ID를 가진 회사를 찾을 수 없다.

"""
def company_create_logo(request,*args,**kwargs):
	"""회사 로고를 생성한다.


	:URL: https://api.server.com/api/1/company/<company_id>/logo_upload/


	:Method: POST, GET


	:param size: 이미지 파일 크기.


	:param checksum: md5 control checksum


	:param path: 로고 파일 이미지의 경로.


	:Return url: 이미지 파일을 업로드 하기 위한 URL


	:Return confirm_url: 업로드 되었는지 확인하기 위한 URL


	:Error 403: 사용자가 회사의 설정을 바꿀 수 있는 권한을 가지고 있지 않다.


	:Error 404: 주어진 ID를 가진 회사를 찾을 수 없다.

"""
def company_create_user(request,*args,**kwargs):
	"""회사를 만든다.


	:URL: https://api.server.com/api/1/accounts/company/<company_id>/create_user/


	:Method: POST, GET


	:param company_id: 필수 사항. URL 문자열로부터 가져온 회사 ID


	:param login: 필수 사항. 사용자 로그인.


	:param name: 필수 사항. 사용자 이름.


	:param password: 필수 사항. 사용자 비밀번호.


	:Return: /accounts/get과 비슷한 사용자 공용 정보.


	:Error 402: 사용자 할당량이 초과되었다.


	:Error 403: 사용자가 회사의 설정을 바꿀 수 있는 권한을 가지고 있지 않다.


	:Error 404: 주어진 ID를 가진 회사를 찾을 수 없다.

"""
def company_get(request,*args,**kwargs):
	"""회사 정보 데이터를 반환한다.


	:URL: https://api.server.com/api/1/accounts/company/<company_id>/


	:Method: GET


	:param company_id: URL문자열로부터 가져온 회사 ID


	:Return 회사 사용자에 대한 것:


	:Return company_id: 회사 ID


	:Return name: 회사 이름


	:Return owner_id: 회사의 소유자 ID


	:Return employees_count: 회사 노동자의 수


	:Return logo_url: 로고 URL


	:Return domain: 서브도메인 네임


	:Return storage_size: 저장 공간 크기


	:Return quota_size: 할당량


	:Return registration_date: 회사 등록 날짜


	:Return 회사 관리자를 위해 api는 모든 사용자의 정보를 보여주고:


	:Return ldap_is_enabled: LDAP 활성화 여부


	:Return ldap_address: LDAP 주소


	:Return ldap_port: LDAP 포트


	:Return ldap_basedn: LDAP 검색을 수행하기 위한 LDAP 기본 DN.


	:Return ldap_user_attribute: 사용자의 로그인 이름을 저장하는 LDAP 서버의 속성


	:Return ldap_user_agent_dn: 전체 사용자 에이전트 DN이 있는 LDAP 속성


	:Return ldap_user_agent_password: 사용자 에이전트 암호가 있는 LDAP 속성


	:Return public_links_allow: 공용 링크의 허용 여부


	:Error 403: 사용자가 회사의 데이터를 열람할 수 있는 권한을 가지고 있지 않다.


	:Error 404: 주어진 ID를 가진 회사를 찾을 수 없다.

"""
def company_get_public(request,*args,**kwargs):
	"""도메인 네임으로 구분한 회사의 공용 정보를 반환한다.


	:param domain: 회사 도메인 값.


	:Return: 회사 정보를 가진 JSON 딕셔너리.


	:Error 404: 이 도메인을 가진 회사를 찾을 수 없다.

"""
def company_user_token_cancel_remove(request,*args,**kwargs):
	"""토큰을 제거를 취소한다.


	:URL: https://api.server.com/api/1/company/user_permanent_token/cancel_remove


	:URL: https://api.server.com/api/1/company/user_tokens/cancel_remove/


	:Method: POST


	:param token_id: 토큰 ID


	:Return: 응답 데이터 없음.


	:Error 403: 사용자가 회사의 데이터를 열람할 수 있는 권한을 가지고 있지 않다.


	:Error 404: 사용자 또는 토큰을 찾을 수 없다.

"""
def company_user_token_remove(request,*args,**kwargs):
	"""회사 사용자의 토큰을 제거하거나 원격으로 토큰을 지운다. 이는 회사 관리자에 의해 사용된다.


	:URL: https://api.server.com/api/1/company/user_permanent_token/remove


	:URL: https://api.server.com/api/1/company/user_tokens/remove/ 


	:Method: POST


	:param token_id: 토큰 ID


	:param remote_wipe: remote wipe 플래그


	:Return: 응답 데이터 없음.


	:Error 403: 사용자가 회사의 데이터를 열람할 수 있는 권한을 가지고 있지 않다.


	:Error 404: 사용자 또는 토큰을 찾을 수 없다.

"""
def company_user_tokens(request,*args,**kwargs):
	"""사용자에 대한 토큰 목록을 반환한다. 이는 회사 관리자에 의해 사용된다.


	:URL: https://api.server.com/api/1/company/user_permanent_tokens


	:URL: https://api.server.com/api/1/company/user_tokens/


	:Method: GET, POST


	:param userid: 회사에서의 사용자 ID.


	:param include_not_permanent: 영구 토큰 미포함.


	:Return: 토큰의 목록, 각 레코드는


	:Return device_description: 설명 문자열


	:Return id: 토큰 ID


	:Return created: 생성된 날짜에 대한 타임스탬프


	:Return is_synced: PC나 MAC에 싱크가 되었는지


	:Return last_action: 마지막 API 요청에 대한 정보

	:Error 403: 사용자가 회사의 데이터를 열람할 수 있는 권한을 가지고 있지 않다.

	:Error 404: 사용자를 찾을 수 없다.

"""
def company_users(request,*args,**kwargs):
	"""회사 고용인의 목록을 반환한다.


	:URL: https://api.server.com/api/1/accounts/company/<company_id>/users


	:Method: GET, POST


	:param company_id: URL 문자열로부터 가져온 회사 ID


	:Return :회사 노동자들의 목록, 각 레코드는


	:Return userid: 노동자 ID


	:Return name: 노동자 이름


	:Return position: 노동자 역할

	:Error 403: 사용자가 회사의 데이터를 열람할 수 있는 권한을 가지고 있지 않다.


	:Error 404: 주어진 ID를 가진 회사를 찾을 수 없다.

"""
def company_users_disable(request,*args,**kwargs):
	"""회사안에서 사용자를 비활성화한다.


	:URL: https://api.server.com/api/1/accounts/company/<company_id>/users_disable/


	:Method: POST


	:param company_id: 필수, URL 문자열로부터 가져온 회사 ID


	:param user_id: 필수, 사용자들의 ID 목록


	:param reason: 비활성화된 이유


	:param remote_wipe: 모든 디바이스의 내용 지우기


	:Return: /accounts/get과 비슷한 사용자 공용 정보


	:Error 404: 주어진 ID를 가진 회사나 사용자를 찾을 수 없다.

"""
def company_users_enable(request,*args,**kwargs):
	"""회사 안에서 사용자를 활성화한다.


	:URL: https://api.server.com/api/1/company/<company_id>/users_enable/


	:Method: POST


	:param company_id: 필수 사항. URL 문자열로부터 가져온 회사 ID


	:param user_id: 필수 사항. 사용자 ID


	:param reason: 활성화 이유


	:Return: /accounts/get과 비슷한 사용자 공용 정보


	:Error 404: 주어진 ID를 가진 회사나 사용자를 찾을 수 없다.

"""
def get_invited(request,*args,**kwargs):
	"""초대 토큰에 따라 사용자의 로그인을 반환한다.


	:URL: https://api.server.com/api/1/accounts/getinvited/


	:Version: 1


	:Method: GET


	:param hash: 필수 사항. 초대 토큰.


	:Return: 초대를 보낸 사용자 로그인을 반환한다.


	:Error 404: 해당 초대 토큰을 가진 사용자를 찾을 수 없다.

"""
def get_value(request,*args,**kwargs):
	"""지정된 key를 사용하여 사용자가 저장한 값을 받아온다.


	:URL: https://api.server.com/api/1/accounts/get_value/


	:Version: 1


	:Method: GET


	:param key: 선택 사항. 이 key는 요청한 값을 검색하는데 사용.


	:Return 200: 다음과 같은 반환 값을 갖는데, key를 찾았으면 {key: value};


	:Return: key를 찾지 못하였으면, {key: null}을 반환한다.

"""
def set_value(request,*args,**kwargs):
	"""지정된 key를 사용하여 사용자가 입력한 임의의 값을 저장한다.


	:URL: https://api.server.com/api/1/accounts/set_value/


	:Version: 1


	:Method: POST


	:param key: 필수 사항. 사용자가 지정한 값을 쓰거나 업데이트하는 데 사용되는 key.


	:param value: 필수 사항. Key에 대한 값.


	:Return 200: 값이 성공적으로 생성되거나 업데이트되었다.

"""
