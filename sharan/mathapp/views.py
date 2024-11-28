from django.shortcuts import render 
def power(request): 
    context={} 
    context['power'] = "0" 
    context['intensity'] = "0" 
    context['resistance'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        intensity = request.POST.get('intensity','0')
        resistance = request.POST.get('resistance','0')
        print('request=',request) 
        print('intensity=',intensity) 
        print('resistance=',resistance) 
        power = (int(intensity) * int(intensity)) * int(resistance)
        context['power'] = power
        context['intensity'] = intensity
        context['resistance'] = resistance 
        print('power=',power) 
    return render(request,'mathapp/math.html',context)

