# Use the official Nginx image as the base image
FROM nginx:alpine

# Copy the HTML files and CSS into the Nginx server
COPY html /usr/share/nginx/html

# Expose port 80
EXPOSE 80

