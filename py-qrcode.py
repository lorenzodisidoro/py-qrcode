import cv2
import numpy as np

cam = cv2.VideoCapture(0)
qrDecoder = cv2.QRCodeDetector()
cv2.namedWindow("QRCode detector")
img_counter = 0

# @function 'display' displays an frame in the specified window
# @param 'frame' type <class 'numpy.ndarray'>
# @param 'subFrame' type <class 'numpy.ndarray'>
def display(frame, subFrame):
    n = len(subFrame)
    for i in range(n):
        cv2.line(frame, tuple(subFrame[i][0]), tuple(subFrame[ (i+1) % n][0]), (255, 0, 0), 3)

# @function 'detect_qr' detect and decode qrcode from frame
# @param 'inputFrame' type <class 'numpy.ndarray'>
# @return if detected type 'bool'
def detect_qr(inputFrame):
    content, subImage, rectifiedImage = qrDecoder.detectAndDecode(inputFrame)
    
    if len(content) > 0:
        print("Decoded data: {}".format(content))

        # color rect
        display(inputFrame, subImage)
        rectifiedImage = np.uint8(rectifiedImage)
        cv2.imshow("Rectified QRCode", rectifiedImage)
        return True
    else:
        return False

# Waiting to capture
print("Waiting to scan a QRCode")
undetected = False
while not(undetected):
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break

    cv2.waitKey(1)
    undetected = detect_qr(frame)
   
cam.release()
cv2.destroyAllWindows()