from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm

# Create your views here.
@login_required
def DocumentAdd(request):
    
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)  #instances are only required for updating...
        print(DocumentForm)    #UserDocumentsForm.user will not work bcz this is a form. But UserDocumentsForm.save().user will work bcz it's a database query set.
        if form.is_valid():
            doc = form.save(commit=False) #doc is nothing but an instance..
            doc.user = request.user
            doc.save()
            print('doc saves !!!!!!!!')
    else:
        form = DocumentForm()
    return render(request, 'DocumentApp/docAdd.html', {'form' : form})

@login_required
def userDocsView(request):
    docs = request.user.document_set.all()
    for i in docs:
        print(i.docImg)
        print(i.docType)
        print(i.expDate)
    return render(request, 'DocumentApp/userDocs.html',{'docs':docs})