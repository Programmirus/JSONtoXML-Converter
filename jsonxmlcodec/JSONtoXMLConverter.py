import json
import traceback
import codec
import os


try:
    path=open("C:/.path.txt",'r', encoding="utf-8")
except:
    print("Unavailable source")
source="" 
i=1
while True:
    try:
        item=path.read(1)
        if(item==""): break
    except:
        print("Unavailable source")
    source=source+item    
    path.seek(i)
    i=i+1        
path.close()



dir=os.listdir(source+"/json")
for file in dir:
    input_path=source+"/json/"+file
    error_path=source+"/errors/"+file
    output_path=source+"/xml/"+file.replace("txt","xml")
    input_data=open(input_path,'r', encoding="utf-8")
    json_data=codec.JSON(input_data)
    input_data.close()

    error_log=open(error_path,'w')
    for raw in json_data.getErrorLog():
      error_log.write(raw+"\n")
    error_log.close()

    xml=codec.JSON.getXMLADI(json_data.getValue(),"<xmladi>")+"\n</xmladi>"
    print(file, " : ", xml)
    if (json_data.getErrorLog()==""):
       output_data=open(output_path,'w', encoding="utf-8")
       output_data.write(xml)
       output_data.close()
    

            


          





     
    
  