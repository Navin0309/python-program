import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from vit_keras import vit

# Load pre-trained EfficientNetB0
base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Add ViT-based classification head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x) 
predictions = vit.ClassificationHead(num_classes=NUM_CLASSES)(x)  

# Create the combined model
model = tf.keras.Model(inputs=base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Data generators (replace with your own dataset paths)
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0/255)
train_generator = train_datagen.flow_from_directory('path/to/train_data', target_size=(224, 224), batch_size=32, class_mode='categorical')

validation_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0/255)
validation_generator = validation_datagen.flow_from_directory('path/to/validation_data', target_size=(224, 224), batch_size=32, class_mode='categorical')

# Train the model
model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Evaluate the model on the test set
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0/255)
test_generator = test_datagen.flow_from_directory('path/to/test_data', target_size=(224, 224), batch_size=32, class_mode='categorical')
test_loss, test_accuracy = model.evaluate(test_generator)
print(f"Test accuracy: {test_accuracy:.4f}")
