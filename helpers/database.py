from pymongo import MongoClient
import configuration

# connection_params = configuration.connection_params

#connect to mongodb
mongoconnection = MongoClient("mongodb+srv://vedantatrivedi:ved23202892@cluster0.fshlc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = mongoconnection.IoTProject
