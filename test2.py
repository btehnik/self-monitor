# import argparse
# argv_parser = argparse.ArgumentParser(description="Spin-up vagrant host and setup Grafana, MySQL, Apache, Graphite, Collectd")
# argv_parser.add_argument("-a", "--argument", help="'init', 'start', 'stop', 'destroy' ")
# args = vars(argv_parser.parse_args())

# if args['argument'] and 'init' in args['argument']:
#     print ("init")
# elif args['argument'] and 'start' in args['argument']:
#     print("start")
# elif args['argument'] and 'stop' in args['argument']:
#     print("stop")
# elif args['argument'] and 'destroy' in args['argument']:
#     print("destroy")
# else:
#     print("\n Use key '-a' and argument: \n 'init' for run vm with all staffs \n 'start' for start vm if it's already created \n 'stop' for stop vm \n 'destroy' fpr destroy vm \n")

import os

file = os.path.expanduser("~/Documents/mine/self-monitor/tmp")

def conf():
    fl = open(file, "a")
    a = fl.write('\n  config.vm.define "just-test" do |t|\n  end\n config.vm.provider "virtualbox" do |v|\n    v.name = "just-test"\n \
 end\nconfig.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1" \n\
config.vm.network "forwarded_port", guest: 3000, host: 3000, host_ip: "127.0.0.1" \n\
config.vm.network "forwarded_port", guest: 443, host: 443, host_ip: "127.0.0.1" \n\
config.vm.network "forwarded_port", guest: 80, host: 80, host_ip: "127.0.0.1"\nend')
    fl.close()
    print ("\n Done \n")

conf()