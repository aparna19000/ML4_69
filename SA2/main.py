import cv2
# import HandDector library from cvzone



cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Creating object to detect hand



while True:
    try:
        check, cameraFeedImg = cap.read()

        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        # Detect hand in cameraFeedImg
       
       
            # Get the landmarks from the detected hand
            
            # Get the hand type from the detected hand ( Left and Right )
           

    except Exception as e:
        print(e)

    cv2.imshow("Image", cameraFeedImg)
    cv2.waitKey(1)
