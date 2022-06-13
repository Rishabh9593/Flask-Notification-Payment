'''
from __init__ import imp
db = imp.db
mongo = imp.mongo
myclient = imp.myclient
'''

#from bot import telegram_chatbot
from datetime import datetime, timedelta
from threading import Timer
import requests, json
from datetime import datetime, timedelta
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')


#bot = telegram_chatbot("config.cfg")
'''
x=datetime.today()
y = x.replace(day=x.day, hour=19, minute=12, second=0, microsecond=0) + timedelta(days=0)
delta_t=y-x
secs=delta_t.total_seconds()
'''
def Noti():
    
    #update_id = None
    mydb = myclient['project']
    mycol = mydb["issue"]
    now = datetime.now().date()
    for x in mycol.find():
        ret_dt = x["Return_date"]
        ret_date = ret_dt.date()
        chat_id = x["user_id"]
        title = x["title"]
        if now > ret_date:
            d0 = now
            d1 = ret_date
            delta = d0 - d1
            amount = delta.days*5
            amt = amount
            amt1 = str(amt)
            myquery = { "user_id": chat_id, "title": title}
            newvalues = { "$set": { "fees": amt } }
            mycol.update_one(myquery, newvalues)    

            URL = "https://api.telegram.org/bot1374267801:AAFBeI6TX4rpsHeYJa3rG1rHHJqIEW9j7I8/sendMessage"
            PARAMS = {'text':'Hello your due fees for book '+title+' is Rs.'+amt1,'chat_id':chat_id} 
            r = requests.get(url = URL, params = PARAMS) 
            data = r.json() 
            print(data)
      

'''
    while True:
        updates = bot.get_updates(offset=update_id)
        updates = updates["result"]
        if updates:
            for item in updates:
                update_id = item["update_id"]
                try:
                    message = str(item["message"]["text"])
                except:
                    message = None
                from_ = item["message"]["from"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, from_)
'''
Noti()
#t = Timer(secs, Noti)
#t.start()