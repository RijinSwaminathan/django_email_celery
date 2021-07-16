# django_email_celery
Implement the project with celery and rabbitmq as the message brocker

# 1. The steps to follow

# 2. Install rabbitmq server
sudo apt-get install rabbitmq-server

# 3. Enable rabbitmq
sudo systemctl enable rabbitmq-server

# 4. Start rabbitmq
sudo systemctl start rabbitmq-server

# 5. Status of rabbitmq
systemctl status rabbitmq-server

# 6. Install celery with the environment
pip install celery

# 7. Create a file in your project directory with name celery.py

# 8. Run celery instance
celery -A projectname worker -l info

# 9. stop rabbitmq server
sudo rabbitmqctl stop


