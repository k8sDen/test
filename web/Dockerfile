FROM node:18.17.1-bullseye as builder

RUN apt-get update
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.18.0-alpine

COPY --from=builder /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
ENTRYPOINT ["nginx","-g","daemon off;"]
