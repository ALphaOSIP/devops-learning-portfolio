FROM python:3.13.4-slim
WORKDIR /app
COPY app.py .
EXPOSE 8000
CMD ["python", "app.py"]