# -*- coding: utf-8 -*-

def check_ws(request,*args,**kwargs):
	"""WebSocket을 확인한다.


	:URL: https://api.server.com/api/0/check_ws/


	:Version: 0


	:Method: GET, POST


	:param: 없음.


	:Return: 성공 또는 실패


	:Error: 없음.

"""
def events(request,*args,**kwargs):
	"""날짜별로 내림차순으로 정렬된 사용자 이벤트 목록을 반환한다.


	:URL: https://api.server.com/api/0/events/


	:Version: 0


	:Method: GET


	:param skip: 선택 사항. 초기 데이터 오프셋. 이 method는 page:by:page 디스플레이를 구성한다.


	:param limit: 선택 사항. 레코드의 수를 제한. 최대 양은 100. 기본 값은 20.


	:param type: 선택 사항. 이벤트 유형으로 필터링.


	:param person: 선택 사항. 이벤트 initiator로 필터링. 이는 다음과 같은 값을 가질 수 있다:


	:param me: 이벤트 initiator는 현재 사용자.


	:param other: 이벤트 initiator는 현재 사용자가 아니다.


	:param from_timestamp: 선택 사항. 데이터 선택의 초기 날짜.


	:param to_timestamp: 선택 사항. 데이터 선택의 마지막 날짜.


	:Return: 이벤트 집합.


	:Return type: 이벤트 유형. See below.


	:Return timestamp: 이벤트 시간 (unixtimestamp UTC, milliseconds).


	:Return path: 파일이나 폴더의 전체 경로.


	:Return deleted: 객체의 삭제 여부 표현.


	:Return oldname: 값이 이름 변경 이벤트에 추가된다. 이는 폴더나 파일의 이전 이름이다.


	:Return oldpath: 값이 이동 이벤트에 추가된다. 이는 폴더나 파일의 이전 경로이다.


	:Return old: 값이 이동 이벤트나 이름 변경 이벤트에 추가된다. 이는 이전 폴더나 파일의 정보이다. (내용과 버전).


	:Return user_id: 값이 공동 작업자를 추가하거나 삭제하는 이벤트에 추가된다. 이는 추가되거나 삭제된 공동 작업자의 ID이다.


	:Return content: 값이 파일 이벤트에 추가된다. 이는 삽입된 필드들에 대한 설명이다. See /metadata.


	:Return version: 값이 파일 이벤트에 추가된다. 이는 파일 버전이다.


	:Return: Event types


	:Return: 1. 폴더 이벤트:


	:Return folder_created: 폴더가 생성되었다.


	:Return folder_deleted: 폴더가 삭제되었다.


	:Return folder_renamed: 폴더의 이름이 변경되었다.


	:Return share_invitation_sent: 새 공동 작업자가 공유 폴더에 추가되었다. 폴더에 접근 할 수 있는 모든 사용자를 포함하여 새 공동 작업자도 해당 알림을 받는다.


	:Return share_invitation_accepted: 공동 작업자가 공유 폴더에 대한 초대를 수락한다. 폴더에 접근 할 수 있는 모든 사용자를 포함하여 새 공동 작업자도 해당 알림을 받는다.


	:Return share_invitation_declined: 공동 작업자가 공유된 폴더에 대한 초대를 취소한다. 폴더에 접근 할 수 있는 모든 사용자를 포함하여 새 공동 작업자도 해당 알림을 받는다.


	:Return share_invitation_revoked: 폴더 소유자가 공유 폴더에 대한 초대를 취소한다. 폴더에 접근 할 수 있는 모든 사용자를 포함하여 새 공동 작업자도 해당 알림을 받는다.


	:Return folder_collab_removed: 폴더 공동 작업자가 삭제되었다. 모든 공동 작업자가 알림을 받는다.


	:Return folder_unshared: 폴더에 대한 접근이 취소되었다. 모든 공동 작업자가 알림을 받는다.


	:Return folder_undeleted: 폴더가 복구되었다.


	:Return folder_moved: 폴더가 다른 폴더로 옮겨졌다.


	:Return: 2. File Events:


	:Return file_created: 파일이 생성되었다.


	:Return file_deleted: 파일이 삭제되었다.


	:Return file_undeleted: 파일이 복구되었다.


	:Return file_new_content: 새 파일 버전이 생성되었다.


	:Return file_version_restored: 이전 파일 버전이 복구 되었다.


	:Return file_renamed: 파일 이름이 변경되었다.


	:Return file_moved: 파일이 다른 폴더로 옮겨졌다.
	"""
def notices(request,*args,**kwargs):
	"""시간별로 필터링 된 사용자 알림 목록을 내림차순으로 반환한다.


	:URL: https://api.server.com/api/0/notices/


	:Version: 0


	:Method: GET


	:param type: 선택 사항. 알림 유형으로 필터링.


	:param global: 모든 사용자에게 보낸 알림.


	:param personal: 특정 사용자에게 보낸 알림.


	:param behavior: 선택 사항. 작동 유형으로 필터링.


	:param interactive: 사용자의 행동에 따른 알림 (confirmations, cancellation, etc.)


	:param static: 사용자들에게 정보를 알리기 위해 사용하는 공지.


	:param status: 선택 사항. 알림의 상태로 필터링.


	:param new: 새로운 알림.


	:param viewed: 확인한 알림 (정적인 알림에 대해).


	:param waiting: 확인을 기다리는 알림.


	:param declined: 거부된 알림. 


	:param Accepted: 허락된 알림.


	:Return: 알림 집합.

"""