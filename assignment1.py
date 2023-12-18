import cv2, numpy as np, math
polygon = cv2.imread("polygon.jpeg", 1)
polygonGray = cv2.cvtColor(polygon, cv2.COLOR_BGR2GRAY)
#blurredPolygon = cv2.GaussianBlur(polygonGray, (11,11), sigmaX = 0)
val, thresh = cv2.threshold(polygonGray, 10, 255, cv2.THRESH_BINARY)
# displaying the original image in binary and applied gaussian blur to reduce the noise
cv2.imshow("threshold Image", thresh)
#====================================#
contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
f = open("D:\\AKSHIT\\Akshit_coding\\pythonRoboticsWinterCamp\\data.txt", 'a')
f.write("Shape\tCentroidX\tCentroidY\n")
for i in range(0,3):
    cnt = contour[i]
    # since some shapes have so many ridges therfore applying contour approximations
    epoch = 0.01 * cv2.arcLength(cnt, True)
    approxContour = cv2.approxPolyDP(cnt, epoch, True)
    sumX=0
    sumY=0
    v=len(approxContour) # no of vertices in a particular polygon
    for j in range(v-1):
        sumX+=approxContour[j,0,0]
        sumY+=approxContour[j,0,1]
    centroid = (round(sumX/v,2), round(sumY/v,2))
    
    if v==3:
        shape="triangle"
    elif v==4:
        shape="square"
    else:
        shape="hexagon"
    f.write(("{0}\t{1}\t{2}\n").format(shape, centroid[0], centroid[1]))
    cv2.drawContours(polygon, [cnt], -1, (0,255,0), 4)
f.close()
cv2.imshow("contour", polygon)
#=====================================#
cv2.waitKey(0)
cv2.destroyAllWindows()