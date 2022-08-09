# syntax=docker/dockerfile:experimental
#
# ^ the above line is necessary for 'RUN --mount=type=ssh' below, which in turn
# enables using private git repositories in builds.

FROM python:3.9

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONPATH=/app


WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .
EXPOSE 8000:8000
# USER app
# ENTRYPOINT [ "/rodeo/entrypoint" ]
# Run the application in the port 8000
# CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app:app"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0",  "--port", "8000", "--reload"]