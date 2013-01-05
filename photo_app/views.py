from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from photo_app.models import Fotografija
from photo_app.models import Komentar
from photo_app.models import PhotoUploadForm
from photo_app.models import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
    
def index(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newphoto = Fotografija(naziv = request.POST['naziv'], opis = request.POST['opis'], putanja= request.FILES['fotografija'], broj_pogleda=0)
            newphoto.save()

            return HttpResponseRedirect('')
    else:
        form = PhotoUploadForm() 
        
    fotografije_list = Fotografija.objects.all()
    paginator = Paginator(fotografije_list, 8)
    
    page = request.GET.get('page')
    
    try:
        fotografije = paginator.page(page)
    except PageNotAnInteger:
        fotografije = paginator.page(1)
    except EmptyPage:
        fotografije = paginator.page(paginator.num_pages)
       
    
    return render_to_response(
        'index.html',
        {'form': form,
         'fotografije': fotografije,},
        context_instance=RequestContext(request)
    )

def view_photo(request, photo_id):
    form = CommentForm() 
    fotografija = Fotografija.objects.get(pk=photo_id)
    komentari = Komentar.objects.filter(fotografija_id=photo_id)
    return render_to_response(
        'view_photo.html',
        {'fotografija': fotografija,
         'form': form,
         'komentari':komentari},
        context_instance=RequestContext(request)
    )

def comment (request, photo_id):
    if request.method == 'GET' and request.GET['komentar']:
        komentar = Komentar(fotografija_id = photo_id, komentar = request.GET['komentar'], vrijeme_komentiranja = datetime.now())
        komentar.save()
    komentari = Komentar.objects.filter(fotografija_id=photo_id)
    return render_to_response(
        'comments.html',
        {'komentari':komentari},
        context_instance=RequestContext(request)
    )