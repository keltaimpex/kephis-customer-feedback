from django.shortcuts import render, redirect
from .models import CustomerFeedback

def cf(request):
    return render(request, 'feedback/cf.html')

def services(request):
    if request.method == 'POST':        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        
        context = {
            'name': name,
            'email': email,
            'phone': phone,
        }
        return render(request, 'feedback/services.html', context)

    # Prevents direct GET access to services page (optional)
    return redirect('feedback:cf')

def RATING(request):
    if request.method == "POST":
        return render(request, 'feedback/RATING.html', {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'serviceType': request.POST.get('serviceType'),
            'specificService': request.POST.get('specificService'),
            'kephisRegion': request.POST.get('kephisRegion'),
            'kephisOffice': request.POST.get('kephisOffice'),
        })
    return redirect('feedback:services')

def submit(request):
    if request.method == "POST":
        CustomerFeedback.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            service_type=request.POST.get('serviceType'),
            specific_service=request.POST.get('specificService'),
            region=request.POST.get('kephisRegion'),
            office=request.POST.get('kephisOffice'),
            rating_working_environment=request.POST.get('rating1'),
            rating_courtesy=request.POST.get('rating2'),
            rating_professionalism=request.POST.get('rating3'),
            rating_waiting_time=request.POST.get('rating4'),
        )
        return redirect('feedback:cf')
    return redirect('feedback:cf')
