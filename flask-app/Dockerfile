FROM ubuntu:22.04

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    curl gnupg2 lsb-release ca-certificates \
    nginx python3 python3-pip git

# Install Anchore scan tool
# Flask
COPY requirements.txt .
RUN pip install -r requirements.txt && \
    curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin && \
    curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin

COPY . /workspace
CMD ["python3", "server.py"]
