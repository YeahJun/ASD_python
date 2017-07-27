# -*- coding: utf-8 -*-

def list_timeline(request,*args,**kwargs):
	"""사용자 앨범을 나열한다.


	:URL: https://api.server.com/api/1/timeline/<path>


	:Version: 1


	:Method: GET


	:Header: Mountbit:Auth: 사용자 인증 토큰.


	:param path: 사용되지 않음. (reserved, not used)


	:param only_photo_dir: 선택 사항. 저장 폴더에서 사진과 비디오를 반환하는 플래그


	:param deleted: 선택 사항. 기본적으로 값은 False 설정된다. True 면 제거된 객체들이 리스트에 포함된다. False 면 포함되지 않는다.


	:param offset: 선택 사항. 기본적으로 값은 0으로 설정된다. 폴더의 내용 리스트의 시작 지점으로부터의 오프셋


	:param limit: 선택 사항. 기본적으로 값은 0으로 설정된다. 객체의 최대 수는 폴더 목록으로부터 반환된다.


	:Return: 이 정보는 API / metadata method에서 반환한 것과 동일하다. 헤더 ETag 외에도 전체 타임 라인의 해시가 반환된다. 이 해시는 If:None:Match 헤더에 포함되어 서버에 전달하여 클라이언트 쪽에서 캐싱에 사용할 수 있다. 서버의 타임 라인이 변경되지 않은 경우 코드 304와 빈 본문이 응답으로 반환된다. 일반적인 API / metadata 필드를 제외한 각 파일에는 새로운 필드가 추가된다:


	:Return is_photo_dir: true 인 경우 파일은 모바일 클라이언트의 사진 / 비디오 저장 폴더 내에 있다.


	:Return shooting_time: 이미지 / 비디오 생성 또는 슈팅 시간 (UTC 타임스탬프)


	:Error 304: 폴더 내용 중 수정된 것이 없다. (If:None:Match 헤더에 의해서 결정됨)

"""