import os
from FCNdense import FCN_model 
from generator import Generator
import tensorflow as tf

def train(model, train_generator, val_generator, epochs = 50):
    # To continue training with a saved state of the model, uncomment and use the following line 
    #model.load_weights('./snapshots/model_epoch_21_loss_1.13_acc_0.66_val_loss_0.83_val_acc_0.81.h5')
    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.0001),
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    checkpoint_path = './snapshots'
    os.makedirs(checkpoint_path, exist_ok=True)
    model_path = os.path.join(checkpoint_path, 'model_epoch_{epoch:02d}_loss_{loss:.2f}_acc_{accuracy:.2f}_val_loss_{val_loss:.2f}_val_acc_{val_accuracy:.2f}.h5')
    
    history = model.fit_generator(generator=train_generator,
                                    steps_per_epoch=len(train_generator),
                                    epochs=epochs,
                                    callbacks=[tf.keras.callbacks.ModelCheckpoint(model_path, monitor='val_loss', save_best_only=True, verbose=1)],
                                    validation_data=val_generator,
                                    validation_steps=len(val_generator))

    return history

if __name__ == "__main__":
    
    # Create FCN model
    model = FCN_model(len_classes=2, dropout_rate=0.2)

    # The below folders are created using utils.py
    train_dir = 'train'
    val_dir = 'test'
    
    # You can increase the batch size unless you get out of memory error
    BATCH_SIZE=2
    train_generator = Generator(train_dir, BATCH_SIZE, shuffle_images=True, image_min_side=24)
    val_generator = Generator(val_dir, BATCH_SIZE, shuffle_images=True, image_min_side=24)

    EPOCHS=100
    history = train(model, train_generator, val_generator, epochs=EPOCHS)