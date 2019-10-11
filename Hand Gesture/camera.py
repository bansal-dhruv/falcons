import numpy as np
import cv2
from keras.layers import Dense
from keras.models import load_model
from keras.models import Model
from keras.applications.vgg16 import VGG16
Image = np.zeros([40, 40, 3])

cap=cv2.VideoCapture(0)
while 1:
	ret, img = cap.read()
	cv2.imshow('img',img)
	k = cv2.waitKey(0)
	print('running')
	if k == 113:
		Image = cv2.resize(img, (40, 40))
		result = ""
		Image = np.reshape(Image, (1, 40, 40, 3))
		model = VGG16(weights = None, include_top = False, input_shape = (40, 40, 3))
		x = model.output
		x = Dense(64, activation='relu')(x)
		x = Dense(29, activation='softmax')(x)
		model = Model(inputs = model.input, outputs = x)
		model.load_weights("model.h5")
		# model.summary()
		result = model.predict(Image)

		map_characters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F..', 6: 'G', 7: 'H', 
		8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 
		17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 
		26: 'del', 27: 'nothing', 28: 'spacebar'}
		result = result[0][0][0]
		i = 0
		for Result in result:
			print(i, Result)
			i += 1
		print(map_characters[np.argmax(result)])
	if k == 27:
		break
