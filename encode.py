import hashlib
import time
import base64

curr_time = time.strftime("%H:%M:%S", time.localtime())
### use url key to generate a tiny url code goes here and tiny url is stored in tinyurl variable

def base62Convertion(data):
    
    sample_string = data
    sample_string_bytes = sample_string.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

def md5_convertion(value):
    newlist =[]
    thisdict = value
    for keys ,  val in thisdict.items():
        if "url" or "URL" in thisdict.keys():
            newlist.append(val)
            break
    result = hashlib.md5(newlist[0].encode())
    baseVal = base62Convertion(result.hexdigest())
    result= result.hexdigest()
    tinyurl = "MyUrl\\"+result[0:10:1] + baseVal[1:6:2]
    thisdict["tinyurl"] = tinyurl
    return thisdict


print(md5_convertion({"url" : "www.google.com" , "time" : curr_time, "tinyurl": ""}))
