import os
import cv2
import numpy as np
from PIL import Image

recog = cv2.createLBPHFaceRecognizer();
path = "dataSet"

def img_id(path):
    imgpath = [os.path.join(path,f) for f in os.listdir(path)]

    faces = []
    ids = []

    for imid in imgpath:
        faceimg = Image.open(imid).convert('L')
        facenp = np.array(faceimg,'uint8')
        ID =int( (os.path.split(imid)[-1].split('.')[1]))
        faces.append(facenp)
        ids.append(ID)
        cv2.imshow("Learning",facenp)
        cv2.waitKey(10)
    return ids, faces

ids,faces = img_id(path)
recog.train(faces,np.array(ids))
recog.save("recognizer/LearningData.yml")
cv2.destroyAllWindows()
