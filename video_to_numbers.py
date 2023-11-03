# Import the EvaDB package
import evadb
import urllib.request

#urllib.request.urlretrieve("https://www.dropbox.com/s/yxljxz6zxoqu54v/mnist.mp4", "mnist.mp4")
cursor = evadb.connect().cursor()

# query = '''OPEN DATABASE sqlite_data WITH ENGINE = "sqlite", PARAMETERS = {
#      "database": "evadb.db"
# };'''

# cursor.query(query).df()

evadb.connect("evadb")

# Load the video into EvaDB
cursor.query("DROP TABLE IF EXISTS MNISTVid").df()
cursor.query("LOAD VIDEO 'mnist.mp4' INTO MNISTVid").df()

# Run a query on video data 
query = cursor.query("""
     SELECT data, MnistImageClassifier(data).label
     FROM MNISTVid
     
""")
response = query.df()

print(response)