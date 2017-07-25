def accounts_delete(request, *args, **kwargs):
	"""사용자 계정을 삭제한다. 


	:URL : https://api.server.com/api/0/admin/accounts_delete/


	:Version : 0


	:Method : POST


	:param :• user_id: 선택 사항. 사용자 ID. 


	:Return : 사용자 정보

"""
def accounts_restore(request, *args, **kwargs):
	"""사용자 계정이 완전히 삭제되지 않은 경우에 복구한다.


	:URL : https://api.server.com/api/0/admin/accounts_restore/


	:Version : 0


	:Method : POST


	:param :• user_id: 필수 사항. 사용자 ID. 


	:Return : 사용자 정보

"""
def admin_accounts_disable(request, *args, **kwargs):
	"""사용자 계정을 비활성화 시킨다. 


	:URL : https://api.server.com/api/1/admin/accounts_disable/


	:Version : 0, 1 


	:Method : POST


	:param :• user_id: 필수 사항. 사용자 ID. 


	:Return : 사용자 정보

"""
def admin_accounts_enable(request, *args, **kwargs):
	"""사용자 계정을 활성화시킨다.


	:URL : https://api.server.com/api/1/admin/accounts_enable/


	:Version : 1 


	:Method : POST


	:param :• user_id: 필수 사항. 사용자 ID. 


	:Return : 사용자 정보

"""
def admin_accounts_find_users(request, *args, **kwargs):
	"""주어진 매개변수들과 함께 사용자들의 리스트를 반환한다. 이 메소드는 관리자만 사용할 수 있다.


	:URL : https://api.server.com/api/1/admin/accounts_find_users/


	:Version : 1 


	:Method : POST


	:param :• user_id: 선택 사항. 찾고자 하는 사용자의 아이디


	:Return : 레코드 양 (개수), 레코드 한도 (한도), 사용자 목록 (사용자), 레코드 목록의 오프셋 (오프셋).


	"""
def admin_accounts_generate_login_key(request, *args, **kwargs):
	"""시스템에 액세스하기 위해 임시 키를 생성한다. 시스템에 액세스하기 위해 / accounts / login 메소드로 키를 보낼 수 있다.


	:URL : https://api.server.com/api/0/admin/accounts_generate_login_key/


	:Version : 0


	:Method : POST


	:param :• user_id: 필수 사항. 사용자의 아이디


	:Return : 사용자 아이디, 액세스 키


	"""
	def admin_accounts_set_password(request, *args, **kwargs):
	"""사용자 비밀번호 바꾸는 것을 허용한다.


	:URL : https://api.server.com/api/1/admin/accounts_set_password/


	:Version : 1


	:Method : POST


	:param :• user_id: 필수 사항. 사용자의 아이디


	:Return : 사용자 정보

"""
def assign_role(request, *args, **kwargs):
	"""사용자의 역할을 바꾼다.


	:URL : https://api.server.com/api/0/admin/assign_role/


	:Version : 0


	:Method : POST


	:param :• user_id: 필수 사항. 사용자의 아이디.


	:Return : 사용자 정보

"""
def companies_find(request, *args, **kwargs):
	"""회사 리스트를 반환한다.


	:URL : https://api.server.com/api/1/admin/find_companies/


	:Version : 0


	:Method : GET, POST


	:param :• offset – 오프셋 값.


	:Return : • 회사 – 회사 레코드 구성


	:Error : • 403 - 사용자는 회사의 리스트를 볼 권한이 없다

"""
def company_approve(request, *args, **kwargs):
	"""
	:URL : https://api.server.com/api/1/admin/company/<company id>/approve/


	:Version : 1


	:Method : GET 

"""
def company_cancel_invite_user(request, *args, **kwargs):
	"""사용자 초대 취소 


	:URL : https://api.server.com/api/1/admin/company/<company id>/invite_user/cancel/


	:Version : 1


	:Method : POST 

"""
def company_deny(request, *args, **kwargs):
	"""
	:URL : https://api.server.com/api/1/admin/company/<company id>/deny/


	:Version : 1


	:Method : GET 

"""
def company_edit_user(request, *args, **kwargs):
	"""사용자 초대 취소 


	:URL : https://api.server.com/api/1/admin/company/<company id>/edit_user/


	:Version : 1


	:Method : POST 

"""
def company_invite_user(request, *args, **kwargs):
	"""사용자 초대


	:URL : https://api.server.com/api/1/company/<company id>/invite_user/


	:Version : 1


	:Method : POST  


	:param :• email - 필수 사항. 초대 받는 사용자의 이메일 


	:Return : 사용자 정보.

"""
def company_remove(request, *args, **kwargs):
	"""회사 제거


	:URL : https://api.server.com/api/1/company/<company id>/remove/


	:Method : POST, GET 


	:param :• company_id - 필수 사항, URL 문자열에서 가져온 회사 아이디


	:Return : 없음


	:Error : • 403 - 사용자가 회사 리스트를 볼 권한 없다

"""
def company_status_change(request, *args, **kwargs):
	"""회사의 상태가 활성/비활성에서 변경이 되었는지 확인 또는 변경한다.


	:URL : https://api.server.com/api/1/company/<company id>/status/


	:Method : POST, GET 


	:param :• company_id - 필수 사항, URL 문자열에서 가져온 회사 아이디


	:Return : 회사 현재 상태


	:Error : • 403 - 사용자가 회사 설정을 볼 권한 없다

"""
def create_user(request, *args, **kwargs):
	""" """
	def create_user(request, *args, **kwargs):
	""" """
	def delete_user_feature(request, *args, **kwargs):
	""" """
	def edit_user(request, *args, **kwargs):
	"""사용자 데이터를 수정하는 것을 허용한다 


	:URL : https://api.server.com/api/1/admin/edit_user/


	:Method : POST 


	:param :• user_id - 필수 사항. 사용자 아이디.


	:Return : 사용자 정보 


	:Error : • 404: 주어진 아이디로 사용자를 찾을 수 없다 

"""
def get_locked_logins(request, *args, **kwargs):
	"""잠긴 로그인 리스트를 가져온다 


	:URL : https://api.server.com/api/1/admin/blocked_logins/


	:Method : POST, GET


	:param :없음 


	:Return : 잠긴 로그인의 리스트 


	:Error : 없음

"""
def get_user_by_login(request, *args, **kwargs):
	""" """
def invite_user(request, *args, **kwargs):
	"""초대 이메일을 발송한다.


	:URL : https://api.server.com/api/0/admin/invite_user/


	:Version : 0


	:Method : POST


	:param :• email: 필수 사항. 초대받은 사용자의 이메일


	:Return : 사용자 정보 

"""
def set_user_feature(request, *args, **kwargs):
	""" """
def get_data(request, *args, **kwargs):
	"""측정항목에 대한 데이터를 반환한다.


	:URL : https://api.server.com/api/0/analytics/get_data/


	:Version : 0


	:Method : POST 


	:param :• token: 인증 토큰.


	:Return : 측정항목 값 


	:Error : • 404: 키를 찾을 수 없다 


	:Note : • 이 메소드는 관리자 권한을 필요로 한다 


	"""
def get_metrics(request, *args, **kwargs):
	"""측정 항목의 리스트를 반환한다.


	:URL : https://api.server.com/api/0/analytics/get_metrics/


	:Version : 0


	:Method : GET 


	:param :• 매개 변수와 측정 항목의 리스트 


	:Return : 측정 항목 값 


	:Note : • 이 메소드는 관리자 권한을 필요로 한다 


	"""
def get_multiple_data(request, *args, **kwargs):
	"""주어진 측정항목 리스트에 대한 데이터를 반환한다 


	:URL : https://api.server.com/api/0/analytics/get_multiple_data/


	:Version : 0


	:Method : POST 


	:param :• date_from: 날짜 범위, 타임스탬프.


	:Return : 이름으로 그룹화된 측정항목 값의 리스트.


	:Note : 관리자 권한이 필요하다.


	"""
	def get_result(request, *args, **kwargs):
	"""비동기 API 메소드의 성능 상태를 수신하는 데 도움을 준다.


	:URL : https://api.server.com/api/0/task/<task_id>/


	:Version : 0


	:Method : GET 


	:param :• task_id: 필수 사항. 백그라운드 작업의 ID 


	:Return : 실행 종료 시 사전에 추가 된 임의의 json 딕셔너리.


	:Error : • 404 - 작업을 찾을 수 없다

"""
def check_ws(request, *args, **kwargs):
	"""웹 소켓이 사용가능한지 확인한다.


	:URL : https://api.server.com/api/0/check_ws/


	:Version : 0


	:Method : GET, POST 


	:param :없음 


	:Return : 성공 또는 실패 


	:Error : 없음 

"""
def events(request, *args, **kwargs):
	"""날짜 내림차순으로 정렬된 사용자 이벤트를 반환한다.


	:URL : https://api.server.com/api/0/events/


	:Version : 0


	:Method : GET 


	:param :• skip: 선택 사항. 초기 데이터 오프셋. (Page_by_page 디스플레이 구성이 가능하다.)


	:Return : 이벤트 집합 


	:Return : • type: 이벤트 타입. 아래를 볼 것


	:Note : 1. 폴더 이벤트 


	"""
def files_download_extra(request, *args, **kwargs):
	""" """
def files_extra_create(request, *args, **kwargs):
	"""지정된 파일에 대한 추가 데이터를 생성한다. 그것은 실시간 생성이거나 대기열에서의 지연일 수 있다. 그것은 특정 유형의 추가 데이터 생성을 담당하는 플러그인 설정에 따라 다르다. 이론적으로, 한 파일에 대해 여러 유형의 추가 데이터가 있으면 이 모든 유형이 만들어진다. 추가 자료를 만들 플러그인을 선택할 수 없다. 일부 파일에 이미 일부 외부 데이터가 있는 경우 다시 만든다.


	:URL : https://api.server.com/api/0/files/create_extra/


	:Version : 0


	:Method : POST 


	:param :• path: 필수 사항. 추가 데이터가 생성될 파일의 경로


	:Return : 시작: 추가 데이터가 생성될 때 대기열에 있으면 (플러그인에 따라 다름) True로 설정한다. 대기중인 작업이 없으면 False로 설정한다.


	:Error : 404: 지정한 경로에 파일을 찾을 수 없다. 또는 존재하지 않는 파일 버전이 입력되었다. 

"""
def links_download_extra(request, *args, **kwargs):
	""" 	"""
def links_extra_create(request, *args, **kwargs):
	"""지정된 파일에 대한 추가 기록 생성. 메소드는 API 메소드 / files / create_extra와 유사하지만 공용 파일을 위한 것이라는 차이점이 있다.


	:URL : https://api.server.com/api/0/links/create_extra


	:Version : 0


	:Method : POST


	:param :• hash: 필수 사항. 게시된 객체의 ID 에 해당하는 해시


	:Return : 시작: 추가 데이터가 생성될 때 대기열에 있으면 (플러그인에 따라 다름) True로 설정한다. 대기중인 작업이 없으면 False로 설정한다.


	:Error : 404: 객체를 찾을 수 없다. 

"""
def shares_create_extra(request, *args, **kwargs):
	"""지정된 파일에 대한 추가 데이터를 생성한다. 그것은 실시간 생성이거나 대기열에서의 지연일 수 있다. 그것은 특정 유형의 추가 데이터 생성을 담당하는 플러그인 설정에 따라 다르다. 이론적으로, 한 파일에 대해 여러 유형의 추가 데이터가 있으면 이 모든 유형이 만들어진다. 추가 자료를 만들 플러그인을 선택할 수 없다. 일부 파일에 이미 일부 외부 데이터가 있는 경우 다시 만든다.


	:URL : https://api.server.com/api/1/shares/create_extra/


	:Version : 1


	:Method : POST 


	:param :• invite_hash: 필수 사항. 공유 폴더에 사용자를 초대하기 위한 고유한 해시. method /folders/shared/add/ 로부터의 해시 결과. 


	:Return : 시작: 추가 데이터가 생성될 때 대기열에 있으면 (플러그인에 따라 다름) True로 설정한다. 대기중인 작업이 없으면 False로 설정한다


	:Error : • 403: 공유된 폴더에 대한 접근 권한이 충분하지 않다

"""
def get_set_key(request, *args, **kwargs):
	"""특정 키에 대해 값들의 집합을 반환한다 


	:URL : https://api.server.com/api/0/keyvalue/<key_name>


	:Version : 0


	:Method : GET, POST 


	:param :• value: POST 요청에 대한 새로운 키 값(문자열 또는 JSON)


	:Return : GET 요청에 대한 키 값


	:Error : • 404 - 키를 찾을 수 없다


	"""
def get_storage():
	""" """
def notices(request, *args, **kwargs):
	"""시간의 내림차순으로 필터링 사용자 알림 리스트 


	:URL : https://api.server.com/api/0/notices/


	:Version : 0


	:Method : GET 


	:param :• type: 선택 사항. 알림 타입에 따라서 필터가 됨.


	:Return : 알림 집합


	"""
def get_updates(request, *args, **kwargs):
	"""현재 가능한 업데이트들을 가져온다.


	:URL : https://api.server.com/api/0/soft/get_update/


	:Version : 0


	:Method : GET 


	:param :• platform: 필수 사항. 플랫폼 타입 (Windows or Mac).


	:Return : 주어진 플랫폼에 따라 현재 가능한 업데이트를 설명한다.


	"""
def get_version(request, *args, **kwargs):
	"""특정 플랫폼에 대한 현재 클라이언트 앱 버전을 반환한다.


	:URL : https://api.server.com/api/0/soft/get_version/


	:Version : 0


	:Method : GET 


	:param :platform: 필수 사항. 플랫폼 타입 (Windows or Mac). 매개 변수가 설정되면 메서드는 지정된 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 목록이 반환된다


	:Return : 특정 플랫폼에 대해 현재 앱 버전을 설명하는 객체 


	:Error : • 403: A version for a non-existing platform is requested 존재하지 않는 플랫폼에 대해나 버전을 요청 


	"""
def list_updates(request, *args, **kwargs):
	"""모든 플랫폼 또는 특정 플랫폼에 대한 업데이트 목록을 반환한다.


	:URL : https://api.server.com/api/0/soft/list_updates/


	:Version : 0


	:Method : GET 


	:param :• platform: 선택 사항. 플랫폼 타입. 매개 변수가 설정되면 메서드는 지정된 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 목록이 반환된다.


	:Return : 업데이트 리스트 

"""
def list_versions(request, *args, **kwargs):
	"""특정 플랫폼에 대한 현재 클라이언트 앱 버전 리스트를 반환한다. (관리자용)


	:URL : https://api.server.com/api/0/soft/list_version/


	:Version : 0


	:Method : GET 


	:param :• platform: 선택 사항. 플랫폼 타입. 매개 변수가 설정되면 메서드는 지정된 플랫폼의 버전 목록을 반환한다. 다른 경우에는 모든 플랫폼에 대한 버전 목록이 반환된다.


	:Return : 최신 버전에서 이전 버전으로 정렬 된 버전 리스트 (즉, 리스트는 추가 시간순으로 정렬).

"""
def set_update(request, *args, **kwargs):
	"""특정 플랫폼에 대한 새로운 업데이트를 설치한다. (관리자용)


	:URL : https://api.server.com/api/0/soft/set_update/


	:Version : 0


	:Method : GET 


	:param :• platform: 필수 사항. 플랫폼 타입


	:Return : 특정 플랫폼에 대해 현재 앱 버전을 설명하는 객체 


	"""
def set_version(request, *args, **kwargs):
	"""지정된 플랫폼에 대해 현재 클라이언트 응용 프로그램 버전을 새로 설정하거나 업데이트한다. (관리자용)


	:URL : https://api.server.com/api/0/soft/set_version/


	:Version : 0


	:Method : GET 


	:param :• platform: 필수 사항. 플랫폼 타입


	:Return : 특정 플랫폼에 대해 현재 앱 버전을 설명하는 객체


	"""
def company_folder_add(request, *args, **kwargs):
	"""
	:Version : 0, 1


	:Method : POST 

"""
def company_folder_add(request, *args, **kwargs):
	"""현재 사용자의 회사 공개 공유 목록에 폴더를 추가한다. 현재 사용자를 위한 방법 메소드이다.


	:URL : https://api.server.com/api/1/shares/company/add/


	:Version : 0


	:Method : GET 


	:param :• path - 필수 사항, 폴더 경로


	:Error : • 403 - 다른 기업의 사용자에게는 폴더 공유가 금지된다.

"""
def company_folder_add(request, *args, **kwargs):
	"""현재 사용자의 회사의 공유 목록에 폴더를 추가한다. 현재 사용자를 위한 메소드이다.


	:URL : https://api.server.com/api/1/shares/company/add/


	:Version : 0


	:Method : GET 


	:param :• path - 필수 사항, 폴더 경로


	:Error : • 403 - 다른 기업의 사용자에게는 폴더 공유가 금지된다. 

"""
def company_folder_hide(request, *args, **kwargs):
	"""회사의 공유 목록에서 폴더를 제거한다. 현재 사용자를 위한 메소드이다. 


	:URL : https://api.server.com/api/1/shares/company/hide/


	:param :둘 중 선택


	:Return : 없음 


	:Error : 404: 회사 폴더 리스트에서 폴더를 찾을 수 없다  """