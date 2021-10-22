from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from .models import Document



# Create your views here.
@login_required
def DocumentAdd(request):
    docs = request.user.document_set.all()
    numberOfDocs = len(docs)
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)  #instances are only required for updating...
        print(DocumentForm)    #UserDocumentsForm.user will not work bcz this is a form. But UserDocumentsForm.save().user will work bcz it's a database query set.
        if form.is_valid():
            doc = form.save(commit=False) #doc is nothing but an instance..
            doc.user = request.user
            doc.save()
            return render(request,'DocumentApp/userDocs.html',{'docs':docs,'numberOfDocs':numberOfDocs})
    else:
        form = DocumentForm()
    return render(request, 'DocumentApp/docAdd.html', {'form' : form})

@login_required
def DocumentDelete(request):
    docs = request.user.document_set.all()
    numberOfDocs = len(docs)
    Document.objects.filter(docId=request.POST.get('docToBeDeleted')).delete()
    return render(request, 'DocumentApp/userDocs.html',{'docs':docs,'numberOfDocs':numberOfDocs})



@login_required
def userDocsView(request):
    docs = request.user.document_set.all()
    # print(len(docs))
    numberOfDocs = len(docs)
    # if len(docs)>0:
    #     numberOfDocs = True
    # else:
    #     numberOfDocs = False
    print(numberOfDocs)
    return render(request, 'DocumentApp/userDocs.html',{'docs':docs,
    'numberOfDocs':numberOfDocs})