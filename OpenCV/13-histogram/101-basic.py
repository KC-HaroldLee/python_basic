# 히스토그램
# 출력보다는 내가 값을 가져와서 뭔갈 하지 않을까 생각

# hist = cv.calcHist(images, channels, mask, histSize, ranges[,hist[,accumulate]])

# image : unit8 또는 float32 타입의 이미지
# channels : 히스토그램계산할 채널의 인덱스
# mask : 마스크 이미지, 전체를 한다면 Mat()이나 None을 사용한다.
# hitSize : 막대의 개수
# ranges : 히스토그램을 범위
