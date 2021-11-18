from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import matplotlib.pyplot as plt 

# <------------------------Importación de la base de datos-------------------------->
cred = credentials.Certificate('D:\\Documentos\\Github\\Proyecto SOFTWARE\\rougue-studios\\proyect-assistent\\ida\\assistent-personal-35dbb-firebase-adminsdk-1sx5y-058487df7f.json')
firebase_admin.initialize_app(cred,{'databaseURL':'https://assistent-personal-35dbb-default-rtdb.firebaseio.com/'})

# <------------------------Correos Enviados y Agregados----------------------------->
ref=db.reference('/calls/Emails/Agregados') 
CorreosAgregados = ref.get()


ref=db.reference('/calls/Emails/Enviados') 
CorreosEnviados = ref.get()


fig = plt.figure(figsize=(7,5))
names = ["Correos Agregados","Correos Enviados"]
scores = [CorreosAgregados,CorreosEnviados]
positions = [0,1]

plt.bar(positions,scores,width=0.5, color="g")

plt.xticks(positions,names)

plt.show()

# <---------------------------Búsquedas en internet---------------------------------->
ref=db.reference('/calls/Facebook/busquedas')
BusquedaFacebook = ref.get()

ref=db.reference('/calls/Google/busquedas')
BusquedaGoogle = ref.get()

ref=db.reference('/calls/Youtube/busquedas') 
BusquedaYoutube = ref.get()

fig = plt.figure(figsize=(7,5))
names = ["Búsquedas en Facebook","Búsquedas en Google", "Búsquedas en Youtube"]
scores = [BusquedaFacebook,BusquedaGoogle,BusquedaYoutube]
positions = [0,1,2]

plt.bar(positions,scores,width=0.5, color="b")
plt.xticks(positions,names)
plt.show()

# <-----------------------------------Oye IDA--------------------------------------->
ref=db.reference('/calls/IDA/oye') 
OyeIDA = ref.get()


fig = plt.figure(figsize=(7,5))
names = ["Oye IDA"]
scores = [OyeIDA]
positions = [0]

plt.bar(positions,scores,width=0.5, color="r")

plt.xticks(positions,names)

plt.show()
