from django.contrib import admin
from .models import Experiment, Order, Data, PreStudyData, PostStudyData, TrainingData

admin.site.register(Experiment)
admin.site.register(Order)
admin.site.register(Data)
admin.site.register(PreStudyData)
admin.site.register(PostStudyData)
admin.site.register(TrainingData)

