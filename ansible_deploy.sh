#!/usr/local/bin/ansible-playbook --ask-vault-pass
---
# Install and setup local env

-  hosts: localhost
   gather_facts: false
   become: yes
##   ignore_errors: yes
   vars_prompt:
     - name: "configure_iplayer"
       prompt: "setup get_iplayer?"

   tasks:
     - name: install iplayer
       include: get_iplayer.yml
       when: configure_iplayer.0 is defined

     - name: install deps
       include: deps.yml
       tags: deps

     - name: install services
       include: services.yml

     - name: install rclone
       include: rclone.yml
