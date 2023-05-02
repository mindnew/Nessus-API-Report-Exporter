#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import json
import time
import pandas as pd
import warnings
import datetime
import re
warnings.filterwarnings("ignore") # To ingore SSL error if it accure


# In[5]:


def download_file(url):
    local_filename = "Downloaded/"+d_fn+"_"+today+"."+report_format
    # NOTE the stream=True parameter below
    with requests.get(url,headers=headers, data=payload, verify=False, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=None): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                if chunk: 
                    f.write(chunk)
    return local_filename

def Convert(string):
    li = list(string.split(","))
    return li


# In[7]:


print ("Enter Nessus IP address and port (example: 10.0.0.1:8834)")

pat = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):[0-9][0-9]?[0-9]?[0-9]?[0-9]?$")


while True: 
    s_address = str(input()) # Server IP
    test = pat.match(s_address)
    if test:
        break
    else:
        print ("Incorrect ip address")
        

        
while True: 
    print ("Input Access key:")
    a_key = str(input())
    print ("Input Secret key:")
    s_key = str(input())
    api_key = "accessKey="+a_key+"; "+"secretKey="+s_key+";"
    
    url = "https://"+s_address
    payload={}
    headers = {
      'X-ApiKeys': api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    if str(response) == "<Response [200]>":
        print ("Connected to "+s_address)
        break
    else:
        print ("WARNING! Incorrect API keys. Try again.") 


# In[9]:


url = "https://"+s_address+"/scans"

payload={}
headers = {
  'X-ApiKeys': api_key
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
#print (response.text)


# In[10]:


y = json.loads(response.text)
folders = y["folders"]
scans = y["scans"]

 
list_folders = pd.DataFrame(folders)
print(list_folders[["id","name"]].to_string(index = False)) 


# In[11]:


scans_table = pd.DataFrame(scans)
print ("--"*10)
print('Enter folder id: ')
f_n = int(input())
print ("--"*10)
list_scans = scans_table[scans_table.folder_id==f_n]
print(list_scans[["id","name"]].to_string(index = False)) 


# In[ ]:


print ("--"*10)
print('Enter scan id (You can enter multiple scans. Example: 105,240,196).')
sn_list = Convert(input())


#print (d_fn+"_"+today)


# In[76]:


print ("Choose the report format (1-2):\n 1. CSV \n 2. Nessus") 
allowed_types = ["1","2"]
while True: 
    f_t = str(input())
    if f_t in allowed_types:
        break
    else:
        print ("Choose the correct number: ")
if f_t == "1":
    report_format = "csv"

if f_t == "2":
    report_format = "nessus"

#if f_t == "3":
#    report_format = "pdf"
    
#if f_t == "4":
#    report_format = "html"


# In[77]:


for s_n in sn_list:
    
    
    url = srv_url+s_n+"/export" 

    payload = json.dumps({
      "format": report_format
      #"filter.0.filter": "severity",
     # "filter.0.quality": "eq",
      #"filter.0.value": f_sev
    })

    headers = {
      'Content-Type': 'application/json',
      'X-ApiKeys': api_key,
    }

    response_export = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print(response_export.text)


    tf_json = json.loads(response_export.text) 
    timeout=0
    print ("--"*10)
    print ("Wait untill the report will be prepared")
    while True: # Ждём готовность отчёта
        token=(tf_json["token"])
        file=(tf_json["file"])

        url = srv_url+s_n+"/export/"+str(file)+"/status"

        payload={}
        headers = {
            'X-ApiKeys': api_key
        }

        response_status = requests.request("GET", url, headers=headers, data=payload, verify=False)

        if ((response_status.text == '{"status":"ready"}') or (timeout == 5000000)):
            break
        else:
            time.sleep(1)
            timeout = timeout+1


    print ("--"*10)
    print("Checking export status: ",response_status.text)


    url = srv_url+s_n+"/export/"+str(file)+"/download" # Скачиваем отчёт

    payload={
    }
    headers = {
      'X-ApiKeys': api_key
    }

    #response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    #print(response.text)

    d_fn = scans_table[scans_table.id==int(s_n)][["name"]].to_string(index = False,header=None) 
    today = str(datetime.datetime.now().strftime("%d-%m-%Y"))

    download_file(url)
    print ("--"*10)
    print ("File saved as: ", d_fn+"_"+today+"."+report_format)

    
print ("---DONE!---")


# In[ ]:




