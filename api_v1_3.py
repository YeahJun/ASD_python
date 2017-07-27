# -*- coding: utf-8 -*-

def metadata(request,*args,**kwargs):
	"""파일이나 폴더의 metadata를 반환한다.


	:URL: https://api.server.com/api/1/metadata/<path>


	:Version: 1


	:Method: GET


	:param Hash: 선택 사항. /metadata에 대한 각 요청은 텍스트의 해시 매개변수를 반환. 다음 /metadata에 대한 요청은 이 값을 포함. 파일 또는 폴더 메타데이터가 마지막 요청에서 변경되지 않은 경우, 응답은 매우 부피가 큰 전체 응답의 텍스트 대신에 304상태(수정되지 않은)를 포함. 경로가 file이나 listing=false에 이어질 경우 이 매개변수는 무시. 공유 폴더에 대한 해시는 모든 사용자에게 동일.


	:param listing: 선택 사항. 기본적으로 true. 만약 true일 경우, 폴더 메타데이터와 목록도 반환. 목록에는 각 목록 항목에 대한 메타데이터 포함. 만약 false일 경우, 반환하지 않음. 


	:param dirs_only: 선택 사항. 기본적으로 false. 만약 true일 경우, 오직 listing=true인 폴더들은 목록에 포함.


	:param deleted: 선택 사항. 기본적으로 false. 만약 true일 경우, 삭제된 객체가 목록에 포함, false일 경우에는 포함하지 않음.


	:param version: 선택 사항. 메타데이터를 제공해야 하는 특정 파일 버전. 디렉터리에 대해 버전이 지원되지 않는 경우, 이 매개변수는 무시. 매개변수가 주어지지 않으면, 가장 최근 버전이 사용.


	:param extra: 선택 사항. 기본적으로 true. Extra data라고 불리는 추가 정보를 메타데이터와 함께 반환. 이는 mp3 태그(파일이 mp3 형태일 경우), 미리보기 정보(파일이 문서일 경우), 썸네일에 대한 정보(파일이 이미지 일 경우) 등. See format CL:1558.


	:param offset: 선택 사항. 기본적으로 0. 폴더 내용 목록의 처음부터 오프셋


	:param limit: 선택 사항. 기본적으로 0. 폴더 목록에 대해 반환되는 최대 개체 수.


	:param order_by: 선택 사항. 기본적으로 ‘name’. 지정된 필드를 기준으로 결과를 정렬. 가능한 값들: ‘name’, ‘:name’, ‘modified_time’, ‘:modified_time’


	:Return: 매개변수 경로에 따라 파일 또는 폴더에 대한 메타데이터. 만약 이것이 파일 경로이고 목록 매개변수가 True로 설정된 경우, 메타데이터에는 이 폴더 목록과 목록의 각 개체에 대한 메타데이터도 포함된다. 게다가, ETag의 헤더는 개체 해시가 포함되어 있다. 이 해시는 If:None:Match 헤더의 서버로 전송될 때 클라이언트 측에서 캐시로 사용할 수 있다. 서버의 객체가 변경되지 않은 경우, 응답은 304 코드를 포함한 빈 메시지를 포함할 것이다.


	:Return: 반환되는 값들


	:Return size: 파일 크기는 사용자가 일반적으로 사용할 수 있는 정도. 폴더는 항상 “0 bytes”을 가지고 있을 것.


	:Return bytes: 파일 크기. 폴더는 항상 0.


	:Return checksum: 파일의 checksum (md5).


	:Return folder: 이것이 폴더인지 파일인지에 대한 표식.


	:Return path: 폴더나 파일의 경로라면, с /로 시작. 루트 폴더의 메타데이터가 요청되었다면, 값은 “/”.


	:Return shared: 폴더가 공유되었는지에 대한 표식.


	:Return shared_hash: 폴더 해시. 폴더가 익명의 사용자에게 공유되어 있을 경우 이 매개변수는 중요.


	:Return public_link: 폴더 또는 파일에 대한 공용 링크가 없는 경우 false.


	:Return deleted: 삭제 되었는지에 대한 표식.


	:Return version: 가장 최근 파일 버전. 폴더들은 항상 0.


	:Return hash: /metadata의 후속 호출에 사용되는 해시. 이는 파일들에 대해 반환하지 않음.


	:Return thumbnail: 파일에 썸네일이 있는 경우, 이는 썸네일의 경로. 만약 썸네일이 없는 경우, 이는 false.


	:Return icon: 지정된 파일 형식의 아이콘 (파일은 썸네일을 지원하지 않는다.)


	:Return modified: 폴더나 파일이 마지막으로 수정된 날짜.


	:Return owner: 파일이나 폴더 소유자의 userid.


	:Return owner_name: 파일이나 폴더 소유자의 이름.


	:Return author: 파일(혹은 지정된 파일 버전)작성자 또는 폴더 작성자의 userid.


	:Return author_name: 파일(혹은 지정된 파일 버전)작성자 또는 폴더 작성자의 이름.


	:Return client_data: 다른 클라이언트에게 보내기 위해 클라이언트 앱 중 하나에 의해 설치된 데이터.


	:Return fs_type: 폴더와 연결된 파일 시스템 유형. 개체가 폴더 또는 마운트 지점이 아닌 경우, 이 필드는 표시되지 않음.


	:Return is_last_page: true인 경우, 이는 폴더 목록의 마지막 결과 페이지 임을 의미, false인 경우 : 아직 페이지가 남음.


	:Error 304: 폴더 내용이 마지막 요청에서 변경되지 않았다 (If:None:Match header에 의해 판단).


	:Error 404: 파일이나 폴더를 찾을 수 없다.
	"""
def metadata_full_listing(request,*args,**kwargs):
	"""작업을 생성하거나 준비된 파일 트리 구조를 다운로드하는 URL을 반환한다.


	:URL: https://api.server.com/api/1/metadata_full_listing/


	:Version: 1


	:Method: GET


	:param listing_request_id: 작업 ID. 선택 사항. 만약 값을 보내지 않거나 빈 값을 보내게 되면, 서버는 사용자의 전체 파일 구조 목록을 작성하고 해당 작업의 ID를 반환. 작업 ID를 전달하면, 작업 결과로 파일을 다운로드할 URL을 반환.


	:Return listing_request_id: 매개변수 listing_request_id가 지정되거나 비어 있지 않은 경우 작업 ID 반환


	:Return url: 매개변수 listing_request_id가 지정되어 있을 경우 결과를 참조.


	:Error 404: 허가되지 않은 요청 ID거나, 요청에 응할 데이터가 아직 준비되지 않았다. 작업이 이미 시작된 경우, 응답 body에 진행 상황에 대한 정보가 포함된다:

	:Note: 서버 목록을 작성하는 작업이 완료된 후, 클라이언트는 이 알림 시스템을 통하여 알림을 받게 된다. 해당 알림은 metadata_full_listing 형식을 갖고 있다.

	:Note: listing_request_id 필드는 반드시 API / metadat_full_listing / 으로부터 얻은 listing_request_id와 일치해야 한다는 것을 유념해야 한다. 이것 이후에, 클라이언트는 파일 트리가 활성화된 URL을 얻기 위해 API method / metadata_full_listing /을 요청해야 한다.
	"""
def files_get(request,*args,**kwargs):
	"""파일 내용을 받기위한 매개변수를 반환한다.


	:URL: https://api.server.com/api/1/files/get/<path>


	:Version: 1


	:Method: GET


	:param version: 선택 사항. 파일 버전. 기본적으로 가장 최근 버전을 사용.


	:param for_view: 선택 사항. 다운로드 링크의 목적을 나타냄: viewing (streaming) : True (the Content:유형 값 설정), download : False (Content:배치 값 설정). 기본적으로 False.


	:param deleted: 선택 사항. True : 다운로드 링크가 제공 됨; False : 요청된 파일이 삭제된 경우, 파일이 삭제되고 에러 404가 나타난다.


	:Return: 다운로드 파일에 대한 정보가 담긴 객체


	:Error 404: 파일을 찾을 수 없다.
	"""
def file_create(request,*args,**kwargs):
	"""서버에 파일을 업로드 하는 데 필요한 매개변수를 반환한다.


	:URL: https://api.server.com/api/1/files/create/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 파일 경로.


	:param overwrite: 선택 사항. 기본적으로 False. 매개변수가 True로 설정되어 있고 서버에 비슷한 이름의 파일이 있을 경우, 이미 있는 파일에 덮어쓴다. 매개변수가 True로 설정되어 있고 서버에 비슷한 이름의 파일이 있는 경우, 해당 method는 에러 코드 409를 반환한다. 이는 PC:client측에서는 항상 False, web:client측에서는 항상 True라고 가정.


	:param version: 선택 사항. 이전 파일의 버전. 이는 파일 버전을 올바르게 갱신하는데 사용된다. 서버의 현재 파일이 지정된 버전과 일치하지 않는 경우, method가 오류를 반환한다.


	:param create_dirs: 선택 사항. 기본적으로 true. 매개변수가 false로 설정되면, 파일을 생성할 때 시스템이 없는 폴더를 생성하지 않는다.


	:param created: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 생성된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param modified: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 수정된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param device_id: 선택 사항. 파일이 업로드 된 디바이스 ID.


	:param device_reference: 선택 사항. API initiator의 로컬 디바이스 스토리지에 파일에 대한 링크를 저장하는 보조 필드.


	:param size: 선택 사항. 생성할 파일의 크기. 매개변수는 중복을 제거하고 파일 업로드가 제대로 되었는지 확인하는데 쓰인다.


	:param checksum: 선택 사항. 파일 중복 제거와 파일 업로드가 제대로 이루어 졌는지 확인하는 checksum(md5).


	:param multipart: 선택 사항. 기본적으로 False. True면, multipart의 업로드가 시작. 이는 추가 헤더를 표시할 수 있는 URL을 사용하여 PUT method를 이용해 실행한다. 매개변수는 POST 요청에서는 사용되지 않는다.


	:Return url: multipart 업로드가 사용되는 경우 파일에 전송해야 하는 파일에 대한 링크


	:Return parameters: POST 요청의 추가적 매개변수 (이는 multipart 업로드에서 PUT method가 적용되는 경우 사용되지 않음).


	:Return headers: 추가적인 HTTP 헤더. POST 요청이 사용될 때, 이러한 헤더들은 매개변수 딕셔너리에 추가.


	:Return confirm_url: 파일 업로드가 완료되었음을 확인하기 위한 주소 링크.


	:Return temp_path: 오직 multipart 업로드가 사용될 때 반환; 이 매개변수는 다른 파일 파트의 업로드 매개변수를 받아오는데 사용된다.


	:Return: 중복 제거가 수행된 경우 method는 /metadata/<path> method와 동일한 값을 반환.


	:Error 201: 중복 제거의 결과로 파일이 생성되었다. 즉, 동일한 크기의 파일과 checksum이 이미 서버에 있다. 응답 텍스트는 /metadata/<path> method의 반환 값을 갖는다.


	:Error 400: 파일 버전이 존재하지 않는다.


	:Error 403: 존재하지 않는 폴더에 파일 업로드를 하려하거나, 덮어 쓰려는 파일의 버전과 일치하지 않는다.


	:Error 404: 존재하지 않는 폴더에 파일 업로드 하려하거나, create_dirs가 False이다.


	:Error 409: 덮어쓰기를 하려는 (이미 존재하는) 객체가 파일의 이름과 같지 않아 충돌이 발생한다.

"""
def file_create_part(request,*args,**kwargs):
	"""multipart 업로드가 사용될 때 파일의 일부를 서버에 업로드 하는 데 필요한 매개변수를 반환한다.


	:URL: https://api.server.com/api/1/files/create_part/


	:Version: 0, 1


	:Method: POST


	:param temp_path: 필수 사항. Multipart 업로드가 시작되었을 때 method/files/create/가 반환한 경로.


	:param part_num: 필수 사항. 업로드 된 파일 일부분의 개수.


	:Return url: 파일이 PUT method를 사용하여 보내질 필요가 있을 경우의 링크


	:Return parameters: 빈 목록은 multipart 업로드에 사용되지 않음.


	:Return headers: 추가적인 HTTP 헤더.


	:Error 404: 지정된 temp_path를 찾을 수 없다. 해당 multipart 업로드가 method/files/create/로 실행되지 않는다.

"""
def diff_create(request,*args,**kwargs):
	"""새로운 버전의 파일을 생성하기 위해 diff를 불러온다.


	:URL: https://api.server.com/api/1/files/create_from_diff/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 파일 경로.


	:param version: 필수 사항. Diff가 로드 되는 클라이언트의 현재 파일 버전.


	:param checksum: 필수 사항. 새로운 파일 버전의 checksum. (diff를 병합하여 얻은 새로 생성된 파일과 서버에서 파일의 이전 버전의 정확도를 확인해야 한다). 파일 checksum을 얻기 위해 CRC32 알고리즘을 사용.


	:param autoconfirm_upload: 선택 사항. Boolean 타입의 표식. 만약 True로 설정되면 (즉, autoconfirm_upload = 1), 클라이언트에서 Amazon으로 diff가 다운로드 된 후에, 응답 코드 200 대신에, 클라이언트가 redirect를 받게 되고 (응답 코드 303), 응답 헤더 중 하나는 backend에서 POST method를 사용한 diff 업로드가 성공하였는지 확인하는 URL에 대한 위치 헤더가 된다. 만약 False로 설정되면, 클라이언트는 응답 코드 200을 받게 되고, 다운로드 자체를 확인하기 위해 URL을 통과한다. 매개변수가 전해지지 않으면 (즉, 없으면), 기본 값을 backend 구성에서 가져온다 (cloudike / amazon / autoconfirm_upload parameter).


	:param created: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 생성된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param modified: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 수정된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param device_id: 선택 사항. 파일에 업로드 된 디바이스 ID.


	:param device_reference: 선택 사항. API initiator의 로컬 디바이스 스토리지에 파일에 대한 링크를 저장하는 보조 필드.


	:Return: Amazon S3에서 diff를 가져오기 위해 필요한 data. 반환된 매개변수들 중 하나는 나중에 /files/confirm_from_diff/ method를 통해 성공적으로 다운로드가 완료되었는지 확인하는 key 매개변수로, 이 매개변수는 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새로운 버전의 파일을 생성할 것임을 알 수 있게 해준다.


	:Error 403: 이 클라이언트의 파일 버전의 기한이 만료되었다. (즉, 클라이언트가 서버에 이미 해당 버전이 있거나, 최신일 때 새로운 버전의 파일을 생성하기 위해 diff를 가져오려 하는 경우, 클라이언트는 파일의 최신 버전을 생성하지 못하게 된다).


	:Error 409: 서버에서 diff를 통해 생성된 checksum 파일과 클라이언트에서 변경된 파일이 일치하지 않는다.


	:Error 410: 서버에서 새로운 파일을 생성하는 동안 오류가 발생하였다. (diff를 사용).


	:Note: 이 method는 /files/create와 완벽히 유사하고, 파일이 아닌 diff를 불러온다는 차이점이 있다.

"""
def file_confirm(request,*args,**kwargs):
	"""Amazon S3에 파일이 성공적으로 업로드 되었는지 확인한다.


	:URL: https://api.server.com/api/1/files/confirm/<path>


	:Version: 1


	:Method: POST


	:param user_id: 필수 사항. 사용자 ID.


	:param temp_name: 필수 사항. 임시 파일 이름.


	:param overwrite: 선택 사항. 기본적으로 False. 매개변수가 True이고 서버에 유사한 이름의 파일이 있을 경우, 기존 파일에 덮어씀.


	:param version: 선택 사항. 이전 파일 버전.


	:param size: 선택 사항. 생성된 파일의 크기. 파일 업로드가 제대로 되었는지 확인 할 때 사용한다.


	:param checksum: 선택 사항. 파일 내용의 업로드가 제대로 수행되었는지 확인할 때 사용하는 checksum(md5)


	:Return: 업로드 된 파일의 메타데이터.


	:Error 403: 파일 버전이 올바르지 않다.


	:Error 404: 지정된 파일을 찾을 수 없다.


	:Error 409: 요청한 경로에 이미 객체가 존재한다 (객체가 폴더 또는 파일이거나 매개변수가 False일 경우에만 해당).

"""
def diff_confirm(request,*args,**kwargs):
	"""Amazon S3로부터 diff가 성공적으로 가져와 졌는지 확인한다.


	:URL: https://api.server.com/api/1/files/confirm_from_diff/<path>


	:Version: 1


	:Method: POST


	:param version: 필수 사항. Diff를 가져오기 위한 클라이언트에 있는 현재 파일의 버전.


	:param key: 필요한 경우, /files/create_from_diff/ method로부터 얻는 이 매개변수를 통해 특정 사용자가 diff를 통해 새 버전의 파일을 정확하게 생성할 수 있는 것을 식별 가능.


	:Return: 새 파일에 대한 메타데이터.


	:Error 403: 이 클라이언트의 파일 버전의 기한이 만료되었다. (즉, 클라이언트가 서버에 이미 해당 버전이 있거나, 최신일 때 새로운 버전의 파일을 생성하기 위해 diff를 가져오려 하는 경우, 클라이언트는 파일의 최신 버전을 생성하지 못하게 된다).


	:Error 409: 새로운 버전의 파일을 생성한 후에(diff와 이전 파일의 버전으로), 새로 생성된 파일의 checksum이 확인을 위한 /files/create_from_diff method의 checksum과 일치하지 않는다.

"""
def file_versions_to_update(request,*args,**kwargs):
	"""클라이언트 앱의 특정 파일을 최신 버전으로 갱신하기 위해 오름차순으로 정렬된 파일 버전 목록을 반환한다.


	:URL: https://api.server.com/api/1/files/versions_to_update/


	:Version: 0, 1


	:Method: GET


	:param path: 필수 사항. 파일 경로.


	:param version: 필수 사항. 정수, 클라이언트 앱의 파일 버전.


	:Return: 파일 버전을 설명하는 객체 배열.


	:Error 404: 지정된 파일을 찾을 수 없다.
	"""
def files_get_diff(request,*args,**kwargs):
	"""Diff 파일을 가져올 내용을 반환한다.


	:URL: https://api.server.com/api/1/files/get_diff/<path>


	:Version: 0, 1


	:Method: GET


	:param version: 필수 사항. diff를 통해 다시 생성하려는 파일의 버전. 이는 /files/versions_to_update/ 를 통해 얻을 수 있다.


	:Return: 다운로드 중인 diff에 대한 정보를 포함하는 객체


	:Error 404: 파일을 찾을 수 없다.
	"""
def files_versions(request,*args,**kwargs):
	"""파일 버전 목록을 반환한다. 버전은 생성 날짜로부터 재귀적으로 정렬되며, 첫번째 버전은 현재 버전이다.


	:URL: https://api.server.com/api/1/files/versions/<path>


	:Version: 1


	:Method: GET


	:param skip: 선택 사항. Page:by:page 디스플레이 활성화.


	:param limit: 선택 사항. 레코드 양 제한.


	:param extra: 선택 사항. 각 파일 버전에 대한 정보에 extra:data를 추가.


	:Return: 파일 버전을 설명하는 객체의 배열.


	:Error 404: 지정된 파일을 찾을 수 없다.

	:Note: 복원된 매개변수 restored_timestamp#은 유닉스 타임스탬프 UTC 버전의 복원된 버전을 위한 것이다.

"""
def files_restore_version(request,*args,**kwargs):
	"""지정된 파일 버전을 복원한다. 파일은 새 버전을 갖게 된다.


	:URL: https://api.server.com/api/1/files/restore/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 파일의 경로.


	:param version: 필수 사항. 버전 숫자.


	:Return: 복원된 버전의 파일에 대한 메타데이터.


	:Error 404: 지정된 파일이나 버전을 찾을 수 없다.

"""
def download_entire_folder(request,*args,**kwargs):
	"""폴더 및 파일을 보관한다. 작업 지속 시간은 파일의 수에 따라 달라지며, 때문에 결과에 대한 API method를 정기적으로 요청해야 한다. 작업의 준비상태는 https://api.server.com/api/1/task/<taskid>/에서 요청된다.


	:URL: https://api.server.com/api/1/files/download_as_archive/


	:Version: 0, 1


	:Method: GET


	:param path: 필수 사항. 아카이브에 추가될 폴더 및 파일로 설정된 경로. 예시: path=/1/2/3&path=/1/2/4


	:param parent_folder: 선택 사항. 아카이브 생성 요청을 수신한 시점에 사용자가 열어 놓은 폴더.


	:Return: 작업 ID
	"""