# importa os pacotes necessários
import argparse
import time
import cv2
import os

# inicializa modelo de super-resolução apredizagem profunda
#modelName = args["model"].split(os.path.sep)[-1].split("_")[0].lower()
modelName = "models/EDSR_x4.pb".split(os.path.sep)[-1].split("_")[0].lower()
modelScale = "models/EDSR_x4.pb".split("_x")[-1]
modelScale = int(modelScale[:modelScale.find(".")])

print("[INFO] carregando modelo de super-resolucao: {}".format("models/EDSR_x4.pb"))
print("[INFO] nome do modelo: {}".format(modelName))
print("[INFO] escala do modelo: {}".format(modelScale))
sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel("models/EDSR_x4.pb")
sr.setModel(modelName, modelScale)

#image = cv2.imread(args["image"])
image = cv2.imread("../caneca.jpg")

print("[INFO] largura: {}, altura: {}".format(image.shape[1], image.shape[0]))
# marcação de tempo para execução

start = time.time()
#roi = image[100:100 + 50, 300:300 + 180]  # corta rois
roi = image
#APLICA A SUPER RESOLUÇÃO
upscaled = sr.upsample(roi)
end = time.time()

#aumenta imagem por interpolação bicúbica
start = time.time()
bicubic = cv2.resize(roi, (upscaled.shape[1], upscaled.shape[0]),	interpolation=cv2.INTER_CUBIC)
end = time.time()
print("[INFO] interpolação bicubica em {:.6f} segundos".format(end - start))

# show the original input image, bicubic interpolation image, and
# super resolution deep learning output
cv2.imshow("Original", image)
cv2.imshow("Bicubica", bicubic)
cv2.imshow("Super Resolucao", upscaled)
cv2.waitKey(0)