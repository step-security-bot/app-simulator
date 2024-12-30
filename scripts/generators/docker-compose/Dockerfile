# Use a lightweight Python base image
FROM python:3.14-alpine

WORKDIR /app

RUN apk addgroup -S appgroup && adduser -S appuser -G appgroup

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY createComposeFile.py .

RUN chown -R appuser:appgroup /app && chmod +x createComposeFile.py
USER appuser

# Define the default entrypoint to run the script
ENTRYPOINT ["python", "createComposeFile.py"]
