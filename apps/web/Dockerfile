FROM node:20-slim

WORKDIR /app

COPY apps/web/package*.json /app/

RUN if [ -f package-lock.json ]; then npm ci; else npm install; fi

COPY apps/web /app

ENV NODE_ENV=production

RUN npm run build

CMD ["npm", "run", "start"]
