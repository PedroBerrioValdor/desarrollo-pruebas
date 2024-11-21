FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000"]