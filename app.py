from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import datetime

class DevOpsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Joseph's DevOps Journey</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }}
                .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
                .highlight {{ color: #2196F3; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Joseph Prince - DevOps Engineer in Training</h1>
                <p><strong>Current Date:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>Container Status:</strong> <span class="highlight">Running Successfully!</span></p>
                <p><strong>Skills Developing:</strong> Docker, Linux, AWS, Kubernetes, CI/CD</p>
                <h3>Recent Achievements:</h3>
                <ul>
                    <li>✅ Enabled hardware virtualization</li>
                    <li>✅ Successfully installed Docker Desktop</li>
                    <li>✅ Created first containerized application</li>
                    <li>🔄 AWS Cloud Practitioner in progress</li>
                </ul>
                <p><em>This application is running in a Docker container!</em></p>
            </div>
        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    server = HTTPServer(("", port), DevOpsHandler)
    print(f"DevOps Learning Server running on port {port}")
    print(f"Visit: http://localhost:{port}")
    server.serve_forever()