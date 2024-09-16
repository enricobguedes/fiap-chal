import tornado.web;
import tornado.ioloop;
import json;
import os;
import db_factory_utils;

serverAddress = os.environ.get('127.0.0.1')

def addHeaders(self):
        self.add_header("Access-Control-Allow-Origin",serverAddress);
        self.add_header("Access-Control-Allow-Private-Network","true");
        self.add_header("Referrer",serverAddress + "/");

class getUserHandler(tornado.web.RequestHandler):
    def get(self, userdata):
        response = db_select.getinformation("user",userdata); 
        addHeaders(self)
        self.write(json.dumps(response));

class getEmailListHandler(tornado.web.RequestHandler):
    def get(self):
        response = db_select.getinformation("emailist",userdata);
        addHeaders(self)
        self.write(json.dumps(response));

class getCalendarAppointmentsHandler(tornado.web.RequestHandler):
    def get(self):
        response = db_select.getinformation("calendarList",userdata); 
        addHeaders(self);
        self.write(json.dumps(response));

class getUserConfigHandler(tornado.web.RequestHandler):
    def get(self, testcase):
        response = db_select.getinformation("userconfig",userdata); 
        addHeaders(self);
        self.add_header("Access-Control-Allow-Methods", "GET, POST, PUT");
        self.write(json.dumps(response));

class getSecurityHandler(tornado.web.RequestHandler):
    def get(self, scriptName, timestamp):
        addHeaders(self);
        self.add_header("Access-Control-Allow-Methods", "GET, POST, PUT");
        self.write(json.dumps(response));

class createUserHandler(tornado.web.RequestHandler):
    def post(self, action):
        addHeaders(self);
        self.add_header("Access-Control-Allow-Methods", "GET, POST, PUT");
        data = json.loads(self.request.body)
        response = db_create.createData("newuser",data)
        self.write(json.dumps(response));

class sendEmailHandler(tornado.web.RequestHandler):
    def post(self, action):
        addHeaders(self);
        self.add_header("Access-Control-Allow-Methods", "GET, POST, PUT");
        data = json.loads(self.request.body)
        response = db_create.createData("sendemail",data)
        self.write(json.dumps(response));

class createSimpleCalHandler(tornado.web.RequestHandler):
    def post(self, action):
        addHeaders(self);
        self.add_header("Access-Control-Allow-Methods", "GET, POST, PUT");
        data = json.loads(self.request.body)
        response = db_create.createData("simplecal",data)
        self.write(json.dumps(response));

class createEmailCalHandler(tornado.web.RequestHandler):
    def post(self, action):
        addHeaders(self);
        self.add_header("Access-Control-Allow-Methods", "GET, POST, PUT");
        data = json.loads(self.request.body)
        response = db_create.createData("emailcal",data)
        self.write(json.dumps(response));

class updateUserConfigHandler(tornado.web.RequestHandler):
    def post(self, action):
        addHeaders(self);
        self.add_header("Access-Control-Allow-Methods", "GET, POST, PUT");
        data = json.loads(self.request.body)
        response = db_create.createData("uconfig",data)
        self.write(json.dumps(response));

###
# Cada endpoint criado precisa ser exposto nesta lista para que o servidor consiga criar listeneres. 
# 
# @PARAMS:
# 
# - Endereço do endpoint
# - Handler
###

if __name__ == "__main__":
    app = tornado.web.Application([
        # getUser para manipular infos locais
        # /get/getUser/email
        (r"/get/getUser/(([A-Za-z0-9-_@]+))", getUserHandler),
        # getEmail para puxar a lista de emails do user
        # /get/getEmail/{user id}
        (r"/get/getEmail/([A-Za-z0-9-_@]+)", getEmailListHandler),
        # getCalendar para puxar os registros
        # /get/getCalendar/{user id}
        (r"/get/getCalendar/([A-Za-z0-9-_@]+)", getCalendarAppointmentsHandler), 
        # getUserConfig para puxar temas e/ou afins
        # /get/getUserConfig/{user id}
        (r"/get/getUserConfig/([A-Za-z0-9-_@]+)", getUserConfigHandler), 
        # getSecurity
        (r"/get/getSecurity", getSecurityHandler),
        # createUser criar user
        # /post/createUser/email do novo user
        # Olhar em baixo para ver a estrutura de objetos esperada
        # retorna USERID. MANTER COMO VARIAVEL PARA TODAS AS OPERACOES DO USER
        (r"/post/createUser/([A-Za-z0-9-_]+)", createUserHandler),
        # sendEmail para enviar emails
        # /post/sendEmail/userid
        # Olhar em baixo para ver a estrutura de objetos esperada
        # retorna emailid. MANTER COMO VARIAVEL PARA TODAS AS OPERACOES RELACIONADAS AO EMAIL
        (r"/post/sendEmail/([A-Za-z0-9-_]+)", sendEmailHandler),
        # createCalendar para criar calendarios ou criar calendarios a partir de um email
        # /post/createCalendar/userid
        # /post/createCalendar/userid/emailid - se criado de um email
        # Olhar em baixo para ver a estrutura de objetos esperada
        # MANTER COMO VARIAVEL PARA TODAS AS OPERACOES RELACIONADAS AO EMAIL
        (r"/post/createCalendar/([A-Za-z0-9-_]+)", createSimpleCalHandler),
        (r"/post/createCalendar/([A-Za-z0-9-_]+)/([A-Za-z0-9-_]+)", createEmailCalHandler),
        # setUserConfig para configurar temas
        # /post/setUserConfig/user id
        # Olhar em baixo para ver a estrutura de objetos esperada
        # Retorna json com as configurações do usuario
        (r"/post/setUserConfig/([A-Za-z0-9-_]+)", updateUserConfigHandler)
        ])

### Porta pode ser qualquer...
    port = 8882;
    app.listen(port);
    print(f"Application is listening at port {port}");

    #Loop para manter serivdor de pé
    tornado.ioloop.IOLoop.current().start();




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

