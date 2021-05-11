# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:34:23 2020

@author: vlad.krivorotenko
"""
import json
import traceback
import codec
from functools import singledispatch
from multipledispatch import dispatch

class JSON:
 
    
        
    def __init__(self,input_data):
        try:
            self._value=json.load(input_data)
            self._error_log=""
        except:
            self._value=""
            self._error_log=traceback.format_exc().splitlines()
      
 
    def getValue(self):
      return self._value
  
    def getErrorLog(self):
      return self._error_log
  
    @staticmethod
    def getXMLADI(data,xml, parent_tag=""):
        try:
            assert(isinstance(data,dict)==True)
            for item in data:
            
                if(isinstance(data[item],list)==True):
                    xml=JSON.getXMLADI(data[item],xml,item)
                else:
                    xml=xml+"<"+item+">"
                    xml=JSON.getXMLADI(data[item],xml)+"</"+item+">"
            return xml
                
       
        except:
            try:
                assert(isinstance(data,list)==True)
                open_tag=""
                close_tag=""
                if(parent_tag!=""):
                    open_tag="<"+parent_tag+">"
                    close_tag="</"+parent_tag+">"
                    a=""
                for item in data:
                    try: 
                      a=a+open_tag+str(JSON.getXMLADI(item,""))+close_tag 
                    except:
                      #print(item)
                      a=str(item)
                xml=xml+a
                return xml
            
            except:
                xml=xml+str(data)
                #print(data)
                return xml
    
  
            
     