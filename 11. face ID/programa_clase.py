from easyfacenet.simple import facenet
import numpy as np 

np_load_old = np.load 
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

images = ["images/image1.jpg","images/image1.jpg", "images/image3.jpg", "images/image2.jpg"]
aligned = facenet.align_face(images)
comparar = facenet.compare(aligned)
print(bool(comparar[0][1]))
print(bool(comparar[0][2]))
print(bool(comparar[0][3]))

np.load = np_load_old