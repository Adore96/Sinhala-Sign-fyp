import cv2

cap = cv2.VideoCapture(0)  # give the file name you need to read or the camera number(try with 0 , -1,1)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('WebcamVideos/output.mp4', fourcc, 20.0, (
1280, 720))  # name of the output , fourcc format(fourcc.org), number of frames /sec , size of the current video

if (cap.isOpened()):
    while (True):  # is working only if the cap opened that means if the filepath or camera is correct.
        ret, frame = cap.read()  # ret value will be 0 or 1 for true and false in the while loop value and the frame will be storing captured frames
        # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow("Frame", frame)
        print("[INFO] : Video Size ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT), ",", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

else:
    print('[INFO] Invalid file format or path to the camera is not set.')

cap.release()
out.release()
cv2.destroyAllWindows()
