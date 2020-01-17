import sys
import os
import getopt

fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]

print (argumentList)

options = ["init", "start", "stop"]

try:
    arguments, values = getopt.getopt(argumentList, options)
except getopt.error as err:
    print (str(err))
    sys.exit(2)

# path = os.path.expanduser("~/test1")

def createvm():

    # try:
    #     os.makedirs(path)
    # except OSError:
    #     print ("\n", "Create directory %s failed" % path, "\n")
    # else:
    #     print ("\n", "Successfully created directory %s" % path, "\n")

    # cmd1 = 'cd ~/test1 && cp ~/v v'
    # os.system(cmd1)

    # file = os.path.expanduser("~/test1")

    # readFile = open(file)
    # lines = readFile.readlines()
    # readFile.close()
    # w = open(file,'w')
    # w.writelines([item for item in lines[:-2]])
    # w.close()

    # fl = open(file, "a")
    # a = fl.write('\n  config.vm.define "ubuntu-test" do |t|\n  end\n config.vm.provider "virtualbox" do |v|\n    v.name = "ubuntu-test"\n  end\nend')
    # fl.close()
    print ("function was run")
    

#createvm()
for currentArgument in arguments:
    if currentArgument=='init':
        createvm()
        print("It's INIT!")
    elif currentArgument=="start":
        print("args=start")
    elif currentArgument=="stop":
        print("args=stop")