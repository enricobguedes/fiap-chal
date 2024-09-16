FROM ubuntu:latest
LABEL maintainer "EBG"
WORKDIR /
EXPOSE 3306:3306
EXPOSE 8882:8882

SHELL ["/bin/bash", "-c"]

## Ferramentas da VM
RUN apt update && apt install -y systemd lsb-release ffmpeg curl sudo vim procps


## Ferramentas do Serivdor
RUN apt install -y python3 python3-pip

RUN pip3 install tornado --break-system-packages && pip3.12 install mysql-connector-python --break-system-packages


ENV PATH="$PATH"
ENV DOCKER="true"

# Banco de dados
ENV DB_ADDRESS="127.0.0.1"
ENV DB_USER="fiapadmin"
ENV DB_PW="fiapadmin"
ENV DB_NAME="fiapchalemail"
ENV USER_TABLE="tbuser"
ENV U_CONFIG_TABLE="tbuserconfig"
ENV EMAIL_TABLE="tbemail"
ENV CALENDARIO_TABLE="tbcalendario"
ENV SEC_TABLE="tbsecurity"

run mkdir /backend
run mkdir /backend/db_factory_utils

COPY docker-files/* /
COPY backend/startServer.py /backend/
COPY backend/db_factory_utils/* /backend/db_factory_utils/

RUN chmod +x /startDBService.sh

RUN mkdir /logsGeral

CMD ["/bin/bash"]


