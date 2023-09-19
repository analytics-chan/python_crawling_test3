# pip install pyautogui

import pyautogui
import time

# 마우스 커서 위치 확인
pyautogui.position()

# 마우스 이동
pyautogui.moveTo(2730, 1412, 2)

# 마우스 클릭
pyautogui.click()

# 마우스 더블 클릭
pyautogui.doubleClick()

# 1초 시간 지연
time.sleep(1)

# 키보드 타이핑
pyautogui.typewrite('테스트')

# 키보드 엔터
pyautogui.typewrite(['enter'])

# 여러개 키보드 타이핑
pyautogui.typewrite(['a', 'b', 'c', 'enter'])