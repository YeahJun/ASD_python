# -*- coding: utf-8 -*-

def shares_get(request,*args,**kwargs):
	"""공유된 폴더 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/


	:Version: 1


	:Method: GET


	:param whose: 선택 사항. 공유 폴더의 유형을 정의.


	:param 가능한 값:


	:param my: 소유자의 폴더만 반환.


	:param others: 다른 사용자가 공유하는 폴더를 본인의 공동 작업으로 반환.


	:param company: 사용자의 회사에서 공유 및 공개된 폴더를 반환.


	:param 기본적으로, method는 공유된 모든 형식들을 반환한다.


	:Return 200: 각 폴더를 위한 메타데이터 목록

"""
def shares_get_invites(request,*args,**kwargs):
	"""공동 작업자가 제공할 수 있는 초대 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/invites/


	:Version: 1


	:Method: GET


	:Return 200: 아직 수락되지 않은 초대장 목록
	"""
def shared_folder_add(request,*args,**kwargs):
	"""다른 사용자에게 공유 폴더에 대한 초대를 보낸다. 만약 공동 작업자의 정보(이메일과 같은)가 존재하지 않으면, 이 시스템은 주어진 이메일로 새로운 비활성 사용자를 생성하고, 해당 이메일로 ‘폴더를 공유하고, 접근하기 위해서는 등록해야 한다.’는 메시지를 보낸다. 이 메시지에는 초대 해시와 연결된 링크가 포함되어 있다. 이 초대 해시(method/accounts/create)를 사용하여 사용자는 이메일 등록 절차없이 등록할 수 있다. 사용자가 링크를 클릭하면, 사용자는 자동적으로 공유 폴더에 접근할 수 있다. Group_id를 사용하여 그룹을 지정하면 회원 이메일 매개 변수가 무시된다. 초대장은 그룹의 모든 구성원에게 전송된다.


	:URL: https://api.server.com/api/1/shares/add/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 파일의 경로.


	:param member_login: 선택 사항. 폴더에 접근하고 싶은 사용자의 로그인. 만약 매개 변수를 지정하지 않으면 모든 사용자가 초대를 수락할 수 있도록 접근 권한이 부여됨.


	:param writer: 선택 사항. 만약 사용자가 폴더 내에 객체를 생성할 권한이 있는 경우. 기본적으로, False로 설정.


	:param invitation: 선택 사항. 초대하는 사용자에게 보내질 초대장의 내용.


	:param public_view: 선택 사항. 초대 해시를 통해 모든 사용자에게 읽기 권한을 부여. 기본적으로 false로 설정. 초대를 수락하거나 거부한다면 읽기 권한이 사라짐.


	:param group_id: 선택 사항. 폴더를 공유할 그룹의 식별자. Group_id가 지정된 경우 member_login이 무시됨.


	:Return: 공유된 폴더를 위한 고유한 초대 토큰.


	:Error 403: 폴더 접근 권한을 부여할 수 없다.


	:Error 404: 폴더를 찾을 수 없다.


	:Error 409: 사용자가 자신을 위해 폴더 접근 권한을 부여하려고 한다.


	:Error 424: 다른 사용자가 공유하는 폴더 루트가 있는 폴더에 접근 권한을 부여하려고 한다. (이러한 폴더에 대한 접근 권한을 부여할 수 없다.) 예를 들어, 사용자 A가 사용자 B에게 폴더 접근 권한을 부여하려고 한다. 사용자 B는 이 루트 폴더를 자신의 폴더 트리의 일부로 이동하고 사용자 C 폴더에 접근 권한을 부여한다. 이러한 방법으로, 사용자 C는 사용자 A에서 공유되는 파일 및 폴더에 접근할 수 있으며 사용자 A는 이에 대해 알지 못 한다.


	:Note: 공동 작업자가 이미 폴더에 대한 접근 권한을 부여 받은 경우, 이 방법은 빈 텍스트 메시지에서 코드 200을 반환한다.
	"""
def shared_folder_accept(request,*args,**kwargs):
	"""공유 폴더에 대한 초대를 수락한다. 새 폴더가 사용자 루트 폴더에 나타난다. 이미 이름이 같은 폴더가 있는 경우 이름에 시퀀스 번호가 추가된다. (최대 시퀀스 번호는 10이다.) 공동 작업자가 폴더의 이름을 바꿀 수 있다. 폴더 이름 변경은 다른 공동 작업자의 시스템에 있는 이 폴더의 이름에 영향을 주지 않는다.


	:URL: https://api.server.com/api/1/shares/accept/


	:Version: 1


	:Method: POST


	:param hash: 필수 사항. 공유된 폴더에 대한 고유한 초대 해시. 해시는 ‘method /folders/shared/add/’로부터 받아진다.


	:Return 200: 사용자가 공유된 폴더를 삭제했다.


	:Error 403: 해시는 특정 사용자의 공유 폴더를 지정하지 않는다.

"""
def shared_folder_decline(request,*args,**kwargs):
	"""공유 폴더 초대를 거부한다.


	:URL: https://api.server.com/api/1/shares/decline/


	:Version: 0, 1


	:Method: POST


	:param hash: 필수 사항. 사용자를 공유 폴더에 초대하는 고유한 초대 해시. 해시는 ‘method /folders/shared/add/’의 결과.


	:Return 200: 사용자가 공유된 폴더를 삭제했다.


	:Error 403: 해시는 특정 사용자의 공유 폴더를 지정하지 않는다.

"""
def shared_folder_uninvite(request,*args,**kwargs):
	"""공동 작업자 또는 그룹과 함께 공유 폴더에 초대한다. 그룹을 지정하면 member_login 매개 변수가 무시된다.


	:URL: https://api.server.com/api/1/shares/uninvite/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 폴더의 경로.


	:param member_login: 선택 사항. 초대를 받을 사용자의 고유한 ID. 매개 변수를 지정하지 않으면 모든 사용자로부터 액세스가 반환된다.


	:param group_id: 선택 사항. 만약 group_ID가 지정된 경우, member_ ID는 무시된다.


	:Return 200: 초대장이 성공적으로 취소되었다.


	:Error 403: 초대장이 취소되지 않았다. (예를 들어, 이미 받아들여졌다)

"""
def shared_folder_remove(request,*args,**kwargs):
	"""공유된 폴더로부터 사용자를 제거한다.


	:URL: https://api.server.com/api/1/shares/remove/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 폴더의 경로.


	:param member_login: 필수 사항. 공유 폴더에서 삭제해야 하는 사용자의 로그인.


	:Return 200: 사용자가 공유된 폴더에서 삭제되었다.


	:Error 403: 사용자가 폴더 공동 작업자가 아니다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def shared_collaborators(request,*args,**kwargs):
	"""공유 폴더에 대한 공동 작업자 목록을 반환한다.


	:URL: https://api.server.com/api/1/shares/collaborators/


	:Version: 1


	:Method: GET


	:param path: 필수 사항. 폴더의 경로.


	:Return: 공동 작업자의 집합.


	:Error 404: 폴더를 찾을 수 없다.

	:Note: is_indirect: 공유 폴더의 직접적이거나 간접적인 공동 작업자. 만약 False이면, 이것은 폴더에 대한 접근 권한을 부여 받은 직접적인 공동 작업자이다. 만약 True이면, 이것은 상위 폴더에 대한 액세스 권한을 부여 받은 간접적인 공동 작업자이다.

"""
def shared_update_collaborator(request,*args,**kwargs):
	"""몇몇 디렉토리에 접근을 허가 받은 몇몇 공동 작업자의 액세스 권한을 갱신한다.


	:URL: https://api.server.com/api/1/shares/update_collaborator/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 폴더의 경로.


	:param member_login: 필수 사항. 공유된 폴더의 접근이 부여된 사용자의 로그인.


	:param writer: 필수 사항. True나 False. 쓰기 권한을 제공.


	:param group_id: 선택 사항. 공유 디렉터리에 대한 액세스 권한이 부여된 사용자 그룹의 ID. Member_login이 지정된 경우 이 매개 변수는 무시.


	:Return 200: 업데이트가 성공적으로 이루어졌다.


	:Error 403: 폴더 액세스 권한이 부여되지 않았다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def shared_folder_unshare(request,*args,**kwargs):
	"""폴더 액세스를 취소하고 모든 공동 작업자를 삭제한다. 모든 공동 작업자의 계정에서 폴더가 사라진다.


	:URL: https://api.server.com/api/1/shares/unshare/


	:Version: 0, 1


	:Method: POST


	:param path: 필수 사항. 폴더의 경로.


	:Return 200: 취소가 성공적으로 이루어졌다.


	:Error 404: 지정된 경로가 있는 공유 폴더를 찾을 수 없다.

"""
def handover(request,*args,**kwargs):
	"""공동 작업자 중 하나에 공유 폴더를 할당한다. 다음의 작업이 수행된다: 공동 작업자의 스토리지에 파일을 복사한다 / 공유 폴더에 대한 액세스를 다시 시도한다 / 모든 동료를 이전 소유자의 폴더에서 새 소유자의 폴더로 이동한다 / 이전 소유자는 파일 복사본을 보존한다.


	:URL: https://api.server.com/api/1/fileops/handover/


	:Version: 0, 1


	:Method: POST


	:param path: 필수 사항. 새 공동 작업자에게 전달될 폴더의 경로.


	:param member_id: 필수 사항. 소유권 권한이 부여된 공동 작업자 ID.


	:Return: 없음.


	:Error 400: 필수 매개 변수 중 하나가 설정되지 않았다.


	:Error 404: 새 공동 작업자에게 할당해야 하는 폴더를 찾을 수 없다. 또는 지정된 사용자가 존재하지 않는다.


	:Error 403: 지정한 공동 작업자가 폴더에 대한 액세스 권한이 없거나 공동 작업자가 아직 초대를 수락하지 않았다.


	:Note: 폴더 공유는 백그라운드에서 수행된다. 공동 작업자는 공유 폴더가 추가되고 이 폴더의 파일이 공유 폴더와 동일한 이름을 가진 새 폴더로 복사되는 것을 볼 수 있다.

"""
def links_get(request,*args,**kwargs):
	"""사용자가 생성한 공용 링크 목록을 반환한다.


	:URL: https://api.server.com/api/1/links/


	:Version: 1


	:Method: GET


	:param: 없음.


	:Return: 공용 링크가 생성된 일련의 파일 메타 데이터.
	"""
def folder_or_file_link(request,*args,**kwargs):
	"""공용 링크를 생성한다.


	:URL: https://api.server.com/api/1/links/create/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 파일이나 폴더의 경로.


	:param ttl: 선택 사항. 링크 작업 시간, 이 시간 이후에 링크는 무효하다. 간격의 초 단위 값 [0, 31536000]


	:param download_max: 선택 사항. 링크에 대한 참조 수 제한.


	:param password: 선택 사항. 암호를 지정하여 링크의 데이터에 액세스 가능.


	:param notify: 선택 사항.


	:param upload_folder: 서버에 파일을 업로드하기 위해 링크가 생성되었음을 나타내는 플래그.


	:Return: 파일이나 폴더를 위한 메타데이터.


	:Error 400: 파일의 다운로드 폴더에 대한 링크를 생성하려 한다.


	:Error 403: 존재하지 않는 파일에 대한 링크를 생성하려 한다.


	:Error 404: 파일이나 폴더를 찾을 수 없다.

"""
def folder_or_file_unlink(request,*args,**kwargs):
	"""공용 링크를 삭제한다.


	:URL: https://api.server.com/api/1/links/delete/


	:Version: 1


	:Method: POST


	:param path: 필수 사항. 파일이나 폴더의 경로.


	:Return: 파일이나 폴더를 위한 메타데이터.


	:Error 404: 공용 링크를 찾을 수 없다.

"""
def file_resolve_link(request,*args,**kwargs):
	"""게시된 파일에 대한 정보를 표시한다. (다운로드 URL 포함)


	:URL: https://api.server.com/api/1/links/get/<hash>/<path>


	:Version: 0, 1


	:Method: GET


	:param hash: 필수 사항. 게시된 노드의 해시. 노드를 검색하는데 사용되는 일종의 ID.


	:param path: 선택 사항. 게시된 디렉토리와 관련된 파일 경로(즉, 파일이 위치한 폴더가 아닌 폴더가 게시됨.)


	:param for_view: 선택 사항. 다운로드 링크가 필요한 용도를 지정: viewing(스트리밍) : True(컨텐츠 값 : 유형이 설정됨), 다운로드 : False(컨텐츠 값 : Disposition 설정). 기본적으로, False로 설정.


	:Return: 다운로드한 파일에 대한 정보가 들어 있는 객체.


	:Error 404: 노드를 찾을 수 없다. 찾을 수 없는 이유: 경로가 잘못 들어갔거나, 노드가 더 이상 공용이 아니거나 노드가 삭제되었다.


	:Error 403: 저작권 침해로 인해 링크가 차단되었다.

"""
def link_metadata(request,*args,**kwargs):
	"""게시된 노드에 대한 정보를 반환한다. 노드가 별도의 항목으로 게시되거나 게시된 폴더의 일부로 게시된 경우에는 매트(mat)되지 않는다.


	:URL: https://api.server.com/api/1/links/metadata/<hash>/<path>


	:Version: 1


	:Method: GET


	:param hash: 필수 사항. 공용 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:param path: 선택 사항. 게시된 폴더와 관련된 파일 또는 폴더의 경로.


	:param dirs_only: 선택 사항. 기본적으로 False. True이면, listing=true일 때 폴더에 포함된다.


	:param extra: Optional. 선택 사항. 기본적으로 True. 메타데이터와 함께 추가 정보(예: extra_data) 반환. MP3 태그(파일이 있는 경우), 미리 보기 정보(파일이 문서인 경우) 또는 미리 보기 정보(파일이 이미지인 경우) 등.


	:param offset: 선택 사항. 기본적으로 0으로 설정. 폴더 내용 목록의 처음부터 오프셋.


	:param limit: 선택 사항. 기본적으로 0으로 설정. 폴더를 나열할 때 반환되는 객체 이름의 최대값.


	:Return: 파일이나 폴더를 위한 메타데이터. 결과는 API method 메타 데이터에 의해 생성되는 것과 유사하지만 게시된 폴더와 관련하여 모든 경로가 입력된다는 차이점이 있다. 공유 루트 폴더에 대한 정보가 표시되면, JSON 결과에도 게시된 루트 폴더의 이름이 포함된 매개 변수 이름이 존재한다. (이 경우에 해당하는 경우와 마찬가지로 경로에서 이름을 가져오는 것은 불가능하다.)


	:Error 404: 노드를 찾을 수 없다. 찾을 수 없는 이유: 경로가 잘못 들어갔거나, 노드가 더 이상 공용이 아니거나 노드가 삭제되었다.


	:Error 403: 저작권 침해로 인해 링크가 차단되었다.

"""
def download_entire_public_folder(request,*args,**kwargs):
	"""전체 공유 폴더 또는 일부 선택된 항목을 아카이브로 다운로드한다. 작업 지속 시간은 추가된 파일 수에 따라 달라지며, 결과에 대한 API method를 정기적으로 요청해야 한다. 작업 준비는  https://api.server.com/api/1/task/<taskid>/ 에서 요청한다.


	:URL: https://api.server.com/api/1/links/download_as_archive/<hash>/


	:Version: 0, 1


	:Method: GET


	:param hash: 필수 사항. 게시된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:param path: 필수 사항. 아카이브에 추가될 파일 및 폴더에 대해 설정된 경로. 예: path=/1/2/3 & path=1/2/4


	:param parent_folder: 선택 사항. 아카이브 생성 요청이 발생할 때 열려 있는 사용자 폴더. 예: parent_folder=/1/2


	:Return: 작업 ID.


	:Error 403: 저작권 침해로 인해 링크가 차단되었다.
	"""
def add_public_link_to_storage(request,*args,**kwargs):
	"""게시된 폴더 또는 파일을 스토리지에 추가한다. 작업 지속 시간은 추가된 파일 수에 따라 달라진다. 따라서 https://api.server.com/api/0/task/<taskid>/에서 요청해야 한다/


	:URL: https://api.server.com/api/1/links/add_to_storage/<hash>/


	:Version: 0, 1


	:Method: GET


	:param hash: 필수 사항. 게시된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:param target_path: 선택 사항. 복사할 폴더.


	:Return: 작업 ID.


	:Error 402: 객체를 옮길 공간이 충분하지 않다.


	:Error 403: 저작권 침해로 인해 링크가 차단되었다.
	"""
