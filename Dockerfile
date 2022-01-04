FROM python:3

# setup environment
ENV FLASK_APP=app.py
ENV FLASK_HOST=0.0.0.0
ENV FLASK_ENV=production
# ENV SECRET_KEY="development key"
# ENV DATABASE_URI="sqlite:///:memory:"

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# cache required nltk data in separate build layer
COPY words.py ./
RUN python words.py

# copy application files
COPY . .

# use a production web server
RUN pip install gunicorn
CMD ["python", "-m", "gunicorn", "--workers=2", "--threads=4", "--worker-class=gthread", "--log-file=-", "--worker-tmp-dir", "/dev/shm", "--bind", "0.0.0.0:8000","app:app"]
