# -*- coding: utf-8 -*-

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
