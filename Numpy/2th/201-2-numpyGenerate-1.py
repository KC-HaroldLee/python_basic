import numpy as np

np.array(object, dtype=None, copy=True, order='K', subok = False, ndmin = 0) 

# object : numpy 배열, 202처럼 수동으로 만들거나, 외부 numpy배열을 가져온다.
# dtype : 데이터 타입
# copy : 객체를 복사할 것인지(?) False라면 자료형이나 순서를 고려한다고 한다.
    # 자료형이나 형태가 다르다면 copy의 인수가 False이어도 객체를 복사하여 생성한다.
# order : 메모리 레이아웃을 설정한다. 

    # C 스타일
    # 다차원 배열에서 가장 바르게 변화하는 색인 순서로 할당된다. [i][j][k]형태로 색인이 구성되어 있다면 k값부터 순차적으로 증가하고, 뒤의 배열 색인이 최댓값이 도달하면 앞의 값([j])﻿이 증가하는 구조이다.

    # Fortran 스타일
    # (역시)다차원 배열을 대상으로 할 때, 위와 반대로 [i]부터 증가하는 형식이다. 

        # order = ?
        # 'K' : 레이아웃에 최대한 일치
        # 'A' : 포틀란에 가까운지 보고 F, 아니면 C
        # 'C' : C스타일 (copy=에 영향을 받음)
        # 'F' : F스타일 (copy=에 영향을 받음)

# subok : 하위 클래스에서 배열 생성여부를 나타낸다.
    # True인경우  하위 클래스에 전달되고, False인 경우 반환된 배열은 ndarray가 된다.

# ndmin : 최소 차원 수를 나타낸다.
