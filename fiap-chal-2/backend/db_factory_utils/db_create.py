import mysql.connector;
import os;
import datetime;

def createData(action,data):
    appender="\",\""
    if(kindofinfo=="newuser"):
        rowstamp=now.strftime("%Y/%m/%d %H:%M:%S");

        column='uname,upwd,uendereco,rowstamp'
        values="\"" + data.get("uname") + appender + data.get("upwd") + appender + data.get(uendereco) + appender + rowstamp + "\""

        response = db_connection.inserttx(column, values, tbuser)
        return response

    if(kindofinfo=="sendemail"):
        rowstamp=now.strftime("%Y/%m/%d %H:%M:%S");

        column='uname,upwd,uendereco,rowstamp'
        values="\"" + data.get("uname") + appender + data.get("upwd") + appender + data.get(uendereco) + appender + rowstamp + "\""

        response = db_connection.inserttx(column, values, tbuser)
        return response

    if(kindofinfo=="simplecal"):
        rowstamp=now.strftime("%Y/%m/%d %H:%M:%S");

        column='uname,upwd,uendereco,rowstamp'
        values="\"" + data.get("uname") + appender + data.get("upwd") + appender + data.get(uendereco) + appender + rowstamp + "\""

        response = db_connection.inserttx(column, values, tbuser)

        return response

    if(kindofinfo=="emailcal"):
        rowstamp=now.strftime("%Y/%m/%d %H:%M:%S");

        column='uname,upwd,uendereco,rowstamp'
        values="\"" + data.get("uname") + appender + data.get("upwd") + appender + data.get(uendereco) + appender + rowstamp + "\""

        response = db_connection.inserttx(column, values, tbuser)

        return response

    if(kindofinfo=="uconfig"):
        rowstamp=now.strftime("%Y/%m/%d %H:%M:%S");

        column='uname,upwd,uendereco,rowstamp'
        values="\"" + data.get("uname") + appender + data.get("upwd") + appender + data.get(uendereco) + appender + rowstamp + "\""

        response = db_connection.inserttx(column, values, tbuser)

        return response
    

#createUser:
## JSON esperado: 
#    'uname'='USER_TESTE', 
#    'upwd'= '01234567',
#    'uendereco'='test@test.br',

#sendEmail:
## JSON esperado: 
#    usid=user id,
#    usdestinatario=email destinatario,  
#    eassunto=assunto do email, 
#    hasCal= boolean se tiver item de calendario, 
#    ecompleto= corpo do email , 
#    egigante= corpo do email se for maior que 2k char

#createCalendar:
## JSON esperado: 
#    usid = user id 
#    ueid = email id (retornado do sendEmail se tiver sido enviado em email) 
#    calinicio = formato timestamp de SQL
#    calfinal= formato timestamp de SQL
#    caldestinatario = email de quem irá receber/quem convidou

