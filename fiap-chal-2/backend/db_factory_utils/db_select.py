import mysql.connector;
import os;
import json;
import db_connection;

def getinformation(kindofinfo, userdata):
    if not "@" in userdata:
        return "User not existent"

    if(kindofinfo=="user"):
        wherestatement="uendereco = " + userdata
        response = db_connection.selecttx(wherestatement, "tbuser")
        return response
    if(kindofinfo=="emailist"):
        wherestatement="usid = " + userdata
        response = db_connection.selecttx(wherestatement, "tbuser")
        return response
    if(kindofinfo=="calendarList"):
        wherestatement="usid = " + userdata
        response = db_connection.selecttx(wherestatement, "tbuser")
        return response
    if(kindofinfo=="userconfig"):
        wherestatement="usid = " + userdata
        response = db_connection.selecttx(wherestatement, "tbuser")
        return response