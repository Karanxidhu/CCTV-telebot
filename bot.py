import cv2
import telepot
import os

apiToken = '6829665757:AAEnNgJG1HZUMIeJPMtC94XcbVLrYUx7NGg'
chatID = 1020187657
bot = telepot.Bot(apiToken)
os.chdir('/home/karanxidhu/code/telegram bot')
cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, image = cap.read()
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # detect humans in input image
    (humans, _) = hog.detectMultiScale(image, winStride=(10, 10),
    padding=(32, 32), scale=1.1)

    # getting no. of human detected
    print('Human Detected : ', len(humans))

    # loop over all detected humans
    for (x, y, w, h) in humans:
        pad_w, pad_h = int(0.15 * w), int(0.01 * h)
        cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

    if len(humans)>0:
        if count == 0:
            bot.sendMessage(chatID, '👨 peroson detected! 👨')
        cv2.imwrite(f'{count}.jpg', image) 
        bot.sendPhoto(chatID,photo=open(f'{count}.jpg', 'rb'))
        if os.path.exists(f"{count}.jpg"):
            os.remove(f"{count}.jpg")
        count = count + 1
    else: 
        count = 0
    # display the output image
    cv2.imshow("Image", image)

    if cv2.waitKey(30) & 0xFF == 27:
        break
cv2.destroyAllWindows()