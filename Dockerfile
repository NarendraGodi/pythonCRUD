# start by pulling a base image.
FROM ubuntu
# update the repositories.
RUN apt-get update && apt-get -y upgrade
# Setting up the password for mysql db access.
ENV MYSQL_ROOT_PASSWORD = ""
# Install apt utilities.
#RUN apt install apt-utils -y
# Install Python and PIP.
RUN apt install -y python3 && apt install -y pip
RUN apt-get install libmysqlclient-dev -y && apt-get install python3-dev -y
# Install Flask Package for the execution of Flask Application.
RUN pip install Flask && pip install mysql-connector-python
# Install Git, as we will use it for cloning the source code.
RUN apt install -y git
# Clone the Git repository for the source code.
RUN git clone https://github.com/NarendraGodi/pythonCRUD.git
# switch working directory
WORKDIR /pythonCRUD
# Execute the application.
ENTRYPOINT FLASK_APP=/pythonCRUD/app.py flask run --host=0.0.0.0 --port=8080
# make sure the container doesnt exit.
CMD tail -f /dev/null