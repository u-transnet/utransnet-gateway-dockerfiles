FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
RUN mkdir /src
RUN mkdir /public
RUN mkdir /public/static
RUN mkdir /public/media
RUN git clone -b dev https://github.com/u-transnet/utransnet-gateway /src
ADD /config/settings.py /src/settings/local.py
ADD /config/create_admin_user.py /src/create_admin_user.py
RUN pip install gunicorn
RUN pip install psycopg2
WORKDIR /src
RUN python3 create_pip_requirements.py
RUN pip install -r requirements.txt
