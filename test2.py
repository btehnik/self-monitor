import argparse
argv_parser = argparse.ArgumentParser(description="Spin-up vagrant host and setup Grafana, MySQL, Apache, Graphite, Collectd")
argv_parser.add_argument("-a", "--argument", help="'init', 'start', 'stop', 'destroy' ")
args = vars(argv_parser.parse_args())

if args['argument'] and 'init' in args['argument']:
    print ("init")
elif args['argument'] and 'start' in args['argument']:
    print("start")
elif args['argument'] and 'stop' in args['argument']:
    print("stop")
elif args['argument'] and 'destroy' in args['argument']:
    print("destroy")
else:
    print("\n Use key '-a' and argument: \n 'init' for run vm with all staffs \n 'start' for start vm if it's already created \n 'stop' for stop vm \n 'destroy' fpr destroy vm \n")