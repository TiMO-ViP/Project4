# Multi-Stage Production & Development Dockerfile
FROM node:24-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production 2>/dev/null || true

FROM base AS runner
WORKDIR /app
ENV NODE_ENV=production
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
