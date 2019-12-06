import mysql.connector 



class ArtistsDAO:     

	db=""     

	def __init__(self):          

	    self.db = mysql.connector.connect(        

		host="localhost",

		user="root",

		password="root",

		auth_plugin='mysql_native_password',        

		database="artists"

		)     

		

	def create(self, values):

		cursor = self.db.cursor()

		sql="insert into artists (name, genre, albums) values (%s,%s, %s)"

		cursor.execute(sql, values)

		self.db.commit()

		return cursor.lastrowid

		

	def getAll(self):

		cursor = self.db.cursor()

		sql="select * from artists"

		cursor.execute(sql)

		results = cursor.fetchall()

		

		returnArray = []

		print(results)

		for result in results:

			print(result)

			returnArray.append(self.convertToDictionary(result))

		

		return returnArray

		

	def findByID(self, id):

		cursor = self.db.cursor()

		sql="select * from artists where id = %s"

		values = (id,)

		

		cursor.execute(sql, values)

		result = cursor.fetchone()

		return self.convertToDictionary(result)

		

	def update(self, values):

		cursor = self.db.cursor()

		sql="update artists set name= %s, genre=%s, albums=%s  where id = %s"

		cursor.execute(sql, values)

		self.db.commit()

		

	def delete(self, id):

		cursor = self.db.cursor()

		sql="delete from artists where id = %s"

		values = (id,)

		cursor.execute(sql, values)

		self.db.commit()

		print("delete done") 

		

	def convertToDictionary(self, result):

		colnames=['id','name','genre','albums']

		

		item = {}

		

		if result:

			for i, colName in enumerate(colnames):

				value = result[i]

				item[colName] = value

		

		return item

		

 

artistsDAO = ArtistsDAO() 
