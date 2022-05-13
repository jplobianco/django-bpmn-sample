from django.db import models


class BPMN(models.Model):
    diagram = models.TextField('Diagram')

    def __repr__(self):
        return f'BPMN [{self.id}]'

    def __str__(self):
        return f'BPMN [{self.id}]'




