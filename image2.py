from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Load an example image
img = load_img('/media/navnkumar/New Volume/dog.jpeg')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
i = 0
for batch in datagen.flow(x, batch_size=1, save_to_dir='/media/navnkumar/New Volume/output', save_prefix='01', save_format='png'):
    i += 1
    if i > 20:
        break
