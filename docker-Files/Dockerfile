FROM python:3.10.4-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install -r reqirements.txt
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5\
		CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOiNT ["python","./src/assigement.py"]