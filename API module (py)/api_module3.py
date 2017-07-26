# -*- coding: utf-8 -*-

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