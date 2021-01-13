import tensorflow.keras as keras
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

model = keras.models.load_model('../data/rsimple/models.keras')
print(model)
print(model.summary)
datagen = ImageDataGenerator()
test_it = datagen.flow_from_directory('../data/rsimple/p_test/',target_size=(224, 224), class_mode='binary',batch_size=40,shuffle = False)
Y_pred = model.predict(test_it,verbose = 1,batch_size = 40)
y_pred = np.where(Y_pred > 0.5, 1,0)
print(confusion_matrix(test_it.classes, y_pred))
# val_loss = model.evaluate(val_it)
# test_loss = model.evaluate(test_it)

print(test_it.class_indices)

print(classification_report(test_it.classes,y_pred))