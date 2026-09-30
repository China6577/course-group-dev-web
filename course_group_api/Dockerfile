FROM python:3.12.3-slim

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt update && \
    apt install -y --no-install-recommends gcc pkg-config default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN /opt/venv/bin/python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-c", "/app/gunicorn_config.py", "course_group_api.wsgi:application"]
