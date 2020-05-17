from sys import platform
import time
import sqlite3
import json

conn = sqlite3.connect('TRACKER.db')
try:
	conn.execute('CREATE TABLE if not exists tracker (lane TEXT, day TEXT)')
	conn.close()
except:
	print("Error while creating avg table")
	conn.close()

#conn = sqlite3.connect('database.db')
#try:
#	conn.execute('CREATE TABLE if not exists temperature (city TEXT, day TEXT, temperature TEXT)')
#	conn.close()
#except:
#	print("Error while creating temperature table")
#	conn.close()
#
#conn = sqlite3.connect('database.db')
#try:
#	conn.execute('CREATE TABLE if not exists humidity (city TEXT, day TEXT, humidity TEXT)')
#	conn.close()
#except:
#	print("Error while creating humidity table")
#	conn.close()
#
#conn = sqlite3.connect('T.db')
#try:
#	conn.execute('CREATE TABLE if not exists wind (city TEXT, day TEXT, wind TEXT)')
#	conn.close()
#except:
#	print("Error while creating rainfall table")
#	conn.close()


if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
    import libmqttclient
elif platform == 'win32':
    from ctypes import *
    libmqttclient = PyDLL('./libmqttclient.dll')
    start = PYFUNCTYPE(py_object, py_object)
    start_client = start(('start_client', libmqttclient))
    stop = PYFUNCTYPE(py_object, py_object)
    stop_client = stop(('stop_client', libmqttclient))
    publish = PYFUNCTYPE(py_object, py_object)
    publish_data = publish(('publish_data', libmqttclient))
    unsubscribe = PYFUNCTYPE(py_object, py_object)
    unsubscribe_topic = unsubscribe(('unsubscribe_topic', libmqttclient))
    subscribe = PYFUNCTYPE(py_object, py_object)
    subscribe_topic = subscribe(('subscribe_topic', libmqttclient))

class MQTTclient:

    def __init__(self, clientid, portno=1883, timeout=40, hostname='localhost', clear_session=0, username='', password='', willflag=False, willqos=0, willretain=False, willtopic='', willmessage=''):
        self.portno = portno
        self.timeout = timeout
        self.hostname = hostname
        self.clientid = clientid
        self.sockfd = 0
        self.user_pub_callback = None
        self.set_clearSession(clear_session)
        self.username = username
        self.password = password
        self.set_willflag(willflag)
        self.willqos = willqos
        self.set_willretain(willretain)
        self.willtopic = willtopic
        self.willmessage = willmessage
        return

    def set_portno(self, portno):
        self.portno = portno

    def set_timeout(self, timeout):
        self.timeout = timeout

    def set_hostname(self, hostname):
        self.hostname = hostname

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_clearSession(self, clear_session):
        if clear_session == 1:
            self.clear_session = 1
        else:
            self.clear_session = 0

    def set_willflag(self, willflag):
        if willflag:
            self.willflag = 1
        else:
            self.willflag = 0

    def set_willretain(self, willretain):
        if willretain:
            self.willretain = 1
        else:
            self.willretain = 0

    def set_willqos(self, willqos):
        self.willqos = willqos

    def set_willtopic(self, willtopic):
        self.willtopic = willtopic

    def set_willmessage(self, willmessage):
        self.willmessage = willmessage

    def publish_onrecv(self, topic_name, data, sockfd):
        if self.user_pub_callback == None:
            print (' MESSAGE RECEIVED:- {0} : Topic : {1} Message received : {2}\n').format(self.clientid, topic_name, data)
            
            temp = topic_name.split("/")
            jsonData  = eval(json.loads(data))
#            print("Alert bhai ",jsonData['alert'])
            if(jsonData['alert']=='1'):
		        with sqlite3.connect("TRACKER.db") as con:
					cur = con.cursor()
					
					#date1 = json1["date"]
#					print("temp, ", temp[0], data)
					if(temp[0]=='SGN1'):
#						print(jsonData['key'])
#						print(jsonData['t'])
						cur.execute("INSERT INTO tracker (lane, day) values(?,?)",('1',jsonData['t']))

					elif(temp[0]=='SGN2'):
#						print(jsonData['key'])
#						print(jsonData["t"])
						cur.execute("INSERT INTO tracker (lane, day) values(?,?)",('2',jsonData['t']))

					elif(temp[0]=='SGN3'):
#						print(jsonData["key"])
#						print(jsonData["t"])
						cur.execute("INSERT INTO tracker (lane, day) values(?,?)",('3',jsonData['t']))

					elif(temp[0]=='SGN4'):
#						print(jsonData["key"])
#						print(jsonData["t"])
						cur.execute("INSERT INTO tracker (lane, day) values(?,?)",('4',jsonData['t']))
					con.commit()


            
            
        else:
            self.user_pub_callback(topic_name, data)
        return

    def set_publish_callback(self, user_callback):
        self.user_pub_callback = user_callback

    def get_clientid(self):
        return self.clientid

    def connect(self):
        if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            self.sockfd = libmqttclient.start_client(self.timeout, self.portno, self.hostname, self.clientid, len(self.clientid), self.username, len(self.username), self.password, len(self.password), self.clear_session, self.willflag, self.willqos, self.willretain, self.willtopic, len(self.willtopic), self.willmessage, len(self.willmessage), self.publish_onrecv)
            if self.sockfd == 0:
                return False
            return True
        if platform == 'win32':
            self.sockfd = start_client((self.timeout, self.portno, self.hostname, self.clientid, len(self.clientid), self.username, len(self.username), self.password, len(self.password), self.clear_session, self.willflag, self.willqos, self.willretain, self.willtopic, len(self.willtopic), self.willmessage, len(self.willmessage), self.publish_onrecv))
            if self.sockfd == 0:
                return False
            return True

    def subscribe(self, topic_name, topic_qos=0):
        if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            result = libmqttclient.subscribe_topic(topic_name, topic_qos, len(topic_name), self.sockfd)
            return result
        if platform == 'win32':
            result = subscribe_topic((topic_name, topic_qos, len(topic_name), self.sockfd))
            return result

    def unsubscribe(self, topic_name):
        if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            result = libmqttclient.unsubscribe_topic(topic_name, len(topic_name), self.sockfd)
            return result
        if platform == 'win32':
            result = unsubscribe_topic((topic_name, len(topic_name), self.sockfd))
            return result

    def publish(self, topic_name, data, retain=1, qos=0):
        if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            result = libmqttclient.publish_data(topic_name, data, retain, qos, len(topic_name), len(data), self.sockfd)
            return result
        if platform == 'win32':
            result = publish_data((topic_name, data, retain, qos, len(topic_name), len(data), self.sockfd))
            return result

    def disconnect(self):
        if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
            result = libmqttclient.stop_client(self.sockfd)
            return result
        if platform == 'win32':
            result = stop_client((self.sockfd,))
            return result
