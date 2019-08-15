from django.shortcuts import render


def example(request):
    context = {"title": "This is a title!"}
    return render(request, "page.html", context)
