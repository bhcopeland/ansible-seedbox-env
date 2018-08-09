#!/usr/bin/ansible-playbook --ask-vault-pass
---
# Install and setup local env

-  hosts: localhost
   gather_facts: false
   become: yes
##   ignore_errors: yes
   tasks:
     - name: install deps
       include: deps.yml
       tags: deps

     - name: install services
       include: services.yml
