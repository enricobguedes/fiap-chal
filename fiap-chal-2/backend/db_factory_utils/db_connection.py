import mysql.connector;
import os;


serverAddress= os.environ.get('DB_ADDRESS');
dbuser= os.environ.get('DB_USER');
dbpassword= os.environ.get('DB_PW');
databaseName= os.environ.get('DB_NAME');

config = {
  'user': dbuser,
  'password': dbpassword,
  'host': serverAddress,
  'database': databaseName,
  'raise_on_warnings': True
}

conn = None;



def sendtx(statement, table):
    conn = mysql.connector.connect(**config)
    if(conn):
        print(f'Connected to db {config.get("database")}');
    
    if(statement):
        prepState = conn.cursor();
        prepState.execute(statement);
        returnStatement = prepState.fetchall();
        conn.commit();
        conn.close();

        if (table):
            response = dataSanitization(returnStatement, table);
            return response; 
        else:
            return returnStatement;
    else:
        conn.close();

def dataSanitization(returnStatement, table):
    response = [];
    if (kindOfRequest == "tbuser"):
        for i in range(len(returnStatement)):
            usid, uname, upwd, uendereco, rowstamp = returnStatement[i];
            response={'usid': usid,'uname': uname,'upwd': upwd,'uendereco': uendereco,'rowstamp': rowstamp};
        return response;

    elif (kindOfRequest == "tbuserconfig"):
        for i in range(len(returnStatement)):
            ucid, usid, uctema, rowstamp = returnStatement[i];
            response={'ucid': ucid,'usid': usid,'uctema': uctema,'rowstamp': rowstamp};
        return response;
    elif (kindOfRequest == "tbemail"):
        for i in range(len(returnStatement)):
            ueid, usid, usdestinatario, eassunto, hasCal, isFav, calid, ecategoria, ecompleto, egigante = returnStatement[i];
            response={'ueid': ueid,'usid': usid,'usdestinatario': usdestinatario,'eassunto': eassunto,'hasCal': hasCal, 'isFav': isFav,'calid': calid,'ecategoria': ecategoria,'ecompleto': ecompleto,'egigante': egigante};
        return response;
    elif (kindOfRequest == "tbcalendario"):
        for i in range(len(returnStatement)):
            usid, uname, upwd, uendereco, rowstamp = returnStatement[i];
            response={'calid': calid,'usid': usid,'ueid': ueid,'calinicio': calinicio,'calfinal': calfinal,'rowstamp': rowstamp,'caldestinatario': caldestinatario};
        return response;
    elif (kindOfRequest == "tbsecurity"):
        for i in range(len(returnStatement)):
            usid, uname, upwd, uendereco, rowstamp = returnStatement[i];
            response={'usid': usid,'uname': uname,'upwd': upwd,'uendereco': uendereco,'rowstamp': rowstamp};
        return response;

    else:
        return response;


def selecttx(wherestatement, table):
    if (!wherestatement):
        return "Nothing to process";
    
    prestatement="SELECT * FROM " + table;
    wherestatement=" WHERE " + wherestatement;

    statement=prestatement + wherestatement;
    response = db_connection(statement, table);
    return response;
    
def inserttx(column, values, table):
    if (!column or !values or !table):
        return "Nothing to process";
    
    prestatement="INSERT INTO " + table;
    columnstatement="("+ column + ")"
    valuestatement=" VALUES" + "(" + values + ")"

    statement= prestatement + columnstatement + valuestatement;
    response = db_connection(statement, table);
    return response;