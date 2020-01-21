# Self-monitoring script


This script install VM in VirtualBox with next ports forwarding:
- 8080 - http port for graphite.
- 4430 - https port for grafana via Apache reverse proxy (443 to 3000).
- 3000 - http port for grafana.

http://localhost:8080 - Graphite web interface.

https://localhost:4430/grafana/ - Grafana web intarface.

### Requirements
Please, do `git clone` in ~/Documents/

### Usage
`python3 self-monitoring.py -a 'argument' `

Ansible password = vagrant. 
Script will ask you about it and give hint during installation.

#### Argumets: 
- __init__ - Spin-up vagrant host with Ubuntu_16 in VirtualBox and configure Grafana, MySQL, Apache, Graphite, Collectd via ansible-playbook.
- __start__ - For runing `vagrant up`
- __stop__ - For runing `vagrant halt`
- __destroy__ - For runing `vagrant destroy` and removing vagrant directory

### Examples
`python3 self-monitor.py -a init` 

`python3 self-monitor.py -a stop` 

`python3 self-monitor.py -a start` 

`python3 self-monitor.py -a destroy` 

