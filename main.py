from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

def handler(request, response):
    # For the root path, serve index.html
    if request.path == '/' or request.path == '/index.html':
        try:
            with open('index.html', 'rb') as f:
                response.status_code = 200
                response.headers['Content-Type'] = 'text/html'
                return response.send(f.read())
        except FileNotFoundError:
            response.status_code = 404
            return response.send('File not found')

    # For static files in public directory
    if request.path.startswith('/assets/'):
        file_path = os.path.join('public', request.path[1:])
        try:
            with open(file_path, 'rb') as f:
                content_type = get_content_type(file_path)
                response.status_code = 200
                response.headers['Content-Type'] = content_type
                return response.send(f.read())
        except FileNotFoundError:
            response.status_code = 404
            return response.send('File not found')

    # Default 404 response
    response.status_code = 404
    return response.send('Not found')

def get_content_type(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    content_types = {
        '.html': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.ico': 'image/x-icon'
    }
    return content_types.get(extension, 'application/octet-stream') 