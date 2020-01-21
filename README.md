# Self-monitoring script

### Requirements
Please, do 'git clone' in ~/Documents/ directory.

### Usage
python3 self-monitoring.py -a 'argument'
*** Argumets ***: 
- init - Spin-up vagrant host with Ubuntu_16 and configure Grafana, MySQL, Apache, Graphite, Collectd via nsible-playbook.
- start - For runing 'vagrant up'
- stop - For runing 'vagrant halt'
- destroy - For runing 'vagrant destroy'

This script install VM in VirtualBox with next ports forwarding:
8080 - http port for graphite.
4430 - https port for grafana.
3000 - http port for grafana.
http://localhost:8080 - Graphite web interface
https://localhost:8080/grafana/ - Grafana web intarface.

*** Example ***
'python3 self-monitor.py -a init'
