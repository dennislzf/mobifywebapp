from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template.defaulttags import csrf_token
from django.template import RequestContext
from django.contrib.auth import authenticate,login,get_user
from django.core.urlresolvers import reverse
from django.http import  HttpResponseRedirect
from django.core.cache import cache
from datetime import datetime
import time
import Image
import os
from django.views.decorators.csrf import csrf_exempt
import json 



#Post request for increment counter
@csrf_exempt
def incrementcounter(request):
    #if request is a post increment counter.
    if request.method == 'POST':
        #check if session variable incrementer is stored in session
        if 'incrementer' not in request.session:
            request.session['incrementer'] = 1
        else:
            x = request.session['incrementer']
            x = x + 1    
            request.session['incrementer'] = x 
        return HttpResponse(status=200)
    else:
        return HttpResponse("<html><p>Must be a post method to increment counter</p></html>")
    
    
@csrf_exempt
def echo(request):
    ##check if request is post
    if request.method == 'POST':
        responsedata = dict()
        #iterate throught keys
        for key in request.GET.iterkeys(): 
            valuelist = request.GET.getlist(key)
            #assign value to the key
            for val in valuelist:
                responsedata[key] = val   
        #create http response with jason key value pairs with mime type application/json
        return HttpResponse(json.dumps(responsedata), mimetype="application/json")
    else: 
        return HttpResponse("<html><p>Must be a POST request</p></html>")

def getcounter(request):
    #check if incrementer session variable is in session
    if 'incrementer' not in request.session:
        request.session['incrementer'] = 0
    #if request is a post, we increment counter
    if request.method == 'POST':
        x = request.session['incrementer']
        x = x +1  
        request.session['incrementer'] = x
        #create custom header X-HELLO-MOBIFY-ROBOT  
        postresponseheader = responseheader(x)
        postresponse = HttpResponseRedirect('get-counter.html')
        postresponse[postresponseheader] = 'hi'
        return postresponse
        
    i = request.session['incrementer']
    getresponse = render_to_response("getcounter.html",{
        'i': i},context_instance=RequestContext(request))
    getresponseheader = responseheader(i)
    getresponse[getresponseheader] = 'hi'
    return getresponse

def responseheader(i):
    s = str(i) + "-HELLO-MOBIFY-ROBOT" 
    return s

def index(request):
    return render_to_response("index.html")
    
def cachedtimestamp(request):
    #check to see if value in cache with id 'timevalue' exists, if it doesnt exist, set new cache value
    if cache.get('timevalue') == None:
        timevalue =  int(time.time())
        cache.set('timevalue', timevalue, 15)
    #if  value in cache with id 'timevalue' exists, use that value
    timevalue = cache.get('timevalue')
    return render_to_response("cachedtimestamp.html",{
        'timevalue': timevalue},context_instance=RequestContext(request))
    
def getsizedimage(request,width,height):
   
    width= int(width)
    height = int(height)
    scalarwidth = 1.66
    scalarheight = 0.603
    widthscaled = height * scalarwidth
    #check to see if both height and width are less then max
    if (width>580 and height>350):
        width = 580
        height = 350
    #if width is more then the scaled value of height, and below max width, set width to
    #scaled height value
    elif width>(height * scalarwidth) and widthscaled < 580:
        width = height * scalarwidth
    #if height is larger the width scaled value, then set height to the scaled value based on width
    elif height >  (width * scalarheight ) and height<350:
        height = width* scalarheight 
    width = int(width)
    height = int(height)
    resizeimage(width,height)
    response = HttpResponse(mimetype="image/png")
    img = Image.open("C:/Users/Administrator/workspace/mobifywebapp/media/cropped.png")
    img.save(response,'png')
    return response
   
    
def resizeimage(width,height):
    
    imageFile = "C:/Users/Administrator/workspace/mobifywebapp/media/un-intense-hiring-team.png"
    image = Image.open(imageFile)
    croppedimage = image.resize((width, height), Image.ANTIALIAS)
    croppedimage.save("C:/Users/Administrator/workspace/mobifywebapp/media/cropped.png")
    
    
    
    
