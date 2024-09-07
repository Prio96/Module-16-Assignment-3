from django.db import models
from Category.models import TaskCategoryModel
import datetime
# Create your models here.
class TaskModel(models.Model):
    Task_Title=models.CharField(max_length=80)
    Task_Description=models.CharField(max_length=255)
    Is_Completed=models.BooleanField(default=False)
    Categories=models.ManyToManyField(TaskCategoryModel)
    Task_Assign_Date=models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.Task_Title
