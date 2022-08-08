#Step -1
import math
import cv2
import numpy as np

def nothing(x):
    pass

#camera = "http://192.168.43.1:8080/video"
cap = cv2.VideoCapture(0)
#cap.open(camera)

# step - 2
cv2.namedWindow("Color Adjustments")
cv2.resizeWindow("Color Adjustments", (300,300))
cv2.createTrackbar("Thresh", "Color Adjustments", 0, 255, nothing)


# COlor Detection Track

cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)
cv2.createTrackbar("Upper_H", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)


while cap.isOpened():
    rest, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (600, 500))
    cv2.rectangle(frame, (0,1), (300, 500), (255, 0, 0), 0)
    crop_img = frame[1:500, 0:300]
    hsv  = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
    # step - 4
    # detecting hand
    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustments")

    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustments")

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    # Creating Mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)        # inRange() return lower and upper range within bg white and fg black
    filter = cv2.bitwise_and(crop_img, crop_img, mask=mask)  # in filter return value is mask contain only values

    # step -5
    mask1 = cv2.bitwise_not(mask)                            # for contours bg = black and fg = white so i have performed bitwise_not operations.
    m_g = cv2.getTrackbarPos("Thresh", "Color Adjustments")  # getting track bar value
    ret, thresh = cv2.threshold(mask1, m_g, 255, cv2.THRESH_BINARY)
    dilata = cv2.dilate(thresh, (1, 1), iterations=6)

    # step -6

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # findcoutours  return to coordinate of selected objects using threshold. as well as herichay
    try :


        contours_max   = max(contours, key=lambda x: cv2.contourArea(x))     # find maximum of contours in crop_image return maximum coordinate  if coutours isn't available in then error occure so i have already use try and except.
        epsilon = 0.0005*cv2.arcLength(contours_max, True)  # for convexfull find minimum vertex
        data= cv2.approxPolyDP(contours_max,epsilon,True)
        hull = cv2.convexHull(contours_max)   #contours_max coordinate of contours_max and pass convexHull and retunn hull list

        cv2.drawContours(frame, [contours_max], -1, (50, 50 , 150), 2)
        cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)

        # step -8
        # find convexity defects
        hull = cv2.convexHull(contours_max, returnPoints=False) # if return=False then it is return acculay coordinate of convexHull
        defects = cv2.convexityDefects(contours_max, hull)
        count_defects = 0
        for i in range(defects.shape[0]):
            s, e, f, a = defects[i, 0]
            start = tuple(contours_max[s][0])
            end = tuple(contours_max[e][0])
            far = tuple(contours_max[f][0])
            # cosin Rule


            a = math.sqrt((end[0]- start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1]- far[1])**2)
            angle = (math.acos((b**2 + c**2 - a**2)/(2 *b*c))*180)/3.14
            if angle <= 50:
                count_defects +=  1
                cv2.circle(crop_img, far, 5, [255,255,255], -1 )
        # step-9

        #print(count_defects)
        if count_defects == 0:

            cv2.putText(frame, "1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 1:
            cv2.putText(frame, "2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 2:

            cv2.putText(frame, "3", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 3:

            cv2.putText(frame, "4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 4:

            cv2.putText(frame, "5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            pass


    except:
        pass
    cv2.imshow("original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Thresh", thresh)

    k = cv2.waitKey(25)  & 0XFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
