FROM python:3.10.6

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 9006

CMD ["python", "manage.py", "runserver", "0.0.0.0:9006"]


# Step to Create docker images 

# docker build --tag claim_assure:latest .
# docker image ls
# docker run --name claim_assure -d -p 8000:8000 claim_assure:latest
# docker container ps