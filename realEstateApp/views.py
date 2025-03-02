from django.shortcuts import render, get_object_or_404, redirect
from .models import Homesforsale, Homesforrent, Post, Homessold, Agent, SavedSale, AuthUser
from .forms import signupform, salesdata, agentsignupform, AgentForm, SalesForm, AddNewListing, InquiryForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
import folium
from django.forms import modelformset_factory
from geopy.geocoders import Nominatim
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .filters import SalesFilter
from django.views.generic import ListView
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import *
from .serializers import *
from elasticsearch import Elasticsearch
from django.contrib.auth.decorators import login_required
from elasticsearch_dsl import Search
from django.views.decorators.csrf import csrf_exempt
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)

def index(request):
    return render(request, 'index.html')

def indexLater(request):
    return render(request, 'index-later.html')

def aboutus(request):
    return render(request, 'about-us.html')

def salepage(request):
    sales = Homesforsale.objects.all()
    context = {
        'sales' : sales
    }
    return render(request, 'for-sale.html', context)

def salepagedetails(request, id):
    sales = Homesforsale.objects.all()
    sales1 = get_object_or_404(Homesforsale, id = id)
    if sales1:
        latitude = sales1.latitude
        longitude = sales1.longitude
        m = folium.Map(location = [latitude, longitude], zoom_start = 14)
        coordinates = (sales1.latitude, sales1.longitude)
        folium.Marker(coordinates, popup = sales1.address).add_to(m)
        map_html = m._repr_html_()
    else:
        map_html = None
    context = {
        'sales' : sales,
        'sales1' : sales1,
        'map_html' : map_html,
    }
    return render(request, 'salepage-details.html', context)

def rentpagedetails(request, id):
    rentals = Homesforrent.objects.all()
    rentals1 = get_object_or_404(Homesforrent, id = id)
    if rentals1:
        latitude = rentals1.latitude
        longitude = rentals1.longitude
        m = folium.Map(location = [latitude, longitude], zoom_start = 14)
        coordinates = (rentals1.latitude, rentals1.longitude)
        folium.Marker(coordinates, popup = rentals1.address).add_to(m)
        map_html = m._repr_html_()
    else:
        map_html = None
    context = {
        'rentals' : rentals,
        'rentals1' : rentals1,
        'map_html' : map_html,
    }
    return render(request, 'rentpage-details.html', context)

def agentdetails(request, agent_name):
    agents = Agent.objects.all()
    agents1 = get_object_or_404(Agent, agent_name = agent_name)
    sales = Homesforsale.objects.filter(broker_name = agent_name)
    context = {
        'agents': agents,
        'agents1': agents1,
        'sales' : sales
    }
    return render(request, 'agent-details.html', context)

def soldpagedetails(request, id):
    sold = Homessold.objects.all()
    sold1 = get_object_or_404(Homessold, id = id)
    if sold1:
        latitude = sold1.latitude
        longitude = sold1.longitude
        m = folium.Map(location = [latitude, longitude], zoom_start = 14)
        coordinates = (sold1.latitude, sold1.longitude)
        folium.Marker(coordinates, popup = sold1.address).add_to(m)
        map_html = m._repr_html_()
    else:
        map_html = None
    context = {
        'sold': sold,
        'sold1': sold1,
        'map_html': map_html
    }
    return render(request, 'soldpage-details.html', context)

def salesearch(request):  
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            sales = Homesforsale.objects.filter(city__icontains = query)
            if not sales:
                print("Sales Not Found")
                return render(request, 'sale-search.html', {})
            latitude = sales.first().latitude
            longitude = sales.first().longitude
            m = folium.Map(location = [latitude, longitude], zoom_start = 13)
            for sale in sales:
                coordinates = (sale.latitude, sale.longitude)
                folium.Marker(coordinates, popup = sale.address).add_to(m)
            return render(request, 'sale-search-results.html', {'sales': sales, 'map': m._repr_html_(), 'query': query})
        else:
            print("Query parameter not provided")
            return render(request, 'sale-search-results.html', {})
    else:
        print("Invalid request method")
        return render(request, 'sale-search-results.html', {})
    
def rentsearch(request):  
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            rentals = Homesforrent.objects.filter(city__icontains = query)
            if not rentals:
                print("Sales Not Found")
                return render(request, 'rent-search.html', {})
            latitude = rentals.first().latitude
            longitude = rentals.first().longitude
            m = folium.Map(location = [latitude, longitude], zoom_start = 13)
            for rent in rentals:
                coordinates = (rent.latitude, rent.longitude)
                folium.Marker(coordinates, popup = rent.address).add_to(m)
            return render(request, 'rent-search-results.html', {'rentals': rentals, 'map': m._repr_html_(), 'query': query})
        else:
            print("Query parameter not provided")
            return render(request, 'rent-search-results.html', {})
    else:
        print("Invalid request method")
        return render(request, 'rent-search-results.html', {})
    
def soldsearch(request):  
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            sold = Homessold.objects.filter(city__icontains = query)
            if not sold:
                print("Sales Not Found")
                return render(request, 'sold-search.html', {})
            latitude = sold.first().latitude
            longitude = sold.first().longitude
            m = folium.Map(location = [latitude, longitude], zoom_start = 13)
            for sold1 in sold:
                coordinates = (sold1.latitude, sold1.longitude)
                folium.Marker(coordinates, popup = sold1.address).add_to(m)
            return render(request, 'sold-search-results.html', {'sold': sold, 'map': m._repr_html_(), 'query': query})
        else:
            print("Query parameter not provided")
            return render(request, 'sold-search-results.html', {})
    else:
        print("Invalid request method")
        return render(request, 'sold-search-results.html', {})

def soldsearch(request):
    sold = []
    m = None
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            sold = Homessold.objects.filter(city__icontains = query)
            for sold1 in sold:
                latitude = sold1.latitude
                longitude = sold1.longitude
            m = folium.Map(location = [latitude, longitude], zoom_start = 13)
            for sold1 in sold:
                coordinates = (sold1.latitude, sold1.longitude)
                folium.Marker(coordinates, popup = sold1.address).add_to(m)
        else:
            print("Homes sold not found")
            return render(request, 'sold-search-results.html', {})
    return render(request, 'sold-search-results.html', {'sold': sold, 'map': m._repr_html_()})

def agents(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            agents = Agent.objects.filter(city__icontains = query)
        else:
            print("Agents not found")
            return render(request, 'agent-results.html')
    return render(request, 'agent-results.html', {'agents': agents})

def salesearchblock(request):
    return render(request, 'sale-search.html')

def elasticview(request):
    return render(request, 'sales-document-lists.html')

class SalesDocumentView(DocumentViewSet):
    document = SalesDocument
    serializer_class = SalesDocumentSerializer

    filter_backends = {
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    }

    search_fields = ('address', 'city', 'beds', 'bathrooms', 'id', 'description')

    multi_match_search_fields = ('address', 'city', 'beds', 'bathrooms', 'id', 'description')

    filter_fields = {
        'address': 'address',
        'city': 'city',
        'beds': 'beds',
        'bathrooms': 'bathrooms',
        'id': 'id',
        'description': 'description'
    }
    
    def list(self, request, *args, **kwargs):
        es = Elasticsearch()
        search_query = request.GET.get('search_query')

        if search_query:
            search_terms = search_query.split()
            s = Search(using = es, index = 'elastic_demo')
            for term in search_terms:
                s = s.query("multi_match", query = term, fields = ['address', 'city', 'beds', 'bathrooms', 'id', 'description'])
            response = s.execute()
            documents = [hit.to_dict() for hit in response]
            sales = Homesforsale.objects.filter(id__in = [doc['id'] for doc in documents])
            m = folium.Map(location = [sales[0].latitude, sales[0].longitude], zoom_start = 13)
            for sale in sales:
                coordinates = (sale.latitude, sale.longitude)
                folium.Marker(coordinates, popup = sale.address).add_to(m)
        else:
            documents = []
            sales = []
            m = folium.Map(location = [25.761681, -80.191788], zoom_start = 13)
        context = {
            'documents': documents,
            'sales': sales,
            'map' : m._repr_html_()
        }
        return render(request, 'elastic-view-results.html', context)

def signupview(request):
    form = signupform()
    if request.method == "POST":
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signupform()
    context = {'form': form}
    return render(request, 'signup.html', context)
    
def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
    
def logoutpage(request):
    logout(request)
    return redirect('index')

    '''def list(self, request, *args, **kwargs):
        es = Elasticsearch()

        address = request.GET.get('address')
        city = request.GET.get('city')
        beds = request.GET.get('beds')
        bathrooms = request.GET.get('bathrooms')

        s = Search(using = es, index = 'elastic_demo')

        if address:
            s = s.query("match", address = address)
        if city:
            s = s.query("match", city = city)
        if beds:
            s = s.query("match", beds = beds)
        if bathrooms:
            s = s.query("match", bathrooms = bathrooms)

        response = s.execute()
        documents = [hit.to_dict() for hit in response]
        return render(request, 'sales-document-list.html', {'documents': documents})'''
    
def blogs(request):
    blogs = Post.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def blogpost(request):
    blogs = Post.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog-detail.html', context)

def salesfilter(request):
    if request.method == "GET":
        city_query = request.GET.get('city_query')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        bathrooms = request.GET.get('bathrooms')
        beds = request.GET.get('beds')

        sales = Homesforsale.objects.filter(city__icontains = city_query)
        if min_price:
            sales = sales.filter(price__gte = min_price)
        if max_price:
            sales = sales.filter(price__lte = max_price)
        if beds:
            sales = sales.filter(beds = beds)
        if bathrooms:
            sales = sales.filter(bathrooms = bathrooms)

        latitude = sales.first().latitude
        longitude = sales.first().longitude

        m = folium.Map(location = [latitude, longitude], zoom_start = 13)
        for sale in sales:
            coordinates = (sale.latitude, sale.longitude)
            folium.Marker(coordinates, popup = sale.address).add_to(m)

        return render(request, 'sale-search-results.html', {'sales': sales, 'map': m._repr_html_()})
    else:
        print("Invalid request method")
        return render(request, 'sale-search-results.html')
    
def rentfilter(request):
    if request.method == "GET":
        city_query = request.GET.get('city_query')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        bathrooms = request.GET.get('bathrooms')
        beds = request.GET.get('beds')

        rentals = Homesforrent.objects.filter(city__icontains = city_query)
        if min_price:
            rentals = rentals.filter(price__gte = min_price)
        if max_price:
            rentals = rentals.filter(price__lte = max_price)
        if beds:
            rentals = rentals.filter(beds = beds)
        if bathrooms:
            rentals = rentals.filter(bathrooms = bathrooms)

        latitude = rentals.first().latitude
        longitude = rentals.first().longitude

        m = folium.Map(location = [latitude, longitude], zoom_start = 13)
        for rent in rentals:
            coordinates = (rent.latitude, rent.longitude)
            folium.Marker(coordinates, popup = rent.address).add_to(m)

        return render(request, 'rent-search-results.html', {'rentals': rentals, 'map': m._repr_html_()})
    else:
        print("Invalid request method")
        return render(request, 'rent-search-results.html')

def soldfilter(request):
    if request.method == "GET":
        city_query = request.GET.get('city_query')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        bathrooms = request.GET.get('bathrooms')
        beds = request.GET.get('beds')

        sold = Homessold.objects.filter(city__icontains = city_query)
        if min_price:
            sold = sold.filter(price__gte = min_price)
        if max_price:
            sold = sold.filter(price__lte = max_price)
        if beds:
            sold = sold.filter(beds = beds)
        if bathrooms:
            sold = sold.filter(bathrooms = bathrooms)

        latitude = sold.first().latitude
        longitude = sold.first().longitude

        m = folium.Map(location = [latitude, longitude], zoom_start = 13)
        for sold1 in sold:
            coordinates = (sold1.latitude, sold1.longitude)
            folium.Marker(coordinates, popup = sold1.address).add_to(m)

        return render(request, 'sold-search-results.html', {'sold': sold, 'map': m._repr_html_()})
    else:
        print("Invalid request method")
        return render(request, 'sold-search-results.html')

def account_view(request):
    user = request.user
    user1 = AuthUser.objects.filter(is_staff = 0)
    agent = AuthUser.objects.filter(is_staff = 1)
    agents = Agent.objects.filter(username = user).first()
    sales = Homesforsale.objects.filter(broker_name = agents.agent_name) if agents else []
    context = {
        'user': user,
        'agent': agent,
        'user1': user1,
        'agents': agents,
        'sales': sales
    }
    return render(request, 'account.html', context)

@login_required
def my_saves(request):
    saved_sales = SavedSale.objects.filter(user = request.user)
    sales = Homesforsale.objects.filter(id__in = [saved_sale.sale_id for saved_sale in saved_sales])
    print("Saved sales:", saved_sales)
    return render(request, 'mysaves.html', {'saved_sales': saved_sales, 'sales': sales})

@login_required
def get_saved_sales(request):
    try:
        saved_sales = SavedSale.objects.filter(user=request.user).values_list('sale_id', flat=True)
        saved_sales_list = list(saved_sales)
        return JsonResponse(saved_sales_list, safe=False)
    except Exception as e:
        return JsonResponse({'error': 'An error occurred while retrieving saved sale IDs'}, status=500)

@csrf_exempt
@login_required
def save_sale(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            sale_id = data.get('sale_id')
            print("Received sale ID:", sale_id)
            print("Current user:", request.user)
            if not sale_id:
                return JsonResponse({'error': 'Sale ID is missing'}, status=400)
            existing_entry = SavedSale.objects.filter(user=request.user, sale_id=sale_id).first()
            if existing_entry:
                existing_entry.delete()
                return JsonResponse({'message': 'Sale removed successfully'}, status=200)
            else:
                SavedSale.objects.create(user=request.user, sale_id=sale_id)
                return JsonResponse({'message': 'Sale saved successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def agentsignupview(request):
    form = agentsignupform()
    if request.method == "POST":
        form = agentsignupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = agentsignupform()
    context = {'form': form}
    return render(request, 'agent-signup.html', context)

def agentloginview(request):
    if request.method == "POST":
        agent_name = request.POST.get('agent_name')
        password = request.POST.get('password')
        try:
            agent = Agent.objects.get(agent_name = agent_name)
        except Agent.DoesNotExist:
            agent = None
        if agent and check_password(password, agent.password):
            login(request, agent)
            request.session['agent_name'] = agent_name
            return redirect('index')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'agent-login.html', context)
    else:
        return render(request, 'agent-login.html')
    
def agentlogoutview(request):
    if 'agent_name' in request.session:
        del request.session['agent_name']
    logout(request)
    return redirect('login')

'''@login_required
def agentFormView(request):
    existing_user = Agent.objects.filter(username = request.user).exists()
    if existing_user:
        messages.error(request, "form already submitted")
        return redirect('account-view')
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            agent = form.save(commit = False)
            agent.username = request.user
            agent.username = request.user.username
            agent.save()
            form.save()
            return redirect('account-view')
    else:
        form = AgentForm()
    return render(request, 'agent-form.html', {'form': form})'''

@login_required
def agentFormView(request, id):
    agent = get_object_or_404(Agent, id = id)
    if request.method == 'POST':
        form = AgentForm(request.POST, instance = agent)
        if form.is_valid():
            form.save()
            return redirect('account-view')
    else:
        form = AgentForm(instance = agent)
    return render(request, 'agent-form.html', {'form': form})

def agentEdit(request, id):
    user = request.user
    agents = Agent.objects.filter(username = user).first()
    sale = get_object_or_404(Homesforsale, id = id, broker_name = agents.agent_name)
    if request.method == 'POST':
        form = SalesForm(request.POST, instance = sale)
        if form.is_valid():
            form.save()
            return redirect('account-view')
    else:
        form = SalesForm(instance = sale)
    return render(request, 'agent-edit.html', {'form': form, 'user': user, 'sale': sale})

def delete_listing(request, id):
    listing = get_object_or_404(Homesforsale, id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('account-view')
    return render(request, 'delete-listing.html', {'listing': listing})

def add_new_listing(request):
    if request.method == 'POST':
        form = AddNewListing(request.POST)
        if form.is_valid():
            if form.cleaned_data['add_new_listing']:
                form.save()
                return redirect('account')
            else:
                form.save()
                return redirect('account')
    else:
        form = AddNewListing()
    return render(request, 'listing-form.html', {'form': form})

def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        print(to, content)
        send_mail(
            'Enquiry',
            content,
            settings.EMAIL_HOST_USER,
            [to]
        )

        return render(
            request,
            'email.html',
            {
                'title': 'send an email'
            }
        )
    else:
        return render(
            request,
            'email.html',
            {
                'title': 'send an email'
            }
        )
    
def inquiryView(request):
    user = request.user
    agents = Agent.objects.filter(username = user).first()
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            agent_email = agents.email
            subject = 'Inquiry'
            body = f'Name: {name}\nMessage: {message}'
            send_mail(subject, body, agent_email, [agent_email])
            return render(request, 'thank-you.html')
        else:
            return HttpResponse("Invalid Form Submission!")
    else:
        form = InquiryForm()
    return render(request, 'inquiry-form.html', {'form': form})

def inquiryViewReal(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            agent_email = 'realystsearch@gmail.com'
            subject = 'Inquiry'
            body = f'Name: {name}\nMessage: {message}'
            send_mail(subject, body, agent_email, [agent_email])
            return render(request, 'thank-you.html')
        else:
            return HttpResponse("Invalid Form Submission!")
    else:
        form = InquiryForm()
    return render(request, 'inquiry-form-real.html', {'form': form})

def inquiryViewSale(request, id):
    sales = get_object_or_404(Homesforsale, id = id)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            agent_email = sales.agent_email
            subject = 'Inquiry'
            body = f'Name: {name}\nMessage: {message}'
            send_mail(subject, body, agent_email, [agent_email])
            return render(request, 'thank-you.html')
        else:
            return HttpResponse("Invalid Form Submission!")
    else:
        form = InquiryForm()
    return render(request, 'inquiry-form-sales.html', {'form': form, 'sales': sales})

def inquiryViewRent(request, id):
    rentals = get_object_or_404(Homesforrent, id = id)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            agent_email = rentals.agent_email
            subject = 'Inquiry'
            body = f'Name: {name}\nMessage: {message}'
            send_mail(subject, body, agent_email, [agent_email])
            return render(request, 'thank-you.html')
        else:
            return HttpResponse("Invalid Form Submission!")
    else:
        form = InquiryForm()
    return render(request, 'inquiry-form-rent.html', {'form': form, 'rentals': rentals})

def inquiryViewSold(request, id):
    sold = get_object_or_404(Homessold, id = id)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            agent_email = sold.agent_email
            subject = 'Inquiry'
            body = f'Name: {name}\nMessage: {message}'
            send_mail(subject, body, agent_email, [agent_email])
            return render(request, 'thank-you.html')
        else:
            return HttpResponse("Invalid Form Submission!")
    else:
        form = InquiryForm()
    return render(request, 'inquiry-form-sold.html', {'form': form, 'sold': sold})