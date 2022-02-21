#!/usr/bin/ansible-playbook --ask-vault-pass
---
# Install and setup local env

-  hosts: localhost
   gather_facts: false
   become: yes
##   ignore_errors: yes
#   vars_prompt:
#     - name: "configure_iplayer"
#       prompt: "setup get_iplayer?"

   tasks:
     - name: install deps
       include: deps.yml
       tags: deps

     - name: install services
       include: services.yml

     - name: install docker # ansible 2.8 or newer
       include: docker.yml

     - name: install ufw
       include: ufw.yml
