import os.path

path = os.path.expanduser("~/vgrnt/ubuntu-test1")

try:
    os.makedirs(path)
except OSError:
    print ("\n", "Create directory %s failed. Maybe it exists already." % path, "\n")
else:
    print ("\n", "Successfully created directory %s" % path, "\n")

cmd1 = 'vagrant box add bento/ubuntu-16.04 --force && cd ~/vgrnt/ubuntu-test1 && vagrant init bento/ubuntu-16.04'
os.system(cmd1)

file = os.path.expanduser("~/vgrnt/ubuntu-test1/Vagrantfile")

#print ("\n", "file =" , file, "\n")

readFile = open(file)
lines = readFile.readlines()
readFile.close()
w = open(file,'w')
w.writelines([item for item in lines[:-2]])
w.close()

fl = open(file, "a")
a = fl.write('\n  config.vm.define "ubuntu-test" do |t|\n  end\n config.vm.provider "virtualbox" do |v|\n    v.name = "ubuntu-test"\n  end\nend')
fl.close()
