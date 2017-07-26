# -*- coding: utf-8 -*-

def metadata(request,*args,**kwargs):
	"""파일이나 폴더의 메타데이터를 반환한다.


	:URL: https://api.server.com/api/0/metadata/<path>


	:Version: 0


	:Method: GET


	:param hash: 선택 사항. /metadata에 대한 각 요청은 텍스트의 해시 매개변수를 반환. 다음 /metadata에 대한 요청은 이 값을 포함한다. 파일 또는 폴더 메타 데이터가 마지막 요청에서 변경되지 않은 경우, 응답은 매우 부피가 큰 전체 응답의 텍스트 대신에 304상태(수정되지 않은)을 포함한다. 경로가 file이나 listing=false에 이어질 경우 이 매개 변수는 무시된다. 공유 폴더에 대한 해시는 모든 사용자에게 동일하다.


	:param listing: 선택 사항. 기본적으로 true. 만약 true일 경우, 폴더 메타데이터만이 아니라 목록도 반환한다. 목록에는 각 목록 항목에 대한 메타데이터를 포함한다. 만약 false일 경우, 반환하지 않는다.


	:param dirs_only: 선택 사항. 기본적으로 false. 만약 true일 경우, 오직 listing=true인 폴더들만 목록에 포함한다.


	:param deleted: 선택 사항. 기본적으로 false. 만약 true일 경우, 삭제된 객체가 목록에 포함된다. , false일 경우에는 포함하지 않는다.


	:param version: 선택 사항. 메타 데이터를 제공해야 하는 특정 파일 버전. 디렉터리에 대해 버전이 지원되지 않는 경우, 이 매개 변수는 무시된다. 매개 변수가 주어지지 않으면, 가장 최근 버전이 사용된다.


	:param extra: 선택 사항. 기본적으로 true. Extra data라고 불리는 추가 정보를 메타 데이터와 함께 반환한다. 이는 mp3 태그(파일이 mp3 형태일 경우), 미리보기 정보(파일이 문서일 경우), 썸네일에 대한 정보(파일이 이미지 일 경우) 등. See format CL:1558.


	:param offset: 선택 사항. 기본적으로 0. 폴더 내용 목록의 오프셋.


	:param limit: 선택 사항. 기본적으로 0. 폴더 목록에 대해 반환되는 객체의 최대 수.


	:Return: 매개 변수 경로에 따라 파일 또는 폴더에 대한 메타데이터. 만약 이것이 파일 경로이고 목록 매개 변수가 True로 설정된 경우, 메타 데이터에는 이 폴더 목록만이 아니라 목록의 각 객체에 대한 메타 데이터도 포함된다. 게다가, ETag의 헤더는 객체 해시가 포함되어 있다. 이 해시는 If:None:Match 헤더의 서버로 전송될 때 클라이언트 측에서 캐시로 사용할 수 있다. 서버의 객체가 변경되지 않은 경우, 응답은 304 코드를 포함한 빈 메시지를 포함한다.


	:Return: Description of returned values


	:Return size: 파일 크기는 사용자가 일반적으로 사용할 수 있는 정도. 폴더는 항상 “0 bytes” 를 갖고 있다.


	:Return bytes: 파일 크기. 폴더는 항상 0.


	:Return checksum: 파일의 checksum (md5).


	:Return folder: 폴더인지 파일인지에 대한 플래그.


	:Return path: 폴더나 파일의 경로라면, с /로 시작. 루트 폴더의 메타데이터가 요청되었다면, 값은 “/”.


	:Return shared: 폴더가 공유되었는지에 대한 표식.


	:Return public_link: 폴더 또는 파일에 대한 공용 링크가 없는 경우 false.


	:Return deleted: 삭제 여부에 대한 표식.


	:Return version: 가장 최근 파일 버전. 폴더들은 항상 0.


	:Return hash: /metadata의 후속 호출에 사용되는 해시. 이는 파일들에 대해 반환하지 않는다.


	:Return thumbnail: 파일에 썸네일이 있는 경우, 이는 썸네일의 경로. 만약 썸네일이 없는 경우, 이는 false.


	:Return icon: 지정된 파일 형식의 아이콘 (파일은 썸네일을 지원하지 않는다.)


	:Return modified: 폴더나 파일이 마지막으로 수정된 날짜.


	:Return owner: 파일이나 폴더 소유자의 ID.


	:Return owner_name: 파일이나 폴더 소유자의 이름.


	:Return author: 파일(혹은 지정된 파일 버전)작성자 또는 폴더 작성자의 ID.


	:Return author_name: 파일(혹은 지정된 파일 버전)작성자 또는 폴더 작성자의 이름.


	:Return client_data: 다른 사용자들에게 보내기 위한 클라이언트 앱의 설치 데이터.


	:Return fs_type: 폴더와 연결된 파일 시스템 유형. 객체가 폴더 또는 마운트 지점이 아닌 경우, 이 필드는 표시되지 않음.


	:Return is_last_page: true인 경우, 이는 폴더 목록의 마지막 결과 페이지 임을 의미, false인 경우 : 아직 페이지가 남음.


	:Error 304: 폴더 내용이 마지막 요청에서 변경되지 않았다(If:None:Match header에 의해 판단).


	:Error 404: 파일이나 폴더를 찾을 수 없다.
	"""
def file_create(request,*args,**kwargs):
	"""파일을 서버에 업로드 하는데 필요한 매개 변수를 반환합니다.


	:URL: https://api.server.com/api/0/files/create/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 파일의 경로.


	:param overwrite: 선택 사항. 기본적으로 False로 설정. 매개 변수가 True로 설정되고 서버에 유사한 이름을 가진 파일이 있을 경우, 존재하는 파일에 덮어쓴다. 매개 변수가 False로 설정되고 서버에 유사한 이름을 가진 파일이 있을 경우, 이 method는 에러 코드 409를 반환한다. 이는 PC:client측에서는 항상 False, web:client측에서는 항상 True라고 가정한다.


	:param version: 선택 사항. 이전 파일의 버전. 이는 파일 버전을 올바르게 갱신하는데 사용된다. 서버의 현재 파일이 지정된 버전과 일치하지 않는 경우, method가 오류 코드를 반환한다.


	:param create_dirs: 선택 사항. 기본적으로 true로 설정. 매개 변수가 false로 설정되면, 시스템이 파일을 생성하기 위해 누락된 폴더를 생성하지 않는다.


	:param created: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 생성된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param modified: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 수정된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param size: 선택 사항. 생성할 파일의 크기. 매개 변수는 중복을 제거하고 파일 업로드가 제대로 되었는지 확인하는데 쓰인다.


	:param checksum: 선택 사항. 파일 중복 제거와 파일 업로드가 제대로 이루어 졌는지 확인하는 checksum(md5).


	:param multipart: 선택 사항. 기본적으로 False. 만약 True면, multipart의 업로드가 시작. 이는 추가 헤더를 표시할 수 있는 URL을 사용하여 PUT method를 이용해 실행. 매개 변수는 POST 요청에서 사용되지 않는다.


	:Return url: 전송되어야 하는 파일에 대한 링크 또는 업로드 되는 파일의 링크.


	:Return parameters: POST 요청의 추가적 매개 변수 (multipart 업로드에서 PUT method가 적용되는 경우 사용되지 않는다).


	:Return headers: 추가적인 HTTP 헤더. POST 요청이 사용될 때, 이러한 헤더들은 매개 변수 딕셔너리에 추가.


	:Return confirm_url: 파일 업로드가 완료되었음을 확인하기 위한 주소 링크.


	:Return temp_path: 오직 multipart 업로드가 사용될 때 반환; 이 매개 변수는 다른 파일 파트의 업로드 매개 변수를 받아오는데 사용된다.


	:Return: 중복 제거가 수행된 경우 method는 /metadata/<path> method와 동일한 값을 반환.


	:Error 201: 중복 제거의 결과로 파일이 생성되었다. 즉, 동일한 크기의 파일과 checksum이 이미 서버에 있다. 응답 텍스트는 /metadata/<path> method의 반환 값을 갖게 된다.


	:Error 400: 파일 버전이 존재하지 않는다.


	:Error 403: 파일 업로드를 존재하지 않는 폴더에 하려하거나, 덮어 쓰려는 파일의 버전과 일치하지 않는다.


	:Error 404: 파일 업로드를 존재하지 않는 폴더에 하려하거나, create_dirs가 False이다.


	:Error 409: 파일의 이름과 덮어쓰기를 하려는 객체가 같지 않습니다.

"""
def diff_create(request,*args,**kwargs):
	"""새로운 버전의 파일을 생성하기 위해 diff를 불러온다.


	:URL: https://api.server.com/api/0/files/create_from_diff/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 파일의 경로.


	:param version: 선택 사항. 클라이언트에 있는 현재 파일의 버전.


	:param checksum: 필수 사항. 새 버전 파일의 checksum. (서버에 있는 이전 파일 버전과 diff를 병합해 만든 새로운 파일의 버전의 정확도를 확인해야 한다.) 파일의 checksum을 얻기 위해 CRC32 알고리즘이 사용된다.


	:param autoconfirm_upload: 선택 사항. Boolean 타입의 표식. 만약 True로 설정된다면 (즉, autoconfirm_upload = 1), 클라이언트에서 Amazon으로 diff를 다운로드한 후, 응답 코드 200대신에 클라이언트는 리다이렉트 (응답 코드 303)를 받게 된다. 응답 헤더들 중 하나는 백엔드에서 diff가 POST method를 통해 성공적으로 업로드 되었는지 확인하기 위해 사용되는 URL인 Location 헤더가 된다. False로 설정된다면, 클라이언트는 응답 코드 200을 받게 되며, 다운로드를 확인하기 위해 URL을 통과한다. 매개 변수가 전달되지 않았다면 (즉, None), 백엔드 구성으로부터 기본 값을 가져오게 된다. (cloudike / amazon / autoconfirm_upload parameter).


	:param created: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 생성된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:param modified: 선택 사항. 동기화를 위한 클라이언트 앱이 설치된 사용자 운영 체제에서 파일이 수정된 경우, 시간에 대한 유닉스 타임스탬프 (milliseconds).


	:Return: Amazon S3에서 diff를 가져오기 위해 필요한 데이터. 반환된 매개 변수 중 하나는 나중에 /files/confirm_from_diff method를 통해 다운로드가 성공적으로 완료되었는지 확인하기 위해 필요한 key 매개 변수다. 이 매개 변수를 통해 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새 버전의 파일을 생성함을 알 수 있다.


	:Error 403: 클라이언트의 파일 버전이 매우 오래 되었다. (즉, 클라이언트가 새 버전을 이미 가지고 있거나, 최신 버전의 파일이 없는 경우 클라이언트가 새 버전을 생성하려고 시도한다).


	:Error 409: 서버에서 diff를 통해 생성된 파일의 checksum과 클라이언트에서 변경된 파일이 서로 일치하지 않는다.


	:Error 410: 서버에서 diff를 사용해 새 파일을 생성하는 중 오류가 발생했다.


	:Note: 이 method는 /files/create와 완전히 유사하며, 유일한 차이점은 파일이 아니라 diff를 가져온다는 점이다.

"""
def file_confirm(request,*args,**kwargs):
	"""Amazon S3에 성공적으로 파일이 업로드 되었는지 확인한다.


	:URL: https://api.server.com/api/0/files/confirm/<path>


	:Version: 0


	:Method: POST


	:param key: 필수 사항. 이 매개 변수는 /files/create method에서 사전에 수신. 특정 사용자(즉, 클라이언트 시스템)가 새 파일을 업로드하는 것을 식별하는데 사용된다.


	:param size: 선택 사항. 생성한 파일의 크기. 파일 업로드가 올바르게 되었는지를 확인하는데 사용한다.


	:param checksum: 선택 사항. 파일 중복 제거와 파일 업로드가 제대로 이루어 졌는지 확인하는 checksum(md5).


	:Return: 업로드 된 파일의 메타 데이터.


	:Error 403: 파일 버전이 올바르지 않다.


	:Error 404: 특정 파일을 찾을 수 없다.

"""
def diff_confirm(request,*args,**kwargs):
	"""Amazon S3에 성공적으로 파일이 업로드 되었는지 확인한다.


	:URL: https://api.server.com/api/0/files/confirm/<path>


	:Version: 0


	:Method: POST


	:param version: 필수 사항. Diff를 가져오기 위한 클라이언트에 있는 현재 파일의 버전.


	:param key: 필수 사항. /files/confirm_from_diff method를 통해 다운로드가 성공적으로 완료되었는지 확인하기 위해 필요한 매개 변수이며, 이를 통해 특정 사용자(즉, 클라이언트 시스템)가 diff를 통해 새 버전의 파일을 생성함을 알 수 있다.


	:Return: 새로운 파일을 위한 메타데이터.


	:Error 403: 클라이언트의 파일 버전이 매우 오래 되었다. (즉, 클라이언트가 새 버전을 이미 가지고 있거나, 최신 버전의 파일이 없는 경우 클라이언트가 새 버전을 생성하려고 시도한다).


	:Error 409: 새로운 파일 버전을 생성하고 난 후 (diff와 파일의 이전 버전을 통해), 새로 생성된 파일의 checksum이 (확인을 위해 /files/create_from_diff method로 전송된) checksum과 일치하지 않는다.

"""
def files_versions(request,*args,**kwargs):
	"""파일 버전 목록을 반환한다. 버전은 생성한 날짜를 기준으로 (재귀적으로) 정렬되며, 첫번째 버전은 현재 버전이다.


	:URL: https://api.server.com/api/0/files/versions/<path>


	:Version: 0


	:Method: GET


	:param skip: 선택 사항. Page:by:page 디스플레이를 활성화.


	:param limit: 선택 사항. 제한된 레코드의 양


	:param extra: 선택 사항. 각 파일 버전에 대한 정보에 extra:data를 추가


	:Return: 파일 버전을 설명하는 객체 배열.


	:Error 404: 지정된 파일을 찾을 수 없다.


	:Note: 매개 변수 restored_timestamp #은 복원된 유닉스 타임스탬프 UTC 버전의 복원된 버전이다.

	"""
def files_restore_version(request,*args,**kwargs):
	"""지정된 파일을 복원한다. “복원된”유형의 새 버전을 가져온다.


	:URL: https://api.server.com/api/0/files/restore/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 파일 경로.


	:param version: 필수 사항. 파일의 버전 숫자.


	:Return: 복원된 버전 파일의 메타데이터.


	:Error 404: 지정된 파일이나 버전을 찾을 수 없다.

"""