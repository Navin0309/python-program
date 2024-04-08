import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow_io.experimental import vision_transformer

# Data Preparation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2)  # Splitting the data into training and validation sets

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'path_to_training_data',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training')

validation_generator = train_datagen.flow_from_directory(
    'path_to_training_data',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='validation')

# EfficientNetB0 Model
effnet_model = EfficientNetB0(include_top=False, input_shape=(224, 224, 3))
effnet_model.trainable = False  # Freeze the weights of the pretrained model

# Vision Transformer (ViT) Model
vit_model = vision_transformer.VisionTransformer(
    image_size=(224, 224, 3),
    patch_size=(16, 16),
    num_layers=6,
    num_classes=10,  # Change this according to your number of classes
    d_model=512,
    num_heads=8,
    mlp_dim=1024,
    channels=3,
    dropout=0.1,
    name='vision_transformer',
)

# Combine EfficientNetB0 and ViT models
inputs = layers.Input(shape=(224, 224, 3))
x1 = effnet_model(inputs)
x2 = vit_model(inputs)
x = layers.Concatenate()([x1, x2])
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.2)(x)
outputs = layers.Dense(10, activation='softmax')(x)  # Adjust the number of classes accordingly

combined_model = models.Model(inputs=inputs, outputs=outputs)

# Compile the model
combined_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = combined_model.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator)

# Evaluate the model
test_generator = test_datagen.flow_from_directory(
    'path_to_test_data',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical')

test_loss, test_accuracy = combined_model.evaluate(test_generator)
print(f'Test accuracy: {test_accuracy}')


# https://github.com/Navin0309/python-program.git