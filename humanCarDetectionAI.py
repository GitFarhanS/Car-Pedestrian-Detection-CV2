import cv2

print(cv2.__file__)


classifierFile = "cars.xml"

video = cv2.VideoCapture('lowRes.mp4')

carTrackerFile = 'cars.xml'
pedestrianTrackerFile = "pedestrian.xml"

carTracker = cv2.CascadeClassifier(classifierFile)
pedestrianTracker = cv2.CascadeClassifier(pedestrianTrackerFile)




#run forever until
while True:
    (readSuccessful, frame) = video.read()

    if readSuccessful == True:
        greyScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    else:
        break

    cars = carTracker.detectMultiScale(greyScale)
    pedestrian = pedestrianTracker.detectMultiScale(greyScale)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
    for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('hehhe', frame)

    cv2.waitKey(1)
     