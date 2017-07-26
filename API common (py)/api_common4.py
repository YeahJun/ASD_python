# -*- coding: utf-8 -*-

def edit_complaint(request,*args,**kwargs):
	"""불만 사항 상태를 편집한다. (관리자 권한이 있어야 한다.)


	:URL: https://api.server.com/api/0/copyright/edit_complaint/


	:Version: 0


	:Method: POST


	:param complaint_id: 선택 사항. 불만을 제시한 ID.


	:param status: 선택 사항. 불만 사항 접수. [새로운, 받아들여진, 거절된]


	:Error 404: 불만 사항을 찾을 수 없다.

"""
def get_complaints(request,*args,**kwargs):
	"""불만 사항 목록을 반환한다. (관리자 권한이 있어야 한다.)


	:URL: https://api.server.com/api/0/copyright/get_complaints/


	:Version: 0


	:Method: POST


	:param content_type: 필수 사항. 컨텐츠 유형.


	:param copyright_holder: 필수 사항. 저작권 소유자의 이름.


	:param name: 필수 사항. 불만을 제기하는 사용자의 이름.


	:param email: 필수 사항. 이메일.


	:param complaint_id: 필수 사항. 불만 사항 사용자의 ID.


	:param position: 선택 사항. 불만을 제기하는 사용자의 위치.


	:param phone: 선택 사항. 연락처.


	:param fax: 선택 사항. 팩스.


	:param address: 선택 사항. 주소.


	:param city: 선택 사항. 도시.


	:param region: 선택 사항. 지역.


	:param postcode: 선택 사항. 우편번호


	:param country: 선택 사항. 나라.


	:param status: 선택 사항. 불만 현황. [새로운, 받아들여진, 거절된]


	:param limit: 선택 사항. 불만 개수.


	:param offset: 선택, 첫 번째 항목에서의 오프셋.


	:param order_field: 선택 사항. 정렬할 수 있는 필드.


	:param order_direction: 선택. 방향 정렬.


	:Return: 불편 사항 목록.

	"""
def make_complaint(request,*args,**kwargs):
	"""저작권 침해 신고를 작성한다. 다른 허가가 필요 하진 않다.


	:URL: https://api.server.com/api/0/copyright/make_complaint/


	:Version: 0


	:Method: POST


	:param content_type: 필수 사항. 컨텐츠 유형.


	:param url: 필수 사항. 저작권 침해의 주소 목록.


	:param description: 필수 사항. 위반이 발생한 것과 관련된 작업에 대한 설명.


	:param copyright_holder: 필수 사항. 저작권 소유자의 이름.


	:param name: 의무, 불만을 제기하는 사용자의 이름.


	:param sign: 필수 사항. 필드에 전체 이름을 입력하는 것은 디지털 서명과 동일.


	:param email: 필수 사항. 이메일.


	:param position: 선택 사항. 불만을 제기하는 사용자의 위치.


	:param phone: 선택 사항. 연락처.


	:param fax: 선택 사항. 팩스.


	:param address: 선택 사항. 주소.


	:param city: 선택 사항. 도시.


	:param region: 선택 사항. 지역.


	:param postcode: 선택 사항. 우편번호


	:param country: 선택 사항. 나라.


	:Error 404: 불만 사항을 찾을 수 없다.


	:Return JSON 형식으로 생성된 불만 사항.
	"""
