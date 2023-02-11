from django.db import models
from  django.contrib.auth.models import User

class QTests(models.Model):
    LangChoices = (
        ("Python","Python"),
        ("C","C")
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.TextField()
    allow_lang = models.CharField(choices=LangChoices, default="C",max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
