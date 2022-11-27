from django.shortcuts import render
from django.http import HttpResponse
from glossary.models import OriginalWords

def say_hello(request):
  query_set = OriginalWords.objects.all()
  for word in query_set:
    print(word) 

  return render(request, 'hello.html', {'name': 'Nazar'})