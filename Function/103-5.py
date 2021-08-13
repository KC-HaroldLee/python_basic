def idCardBuilder(name, gender, **etcInfo):
    print("이름: %s | 성별: %s 기타사항 : %s" %(name, gender, etcInfo))


idCardBuilder('코베인','남자')
idCardBuilder('커트니','여자', part='개발팀')
idCardBuilder('데이브','남자', part='개발팀', now='퇴사예정')
