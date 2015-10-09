from flask import render_template, request
from app import app

@app.route('/get_response', methods=['POST'])
def get_response():
	query = request.json['question']
	
	import unirest

	import json
	import urllib2
	import urllib
	
	
	#Get past the LM Proxy
	proxy = urllib2.ProxyHandler({'https': 'http://www-proxy.lmig.com:80'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)
	
	urllib.unquote(query).decode('utf8')
	
	# This code uses an open-source library. http://unirest.io/python
	response = unirest.get("https://jeannie.p.mashape.com/api?input="+query+"&locale=en&location=42.4,71.1&page=1&timeZone=%2B120&dialog=Sandbox",
	headers={
		"X-Mashape-Key": "XtsevWZQWnmshJeFehr8Jirln9ayp1Qww8NjsnL1sTDXoZPfMT",
		"Accept": "application/json"
	}
	)
	
	return response.raw_body


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')