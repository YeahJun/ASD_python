def edit_complaint(request, *args, **kwargs):
	"""불만 사항 상태를 편집한다. (관리자 권한이 있어야 한다.)


	:URL : https://api.server.com/api/0/copyright/edit_complaint/


	:Version : 0


	:Method : POST


	:param :complaint_id: 선택 사항. 불만을 제시한 ID.


	:Error : 404: 불만 사항을 찾을 수 없다.

"""
def get_complaints(request, *args, **kwargs):
	"""불만 사항 목록을 반환한다. (관리자 권한이 있어야 한다.)


	:URL : https://api.server.com/api/0/copyright/get_complaints/


	:Version : 0


	:Method : POST


	:param :content_type: 필수 사항. 컨텐츠 유형.


	:Return : 불편 사항 목록.


	"""
	def make_complaint(request, *args, **kwargs):
	"""저작권 침해 신고를 작성한다. 다른 허가가 필요 하진 않다.


	:URL : https://api.server.com/api/0/copyright/make_complaint/


	:Version : 0


	:Method : POST


	:param :content_type: 필수 사항. 컨텐츠 유형.


	:Error : 404: 불만 사항을 찾을 수 없다.


	:Return : JSON 형식으로 생성된 불만 사항.


	"""