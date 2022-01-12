FROM python:3

# setup environment
ENV FLASK_APP=app.py
ENV FLASK_HOST=0.0.0.0
ENV FLASK_ENV=production
# ENV SECRET_KEY="development key"
# ENV DATABASE_URI="sqlite:///:memory:"
SHELL ["/bin/bash", "-c"]

COPY . .

# install dependencies
RUN pip install -r requirements.txt

# download required nltk data
RUN cat nltk.txt | xargs python -m nltk.downloader

# use a production web server
CMD ["python", "-m", "gunicorn", "--workers=2", "--threads=4", "--worker-class=gthread", "--log-file=-", "--worker-tmp-dir", "/dev/shm", "--bind", "0.0.0.0:8000","app:app"]
