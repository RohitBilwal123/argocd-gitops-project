FROM python:3.12-slim

WORKDIR /app

COPY app.py .

ENV PORT=8080
EXPOSE 8080

USER 10001:10001

CMD ["python", "-u", "app.py"]
