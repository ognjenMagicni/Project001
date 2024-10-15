import pymysql
import pymysqlpool
from flask import Flask,jsonify,request
from flask_cors import CORS

config={'host':'localhost', 'user':'root', 'password':'Laptop1*', 'database':'properties', 'autocommit':True}
pool = pymysqlpool.ConnectionPool(size=2, maxsize=3, pre_create_num=2, name='pool1', **config)




app = Flask(__name__)

CORS(app,supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getAllSearches/')
def getAllSearches():
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM properties.search"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return jsonify(result)
    except Exception:
        conn.close()

@app.route("/getAllProperties/<int:id>")
def getAllProperties(id):
    conn = pool.get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM properties.property WHERE fk_search= %s"
    values = (id,)
    cursor.execute(query,values)
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

@app.route("/getSearch/<id>")
def getSearch(id):
    conn = pool.get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM properties.search WHERE id= %s"
    values = (id)
    cursor.execute(query,values)
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

@app.route('/getTypes/')
def getTypes():
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM properties.type"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return jsonify(result)
    except Exception:
        print(Exception)

@app.route('/getLocations/')
def getLocations():
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM properties.location"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return jsonify(result)
    except Exception:
        print(Exception)

@app.route("/updateOnOff/<id>",methods=["PUT"])
def onOffUpdate(id):
    conn = pool.get_connection()
    cursor = conn.cursor()
    query = "UPDATE properties.property SET on_off = 1-on_off WHERE id_property=%s"
    values = (id,)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(['a'])

@app.route("/runProgram/",methods=['POST'])
def runProgram():
    import realitica
    realitica.pages = int(request.json['pages'])
    realitica.cityFilter.append(request.json['location'])
    realitica.propertyFilter.append(request.json['type'])
    realitica.minPrice = int(request.json['minPrice'])
    realitica.maxPrice = int(request.json['maxPrice'])
    realitica.title = request.json['title']
    realitica.description = request.json['description']
    try:
        realitica.run()
    except:
        return jsonify({'success':'error'})
    return jsonify({'success':'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    