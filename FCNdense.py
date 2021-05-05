import tensorflow as tf
def FCN_model(len_classes=2, dropout_rate=0.2):
    
    input = tf.keras.layers.Input(shape=(None, None, 3))

    x = tf.keras.layers.Conv2D(filters=32, kernel_size=3, strides=1)(input)
    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.MaxPooling2D()(x)

    x = tf.keras.layers.Conv2D(filters=64, kernel_size=3, strides=1)(x)
    x = tf.keras.layers.Dropout(dropout_rate)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.GlobalMaxPooling2D()(x)
    x = tf.keras.layers.Flatten()(x)

    x = tf.keras.layers.Dense(units=32)(x)
    x = tf.keras.layers.Activation('relu')(x)

    x = tf.keras.layers.Dense(units=len_classes)(x)
    predictions = tf.keras.layers.Activation('softmax')(x)

    model = tf.keras.Model(inputs=input, outputs=predictions)
    
    print(model.summary())
    print(f'Total number of layers: {len(model.layers)}')

    return model

if __name__ == "__main__":
    FCN_model(len_classes=2, dropout_rate=0.2)