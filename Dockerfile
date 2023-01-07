FROM alpine:3.17

# install node, python, postgres, and nginx
RUN apk add --no-cache postgresql
RUN apk add --no-cache nodejs
RUN apk add --no-cache python3
RUN apk add --no-cache nginx
RUN apk add --no-cache py3-pip
RUN apk add --no-cache npm

# configure postgres
RUN mkdir -p /run/postgresql
RUN chown -R postgres:postgres /run/postgresql

# configure nginx
RUN mkdir -p /run/nginx
RUN chown -R nginx:nginx /run/nginx

# install node dependencies
COPY ./frontend/package.json /frontend/package.json
WORKDIR /frontend
RUN npm install

# install python dependencies
COPY ./backend/requirements.txt /backend/requirements.txt
WORKDIR /backend
RUN pip install -r requirements.txt

# configure node
COPY ./frontend /frontend
WORKDIR /frontend
RUN npm run build

# configure django
ENV IS_DOCKER=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY ./backend /backend

# copy files
COPY ./backend /backend

WORKDIR /
COPY ./docker-entrypoint.sh /

CMD ["sh", "docker-entrypoint.sh"]