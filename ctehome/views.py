from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit
this_dir =Path(__file__).resolve().parent

def home_view(request, *args,**kwargs):
   
 return about_view(request, *args,**kwargs)

def about_view(request, *args,**kwargs):
   qs=PageVisit.objects.all()
   Page_qs =PageVisit.objects.filter(path=request.path)
   try:
       percent= (Page_qs.count()*100.0) /qs.count(),
   except:   
       percent = 0      
   my_title="My page"
   html_template = "home.html"
   my_context={
        "page_title":my_title,
        "page_visit_count":Page_qs.count(),
        "percent":Page_qs.count()*100.0/qs.count(),
        "total_visit_count":qs.count(),
       }
   path=request.path
   print("path",path)
   PageVisit.objects.create(path=request.path)
      # html_file_Path=this_dir / "home.html"
      #html_=html_file_Path.read_text()
   return render(request,"home.html",my_context)