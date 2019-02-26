## Using lists
#cards = "{'name':'nubank','flag':'br'}"

#@app.route('/cards/', methods=['GET'])
#def home():
#	return jsonify(cards), 200


#@app.route('/cards/<string:flag>', methods=['GET'])
#def card_flag(flag):
#	cards_per_flag = [card for card in cards if card['flag'] == flag]
#	return jsonify(cards_per_flag), 200


#@app.route('/cards/<int:id>', methods=['GET'])
#def id_cards(id):
#	cards_by_id = [card for card in cards if card['id'] == id]
#	return jsonify(cards_by_id), 200


# @app.route('/cards/new/', methods=['GET'])
# def new_card(name, flag):
# 	#parametros = urllib.urlencode({'name': name, 'flag': flag})
# 	cursor = mysql.connection.cursor()
# 	cursor.execute("CREATE TABLE IF NOT EXISTS cards(PersonID int NOT NULL PRIMARY KEY AUTO_INCREMENT, name varchar(255), flag varchar(100))")
# 	cursor.execute("INSERT INTO cards VALUES(null, name, flag)")
# 	mysql.connection.comit()
# 	cursor.close