rom keras.layers import Dropout
from keras.layers.normalization import BatchNormalization
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D, Convolution2D
from keras.layers import Dropout
from keras.layers.normalization import BatchNormalization
from keras import optimizers
from keras.initializers import RandomNormal
import warnings
warnings.filterwarnings("ignore")

input_dim =  (28, 28, 1)
batch_size = 128 
nb_epoch = 50

#For relu layers
#If we sample weights from a normal distribution N(0,σ) we satisfy this condition with σ=√(2/(ni). 
#h1 =>  σ=√(2/(fan_in) = 0.050  => N(0,σ) = N(0,0.0505)
#h2 =>  σ=√(2/(fan_in) = 0.0625  => N(0,σ) = N(0,0.0625)
#h3 =>  σ=√(2/(fan_in) = 0.0741  => N(0,σ) = N(0,0.0741)
#out =>  σ=√(2/(fan_in+1) = 0.125  => N(0,σ) = N(0,0.125)

model_3_hidden = Sequential()

model_3_hidden.add(Dense(512, activation='relu', input_shape=input_dim, kernel_initializer=RandomNormal(mean=0.0, stddev=0.0505, seed=None)))
model_3_hidden.add(BatchNormalization())
model_3_hidden.add(Dropout(0.5))

model_3_hidden.add(Dense(364, activation='relu', kernel_initializer=RandomNormal(mean=0.0, stddev=0.0625, seed=None)))
model_3_hidden.add(BatchNormalization())
model_3_hidden.add(Dropout(0.5))

model_3_hidden.add(Dense(128, activation='relu', kernel_initializer=RandomNormal(mean=0.0, stddev=0.0741, seed=None)))
model_3_hidden.add(BatchNormalization())
model_3_hidden.add(Dropout(0.5))

model_3_hidden.add(Dense(1, activation='sigmoid', kernel_initializer=RandomNormal(mean=0.0, stddev=0.125, seed=None)))

#Compile the model
optim=optimizers.Adamax(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
model_3_hidden.compile(optimizer=optim, loss='binary_crossentropy', metrics=['accuracy'])

#Get a summary of the model.
print(model_3_hidden.summary())
