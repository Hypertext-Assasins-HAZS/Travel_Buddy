from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from .models import Document
from django.urls import reverse

def DocAddPage(request):
    form = DocumentForm()
    return render(request, 'DocumentApp/docAdd.html', {'form' : form})


# Create your views here.
@login_required
def DocumentAdd(request):
    
    if request.method == 'POST':
        docs = request.user.document_set.all()
        numberOfDocs = len(docs)
        form = DocumentForm(request.POST,request.FILES)  #instances are only required for updating...
           #UserDocumentsForm.user will not work bcz this is a form. But UserDocumentsForm.save().user will work bcz it's a database query set.
        if form.is_valid():
            doc = form.save(commit=False) #doc is nothing but an instance..
            doc.user = request.user
            doc.save()
            # return render(request,'DocumentApp/userDocs.html',{'docs':docs,'numberOfDocs':numberOfDocs})
            #render should not be put after forms as the form will resubmit.
            return HttpResponseRedirect(reverse('userDocs'))
        

@login_required
def DocumentDelete(request):
    docs = request.user.document_set.all()
    numberOfDocs = len(docs)
    if request.method == 'POST':
        Document.objects.filter(docId=request.POST.get('docToBeDeleted')).delete()
        # return render(request, 'DocumentApp/userDocs.html',{'docs':docs,'numberOfDocs':numberOfDocs})
        return HttpResponseRedirect(reverse('userDocs'))
    else:
        return HttpResponseRedirect(reverse('userDocs'))


@login_required
def userDocsView(request):
    docs = request.user.document_set.all()
    numberOfDocs = len(docs)
    print(numberOfDocs)
    return render(request, 'DocumentApp/userDocs.html',{'docs':docs,
    'numberOfDocs':numberOfDocs})