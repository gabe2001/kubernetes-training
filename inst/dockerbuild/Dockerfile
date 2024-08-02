FROM alpine:latest

MAINTAINER ITGilde <info@itgilde.nl>

RUN apk add --update nginx \
 && mkdir /run/nginx

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
