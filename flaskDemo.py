from flask import Flask 
from flask import request

app = Flask(__name__)

def conn_sqlite():
	import sqlite3
	conn = sqlite3.connect('LTS.db')
	cursor = conn.cursor()
	cursor.execute('select * from stockList')
	values = cursor.fetchall()
	cursor.close()
	conn.commit()
	conn.close()
	return values

@app.route('/getStock')
def getStock():
	import json
	values = conn_sqlite()
	jsonData = []
	for row in values:
		result = {}
		result['id'] = row[0]  
		result['name'] = row[1]  
		result['newPrice'] = row[2]
		result['priceLimit'] = row[3]  
		result['priceChange'] = row[4]  
		result['fiveChange'] = row[5]
		jsonData.append(result)
	return json.dumps(jsonData)

app.run(port=9999,debug=True,host='0.0.0.0')