from django.db import models
import random 

class Order(models.Model):
    #change max-length accoridng to new slide number
    slide_order = models.CharField(max_length=100, unique=True)

class Experiment(models.Model):
    participant_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200, null=True)
    group= models.CharField(max_length=1)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    statusBaseline = models.CharField(max_length=200, default='open')
    statusXAI = models.CharField(max_length=200, default='open')

    class Meta:
        verbose_name_plural = 'Experiments'

class Data(models.Model):
    condition = models.CharField(max_length=100)
    slide = models.CharField(max_length=10, null=True)
    tcp_est = models.CharField(max_length=200, null=True)
    confidence_score = models.CharField(max_length=200, null=True)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, null=True)
    time = models.CharField(max_length=10, null=True)

class PreStudyData(models.Model):
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    experience = models.CharField(max_length=100)
    interest_in_tech = models.CharField(max_length=100)
    adoption_of_new_tech = models.CharField(max_length=100)
    familiarity_with_AI = models.CharField(max_length=100)
    experiment = models.OneToOneField(Experiment, on_delete=models.CASCADE, null=True)

class PostStudyData(models.Model):
    condition = models.CharField(max_length=100)
    item1 = models.CharField(max_length=10, null=True)
    item2 = models.CharField(max_length=10, null=True)
    item3 = models.CharField(max_length=10, null=True)
    item4 = models.CharField(max_length=10, null=True)
    item5 = models.CharField(max_length=10, null=True)
    item6 = models.CharField(max_length=10, null=True)
    item7 = models.CharField(max_length=10, null=True)
    item8 = models.CharField(max_length=10, null=True)
    question1 = models.CharField(max_length=200, null=True)
    question2 = models.CharField(max_length=200, null=True)
    question3 = models.CharField(max_length=200, null=True)
    question4 = models.CharField(max_length=200, null=True)
    question5 = models.CharField(max_length=200, null=True)
    question6 = models.CharField(max_length=200, null=True)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, null=True)

class TrainingData(models.Model):
    condition = models.CharField(max_length=100)
    slide = models.CharField(max_length=10, null=True)
    tcp_est = models.CharField(max_length=200, null=True)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, null=True)
