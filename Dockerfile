FROM node:18-alpine

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

WORKDIR /app

COPY package*.json ./

RUN if [ "$NODE_ENV" = "production" ]; then \
        npm ci --only=production; \
    else \
        npm install; \
    fi

COPY . .

RUN if [ "$NODE_ENV" = "production" ]; then \
        npm run build; \
    fi

EXPOSE 3000

CMD if [ "$NODE_ENV" = "production" ]; then \
        npm run start; \
    else \
        npm run dev; \
    fi
