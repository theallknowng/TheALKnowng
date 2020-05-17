#!/usr/bin/env python2.7

#Importing MQTTClient Library
import test
import random
import sys
import time
import json
import datetime
#Getting Connection Information

#Set portno_value to 8883 for Secured connection
SERVER_NAME="devicemanager.bevywise.com"
SERVER_PORT=int(1883)


#Getting MQTT Credential Informations
MQUsername="yJBuz0VlkjamSy7562"
MQPassword="B9XtDL3A4aTeHVIfYf"

#MQTT Connect Details
MQClientID="Laptop_Client"
timeout=60
clean_session=0
willflag=True
willqos=0
willretain=True
willtopic="Laptop_Status"
willmessage="Laptop_is_Shutdown"


#MQTTClient Instance Creation
Client=test.MQTTclient(MQClientID,SERVER_PORT,timeout,SERVER_NAME,clean_session,MQUsername,MQPassword,willflag,willqos,willretain,willtopic,willmessage)


##### Verification Prints	###################
print "#####\tDevice Authentication Credentials\t#####\nUsername: %s \tPassword: %s \n"%(MQUsername,MQPassword)
print "#####\tDevice Details\t#####\n Device_Name: %s\t Willtopic: %s \tWillMessage: %s\n"%(MQClientID,willtopic,willmessage)
print "#####\tConnection Details\t#####\nServerName: %s\t ServerPort: %s \n"%(SERVER_NAME,SERVER_PORT)
raw_input("********->\tPlease see if your confs are correct and Press Enter to connect\t<-*******")



#Connecting MQTTClient With Broker
if not Client.connect():
	print "Error While Connecting"
	sys.exit(0)
else:
    print "******\tMQTT Client Connected\t******\n"

#Subscribe_Topic_Name = "SGN1/status"
#Subscribe_Topic_Qos = 0
#Client.subscribe(Subscribe_Topic_Name,Subscribe_Topic_Qos)
#
#Subscribe_Topic_Name = "SGN2/status"
#Subscribe_Topic_Qos = 0
#Client.subscribe(Subscribe_Topic_Name,Subscribe_Topic_Qos)
#
#Subscribe_Topic_Name = "SGN3/status"
#Subscribe_Topic_Qos = 0
#Client.subscribe(Subscribe_Topic_Name,Subscribe_Topic_Qos)
#
#Subscribe_Topic_Name = "SGN4/status"
#Subscribe_Topic_Qos = 0
#Client.subscribe(Subscribe_Topic_Name,Subscribe_Topic_Qos)


#Subscribe To Topic With Qos1
#Subscribe_Topic_Name = "Laptop_Status"
#Subscribe_Topic_Qos = 1
#Client.subscribe(Subscribe_Topic_Name,Subscribe_Topic_Qos)
sig=['SGN1/status','SGN2/status','SGN3/status','SGN4/status']
count=0
while 1:
	print('======================================================================================================')
	count=count+1
	var=sig[random.randint(0,3)]
	Publish_Retain = 1
	Publish_Qos = 0
	t=str(datetime.datetime.now())
	Publish_Topic_Name = "SGN1/status"
	Publish_Message = "{'alert':'0','key':'1','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN2/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN3/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN4/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
	time.sleep(3)
	print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	Publish_Topic_Name = "SGN1/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN2/status"
	Publish_Message = "{'alert':'0','key':'1','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN3/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN4/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
	time.sleep(3)
	print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	Publish_Topic_Name = "SGN1/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN2/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN3/status"
	Publish_Message = "{'alert':'0','key':'1','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN4/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
	time.sleep(3)
	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	Publish_Topic_Name = "SGN1/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN2/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN3/status"
	Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#	time.sleep(3)
	Publish_Topic_Name = "SGN4/status"
	Publish_Message = "{'alert':'0','key':'1','t':'"+t+"'}"
	Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
	time.sleep(3)
	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	#Disconnect The Client
	print('====================================================================================================================================================')
	if(count==3):
		print('Alert!!! Emergency vehicle at ', var)
		if(var=='SGN1/status'):
			Publish_Topic_Name = "SGN1/status"
			Publish_Message = "{'alert':'1','key':'1','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN2/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN3/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN4/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
			time.sleep(3)
		elif(var=='SGN2/status'):
			Publish_Topic_Name = "SGN1/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN2/status"
			Publish_Message = "{'alert':'1','key':'1','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN3/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN4/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
			time.sleep(3)
		elif(var=='SGN3/status'):
			Publish_Topic_Name = "SGN1/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN2/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN3/status"
			Publish_Message = "{'alert':'1','key':'1','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN4/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
			time.sleep(3)
		elif(var=='SGN4/status'):
			Publish_Topic_Name = "SGN1/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN2/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)

			Publish_Topic_Name = "SGN3/status"
			Publish_Message = "{'alert':'0','key':'0','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
			Publish_Topic_Name = "SGN4/status"
			Publish_Message = "{'alert':'1','key':'1','t':'"+t+"'}"
			Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
			time.sleep(3)

		print('---------------------------------------------------------------------------------------------------')
		count=0
		
		
Client.disconnect()










#EK jamane ka code
#if(var=='SGN1/status'):
#		Publish_Topic_Name = "SGN1/status"
#		Publish_Message = "{'key':'1'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN2/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN3/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN4/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#	elif(var=='SGN2/status'):
#		Publish_Topic_Name = "SGN1/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN2/status"
#		Publish_Message = "{'key':'1'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN3/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN4/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#	elif(var=='SGN3/status'):
#		Publish_Topic_Name = "SGN1/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN2/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN3/status"
#		Publish_Message = "{'key':'1'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN4/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#	elif(var=='SGN4/status'):
#		Publish_Topic_Name = "SGN1/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN2/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN3/status"
#		Publish_Message = "{'key':'0'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)
#		Publish_Topic_Name = "SGN4/status"
#		Publish_Message = "{'key':'1'}"
#		Client.publish(Publish_Topic_Name,json.dumps(Publish_Message),Publish_Retain,Publish_Qos)
#		time.sleep(3)

