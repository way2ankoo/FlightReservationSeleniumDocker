FROM python:3.11-slim

# Install curl jq
RUN apt-get update && apt-get install -y curl jq

# workspace
WORKDIR /app

#copy requirements.txt
COPY requirements.txt .

# install packages
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of the files and code
COPY . .

# set environment variables
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["pytest"]
# CMD ["pytest", "test/", "--maxfail=5", "--disable-warnings"]