import cv2

video = cv2.VideoCapture("video.mp4")

# enquanto houver video carrega frame a frame na janela
while True:
    ret, frame = video.read()

    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    h_eq = cv2.equalizeHist(frame_grayscale)
    cv2.imshow("/Equalizada", h_eq)

    # se o usuario digitar a tecla 1 ou esc, fecha o loop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
