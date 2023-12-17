import cv2, numpy as np

capture = cv2.VideoCapture("assignment2Vid.mp4")
val,bg = capture.read()
h,w = bg.shape[:2]
bg = cv2.resize(bg,(int(w/3), int(h/3)))

# frame visualization
isTrue = True
frame_list=[]
kernel = np.ones((37,37), np.uint8)
kernel2=np.ones((43,43), np.uint8)
while isTrue:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    t= frame.shape[:2]
    frameOriginal = cv2.resize(frame, (int(t[1]/3), int(t[0]/3)))
    frame=cv2.cvtColor(frameOriginal, cv2.COLOR_BGR2GRAY)
    frame = cv2.bilateralFilter(frame, d=51, sigmaColor=35 , sigmaSpace =35)
    threshold,main =cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    main = cv2.erode(main, kernel)
    main = cv2.dilate(main, kernel2)
    mainInv = cv2.bitwise_not(main)
    frame = cv2.bitwise_and(bg, bg, mask=main)
    frameInv = cv2.bitwise_and(frameOriginal, frameOriginal, mask = mainInv)
    final = cv2.add(frame, frameInv)
    cv2.imshow('FRAME', final)   
    if cv2.waitKey(10) & 0xFF == ord('q'): 
            break
capture.release()
cv2.destroyAllWindows()
