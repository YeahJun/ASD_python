def company_folders_get(request, *args, **kwargs):
	"""공유 폴더 목록을 반환한다. 현재 사용자를 위한 method다.


	:URL : https://api.server.com/api/1/shares/company/get/


	:param :folder_hash – 공유된 폴더의 해시.


	:Return : list of maps:

"""
def company_folders_get_one(request, *args, **kwargs):
	"""공유 폴더 정보를 folder_hash로 반환한다. 현재 사용자를 위한 method다.


	:URL : https://api.server.com/api/1/shares/company/get/(?P<folder_hash>[a-zA-Z0-9-_!]+)/


	:param :folder_hash – 공유된 폴더의 해시. 


	:Return : • a map of:

"""
def company_get_shares(request, *args, **kwargs):
	"""회사 관리자에게만 이미 공유되는 공유 폴더 및 공용 링크 목록을 반환한다.


	:URL : https://api.server.com/api/1/shares/company/shared/


	:param :name – 필터의 사용자 이름. 기본적으로 모든 사용자를 위한 method다.


	:Return : • 지도 목록. 각 지도 요소에는 다음 항목들이 포함된다:


	"""
def company_share_access_accept(request, *args, **kwargs):
	"""폴더 공유 요청을 수락한다.


	:URL : https://api.server.com/api/1/shares/company/accept/


	:param :folder_hash – 의무 사항. 회사 폴더 목록 응답의 폴더 해시.


	:Return : 없음.


	:Error : 403 – 폴더가 공유되지 않았거나 현재 사용자에 대해 공유되지 않았다.

"""
def company_share_access_request(request, *args, **kwargs):
	"""공유 폴더 소유자에게 액세스를 요청한다.


	:URL : https://api.server.com/api/1/shares/company/request/


	:param :folder_hash – 의무 사항. 회사 폴더 목록 응답의 폴더 해시.


	:Return : 없음.


	:Error : 403 – 현재 사용자에 대해 이미 공유가 되어 있거나 공유가 불가능하다.

"""
def company_share_get_requests(request, *args, **kwargs):
	"""회사의 공유 액세스 요청을 반환한다.


	:URL : https://api.server.com/api/1/shares/company/requests/


	:param :없음.


	:Return : 공유된 정보 목록.


	
	:Error : 403 – 현재 사용자에 대해 공유되지 않거나 공유가 허락되지 않았다.

"""
def company_shares_collaborators(request, *args, **kwargs):
	"""공유 폴더의 공동 작업자 목록을 반환한다.


	:URL : https://api.server.com/api/1/company/admin/shares/collaborators/


	:Version : 1


	:Method : GET


	:param :userid - 의무 사항. 공유된 폴더 주인의 ID.


	:Return : 공동 작업자 목록.


	
	:Error : 404 – 폴더가 존재하지 않는다.


	:Note : is_indirect - 공유 폴더의 직접적이거나 간접적인 공동 작업자. 만약 False이면, 이것은 폴더에 대한 접근 권한을 부여 받은 직접적인 공동 작업자이다. 만약 True이면, 이것은 상위 폴더에 대한 액세스 권한을 부여 받은 간접적인 공동 작업자이다.

"""
def company_shares_remove(request, *args, **kwargs):
	"""공유 폴더에서 사용자를 삭제한다.


	:URL : https://api.server.com/api/1/company/admin/shares/remove/


	:Method : POST


	:param :userid - 의무 사항. 공유된 폴더 주인의 ID.


	:Return : 200: 공유 폴더에서 사용자가 삭제되었다.


	:Error : 403: 사용자가 공동 작업자가 아니다.

"""
def company_shares_unshare(request, *args, **kwargs):
	"""폴더 공유를 멈추거나 폴더에서 모든 사용자를 삭제한다. 모든 공동 작업자로부터 폴더들이 숨어 있다.


	:URL : https://api.server.com/api/1/company/admin/shares/unshare/


	:Method : POST


	:param :userid - 의무 사항. 공유된 폴더 주인의 ID.


	:Return : 200: 성공적으로 취소되었다.


	:Error : 404: 지정된 경로에서 공유 폴더를 찾을 수 없다.

"""
def diff_confirm(request, *args, **kwargs):
	"""AmazonS3에서 차이를 성공적으로 확인한다.


	:URL : https://api.server.com/api/1/files/confirm_from_diff/<path>


	:Version : 1


	:Method : POST


	:Version : Key – ‘method / files / create_from_diff /’에서 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새 버전의 파일을 생성할 것을 확인 가능.


	:Return : 새로운 파일을 위한 메타데이터. See /metadata


	:Error : 403: 클라이언트의 파일 버전이 매우 낮다.

"""
def diff_create(request, *args, **kwargs):
	"""새로운 버전의 파일을 생성하기 위해 diff를 로드한다.


	:URL : https://api.server.com/api/1/files/create_from_diff/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 파일의 경로.


	:Version : checksum – 의무 사항. 새로운 버전의 파일의 체크섬. (파일의 체크섬을 알기 위한 알고리즘으로 CRC32 사용.)


	:Return : Amazon S3에서 diff를 로드하는 데 필요한 데이터. (반환되는 값 중 하나는 나중에 ‘ /files /confirm_from_diff /method’ 를 통해 다운로드가 성공적이었는 지 확인하는 데 중요한 변수이다. 이 매개 변수를 통해 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새 버전의 파일을 생성하는 것을 확인 할 수 있게 한다.)


	:Error : 403: 클라이언트의 파일 버전이 매우 낮다.

"""
def download_entire_folder(request, *args, **kwargs):
	"""아카이브의 폴더와 파일이다. 작업 지속 시간은 추가된 파일 수에 따라 달라지며, 결과에 따라 API method를 정기적으로 요청해야 한다. 테스크 준비는 


	:URL : https://api.server.com/api/1/files/download_as_archive/


	:Version : 0, 1


	:Method : GET


	:param :path - 의무 사항. 아카이브에 추가될 폴더 및 파일로 설정된 경로. 


	:Return : 테스크 식별자


	"""
def download_entire_public_folder(request, *args, **kwargs):
	"""전체 공유 폴더 또는 일부 선택된 항목을 아카이브로 다운로드한다. 작업 지속 시간은 추가된 파일 수에 따라 달라지며, 결과에 대한 API method를 정기적을 요청해야 한다. 테스크 준비는


	:URL : https://api.server.com/api/1/links/download_as_archive/<hash>/


	:Version : 0, 1


	:Method : GET


	:param :hash – 의무 사항. 공개된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:Return : 테스크 식별자


	:Error : 403: 저작권 침해로 인해 링크가 차단되었다.


	"""
def file_confirm(request, *args, **kwargs):
	"""Amazon S3에 파일을 성공적으로 업로드했는지 확인한다.


	:URL : https://api.server.com/api/1/files/confirm/<path>


	:Version : 1


	:Method : POST


	:param :user_id: 의무 사항. 사용자 ID.


	:Version : size: 선택 사항. 파일의 크기. (매개 변수는 파일 업로드 여부를 확인하는 데 사용)


	:Return : 업로드 되는 파일의 메타데이터. See /metadata.


	:Error : 403: 파일 버전이 다르다.

"""
def file_create(request, *args, **kwargs):
	"""파일을 서버에 업로드하는 데 필요한 매개 변수를 반환한다.


	:URL : https://api.server.com/api/1/files/create/


	:Version : 1


	:Method : POST


	:param :path: 의무 사항. 파일의 경로.


	:Version : create_dirs: 선택 사항. 기본적으로 True로 설정되어 있다. 만약 매개 변수가 False로 설정되면 파일을 생성할 때 시스템이 없는 폴더를 생성하지 않는다.


	:param :headers: 추가적인 HTTP 헤더들. (POST 요청이 사용되는 경우, 이러한 헤더는 매개 변수 사전에 추가됨)


	:Error : 201: 중복 제거로 인해 파일이 생성되었다, 즉, 동일한 크기의 파일과 체크섬이 이미 서버에 존재한다. 응답 텍스트는 ‘method /metadata /<path>’와 동일한 값을 갖는다.

"""
def file_create_part(request, *args, **kwargs):
	"""Multipart 업로드가 사용될 때 파일 부분을 서버에 업로드하는 데 필요한 매개 변수를 반환한다.


	:URL : https://api.server.com/api/1/files/create_part/


	:Version : 0, 1


	:Method : POST


	:param :temp_path: 의무 사항. Multipart 업로드가 시작되었을 때 ‘method/ files/ create/’가 반환되는 경로


	:Return : url: PUT method를 사용하여 파일을 전송해야 하는 링크.


	:param :headers: 추가적인 HTTP 헤더들.


	:Error : 404: 지정한 temp_path가 존재하지 않는다.

"""
def file_resolve_link(request, *args, **kwargs):
	"""게시된 파일에 대한 정보를 표시한다. (다운로드 URL 포함)


	:URL : https://api.server.com/api/1/links/get/<hash>/<path>


	:Version : 0, 1


	:Method : GET


	:param :hash: 의무 사항. 공개된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:Return : 다운로드한 파일에 대한 정보가 들어 있는 객체


	:Error : 404: 노드가 존재하지 않는다. (이유: 잘못된 경로 입력, 노드가 더 이상 공용이 아니거나 노드의 삭제 등)

"""
def file_versions_to_update(request, *args, **kwargs):
	"""클라이언트 앱의 최신 버전으로 특정 파일을 갱신하기 위해 오름차순으로 정렬된 파일 버전 목록을 반환한다. 


	:URL : https://api.server.com/api/1/files/versions_to_update/


	:Version : 0, 1


	:Method : GET


	:param :path – 의무 사항. 파일의 경로.


	:Return : 파일 버전을 설명하는 객체 배열.


	:Error : 404: 노드가 존재하지 않는다.


	"""
def files_get(request, *args, **kwargs):
	"""파일 내용을 수신할 매개 변수를 반환한다.


	:URL : https://api.server.com/api/1/files/get/<path>


	:Version : 1


	:Method : GET


	:Version : for_view: 선택 사항. 다운로드 링크의 목적: viewing (streaming) - True (the Content-Type valude is set up), download - False (Content-Disposition value is set up). 기본적으로 False로 설정.


	:Return : 다운로드한 파일에 관한 정보를 포함한 객체.


	:Error : 404: 노드가 존재하지 않는다.


	"""
def files_get_diff(request, *args, **kwargs):
	"""Diff 파일을 로드 할 컨텐츠를 제공한다.


	:URL : https://api.server.com/api/1/files/get_diff/<path>


	:Version : 0, 1


	:Method : GET


	:Return : 다운로드 중인 diff에 대한 정보를 포함하는 객체.


	:Error : 404: 노드가 존재하지 않는다.


	"""
def files_restore_version(request, *args, **kwargs):
	"""지정된 파일 버전을 복원한다. (파일이 새 버전을 가져온다.)


	:URL : https://api.server.com/api/1/files/restore/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 파일의 경로.


	:Return : 복원된 버전 파일의 메타데이터.


	:Error : 404: 지정된 파일이나 버전을 찾을 수 없다.

"""
def files_search(request, *args, **kwargs):
	"""쿼리 문을 이용해 파일 시스템에서 파일이나 디렉토리를 찾는다.


	:URL : https://api.server.com/api/1/files/search/


	:Version : 1


	:Method : POST


	:param :query – 의무 사항. 검색 쿼리.


	:Return : {

"""
def files_versions(request, *args, **kwargs):
	"""파일 버전의 목록을 반환한다. 생성 날짜 순으로 재귀적으로 정렬되며, 첫 번째 버전은 현재 버전이다.


	:URL : https://api.server.com/api/1/files/versions/<path>


	:Version : 1


	:Method : GET


	:param :skip – 선택 사항. 페이지별로 디스플레이를 활성화.


	:Return : 파일 버전을 설명하는 객체 배열.


	:Error : 404: 지정된 파일이나 버전을 찾을 수 없다.


	"""
def folder_or_file_link(request, *args, **kwargs):
	"""공용 링크를 생성한다.


	:URL : https://api.server.com/api/1/links/create/


	:Version : 1


	:Method : POST


	:param :path: 의무 사항. 파일이나 폴더의 경로.


	:Return : 파일이나 폴더의 메타데이터. See /metadata


	:Error : 400: 파일의 다운로드 폴더에 대한 링크를 생성하려고 시도한다.

"""
def folder_or_file_purge(request, *args, **kwargs):
	"""삭제된 모든 파일(파일 버전 포함)을 지운다.


	:URL : https://api.server.com/api/1/fileops/purge/


	:Version : 1


	:Method : POST


	:param :없음.


	:Return : 200: 파일 및 폴더 제거 작업이 대기 열에 있다.

"""
def folder_or_file_purge_status(request, *args, **kwargs):
	"""사용자 파일 삭제 테스크 상태를 반환한다.


	:URL : https://api.server.com/api/1/fileops/purgestatus/


	:Version : 0, 1


	:Method : POST


	:param :없음.


	:Return : 사용자의 파일 삭제 테스크 상태.


	"""
def folder_or_file_rename(request, *args, **kwargs):
	"""파일이나 폴더의 이름을 수정한다.


	:URL : https://api.server.com/api/1/fileops/rename/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 파일이나 폴더의 경로.


	:Return : 이름이 수정된 객체를 위한 메타데이터. See /metadata.


	:Error : 404: 지정된 파일이나 폴더를 찾을 수 없다.


	:Note : 이름을 바꾸면 이전 이름이 있는 폴더(파일)가 삭제되고 새 파일 또는 새 이름의 폴더가 생성됨.

"""
def folder_or_file_unlink(request, *args, **kwargs):
	"""공용 링크를 삭제한다.


	:URL : https://api.server.com/api/1/links/delete/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 파일이나 폴더의 경로.


	:Return : 이름이 수정된 객체를 위한 메타데이터. See /metadata.


	:Error : 404: 공용 링크를 찾을 수 없다.

"""
def folders_create(request, *args, **kwargs):
	"""새로운 폴더를 생성한다.


	:URL : https://api.server.com/api/1/fileops/folder_create


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 새로운 폴더의 경로.


	:Return : 새로운 폴더를 위한 메타데이터. See /metadata.


	:Error : 403: 주어진 경로의 폴더가 존재하지 않는다.

"""
def folders_or_files_copy(request, *args, **kwargs):
	"""선택한 파일이나 폴더를 새 폴더 또는 동일한 폴더에 복사한다. 파일 버전은 복사되지 않는다.


	:URL : https://api.server.com/api/1/fileops/copy/


	:Version : 1


	:Method : POST


	:param :from_path: 의무 사항. 복사할 파일이나 폴더의 초기 경로.


	:Return : 새로운 파일이나 폴더를 위한 메타데이터.


	:Error : 400: 필수 매개 변수 중 하나가 설정되지 않았다.


	:Note : 파일이나 폴더를 복사하려고 한다. 한 객체(예를 들어, /something)가 복사하려는 폴더에 동일한 이름으로 존재할 때, 그 객체는 something(1)이라는 이름으로 변경되며 위치하게 된다.

"""
def folders_or_files_delete(request, *args, **kwargs):
	"""파일이나 폴더를 삭제한다.


	:URL : https://api.server.com/api/1/fileops/delete/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 삭제될 파일이나 폴더의 경로.


	:Return : 복원된 폴더의 메타데이터. See /metadata.


	:Error : 403: 사용자가 폴더의 삭제를 허용하지 않거나 매개 변수 ‘only_empty’가 True이기에 폴더가 비어 있다. 

"""
def folders_or_files_move(request, *args, **kwargs):
	"""선택된 파일이나 폴더를 새로운 폴더로 옮긴다. 파일 버전은 옮겨지지 않는다. 즉, 버전 관리 지점에서 새 파일을 생성하고 이전 폴더에서 삭제하는 것처럼 보인다.


	:URL : https://api.server.com/api/1/fileops/move/


	:Version : 1


	:Method : POST


	:param :from_path: 의무 사항. 옮겨져야 하는 파일이나 폴더의 초기 경로.


	:Return : 옮겨지는 객체에 대한 정보 (새로운 경로를 포함)


	:Error : 400: 필수 매개 변수 중 하나가 입력되지 않았다.


	:Note : 이동하는 것이 파일이나 폴더라는 것도 중요하지만, 이동하는 장소는 폴더라는 것도 중요하다. 이 API method를 사용할 때 고려해야 할 몇 가지 유의 사항이 있다.

"""
def folders_or_files_multi_delete(request, *args, **kwargs):
	"""여러 파일이나 폴더를 삭제한다.


	:URL : https://api.server.com/api/1/fileops/multi/delete/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 삭제될 파일들이나 폴더들의 경로. 예: path=/1/2/3 & path=/1/2/4


	:Return : 삭제될 파일들이나 폴더들의 메타데이터. See /metadata.


	:Error : 403: 사용자가 폴더의 삭제를 허용하지 않았거나 매개 변수 ‘only_empty’가 True이기에 폴더가 비어 있다. 


	"""
def folders_or_files_multi_undelete(request, *args, **kwargs):
	"""삭제된 파일이나 폴더를 복원한다.


	:URL : https://api.server.com/api/1/fileops/multi/undelete/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 복원될 파일들이나 폴더들의 경로. 예: path=/1/2/3 & path=/1/2/4


	:Return : 응답 텍스트의 필드 error_code에 있는 각 경로.


	:Error : 응답 텍스트에 각 파일이나 폴더의 에러 코드를 나타낸다.


	"""
def folders_or_files_undelete(request, *args, **kwargs):
	"""삭제된 파일이나 폴더를 복원한다.


	:URL : https://api.server.com/api/1/fileops/undelete/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 복원될 파일이나 폴더의 경로.


	:Return : 복원될 파일이나 폴더의 메타데이터. See /metadata.


	:Error : 403: 사용자가 파일이나 폴더의 복원을 허용하지 않았다. (상위 폴더에서 삭제했을 수도 있다.)

"""
def get_encoded_file_name(request, file_name):
	"""Content-Disposition 헤더에 대해 인코딩된 파일 이름을 반환한다.

"""
def get_file_for_download(request, path, version=None, for_view=False, deleted=True):
	"""
	:Version : 0, 1


	:Method : POST

"""
def handover(request, *args, **kwargs):
	"""공동 작업자 중 하나에 공유 폴더를 할당한다. 다음과 같은 작업이 수행된다: 


	:URL : https://api.server.com/api/1/fileops/handover/


	:Version : 0, 1


	:Method : POST


	:param :path: 의무 사항. 새 공동 작업자에게 전달될 폴더의 경로.


	:Return : 없음.


	:Error : 400: 주요 매개 변수가 입력이 안 됐다.


	:Note : 폴더 공유는 백그라운드에서 수행된다. 공동 작업자는 접미사가 공유 폴더에 추가되고 이 폴더의 파일이 공유 폴더와 동일한 이름을 가진 새 폴더로 복사되는 것을 본다.

"""
def link_metadata(request, *args, **kwargs):
	"""공유 노드에 대한 정보를 반환한다. 노드가 분리되어 별도의 항목으로 공유되는 경우에는 실행되지 않는다.


	:URL :  https://api.server.com/api/1/links/metadata/<hash>/<path>


	:Version : 1


	:Method : GET


	:param :hash: 의무 사항. 공유된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:Return : 파일이나 폴더를 위한 메타데이터, 결과는 API method 메타데이터에 의해 생성되는 것과 유사하다. 유일한 차이점은 게시된 폴더와 관련하여 모든 경로가 입력된다는 점이다. 공유 루트 폴더에 대한 정보가 표시되면, JSON 결과에도 게시된 루트 폴더의 이름이 포함된 매개 변수가 존재한다.


	:Error : 403: 저작권 침해로 인해 링크가 차단되었다.

"""
def links_get(request, *args, **kwargs):
	"""사용자가 생성한 공용 링크 목록을 반환한다.


	:URL : https://api.server.com/api/1/links/


	:Version : 1


	:Method : GET


	:param :없음.


	:Return : 공용 링크가 생성된 일련의 메타데이터이다.


	"""
def metadata(request, *args, **kwargs):
	"""파일이나 폴더의 메타데이터를 반환한다.


	:URL : https://api.server.com/api/1/metadata/<path>


	:Version : 1


	:Method : GET


	:param :Hash - 선택 사항. 각 요청에 대한 각 요청은 텍스트에서 해시 매개 변수를 반환한다. 각 /metadata요청은 이 값을 포함해야 한다. 파일 또는 폴더의 메타데이터가 마지막 요청에서 변경되지 않을 경우 응답은 전체 응답 텍스트가 아닌 304 상태를 포함한다. 이 매개 변수는 경로가 파일이나 listing=false일 때 무시된다. 공유 폴더에 대한 해시는 모든 공동 작업자에게 동일하다.


	:Version : extra - 선택 사항. 기본적으로 true로 설정. 추가 정보를 메타데이터와 함께 반환. MP3(파일이 있는 경우), 미리 보기 정보(파일이 있는 경우) 등이 있을 수 있다. CL-1558 형식 참조.


	:Return : 매개 변수 경로에 따라 파일 또는 폴더의 메타데이터. 폴더의 경로이며 목록 매개 변수가 True이면, 메타데이터는 폴더 목록 뿐만 아니라 목록의 각 객체에 대한 메타데이터도 포함한다. 게다가 헤더 ETag에는 객체 해시가 포함되어 있다. 이 해시는 if-None-Match 헤더의 서버로 전송할 때 클라이언트 측에서 캐시에 사용할 수 있다. 서버의 객체가 변경되지 않은 경우, 응답은 304 코드가 포함된 빈 메시지를 포함한다.


	:Error : 304 폴더 내용이 마지막 요청에서 변경되지 않았다. (If-None-Match 헤더에 의해 결정됨)


	"""
def metadata_full_listing(request, *args, **kwargs):
	"""테스크를 생성하거나 준비된 파일 트리 구조를 다운로드하는 URL을 반환한다.


	:URL : https://api.server.com/api/1/metadata_full_listing/


	:Version : 1


	:Method : GET


	:param :listing_request_id: 테스크 식별자. 선택 사항. 빈 값을 전송하거나 보내지 않으면 서버가 사용자의 파일 구조 전체 목록을 생성하고 이 테스크의 식별자를 반환하는 테스크를 생성한다. 테스크 ID를 전달하면 작업 결과로 파일을 다운로드할 URL을 반환한다.


	:Return : Listing_request_id: 테스크ID, 만약 매개 변수 listing_request_id 가 지정되지 않았거나 비어 있다면???


	:Error : 404 – 요청 ID가 잘못 되었거나 데이터가 아직 준비되지 않았다. (테스크가 이미 시작된 경우, 응답 본문에는 진행 상황에 대한 정보가 포함된다.)


	:Note : 서버의 목록을 작성하는 작업이 완료되면 클라이언트는 알림 시스템을 통해 이에 대한 통지를 받게 된다. 이 통지문은 metadata_full_listing의 형식을 가지고 있으며 비슷하게 보인다.


	"""
def migration_contents_accept(request, *args, **kwargs):
	"""컨텐츠 마이그레이션 요청 수락


	:URL : https://api.server.com/api/1/migration_contents/accept/


	:Version : 1


	:Method : POST


	:param :Hash – 의무 사항. 거부를 위한 해시 코드.


	:Return : 마이그레이션에 대한 정보


	"""
def migration_contents_add(request, *args, **kwargs):
	"""한 사용자에서 다른 사용자로 컨텐츠 마이그레이션 요청을 생성한다.


	:URL : https://api.server.com/api/1/migration_contents/add/


	:Version : 1


	:Method : POST


	:param :member_login – 의무 사항. 사용자를 위한 로그인.


	:Return : 수락을 위한 해시 코드.


	"""
def migration_contents_get(request, *args, **kwargs):
	"""마이그레이션 요청에 대한 정보를 반환한다. 현재 사용자를 위한 method이다.


	:param :path – 선택 사항. 파일 경로.


	:Return : 마이그레이션 정보 목록.

"""
def migration_contents_reject(request, *args, **kwargs):
	"""컨텐츠 마이그레이션 요청을 거절한다.


	:URL : https://api.server.com/api/1/migration_contents/reject/


	:Version : 1


	:Method : POST


	:param :hash – 의무 사항. 거절을 위한 해시 코드.


	:Return : 없음.

"""
def migration_contents_remove(request, *args, **kwargs):
	"""컨텐츠 마이그레이션 요청을 제거한다.


	:URL : https://api.server.com/api/1/migration_contents/remove/


	:Version : 1


	:Method : POST


	:param :hash – 의무 사항. 삭제를 위한 해시 코드.


	:Return : 없음.

"""
def shared_collaborators(request, *args, **kwargs):
	"""공유된 폴더를 위한 공동 작업자 목록을 반환한다.


	:URL : https://api.server.com/api/1/shares/collaborators/


	:Version : 1


	:Method : GET


	:param :path: 의무 사항. 폴더의 경로.


	:Return : 공동 작업자의 집합.


	:Error : 404: 폴더를 찾을 수 없다.


	
	:Note : is_indirect: 공유 폴더의 직접적이거나 간접적인 공동 작업자. 만약 False이면, 폴더에 대한 접근 권한을 부여 받은 직접적인 공동 작업자이다. 만약 True이면, 상위 폴더에 대한 접근 권한을 부여 받은 간접적인 공동 작업자이다. 

"""
def shared_folder_accept(request, *args, **kwargs):
	"""공유 폴더에 대한 초대를 수락한다. 새 폴더가 사용자 루트 폴더에 나타난다. 공동 작업자가 이미 이름이 비슷한 폴더를 가지고 있는 경우, 시퀀스 번호가 폴더 이름에 추가된다. 최대 시퀀스 번호는 10이다. 공동 작업자가 폴더의 이름을 바꿀 수 있다. 이름 변경은 다른 공동 작업자의 시스템에 있는 폴더의 이름에 영향을 주진 않는다.


	:URL : https://api.server.com/api/1/shares/accept/


	:Version : 1


	:Method : POST


	:param :hash: 의무 사항. 공유된 폴더에 대한 고유한 초대 해시. 해시는 method /folders /shared /add /에서 수신된다.


	:Return : 200: 사용자가 공유 폴더에서 삭제되었다.


	:Error : 403: 해시가 특정 사용자의 공유 폴더를 지정하지 않았다.

"""
def shared_folder_add(request, *args, **kwargs):
	"""
	:URL : https://api.server.com/api/1/shares/add/


	:Version : 1


	:Method : POST


	:param :path – 의무 사항. 폴더의 경로.


	:Return : 공유된 폴더를 위한 고유한 초대 토큰.


	:Error : 403: 폴더에 대한 액세스 권한을 부여할 수 없다.


	:Note : 공동 작업자가 이미 폴더에 대한 액세스 권한을 부여 받은 경우, 이 method는 빈 텍스트 메시지에서 코드 200을 반환한다.


	"""