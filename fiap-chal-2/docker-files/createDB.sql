CREATE DATABASE IF NOT EXISTS fiapchalemail;

USE fiapchalemail;

CREATE TABLE IF NOT EXISTS tbuser (
    usid INT(12) NOT NULL AUTO_INCREMENT, 
    uname varchar(50) NOT NULL, 
    upwd varchar(30) NOT NULL, 
    uendereco varchar(100),
    rowstamp timestamp,
    PRIMARY KEY (usid)
);

CREATE TABLE IF NOT EXISTS tbuserconfig (
    ucid INT(12) NOT NULL AUTO_INCREMENT, 
    usid INT(12) NOT NULL,
    uctema INT(3) NOT NULL DEFAULT 0, 
    rowstamp timestamp,
    PRIMARY KEY (ucid)
);

CREATE TABLE IF NOT EXISTS tbemail (
    ueid INT(12) NOT NULL AUTO_INCREMENT, 
    usid varchar(50) NOT NULL,
    usdestinatario varchar(100),
    eassunto varchar(30), 
    hasCal INT(1) NOT NULL DEFAULT 0, 
    isFav INT(1) NOT NULL DEFAULT 0,
    calid INT(12),
    ecategoria INT(5) NOT NULL DEFAULT 0,
    ecompleto varchar(2000), 
    egigante varchar(10000),
    
    
    PRIMARY KEY (ueid)
);

CREATE TABLE IF NOT EXISTS tbcalendario (
    calid INT(12) NOT NULL AUTO_INCREMENT, 
    usid varchar(50) NOT NULL, 
    ueid INT(12), 
    calinicio timestamp, 
    calfinal timestamp, 
    rowstamp timestamp, 
    caldestinatario varchar(100),  
    PRIMARY KEY (calid)
);

CREATE TABLE IF NOT EXISTS tbsecurity (
    secid INT(12) NOT NULL AUTO_INCREMENT, 
    sisspam INT(1) NOT NULL DEFAULT 0, 
    eid INT NOT NULL, 
    uendereco varchar(100), 
     
    PRIMARY KEY (secid)
);


INSERT INTO tbuser(
    usid,
    uname, 
    upwd, 
    uendereco,
    rowstamp
) VALUES (
    1,
    'USER_TESTE',
    '01234567',
    'test@test.br',
    CURRENT_TIMESTAMP()
);
INSERT INTO tbuser(
    usid,
    uname, 
    upwd, 
    uendereco,
    rowstamp
) VALUES (
    2,
    'USER_TESTE2',
    '01234567',
    'test2@test.br',
    CURRENT_TIMESTAMP()
);

INSERT INTO tbuserconfig(
    ucid, 
    usid,
    uctema,  
    rowstamp
) VALUES (
    1,
    1,
    1,
    CURRENT_TIMESTAMP()
);
INSERT INTO tbuserconfig(
    ucid, 
    usid,
    uctema,  
    rowstamp
) VALUES (
    0,
    2,
    0,
    CURRENT_TIMESTAMP()
);

INSERT INTO tbemail(
    ueid, 
    usid,
    usdestinatario,
    eassunto, 
    hasCal, 
    isFav,
    calid,
    ecategoria,
    ecompleto, 
    egigante
) VALUES (
    1,
    1,
    'test2@test.br',
    'ASSUNTO',
    1,
    1,
    1,
    2,
    'EMAIL',
    ''
);

INSERT INTO tbemail(
    ueid, 
    usid,
    usdestinatario,
    eassunto, 
    hasCal, 
    isFav,
    calid,
    ecategoria,
    ecompleto, 
    egigante
) VALUES (
    2,
    2,
    'test@test.br',
    'ASSUNTO',
    0,
    0,
    0,
    4,
    '',
    'EGIGANTE'
);

INSERT INTO tbcalendario(
    calid, 
    usid, 
    ueid, 
    calinicio, 
    calfinal, 
    rowstamp, 
    caldestinatario  
) VALUES (
    1,
    1,
    1,
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP(),
    'test@test.br'
);

INSERT INTO tbcalendario(
    calid, 
    usid, 
    ueid, 
    calinicio, 
    calfinal, 
    rowstamp, 
    caldestinatario
) VALUES (
    2,
    2,
    0,
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP(),
    'test@test.br'
);
