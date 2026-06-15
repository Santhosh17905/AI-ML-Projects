import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

IMG_SIZE = (224, 224)

train_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2
)

train_data = train_gen.flow_from_directory(
    'TrainingDataset',
    target_size=IMG_SIZE,
    batch_size=32,
    class_mode='binary',
    subset='training'
)

test_data = train_gen.flow_from_directory(
    'TrainingDataset',
    target_size=IMG_SIZE,
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Transfer Learning
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Callbacks
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=1e-6),
    ModelCheckpoint('model/covid_resnet50.h5', monitor='val_accuracy', save_best_only=True)
]

print("Step 1: Training Head...")
model.fit(train_data, epochs=20, validation_data=test_data, callbacks=callbacks)

# Fine-Tuning
print("Step 2: Fine-tuning Base Model...")
base_model.trainable = True

# Freeze all layers except the last 30
for layer in base_model.layers[:-30]:
    layer.trainable = False

model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_data, epochs=10, validation_data=test_data, callbacks=callbacks)

model.save('model/covid_resnet50.h5')
print("✅ Model Saved")