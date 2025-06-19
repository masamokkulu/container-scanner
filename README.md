# container-scanner
The tool to scan containers and mainstay SBOM and vulnerability list
## Quick Start
```
$ git clone https://github.com/masamokkulu/container-scanner.git
$ docker compose -f docker-compose.yaml up --build -d
```
Access `http://<ipaddress>:12345` from a browser once the container is up and running, and enter:
* Container Repository Name
  * e.g. `<REPO NAME>/<CONTAINER NAME>`
* Container Tag
  * e.g. `latest` `20250619`
* Git URL
