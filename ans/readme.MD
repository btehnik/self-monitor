### Ansible Infrastructure repository structure
```
inventories/
   production/
      hosts               # inventory file for production servers
      environment_vars/   
        environment1      # helper environment wide variables
        environment2
      group_vars/
         group1           # here we assign variables to particular groups
         group2           # ""
      host_vars/
         hostname1        # if systems need specific variables, put them here
         hostname2        # ""

   staging/
      hosts               # inventory file for staging environment
      group_vars/
         group1           # here we assign variables to particular groups
         group2           # ""
      host_vars/
         stagehost1       # if systems need specific variables, put them here
         stagehost2       # ""

library/
filter_plugins/

playbooks/
   site.yml
   webservers.yml
   dbservers.yml

roles/
    common/
    webtier/
    monitoring/
    fooapp/
```



###### Style guide
[** Ansible Infrastructure repo style guide **](doc/styleguide.md)



###### Playbook run
* [**Playbook run**](playbooks/README.md) - Info about playbooks available and how to use them


---

###### Supported operation systems

* Ubuntu 16.x xenial
* CentOS 7
* Debian8 jessie64

---
### Run playbook prepare_host
Run palybook
```
ansible-playbook -i inventory/testing/testing.ini playbooks/prepare_host.yml -u root --ask-pass #for CentOS
ansible-playbook -i inventory/testing/testing.ini playbooks/prepare_host.yml -u ubuntu --ask-pass --sudo #for Ubuntu
```
---
### Run playbook bootstrap_node
Run palybook
```
ansible-playbook -i inventory/testing/testing.ini playbooks/bootstrap_node.yml -u root --ask-pass #for CentOS
ansible-playbook -i inventory/testing/testing.ini playbooks/bootstrap_node.yml -u root --ask-pass --sudo #for Ubuntu
```
---
### Run playbook user-management
Run palybook
```
ansible-playbook -i inventory/testing/testing.ini playbooks/user-management.yml -u $your_user
---
```
###### Tested on

* ansible 2.2.0.0

---

### Authors

DevOps Ukraine Team (devops-ukraine@heg.com)

---
