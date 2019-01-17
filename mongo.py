from flask import Flask,render_template,request
import requests
import pymongo
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('url.html')

@app.route('/url',methods=['POST','GET'])
def  url():
	if request.method=='POST':
		try:
			url = request.form['url']
		except:
			print ("-------------------------------------")

		myClient=pymongo.MongoClient("mongodb://localhost:27017/") 
		mydb=myClient["mydatab"]#create a database if not exists
		mycol=mydb["urll"]#creating a collection

		page = requests.get(url)
		data=page.text
		soup = BeautifulSoup(page.text, 'html.parser')#object of beautiful soup
		name=soup.find()#get data from website
		n=0
		name_list=name.find_all('a')#Fetvh data having <a> tag
	
		for name in name_list:
			n+=1
			names = name.contents[0]
			links = name.get('href')
			mydict={"_id":n,"name":str(names),"links":str(links)}
			x=mycol.insert_one(mydict)  	
			print(x.inserted_id)
		return (str(n)+" entries added to database")



if __name__ == '__main__':
	app.run()
	
