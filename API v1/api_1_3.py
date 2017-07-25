def metadata(request, *args, **kwargs):
	"""파일이나 폴더의 metadata를 반환한다.


	:URL : https://api.server.com/api/1/metadata/<path>


	:Version : 1


	:Method : GET


	:param :• Hash: 선택 사항. /metadata에 대한 각 요청은 텍스트의 해시 매개변수를 반환. 다음 /metadata에 대한 요청은 이 값을 포함. 파일 또는 폴더 메타데이터가 마지막 요청에서 변경되지 않은 경우, 응답은 매우 부피가 큰 전체 응답의 텍스트 대신에 304상태(수정되지 않은)를 포함. 경로가 file이나 listing=false에 이어질 경우 이 매개변수는 무시. 공유 폴더에 대한 해시는 모든 사용자에게 동일.


	:Return : 매개변수 경로에 따라 파일 또는 폴더에 대한 메타데이터이다. 만약 이것이 파일 경로이고 목록 매개변수가 True로 설정된 경우, 메타데이터에는 이 폴더 목록과 목록의 각 개체에 대한 메타데이터도 포함된다. 게다가, ETag의 헤더는 개체 해시가 포함되어 있다. 이 해시는 If-None-Match 헤더의 서버로 전송될 때 클라이언트 측에서 캐시로 사용할 수 있다. 서버의 객체가 변경되지 않은 경우, 응답은 304 코드를 포함한 빈 메시지를 포함할 것이다.


	:Error : • 304: 폴더 내용이 마지막 요청에서 변경되지 않았다 (If-None-Match header에 의해 판단).


	"""
	def metadata_full_listing(request, *args, **kwargs):
	"""작업을 생성하거나 준비된 파일 트리 구조를 다운로드하는 URL을 반환한다.

	:URL : https://api.server.com/api/1/metadata_full_listing/

	:Version : 1


	:Method : GET


	:param :• listing_request_id: 작업 ID. 선택 사항. 만약 값을 보내지 않거나 빈 값을 보내게 되면, 서버는 사용자의 전체 파일 구조 목록을 작성하고 해당 작업의 ID를 반환. 작업 ID를 전달하면, 작업 결과로 파일을 다운로드할 URL을 반환.


	:Return : • listing_request_id: 매개변수 listing_request_id가 지정되거나 비어 있지 않은 경우 작업 ID 반환


	:Error : 404 - 허가되지 않은 요청 ID거나, 요청에 응할 데이터가 아직 준비되지 않았다. 작업이 이미 시작된 경우, 응답 body에 진행 상황에 대한 정보가 포함된다:


	:Note : 서버 목록을 작성하는 작업이 완료된 후, 클라이언트는 이 알림 시스템을 통하여 알림을 받게 된다. 해당 알림은 metadata_full_listing 형식을 가지고 있으며, 아래와 같이 표현된다.


	"""
	def files_get(request, *args, **kwargs):
	"""파일 내용을 받기위한 매개변수를 반환한다.


	:URL : https://api.server.com/api/1/files/get/<path>


	:Version : 1


	:Method : GET


	:param :• version: 선택 사항. 파일 버전. 기본적으로 가장 최근 버전을 사용.


	:Return : 다운로드 파일에 대한 정보가 담긴 객체


	:Error : • 404: 파일을 찾을 수 없다.


	"""
	def file_create(request, *args, **kwargs):
	"""서버에 파일을 업로드 하는 데 필요한 매개변수를 반환한다.


	:URL : https://api.server.com/api/1/files/create/


	:Version : 1


	:Method : POST


	:param :• path: 필수 사항. 파일 경로.


	:Return : • url: multipart 업로드가 사용되는 경우 파일에 전송해야 하는 파일에 대한 링크


	:Error : • 201: 중복 제거의 결과로 파일이 생성되었다. 즉, 동일한 크기의 파일과 checksum이 이미 서버에 있다. 응답 텍스트는 /metadata/<path> method의 반환 값을 갖는다.

"""
def file_create_part(request, *args, **kwargs):
	"""multipart 업로드가 사용될 때 파일의 일부를 서버에 업로드 하는 데 필요한 매개변수를 반환한다.


	:URL : https://api.server.com/api/1/files/create_part/


	:Version : 0, 1


	:Method : POST


	:param :• temp_path: 필수 사항. Multipart 업로드가 시작되었을 때 method/files/create/가 반환한 경로.


	:Return : • url: 파일이 PUT method를 사용하여 보내질 필요가 있을 경우의 링크


	:Error : • 404: 지정된 temp_path를 찾을 수 없다. 해당 multipart 업로드가 method/files/create/로 실행되지 않는다.

"""
def diff_create(request, *args, **kwargs):
	"""새로운 버전의 파일을 생성하기 위해 diff를 불러온다.


	:URL : https://api.server.com/api/1/files/create_from_diff/


	:Version : 1


	:Method : POST


	:param :• path - 필수 사항. 파일 경로.


	:Return : Amazon S3에서 diff를 가져오기 위해 필요한 data. 반환된 매개변수들 중 하나는 나중에 /files/confirm_from_diff/ method를 통해 성공적으로 다운로드가 완료되었는지 확인하는 key 매개변수로, 이 매개변수는 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새로운 버전의 파일을 생성할 것임을 알 수 있게 해준다.


	:Error : • 403: 이 클라이언트의 파일 버전의 기한이 만료되었다. (즉, 클라이언트가 서버에 이미 해당 버전이 있거나, 최신일 때 새로운 버전의 파일을 생성하기 위해 diff를 가져오려 하는 경우, 클라이언트는 파일의 최신 버전을 생성하지 못하게 된다).


	:Note : 이 method는 /files/create와 완벽히 유사하고, 파일이 아닌 diff를 불러온다는 차이점이 있다.

"""
def file_confirm(request, *args, **kwargs):
	"""Amazon S3에 파일이 성공적으로 업로드 되었는지 확인한다.


	:URL : https://api.server.com/api/1/files/confirm/<path>


	:Version : 1


	:Method : POST


	:param :• user_id: 필수 사항. 사용자 ID.


	:Return : 업로드 된 파일의 메타데이터. See /metadata.


	:Error : • 403: 파일 버전이 올바르지 않다.

"""
def diff_confirm(request, *args, **kwargs):
	"""Amazon S3로부터 diff가 성공적으로 가져와 졌는지 확인한다.


	:URL : https://api.server.com/api/1/files/confirm_from_diff/<path>


	:Version : 1


	:Method : POST


	:param :• version – 필수 사항. Diff를 가져오기 위한 클라이언트에 있는 현재 파일의 버전. 


	:Return : 새 파일에 대한 메타데이터. See /metadata.


	:Error : • 403: 이 클라이언트의 파일 버전의 기한이 만료되었다. (즉, 클라이언트가 서버에 이미 해당 버전이 있거나, 최신일 때 새로운 버전의 파일을 생성하기 위해 diff를 가져오려 하는 경우, 클라이언트는 파일의 최신 버전을 생성하지 못하게 된다).

"""
def file_versions_to_update(request, *args, **kwargs):
	"""클라이언트 앱의 특정 파일을 최신 버전으로 갱신하기 위해 오름차순으로 정렬된 파일 버전 목록을 반환한다.


	:URL : https://api.server.com/api/1/files/versions_to_update/


	:Version : 0, 1


	:Method : GET


	:param :• path - 필수 사항. 파일 경로.


	:Return : 파일 버전을 설명하는 객체 배열.


	:Error : • 404: 지정된 파일을 찾을 수 없다.


	"""def files_get_diff(request, *args, **kwargs):
	"""Diff 파일을 가져올 내용을 반환한다.


	:URL : https://api.server.com/api/1/files/get_diff/<path>


	:Version : 0, 1


	:Method : GET


	:param :• version - 필수 사항. diff를 통해 다시 생성하려는 파일의 버전. 이는 /files/versions_to_update/ 를 통해 얻을 수 있다.


	:Return : 다운로드 중인 diff에 대한 정보를 포함하는 객체


	:Error : • 404: 파일을 찾을 수 없다.


	"""
	def files_versions(request, *args, **kwargs):
	"""파일 버전 목록을 반환한다. 버전은 생성 날짜로부터 재귀적으로 정렬되며, 첫번째 버전은 현재 버전이다.


	:URL : https://api.server.com/api/1/files/versions/<path>


	:Version : 1


	:Method : GET


	:param :• skip - 선택 사항. Page-by-page 디스플레이 활성화.


	:Return : 파일 버전을 설명하는 객체의 배열을 반환한다.


	:Error : • 404: 지정된 파일을 찾을 수 없다.


	
	:Note : 복원된 매개변수 restored_timestamp#은 유닉스 타임스탬프 UTC 버전의 복원된 버전을 위한 것이다.

"""
def files_restore_version(request, *args, **kwargs):
	"""지정된 파일 버전을 복원한다. 파일은 새 버전을 갖게 된다.


	:URL : https://api.server.com/api/1/files/restore/


	:Version : 1


	:Method : POST


	:param :• path - 필수 사항. 파일의 경로.


	:Return : 복원된 버전의 파일에 대한 메타데이터.


	:Error : • 404: 지정된 파일이나 버전을 찾을 수 없다.

"""
def download_entire_folder(request, *args, **kwargs):
	"""폴더 및 파일을 보관한다. 작업 지속 시간은 파일의 수에 따라 달라지며, 때문에 결과에 대한 API method를 정기적으로 요청해야 한다. 작업의 준비상태는 https://api.server.com/api/1/task/<taskid>/에서 요청된다.


	:URL : https://api.server.com/api/1/files/download_as_archive/


	:Version : 0, 1


	:Method : GET


	:param :• path - 필수 사항. 아카이브에 추가될 폴더 및 파일로 설정된 경로. 예시: path=/1/2/3&path=/1/2/4


	:Return : 작업 ID
"""