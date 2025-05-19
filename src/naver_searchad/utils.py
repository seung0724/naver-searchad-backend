# 공통 예외 처리나 헬퍼 함수를 넣을 수 있는 곳입니다.

def ensure_list(x):
    """값이 리스트가 아니면 리스트로 감싸 줍니다."""
    return x if isinstance(x, list) else [x]
