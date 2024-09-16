import mysql.connector;
import datetime;
import os;

def createData(kindofinfo, data, db_connection):
    now = datetime.datetime.now()  # Obter a data/hora atual
    rowstamp = now.strftime("%Y/%m/%d%H:%M:%S")
    
    # Inserção de novo usuário
    if kindofinfo == "newuser":
        column = 'uname, upwd, uendereco, rowstamp'
        values = (data.get("uname"), data.get("upwd"), data.get("uendereco"), rowstamp)
        sql = f"INSERT INTO tbuser ({column}) VALUES (%s, %s, %s, %s)"
    
    # Envio de email
    elif kindofinfo == "sendemail":
        column = 'usid, usdestinatario, eassunto, hasCal, ecompleto, egigante, rowstamp'
        values = (
            data.get("usid"), 
            data.get("usdestinatario"), 
            data.get("eassunto"), 
            data.get("hasCal"), 
            data.get("ecompleto"), 
            data.get("egigante"), 
            rowstamp
        )
        sql = f"INSERT INTO tbemail ({column}) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    # Criação de evento de calendário
    elif kindofinfo == "createcalendar":
        column = 'usid, ueid, calinicio, calfinal, caldestinatario'
        values = (
            data.get("usid"), 
            data.get("ueid"), 
            data.get("calinicio"), 
            data.get("calfinal"), 
            data.get("caldestinatario")
        )
        sql = f"INSERT INTO tbcalendar ({column}) VALUES (%s, %s, %s, %s, %s)"
    
    else:
        return "Tipo de informação inválida."

    # Inserir dados no banco de dados
    try:
        cursor = db_connection.cursor()
        cursor.execute(sql, values)
        db_connection.commit()  # Confirmar a transação
        return f"{kindofinfo} inserido com sucesso"
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()

    

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

