# Pull base image
FROM ubuntu:22.04

# Set noninteractive environment
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime && dpkg-reconfigure -f noninteractive tzdata && \
    apt-get install -y mysql-server python3 python3-pip apache2 libapache2-mod-wsgi-py3 openssh-server libmysqlclient-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \

# Set work directory
WORKDIR /var/www/html/

# Copy requirements.txt and install requirements
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy source code to work directory
COPY . .

# Enable apache rewrite module
RUN a2enmod rewrite

# Change owner and group for the html directory
RUN chown -R www-data:www-data /var/www/html

WORKDIR /var/www/html/mysite

# sshd service setting
RUN echo 'root:root' | chpasswd # need change
RUN mkdir /var/run/sshd
RUN chmod 0755 /var/run/sshd   # /var/run/sshd 권한 변경
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose port 8000 for Django
EXPOSE 80

# Start ssh and Django service
CMD exec /bin/bash -c "cd /home/user/django-web/mysite; /etc/init.d/ssh start; python3 manage.py makemigrations; python3 manage.py migrate; python3 manage.py runserver 0.0.0.0:8000"

