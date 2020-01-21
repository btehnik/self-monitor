import os
import argparse

def init():
    path = os.path.expanduser("~/vgrnt/ubuntu-test1")
    try:
        os.makedirs(path)
    except OSError:
     print ("\n", "Create directory %s failed. Maybe it exists already." % path, "\n")
    else:
     print ("\n", "Successfully created directory %s" % path, "\n")
    cmd0 = 'vagrant box add bento/ubuntu-16.04 --force && cd ~/vgrnt/ubuntu-test1 && vagrant init bento/ubuntu-16.04'
    os.system(cmd0)
    print ("\n VM was created \n")

def conf():
    file = os.path.expanduser("~/vgrnt/ubuntu-test1/Vagrantfile")
    readFile = open(file)
    lines = readFile.readlines()
    readFile.close()
    w = open(file,'w')
    w.writelines([item for item in lines[:-2]])
    w.close()
    fl = open(file, "a")
    a = fl.write('\n  config.vm.define "ubuntu-test" do |t|\n  end\n config.vm.provider "virtualbox" do |v|\n    v.name = "ubuntu-test"\n \
 end\nconfig.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1" \n\
config.vm.network "forwarded_port", guest: 3000, host: 3000, host_ip: "127.0.0.1" \n\
config.vm.network "forwarded_port", guest: 443, host: 4430, host_ip: "127.0.0.1" \n\
config.vm.network "forwarded_port", guest: 80, host: 80, host_ip: "127.0.0.1"\nend')
    fl.close()
    cmd1 = 'cd ~/vgrnt/ubuntu-test1/ && vagrant up'
    os.system(cmd1)
    print ("\n VM was configured and is up \n")

argv_parser = argparse.ArgumentParser(description="Spin-up vagrant host and setup Grafana, MySQL, Apache, Graphite, Collectd. \n Example: \n 'python3 test.py -a stop' ")
argv_parser.add_argument("-a", "--argument", help="Argumets: 'init', 'start', 'stop', 'destroy'")
args = vars(argv_parser.parse_args())

if args['argument'] and 'init' in args['argument']:
    init()
    conf()
    cmd2 = 'cd ~/Documents/mine/self-monitor/ans/ && ansible-playbook -e inventory/host_vars/vagrant.yml -i inventory/hosts.ini playbooks/gm.yml  --ask-pass'
    print ("\n Starting Ansible-playbook. Please, enter the password. \n Password = vagrant \n")
    os.system(cmd2)

elif args['argument'] and 'start' in args['argument']:
    cmd2 = 'cd ~/vgrnt/ubuntu-test1/ && vagrant up'
    os.system(cmd2)
elif args['argument'] and 'stop' in args['argument']:
    cmd3 = 'cd ~/vgrnt/ubuntu-test1/ && vagrant halt'
    os.system(cmd3)
elif args['argument'] and 'destroy' in args['argument']:
    cmd4 = 'cd ~/vgrnt/ubuntu-test1/ && vagrant destroy && rm -rf ~/vgrnt/'
    os.system(cmd4)
else:
    print("\n Use key '-a' and argument: \n 'init' for Run vm with all staffs \n 'start' for Start vm if it's already created \n 'stop' for Halt vm \n 'destroy' for Destroy vm \n")