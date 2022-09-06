from turtle import clear
from urllib import request
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
# from dbConnect import delete_one, insert_many, show_all,insert_one, delete_all, softDeleteAll_db, update_one
import time
import hashlib
import base64

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}


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
    tinyurl = result[0:10:1] + baseVal[1:6:2]
    thisdict["tinyurl"] = tinyurl
    return thisdict
# Fetches the data form the DataBase 
@app.get("/fetchData")
async def testmyapi():
    # tinyurl = ""
    curr_time = time.strftime("%H:%M:%S", time.localtime())

    thisdict = {"url" : "www.google.com" , "time" : curr_time, "tinyurl": ""}
    
    ### use url key to generate a tiny url code goes here and tiny url is stored in tinyurl variable
    realResult = md5_convertion(thisdict)
    return realResult



# impliments singele addition
# @app.post("/addinv")
# async def testpostapi(inp: Request):
#     rq= await inp.json()
#     insert_one(rq)
#     return str("200 : Item Added Successfully ")

# # impliments update
# @app.put("/updateinv")
# async def testputapi(inp: Request):
#     rq= await inp.json()
#     update_one(rq)
#     return str("200 : Inventory Is Updated")

# # impliments soft delete
# @app.put("/sDelete")
# async def testputapi(inp: Request):
#     rq= await inp.json()
#     delete_one(rq)
#     return str("200 : Item Availablity Is checked")

# # impliments soft deletea ll
# @app.put("/sDeleteAll")
# async def testputapi(inp: Request):
#     rq= await inp.json()
#     softDeleteAll_db(rq)
#     return str("200 :All Items Deleted ")

# # impliment hard delete all
# @app.get("/deleteall")
# def testmyapi():
#     delete_all()
#     return("200 : Permenently Deleted From Inventory")

# # impliment insert many
# @app.put("/addMultiInv")
# async def testputapi(inp:Request):
#     request_data=await inp.json()
#     insert_many(request_data)
#     return str("200 : OK Items Added To Inventory Successfully")

# # impliment clean messaging for all api type request