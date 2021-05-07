from django.shortcuts import render, redirect
from django.views import View
from .scrapper import Scrapper

class HomeView(View):

    template_name = 'homepage.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        search = request.POST.get('search')
        print(search)

        return redirect('search', product_name=search)


class SearchView(View):

    template_name = 'products.html'

    def get(self, request, product_name):

        scrap = Scrapper()
        links = scrap.get_links(product_name)

        object_list = scrap.get_object_list(links)



        context = {
            'product_name': product_name,
            'object_list': object_list
        }
        return render(request, self.template_name, context)


class DetailView(View):

    template_name = 'reviews.html'

    def get(self, request, id, *args, **kwargs):

        object = [id]
        context = {
            'object': object

        }

        return render(request, self.template_name, context)
