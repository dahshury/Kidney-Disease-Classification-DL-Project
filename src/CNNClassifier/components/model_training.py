from pathlib import Path
import shutil, os
import tensorflow as tf
from CNNClassifier.utils.common import read_yaml
from CNNClassifier.constants import PARAMS_FILE_PATH
from CNNClassifier.entity.config_entity import (TrainingConfig)

class Training:
    def __init__(self, config: TrainingConfig, params_filepath = PARAMS_FILE_PATH):
        self.config = config
        self.params = read_yaml(params_filepath)
        
    # loads model from directory    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)
        
    # generates the train_val split    
    def train_val_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.20
        )
        
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset= 'validation',
            shuffle=False,
            **dataflow_kwargs
        )
        
        # If augmentation = True, augment the training images using the augmentation parameters below
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = self.params.ROTATION_RANGE,
                horizontal_flip = self.params.HORIZONTAL_FLIP,
                width_shift_range = self.params.WIDTH_SHIFT_RANGE,
                height_shift_range = self.params.HEIGHT_SHIFT_RANGE,
                shear_range = self.params.SHEAR_RANGE,
                zoom_range = self.params.ZOOM_RANGE,
                **datagenerator_kwargs
            )
            
        else:
            train_datagenerator = valid_datagenerator
        
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        
        self.model.fit(
            self.train_generator,
            epochs = self.config.params_epochs,
            steps_per_epoch = self.steps_per_epoch,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator,
            
        )
        
        self.save_model(
            path = self.config.trained_model_path,
            model = self.model
            )
        
        os.makedirs('model', exist_ok=True)
        shutil.copy2(self.config.trained_model_path, 'model/model.h5')