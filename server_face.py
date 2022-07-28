


# https://cloud.google.com/dialogflow/es/docs/integrations/dialogflow-messenger




from fnmatch import translate
from itertools import count
import re
from flask import Flask, make_response, render_template, request, jsonify,json
from pandas import to_datetime
import pyrebase
import configration_fierbase

import NLP_sintement

from googletrans import Translator

configration_fierbase.config
t = Translator()
one=NLP_sintement.Trans_Dialog()
# send_coupone="I love Amzone "
from collections import Counter
firebase = pyrebase.initialize_app(configration_fierbase.config)
db=firebase.database()



############################################# lunch server
app = Flask(__name__)
@app.route('/webhook', methods=['GET', 'POST'])


    
def results():

    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    
    # email=req.get('queryResult').get('parameters')
    

    # print(email['email'])
    
    

    # action = "input.m"
    match action:
      case "input.opinion" :
        result = {} 

        result = jsonify(result)
        payload =req
        user_res=(payload['queryResult']['queryText'])
        # trancy=one.translate(user_res)
        # print(trancy)
        trans_ar= t.detect(user_res)
        if trans_ar.lang == 'ar' :
            print(f"{user_res} : 1")

            c_en=t.translate(user_res,dest='en').text
            NLP_sintement.NLP(c_en)
            iteams_to_str=NLP_sintement.NLP.w
            print(f"{c_en} : 2")


            

        elif trans_ar.lang =='en':
            NLP_sintement.NLP(user_res)

            iteams_to_str=NLP_sintement.NLP.w
            
           
            
            
        
        data={"USER_MSG":user_res,"NLP":iteams_to_str ,"phoneNum":"NULL","email":"NULL"}
       
        db.child(f"USERS").push(data)

         
          
        with open('URL_button.json', 'r') as fcc_file:
          
          fcc_data = json.load(fcc_file)
        
          return fcc_data ,"200"
      #   return "200"

             
      case "input.unknown" :
        payload =req
        user_res=(payload['queryResult']['queryText'])
           
        ##### dont forget to add NLP anlyses her to 
        # data={"user_res":user_res}
        # db.push(data)
        result = {} 

        result = jsonify(result)
        return {"fulfillmentText":user_res},"200"

     
      


      case "discountcoupon.discountcoupon-custom" :
        payload =req
        user_res=(payload['queryResult']['queryText'])
           
        
        print(user_res)
        parmeter=req.get('queryResult').get('parameters')

        phone=parmeter['phone-number']
        
        email=parmeter['email']
        
        data_e={"USER_MSG":user_res,"NLP":"NULL" ,"phoneNum":phone,"email":email}
        db.child("USERS").push(data_e)
        result = {} 

        result = jsonify(result)
        
       
       
        return "200"

          

### take from user input
################################# show data in dashbord
push_data={
    
    "USER_MSG":"im happy to day ",
    "NLP":"happy:1",
    "email":"ibrahim@gmail.com",
    "phoneNum":"079123344",
}

#push as defolt bro it to clud
push=db.child("USERS").push(push_data)





    

heders=["NLP","USER MSG","email","phoneNum"]

data=[]

# # grap all data from fierbase as dcit
all_users = db.child("USERS").get()
for user in all_users.each():
   
#     ## make for loop to get the values and use it as list

    
    add=dict(user.val())
    data.append(list(add.values()))
  
    ##{'age': '213', 'name': 'arslan', 'num': '21434'} * count of it
 

print(data)  


@app.route("/index")


def table():
   
    return render_template("index.html",heders=heders,data=data)

if __name__ == '__main__':

   app.run(debug=True,port=2022)