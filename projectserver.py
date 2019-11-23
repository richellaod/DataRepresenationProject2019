#!flask/bin/python

from flask import Flask, jsonify,  request, abort, make_response



# Search for server path

app = Flask ('__name__', static_url_path='', static_folder='.')

# Don't sort array

app.config['JSON_SORT_KEYS'] = False





deezers = [

    {

        "id":123,

        "title":"Abc",

        "artist":"Def",

        "album":"Ghi",

		"duration":123,

		"rank":1

    },

	

	{

        "id":12,

        "title":"Ab",

        "artist":"Cd",

        "album":"EF",

		"duration":12,

		"rank":2

    }

]



# Use method GET to get all data

# curl -i http://localhost:5000/deezers

@app.route('/deezers', methods=['GET'])

def getAll():

    return jsonify(deezers)



# Use method GET to find data by id	

#curl -i http://localhost:5000/deezers/123

@app.route('/deezers/<int:id>', methods =['GET'])

def findById(id):

	foundId = list(filter(lambda t : t['id'] == id , deezers))

	if len(foundId) == 0:

		return jsonify( { 'deezers' : '' }),204



	return jsonify( { 'deezers' : foundId[0] })



# Use method POST to input new data	

# λ  curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":1000000,\"Title\":\"Up\",\"Artist\":\"Punto\",\"Album\":\"PPp\",\"duration\":55,\"rank\":505312}" http://localhost:5000/deezer

@app.route('/deezers', methods=['POST'])

def createDeezer():

    if not request.json:

        abort(400)

    if not 'id' in request.json:

        abort(400)

    deezer={

        "id":request.json['id'],

        "title":request.json['title'],

        "artist":request.json['artist'],

        "album":request.json['album'],

		"duration":request.json['duration'],

		"rank": request.json['rank']

    }

    deezers.append(deezer)

    return jsonify(deezer),201



# Use method PUT to dataset	

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"Fiesta\"}" http://localhost:5000/deezers/123

@app.route('/deezers/<int:id>', methods =['PUT'])

def updateDeezer(id):

    foundDeezers = list(filter(lambda t : t['id'] == id, deezers))

    if (len(foundDeezers) == 0):

        abort(404)

    foundDeezers = foundDeezers[0]

    if not request.json:

        abort(400)

    reqJson = request.json

	

    if 'duration' in request.json and type(reqJson['duration']) is not int:

        abort(400)

    if 'rank' in request.json and type(reqJson['rank']) is not int:

        abort(400)

		

    if 'title' in reqJson:

        foundDeezers['title'] = reqJson['title']

    if 'artist' in reqJson:

        foundDeezers['artist'] = reqJson['artist']

    if 'album' in reqJson:

        foundDeezers['album'] = reqJson['album']

    if 'duration' in reqJson:

        foundDeezers['duration'] = reqJson['duration']

    if 'rank' in reqJson:

        foundDeezers['rank'] = reqJson['rank']		

	    

    return jsonify(foundDeezers)



# Use method DELETE to delete dataset

# curl -X DELETE "http://localhost:5000/deezers/1000000"

@app.route('/deezers/<int:id>', methods =['DELETE'])

def deleteDeezer(id):

    foundDeezers = list(filter (lambda t : t['id'] == id, deezers))

    if len(foundDeezers) == 0:

        abort(404)

    deezers.remove(foundDeezers[0])

    return  jsonify( { 'Completed':True })



# error handling if data not found	

@app.errorhandler(404)

def not_found404(error):

    return make_response( jsonify( {'error':'Not found' }), 404)



# error handling if bad request

@app.errorhandler(400)

def not_found400(error):

    return make_response( jsonify( {'error':'Bad Request' }), 400)



if __name__ == '__main__' :

    app.run(debug= True)
