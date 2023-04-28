FROM nginx
WORKDIR /usr/share/nginx/html/
USER root
COPY default.conf /etc/nginx/conf.d/default.conf
COPY ./dist  /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
