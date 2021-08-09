from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """<h1>Mi web personal</h1>
    <ul>
        <li><a href="/"></a>Portada</li>
        <li><a href="/about-me"></a>Acerca de mi</li>
        <li><a href="/portfolio"></a>Portfolio</li>
        <li><a href="/contact"></a>Contacto</li>
    </ul> """


def home(request):
    return render(request, "core/home.html");
def about(request):
    return render(request, "core/about.html");

def contact(request):
    return render(request, "core/contact.html");