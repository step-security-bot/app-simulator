FROM python:3.13-alpine@sha256:b6f01a01e34091438a29b6dda4664199e34731fb2581ebb6fe255a2ebf441099

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY createManifests.py .

COPY templates ./templates
COPY deployments ./deployments

RUN chown -R appuser:appgroup /app && chmod +x createManifests.py
USER appuser

VOLUME [ "/app/deployments" ]

# Define the default entrypoint to run the script
ENTRYPOINT ["python", "createManifests.py"]
