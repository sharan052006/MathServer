# Ex.05 Design a Website for Server Side Processing
## Date:28-11-2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html


<html>
<head>
    <title>Power Calculation</title>
</head>
<body style="text-align: center;
             background-color: #0f057c;
             padding: 20px;">
    <h1 style="background-color: #82a4e9; color: black; font-size: 80px;">Power of Lamp Filament</h1>
    <form method="POST" style="border: 10px;background-color: #82a4e9; display: inline-block;">
        {% csrf_token %}
        <div style="padding-left: 100px ;padding-right: 100px; padding-top: 100px; padding-bottom: 100px;">
        <label for="intensity" style="color: black; background-color:  rgb(243, 88, 119);font-size: x-large;" >Intensity (I) in amperes:</label><br>
        <input type="number" id="intensity" name="intensity" step="0.01" value="{{ intensity }}" required><br><br>
        
        <label for="resistance" style="color: black; background-color: rgb(243, 88, 119); font-size: x-large;">Resistance (R) in ohms:</label><br>
        <input type="number" id="resistance" name="resistance" step="0.01" value="{{ intensity }}" required><br><br>
        
        <input type="submit" value="Calculate" style="background-color: red; color: black; padding: 10px; cursor: pointer;"><br><br>
        
        <label for="power" style="color: black;">Power (P) in watts:</label><br>
        <input type="number" id="power" name="power" value="{{ power }}" readonly><br>
        </div>
    </form>
</body>
</html>


views.py


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


urls.py


from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('power/',views.power,name="power"),
    path('',views.power,name="powerroot")
]


```

## SERVER SIDE PROCESSING:



## HOMEPAGE:


## RESULT:
The program for performing server side processing is completed successfully.
