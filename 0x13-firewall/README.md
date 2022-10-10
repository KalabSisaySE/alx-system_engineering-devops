# 0x13. Firewall

In this project i have installed `ufw`(Uncomlicated firewall) on `web-01` and `web-02` servers and on the loadbalancer `lb-01`.

## [Task-0](./0-block_all_incoming_traffic_but) (Block all incoming traffic but)

- Installs and configures `ufw` so that it blocks all incoming traffic, except the following TCP ports: 22 (SSH), 443 (HTTPS SSL), 80 (HTTP).

## [Task-1](./100-port_forwarding) (Port forwarding)

- Configures `web-01` so that its firewall redirects port 8080/TCP to port 80/TCP.

