import cv2
from pyzbar.pyzbar import decode

# QR 코드 이미지 파일 경로
image_path = 'qr_code.png'

# 이미지 불러오기
image = cv2.imread(image_path)

# QR 코드 디코딩
decoded_objects = decode(image)

# QR 코드에서 추출된 데이터 출력
for obj in decoded_objects:
    data = obj.data.decode('utf-8')
    print("📦 추출된 데이터:")
    print(data)

    # 만약 HTML 코드라면 저장할 수도 있어요
    if '<html' in data.lower():
        with open("output.html", "w", encoding='utf-8') as f:
            f.write(data)
        print("✅ HTML 코드가 'output.html'로 저장되었습니다.")
