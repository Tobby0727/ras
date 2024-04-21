from flask import Flask
from flask_cors import CORS
from flask import jsonify,request
import pymysql

app=Flask(__name__)
## Nos permite acceder desde una api externa
CORS(app)
## Funcion para conectarnos a la base de datos de mysql
def conectar(vhost,vuser,vpass,vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
    return conn
##consultas especificas
@app.route("/consulta_reptiles/<nombre>",methods=['GET'])
def consulta_reptiles(nombre):
    try:
        conn=conectar('localhost','root','','ras')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM reptiles where nombre='{0}' """.format(nombre))
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'imagen':datos[0],'nombre':datos[1],'nombre_cientifico':datos[2],'veneno':datos[3],'cola_terminal':datos[4],'habitos':datos[4],'habitad':datos[5] }
            return jsonify({'registro':dato,'mensaje':'Registro  encontrado'})
        else:
            return jsonify({'mensaje':'Registro no encontrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
@app.route("/consulta_anfibios/<nombre>",methods=['GET'])
def consulta_anfibios(nombre):
    try:
        conn=conectar('localhost','root','','ras')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM anfibios where nombre='{0}' """.format(nombre))
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
            dato={'imagen':datos[0],'nombre':datos[1],'nombre_cientifico':datos[2],'veneno':datos[3],'habitos':datos[4],'habitad':datos[5]}
            return jsonify({'registro':dato,'mensaje':'Registro  encontrado'})
        else:
            return jsonify({'mensaje':'Registro no encontrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})

##registrar especies 
@app.route("/registrar_reptiles/",methods=['POST'])
def reptiles():
    try:
        conn=conectar('localhost','root','','ras')
        cur = conn.cursor()
        x=cur.execute(""" insert into reptiles (nombre,nombre_cientifico,veneno,habitos,habitad,cola_terminal,escamas) values \
            ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')""".format(request.json['nombre'],\
                request.json['nombre_cientifico'],request.json['veneno'],request.json['habitos'],request.json['habitad'],request.json['cola_terminal'],request.json['escamas']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
        print(ex)

@app.route("/registrar_anfibios/",methods=['POST'])
def anfibios():
    try:
        conn=conectar('localhost','root','','ras')
        cur = conn.cursor()
        x=cur.execute(""" insert into anfibios (nombre,nombre_cientifico,veneno,habitos,habitad) values \
            ('{0}','{1}','{2}','{3}','{4}')""".format(request.json['nombre'],\
                request.json['nombre_cientifico'],request.json['veneno'],request.json['habitos'],request.json['habitad']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
        print(ex)

##actualizar especies
@app.route("/actualizar_reptiles/<cod_reptiles>",methods=['PUT'])
def actualizar_reptiles(cod_reptiles):
    try:
        conn=conectar('localhost','root','','ras')
        cur = conn.cursor()
        x=cur.execute(""" update reptiles set nombre='{0}',nombre_cientifico='{1}',veneno='{2}',habitos='{3}',habitad='{4}',cola_terminal='{5}',escamas='{6}'where \
            cod_reptiles={7}""".format(request.json['nombre'],request.json['nombre_cientifico'],request.json['veneno'],request.json['habitos'],request.json['habitad'],request.json['cola_terminal'],request.json['escamas'],cod_reptiles))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'})
    
@app.route("/actualizar_anfibios/<cod_anfibios>",methods=['PUT'])
def actualizar_anfibios(cod_anfibios):
    try:
        conn=conectar('localhost','root','','ras')
        cur = conn.cursor()
        x=cur.execute(""" update anfibios set nombre='{0}',nombre_cientifico='{1}',veneno='{2}',habitos='{3}',habitad='{4}','where\
            cod_anfibios={5}""".format(request.json['nombre'],request.json['nombre_cientifico'],request.json['veneno'],request.json['habitos'],request.json['habitad'],cod_anfibios))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje':'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje':'Error'}) 

#@app.route("/")
#def tipo_de_especie():
   # try:
     #conn=conectar('localhost','root','','ras')
        #cur = conn.cursor()
        #cur.execute(""" select reptiles.cod_reptiles,reptiles.nombre as nom_reptil,reptiles.nombre_cientifico,anfibios.cod_anfibios,anfibios.nombre as nom_anfibio,anfibios.nombre_cientifico
                        #from tipo_de_especie 
                        #inner join reptiles on tipo_de_especie.cod_especie=reptiles.cod_reptiles
                        #inner join anfibios on tipo_de_especie.cod_especie=anfibios.cod_anfibios""")
        #datos=cur.fetchall()
        #data=[]
        #for row in datos:
            #dato={'codigo_especie,':row[0],'nombre':row[1],'nombre_cientifico,':row[2],}
            #data.append(dato)
       # cur.close()
        #conn.close()
        #return jsonify({'especies':data,'mensaje':'Baul de especies'})
    #except Exception as ex:
        #print(ex)
        #return jsonify({'mensaje':'Error'})








if __name__=='__main__':
    app.run(debug=True)

