import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.click()



pyautogui.hotkey('ctrl', 'right')

pyautogui.press('tab')




pyautogui.moveTo(380, 92)
pyautogui.click()




pyautogui.press('tab', presses=6)



str  = '''높은 나무 가지 잔디 깎기 정리기 양날 원예 트리머
길이 조절 울타리 가드닝 늘이기 잔 가지 트리머 장대
충전식 조경 관목 학교 공기관 헤지 트리머 가지 치기
농구 보관 스포츠 장비 짐볼 거치대 짐볼정리대 요가
가정용 거실 축구공 농구공 수납 랙 프레임 전시 보관
축구공 농구공 보관 체육관 공정리대 디스플레이
축구공 농구공 배드민턴 라켓 보관 디스플레이 랙
홈 플러오 스토리지 마무리 볼 랙 용품 전시 걸이
홈 체육관 강당 실내 축구 농구 배구 공 라켓 보관
볼 공 보관 바구니 랙 수납 정리 스포츠 장비 거치대
거실 피트니스 장비 거실 복도 정리 랙 스탠드 족구공
실내 공간 절약 농구 축구 보관 바구니 정리 홀더
텔레스코픽 울타리 스텐자바라대문 단열방화문 접이식
텔레스코픽 절연 벨트 울타리 가드 레일 콘서트 은행
절연 건설 울타리 안전 가드 이동식 접근금지 펜스
벽걸이 형 경고 벨트 격리 벨트 라인 복도 건물 은행
교통 도로 난간 안전 가드 바리게이트 울타리 휀스
유치원 건설 건축 안전 난간 담 도로 바리게이트 분리
1 미터 라인 전시회 카페 콘서트 야외 보안 대기열
이중층 절연 벨트 은행 보건소 대기열 이동식 울타리
스테인레스 스틸 이동식 길이 조절 유치원 울타리
학교 전원 주택 집 안뜰 벽 정원 울타리 접근 방지
소시지 충진기
수제 소시지 소시지 가공 분쇄기 가정용 업소용 수동
돼지고기 육가공 분쇄기 가정용 업소용 크랭크 공장
전기 전동 자동 고기 분쇄기 충정식 고깃집 고기집
상업용 돼지 소 치킨 닭 고기 다지기 대형 뼈 분쇄기
상업용 공장용 고기 다짐기 분쇄기 소시지 메이커
전기 후추 다진 야채 마늘 생각 분쇄기 빻기 기계
가정용 수동 만두 속 고기 소시지 으깨기 순대 갈개
가정용 식당 캠핑 통조림 순대 소시지 간식 기계
가정용 육회 고기 다짐육 핫도그 햄 충진기 케이싱
수동 회전식 육회 만들기 고기 그라인더 통조림 분쇄
중세 유럽풍 프랑크 소시지 정육점용 업소용 육회
가정용 업소용 레스토랑 수제 소시지 만들기 기계
농업용 수동 비닐 덮기 피복기 멀칭기 고추밭
멀칭 필름 커버 피복기 고추 농사 비닐 멀칭기 덮개
필름 멀칭 기계 커버 텃밭 흑막 필름 비닐 머신 장비
소형 논 밭 멀칭 기계 비닐씌우는 피복기 주말 농장
농업용 농사용 작물 필름 덮기 덮는 기계 피복 덮개
수동 라미네이팅 부설 필름 멀칭 작물 보호 텃밭 관리
필름 라미네이팅 필름 깔기 코팅 농기구 자재 커버
멀칭 버클 필름 커버 비닐 씌우는 기계 잡초 방지
양식 물고기 방수포 하수 탱크 누수 방지 검정색 필름
저수지 하수 탱크 찌꺼기 커버 플라스틱 방수 필름
농업 래핑 랩핑 밀봉 열 수축성 플라스틱 단일 필름
단안 전화 망원경 고배율 고화질 야간 투시경 소형 
휴대폰 원격 야외 모니터 프로브 세트
무선 360도 야간 투시 카메라 야외 CCTV 홈 모니터
hd 휴대 전화 사각 지대 원격 카메라 CCTV 야간 '''

list = str.split('\n')

list.reverse()

for i in range(0, len(list)):
    time.sleep(0.3)
    a = list[i]
    time.sleep(0.3)
    pyperclip.copy(a)
    pyautogui.hotkey('command', 'v')
    pyautogui.press('tab', presses=5)











#ctrlright
# pyautogui.hotkey('command', 'c')



# pyautogui.hotkey('command', 'a')


# pyautogui.hotkey('command', 'v')


# ctrl
# tab
# command

'''
print("--" * 30)
# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()
print(f"screenWidth, screenHeight")
print(screenWidth, screenHeight)
print("--"*30)

# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()
print(f"currentMouseX, currentMouseY")
print(currentMouseX, currentMouseY)
print("--" * 30)

for i in range(0, 20):
    time.sleep(1) # Delay a second.
    currentMouseX -= 100
    currentMouseY -= 100
    pyautogui.moveTo(currentMouseX, currentMouseY)
print("--" * 30)


pyautogui.moveTo(100, 200)

'''