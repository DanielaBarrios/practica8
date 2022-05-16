##practica 8
import numpy as np
from matplotlib import pyplot as plt
import math as ma
import cv2 #opencv

## Laplaciano
ima = cv2.imread("gato.png")
image = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
cv2.imshow("Original",ima)
cv2.waitKey()

lap = cv2.Laplacian(image,cv2.CV_64F)# Detección de borde de Laplace
lap = np.uint8(np.absolute(lap))## Ir al valor absoluto de vuelta
cv2.imshow("Laplacian",lap)
cv2.waitKey()
cv2.destroyAllWindows()

#############################################

##Sobelx y Y
ima = cv2.imread("gato.png")
image = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
cv2.imshow("Original",ima)

 
#Detección 
sobelX = cv2.Sobel(image,cv2.CV_64F,1,0)#x gradiente de dirección
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1)#y gradiente de dirección
 
sobelX = np.uint8(np.absolute(sobelX))#x gradiente de dirección valor absoluto
sobelY = np.uint8(np.absolute(sobelY))#y valor absoluto del gradiente de dirección
 
sobelCombined = cv2.bitwise_or(sobelX,sobelY)#
cv2.imshow("Sobel X", sobelX)
###################################################

##Canny

ima = cv2.imread("gato.png")
image = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
cv2.imshow("Image",ima)#Mostrar imagen

 
#Detección de #CannyEdge
canny = cv2.Canny(image,30,150)
cv2.imshow("Canny",canny)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("Original",ima)
cv2.imshow("Sobel Y", sobelY)
cv2.waitKey()
cv2.destroyAllWindows()
