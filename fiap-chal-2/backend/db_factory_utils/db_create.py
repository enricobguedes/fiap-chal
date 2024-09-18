import mysql.connector;
import datetime;
import os;

def createData(kindofinfo, data, db_connection):
    now = datetime.datetime.now()  # Obter a data/hora atual
    rowstamp = now.strftime("%Y/%m/%d %H:%M:%S")

    # Inserção de novo usuário
    if kindofinfo == "newuser":
        column = 'uname, upwd, uendereco, rowstamp'
        values = "\"" + data.get("uname") + "\",\"" + data.get("upwd") + "\",\"" + data.get("uendereco") + "\",\"" + rowstamp + "\""
        table = "tbuser"
    
    # Envio de email
    elif kindofinfo == "sendemail":
        column = 'usid, usdestinatario, eassunto, hasCal, ecompleto, egigante, rowstamp'
        values = "\"" + data.get("usid") + "\",\"" + data.get("usdestinatario") + "\",\"" + data.get("eassunto") + "\",\"" + str(data.get("hasCal")) + "\",\"" + data.get("ecompleto") + "\",\"" + data.get("egigante") + "\",\"" + rowstamp + "\""
        table = "tbemail"
    
    # Criação de evento de calendário
    elif kindofinfo == "createcalendar":
        column = 'usid, ueid, calinicio, calfinal, caldestinatario'
        values = "\"" + data.get("usid") + "\",\"" + data.get("ueid") + "\",\"" + data.get("calinicio") + "\",\"" + data.get("calfinal") + "\",\"" + data.get("caldestinatario") + "\""
        table = "tbcalendar"
    
    # Criação de tema do usuário
    elif kindofinfo =="uconfig":
        column = 'ucid', 'usid', 'uctema'
        values ="\"" + data.get("ucid") + "\",\"" + data.get("usid") + "\",\"" + data.get("uctema") + "\""
        table = "tbuserconfiog"

     # Criação de evento de calendário
    elif kindofinfo =="emailcal":
        column = 'ucid', 'usid', 'uctema'
        values ="\"" + data.get("ucid") + "\",\"" + data.get("usid") + "\",\"" + data.get("uctema") + "\""
        table = "tbemailcal"

    # Usar o método inserttx através do db_connection para inserir os dados
    try:
        response = db_connection.inserttx(column, values, table)
        return response
    except Exception as err:
        return f"Error: {err}"
