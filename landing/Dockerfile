# Use an official Node.js runtime as the base image
FROM oven/bun:1.1

# Set the working directory
WORKDIR /app

# Install build dependencies for Turbopack
RUN apt-get update && apt-get install -y python3 make g++

# Copy package.json and bun.lock
COPY package*.json ./
COPY bun.lock ./

# Install dependencies using Bun
RUN bun install

# Copy the rest of the application
COPY . .

# Build the Next.js application
RUN bun run build

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["bun", "run", "start"]