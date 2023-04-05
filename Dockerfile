FROM python:3.9-slim-buster
WORKDIR /app
COPY ./Requirements.txt /app
RUN pip install -r Requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=server.py
CMD [ "python3" , "server.py"]