# Pull base image
FROM ubuntu:22.04

# Set noninteractive environment
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime && dpkg-reconfigure -f noninteractive tzdata && \
    apt-get install -y pkg-config mysql-server python3 python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-wheel nginx gunicorn libmysqlclient-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/log/django/ && \
    touch /var/log/django/django.log && \
    chown -R root:root /var/log/django
    

# Set work directory
WORKDIR /var/www/html/

# Copy requirements.txt and install requirements
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy source code to work directory
COPY . .

# Change owner and group for the html directory
RUN chown -R www-data:www-data /var/www/html

WORKDIR /var/www/html/mysite

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled

# Expose port 80 for Nginx
EXPOSE 80

# Start Gunicorn and Nginx
CMD exec /bin/bash -c "service nginx start; gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --chdir/var/www/html/mysite"
