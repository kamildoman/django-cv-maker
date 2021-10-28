from django.shortcuts import render
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import CVForm




def index(request):
    if request.method == "POST":
        names = {'pagesize': "A4"}
        form = CVForm(request.POST or None, request.FILES or None)
        print(form.errors)
        if form.is_valid():
            a = form.save(commit=False)
            names = {"names": a}
            a.save()
        return render(request, 'form/result.html', names)
                
        #return render_to_pdf('form/result.html', names)

    form = CVForm()
    context = {"form": form}
    return render(request, 'form/index.html', context)



def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = context_dict
    html  = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors')



