# -*- coding: utf-8 -*-

def shares_get(request,*args,**kwargs):
	"""공유 폴더 목록을 반환한다.


	:URL: https://api.server.com/api/0/shares/


	:Version: 0


	:Method: GET


	:param whose: 선택 사항. 공유 폴더 유형. 다른 사용자와 같으면 이 메서드는 다른 사용자가 액세스 권한을 부여한 폴더를 반환하고 초대장을 받는다. 기본적으로 이 method는 모든 폴더 유형을 반환한다.


	:Return 200: 각 폴더의 메타데이터 리스트.

"""
def shared_folder_add(request,*args,**kwargs):
	"""공유 폴더에 대한 초대장을 다른 사용자에게 보낸다. member_email과 일치하는 공동 작업자가 없는 경우 시스템은 지정된 이메일을 사용하여 새로운 비활성 사용자를 만든다. 또한 이 사용자에게 폴더를 공유하고 새 사용자가 이 폴더에 액세스하기 위해 등록해야 함을 알리는 메시지를 이메일로 보낸다. 메시지에 초대 해시가 있는 링크가 포함되어 있다. 이 초대 해시 (method / accounts / create)를 사용하면 사용자는 이메일로 등록할 수 있다. 사용자가 링크를 클릭하면 사용자는 자동으로 공유 폴더에 액세스하는 데 동의하게 된다.


	:URL: https://api.server.com/api/0/shares/add/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 폴더 경로.


	:param member_email: 필수 사항. 폴더에 접근하려는 멤버의 이메일.


	:param writer: 선택 사항. 사용자가 폴더에 객체를 만들 권한이 있는 경우. 기본적으로 false로 설정되어 있다.


	:param invitation: 선택 사항. 사용자에게 보내질 초대 메시지


	:Error 403: 공유할 수 없는 폴더이다.


	:Error 404: 폴더를 찾을 수 없다.


	:Error 409: 자기 자신의 폴더를 공유하려 한다.


	:Error 424: 다른 사용자가 공유하는 루트 폴더가 있는 폴더에 대한 액세스 권한을 부여하려고 시도한다 (폴더에 대한 액세스 권한을 부여하는 것이 금지되어 있다. 그렇지 않으면 취약점이 발생할 수 있다). 예를 들어, 사용자 A는 폴더에 대한 액세스 권한을 사용자 B에게 부여한다. 사용자 B는 이 루트 폴더를 자신의 폴더 트리 내의 일부 폴더로 이동하고 최상위 폴더에 대한 액세스 권한을 사용자 C에게 부여한다. 사용자 A가 공유하는 파일 및 폴더에 적용되며 사용자 A는 이에 대해 알지 못한다.


	:Note: 공동 작업자가 공유 폴더에 대한 액세스 권한을 부여 받은 경우 코드 200이 포함 된 빈 텍스트가 반환된다.
	"""
def shared_folder_remove(request,*args,**kwargs):
	"""공유 폴더로부터 사용자를 삭제한다.


	:URL: https://api.server.com/api/0/shares/remove/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 폴더 경로.


	:param member_email: 필수 사항. 공유 폴더에서 제거된 사용자의 이메일.


	:Return 200: 삭제 성공.


	:Error 403: 폴더의 공동작업자가 아니다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def shared_folder_uninvite(request,*args,**kwargs):
	"""공유 폴더에 초대된 공동 작업자를 초대 취소한다.


	:URL: https://api.server.com/api/0/shares/uninvite/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 폴더 경로.


	:param member_email: 필수 사항. 초대장을 취소하려는 사용자의 이메일. 이메일이 지정되어 있지 않으면 모든 사용자가 초대를 수락할 가능성이 없다.


	:Return 200: 초대 취소가 성공적으로 수행되었다.


	:Error 403: 초대 취소를 수행할 수 없다(예를 들어 이미 초대를 승낙한 경우).

"""
def shared_folder_accept(request,*args,**kwargs):
	"""공유 폴더에 대한 초대를 수락한다. 사용자가 루트 폴더에 새 폴더를 보게 됩니다. 공동 작업자가 이미 유사한 이름의 폴더를 가지고 있는 경우, 순번이 폴더 이름에 추가된다. 최대 시퀀스 번호는 10이다. 공동 작업자는 폴더의 이름을 바꿀 수 있다. 이름 바꾸기는 다른 공동 작업자의 폴더 이름에 영향을 주지 않는다.


	:URL: https://api.server.com/api/0/shares/accept/


	:Version: 0


	:Method: POST


	:param hash: 필수 사항. 사용자를 공유 폴더에 초대하는 고유 초대장 해시이다. 해시는 / folders / shared / add / method의 결과이다.


	:Return 200: 폴더가 공유되었다.


	:Error 403: 해시가 해당 사용자에게 공유되지 않았다.

"""
def shared_collaborators(request,*args,**kwargs):
	"""공유된 폴더에 대한 사용자 목록을 반환한다.


	:URL: https://api.server.com/api/0/shares/collaborators/


	:Version: 0


	:Method: GET


	:param path: 필수 사항. 폴더 경로.


	:Return: 공동 작업자 집합.


	:Error 404: 파일을 찾을 수 없다.


	:Note: is_indirect: 공유된 폴더의 사용자가 직접적인지 간접적인지 나타낸다. 만약 False라면, 폴더에 대한 접근 권한을 부여 받은 직접적인 사용자이다. 만약True이면, 상위 폴더에 대한 액세스 권한을 부여 받은 간접적인 사용자이다.
	"""
def shared_folder_accept(request,*args,**kwargs):
	"""공유 폴더에 대한 초대를 수락한다. 사용자가 루트 폴더에 새 폴더를 표시한다. 이미 이름이 비슷한 폴더가 있는 경우 폴더 이름에 시퀀스 번호가 추가된다. 최대 시퀀스 번호는 10이다. 사용자는 폴더의 이름을 재지정할 수 있다. 이름 변경은 다른 사용자의 시스템에 있는 이 폴더의 이름에 영향을 주지 않는다.


	:URL: https://api.server.com/api/0/shares/accept/


	:Version: 0


	:Method: POST


	:param hash: 필수 사항. 사용자를 공유 폴더에 초대하는 고유한 초대 해시. 해시는 /folders/shared/add/의 결과이다.


	:Return 200: 폴더가 공유되었다.


	:Error 403: 해시가 해당 사용자에게 공유되지 않았다.

"""
def shared_update_collaborator(request,*args,**kwargs):
	"""일부 공유된 폴더에 대해 공동 작업자 권한을 부여한다.


	:URL: https://api.server.com/api/0/shares/update_collaborator/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 폴더 경로.


	:param member_email: 필수 사항. 공유된 폴더에 접근할 수 있는 권한을 가진 사용자의 이메일.


	:param writer: 필수 사항. True나 False. 쓰기 권한 제공.


	:Return 200: 업데이트가 성공적으로 진행되었다.


	:Error 403: 폴더에 대한 액세스 권한이 부여되지 않았다.


	:Error 404: 폴더를 찾을 수 없다.

"""
def links_get(request,*args,**kwargs):
	"""사용자가 생성한 공용 링크 목록을 반환한다.


	:URL: https://api.server.com/api/0/links/


	:Version: 0


	:Method: GET


	:param: 없음.


	:Return: 공용 링크가 생성된 파일의 메타데이터 집합.
	"""
def folder_or_file_link(request,*args,**kwargs):
	"""공용 링크를 생성한다.


	:URL: https://api.server.com/api/0/links/create/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 파일이나 폴더의 경로.


	:Return: 파일이나 폴더의 메타데이터.


	:Error 404: 파일이나 폴더를 찾을 수 없다.

"""
def folder_or_file_unlink(request,*args,**kwargs):
	"""공용 링크를 삭제한다.


	:URL: https://api.server.com/api/0/links/delete/


	:Version: 0


	:Method: POST


	:param path: 필수 사항. 파일이나 폴더의 경로.


	:Return: 파일이나 폴더의 메타데이터.


	:Error 404: 공용 링크를 찾을 수 없다.

"""
def link_metadata(request,*args,**kwargs):
	"""게시된 노드에 대한 정보를 반환한다. 노드가 별도의 항목으로 게시되거나 일부 게시된 폴더의 일부로 게시되는 경우에는 매트(mat)되지 않는다.


	:URL: https://api.server.com/api/0/links/metadata/<hash>/<path>


	:Version: 0


	:Method: GET


	:param hash: 필수 사항. 게시된 노드의 해시. 노드를 검색하는 데 사용되는 일종의 ID.


	:param path: 선택 사항. 게시된 폴더와 관련된 파일 또는 폴더의 경로.


	:param dirs_only: 선택 사항. 기본적으로 False. 만약 true라면, listing이 true일 때 폴더는 리스트에 포함.


	:param extra: 선택 사항. 기본적으로 True. Extra_data라고 불리는 추가적인 정보를 메타데이터와 함께 반환. 예: mp3태그(파일이 mp3 형태일 경우), 미리보기 정보(파일이 문서인 경우) 또는 썸네일 정보(파일이 이미지인 경우) 등.


	:param offset: 선택 사항. 기본적으로 0. 폴더 내용 목록의 오프셋.


	:param limit: 선택 사항. 기본적으로 0. 폴더를 나열할 때 반환되는 최대 객체의 이름.


	:Return: 파일 또는 폴더에 대한 메타 데이터. 결과는 API method에 의해 생성되는 것과 유사하다. 게시된 폴더와 관련하여 모든 경로가 입력된다는 차이점이 있다. 공유 루트 폴더에 대한 정보가 표시되면, JSON결과에는 게시된 루트 폴더의 이름이 포함된 매개 변수 이름이 존재한다. (이 경로의 케이스가 /와 같으면 이름을 받아오는 것은 불가능하다.).


	:Error 404: 노드를 찾을 수 없다. 예상 이유: 경로가 잘못 입력 되었거나, 노드가 더 이상 공용이 아니거나 삭제되었기 때문이다.


	:Error 403: 저작권 문제로 인해 링크가 차단되었다.

"""