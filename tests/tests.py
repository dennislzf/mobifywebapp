"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
import time
import Image
import json




class SimpleTest(TestCase):
    def testindex(self):
            response= self.client.post( '' )
            self.assertTemplateUsed( response, 'index.html' )
            
    def testgetcounter(self):
        response= self.client.get( '/get-counter/' )
        self.assertContains(response,"The counter is at 0",status_code=200)
        self.assertTemplateUsed( response, 'getcounter.html' )
    
    def testcachedtimestamp(self):
        response= self.client.get( '/cached-timestamp/' )
        timestamp = int(time.time())
        timestamp=str(timestamp)
        self.assertContains(response,timestamp,status_code=200)
        self.assertTemplateUsed( response, 'cachedtimestamp.html' )
    
    def testgetsizedimagemaxed(self):
        self.client.get( '/get-sized-image/800/800/' )
        img = Image.open("C:/Users/Administrator/workspace/mobifywebapp/media/cropped.png")
        width1,height1 = img.size
        self.assertEquals(width1, 580)
        self.assertEquals(height1, 350)
        
    
    def testgetsizedimagesame(self):
        self.client.get( '/get-sized-image/200/200/' )
        img = Image.open("C:/Users/Administrator/workspace/mobifywebapp/media/cropped.png")
        width2,height2 = img.size
        self.assertAlmostEqual(width2, 200,delta=2)
        self.assertAlmostEqual(height2, 121,delta=2)
    
    def testgetsizedimagewidthlarger(self):
        self.client.get( '/get-sized-image/500/100/' )
        img = Image.open("C:/Users/Administrator/workspace/mobifywebapp/media/cropped.png")
        width,height = img.size
        self.assertAlmostEqual(width, 165,delta=2)
        self.assertAlmostEqual(height, 100, delta=2)
    
    def testpostincrementcounter(self):
        postresponse = self.client.post('/increment-counter')
        self.assertContains(postresponse,"", status_code=200)
        getresponse = self.client.get('/get-counter')
        self.assertContains(getresponse,"The counter is at 1", status_code= 200)
        
    def testpostecho(self):
        emptyresponse = self.client.post("/echo")
        self.assertContains(emptyresponse,"", status_code=200)
        fullresponse = self.client.post("/echo?name=Dennis&lname=Lau&says=mobifyisawesome")
        print fullresponse
        self.assertContains(fullresponse,'{"lname": "Lau", "says": "mobifyisawesome", "name": "Dennis"}',status_code=200)
        
        
        
        
         
         
        
        
 