from marshal import load
from pyexpat import model
from sre_parse import SPECIAL_CHARS
from django.db import models
import joblib
import numpy as np

# Create your models here.


class Cancer(models.Model):
    mean_radius=models.FloatField(null=False)
    mean_texture=models.FloatField(null=False)
    mean_perimeter=models.FloatField(null=False)
    mean_area=models.FloatField(null=False)
    mean_smoothness=models.FloatField(null=False)
    mean_compactness=models.FloatField(null=False)
    mean_concavity=models.FloatField(null=False)
    mean_concave_points=models.FloatField(null=False)
    mean_symmetry=models.FloatField(null=False)
    mean_fractal_dimension=models.FloatField(null=False)
    radius_error=models.FloatField(null=False)
    texture_error=models.FloatField(null=False) 
    perimeter_error=models.FloatField(null=False)
    area_error=models.FloatField(null=False)
    smoothness_error=models.FloatField(null=False)
    compactness_error=models.FloatField(null=False)
    concavity_error=models.FloatField(null=False)
    concave_points_error=models.FloatField(null=False)
    symmetry_error=models.FloatField(null=False)
    fractal_dimension_error=models.FloatField(null=False)
    worst_radius=models.FloatField(null=False)
    worst_texture=models.FloatField(null=False)
    worst_perimeter=models.FloatField(null=False)
    worst_area=models.FloatField(null=False)
    worst_smoothness=models.FloatField(null=False)
    worst_compactness=models.FloatField(null=False)
    worst_concavity=models.FloatField(null=False)
    worst_concave_points=models.FloatField(null=False)
    worst_symmetry=models.FloatField(null=False)
    worst_fractal_dimension=models.FloatField(null=False)
    prediction=models.CharField(max_length=50)
    



    def save(self,*args, **kwargs):
        ml_model=joblib.load('ml_model/ml_model.joblib')
        ml_scale = joblib.load('ml_model/ml_scalar.joblib')

        input_data = (
               self.mean_radius,self.mean_texture,self.mean_perimeter,self.mean_area,self.mean_smoothness,self.mean_compactness,
            self.mean_concavity,self.mean_concave_points,self.mean_symmetry,self.mean_fractal_dimension,self.radius_error,
            self.texture_error,self.perimeter_error,self.area_error,self.smoothness_error,self.compactness_error,
            self.concavity_error,self.concave_points_error,self.symmetry_error,self.fractal_dimension_error,
            self.worst_radius,self.worst_texture,self.worst_perimeter,self.worst_area,self.worst_smoothness,
            self.worst_compactness,self.worst_concavity,self.worst_concave_points,self.worst_symmetry,
            self.worst_fractal_dimension
        )
        input_data = np.array(input_data)

        input_data = input_data.reshape(1,-1)

        scaler_data = ml_scale.transform(input_data)

        predictions = np.round(ml_model.predict(scaler_data))

        if predictions[0]==0:
            self.prediction = 'Malignant'
        else:
            self.prediction = 'Benign'

        return super().save(*args,**kwargs)


    # def __str__(self):
    #     return self.name