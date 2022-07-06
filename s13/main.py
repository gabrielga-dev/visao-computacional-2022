import cv2 as cv


def conta_pixels_brancos(img):
    x = 0
    for l in range(len(img)):
        for c in range(len(img[0])):
            if img[l][c] > 127:
                x += 1
    return x


def retira_roi(img, zone_info):
    return img[
           zone_info['y']:zone_info['y'] + zone_info['h'],
           zone_info['x']:zone_info['x'] + zone_info['w']
           ]


def aplica_processamento_roi(roi_img):
    roi_img = cv.medianBlur(roi_img, 9, dst=None)
    roi_img = cv.medianBlur(roi_img, 9, dst=None)
    roi_img = cv.cvtColor(roi_img, cv.COLOR_BGR2GRAY)
    return roi_img


def main():
    img_vazia = cv.imread('sources/vazio.png')
    roi_a_info = {
        'x': 520,
        'y': 195,
        'w': 80,
        'h': 20,
    }
    roi_a = retira_roi(img_vazia, roi_a_info)
    roi_a = aplica_processamento_roi(roi_a)

    roi_b_info = {
        'x': 480,
        'y': 228,
        'w': 90,
        'h': 40,
    }
    roi_b = retira_roi(img_vazia, roi_b_info)
    roi_b = aplica_processamento_roi(roi_b)

    roi_c_info = {
        'x': 430,
        'y': 290,
        'w': 100,
        'h': 40,
    }
    roi_c = retira_roi(img_vazia, roi_c_info)
    roi_c = aplica_processamento_roi(roi_c)

    rois = [roi_a, roi_b, roi_c]
    rois_info = [roi_a_info, roi_b_info, roi_c_info]

    # PARTE DA CAPTURA DO VIDEO
    captura_video = cv.VideoCapture('sources/trafego.mp4')

    while True:
        ret, frame = captura_video.read()
        movimentos = [False] * len(rois)

        for i in range(len(rois)):
            roi_frame = frame[
                        rois_info[i]['y']:rois_info[i]['y'] + rois_info[i]['h'],
                        rois_info[i]['x']:rois_info[i]['x'] + rois_info[i]['w']
                        ]
            roi_frame = aplica_processamento_roi(roi_frame)
            diff_roi = cv.absdiff(roi_frame, rois[i])
            ret, roi_segmentado = cv.threshold(diff_roi, 45, 255, cv.THRESH_BINARY)

            movimentos[i] = conta_pixels_brancos(roi_segmentado) > 200
            if movimentos[i]:
                cv.rectangle(
                    frame,
                    (rois_info[i]['x'], rois_info[i]['y']),
                    (rois_info[i]['x'] + rois_info[i]['w'], rois_info[i]['y'] + rois_info[i]['h']),
                    (0, 255, 255),
                    2
                )
            else:
                cv.rectangle(
                    frame,
                    (rois_info[i]['x'], rois_info[i]['y']),
                    (rois_info[i]['x'] + rois_info[i]['w'], rois_info[i]['y'] + rois_info[i]['h']),
                    (0, 255, 0),
                    2
                )

        if movimentos[2]:
            # Desenha o texto na pista 1
            cv.putText(frame, "PARE!", (int(280), int(280)), cv.QT_FONT_NORMAL, 1, (0, 0, 255), 3)
        elif movimentos[1]:
            cv.putText(frame, "ATENCAO!", (int(250), int(280)), cv.QT_FONT_NORMAL, 1, (0, 255, 255), 3)
        else:
            cv.putText(frame, "SIGA!", (int(250), int(280)), cv.QT_FONT_NORMAL, 1, (0, 255, 0), 3)

        cv.imshow("pressione Q para sair!", frame)

        # se o usuario digitar a tecla q ou esc, fecha o loop
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    captura_video.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
