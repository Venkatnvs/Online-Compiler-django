from django.shortcuts import render
from .models import QTests

def main(request):
    a = QTests.objects.first()
    return render(request,'qtest/index.html',{"qtest":a.question})