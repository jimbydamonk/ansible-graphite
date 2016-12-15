# ansible-libselinux-python
[![Build Status](https://travis-ci.org/jimbydamonk/ansible-graphite.svg?branch=master)](https://travis-ci.org/jimbydamonk/ansible-graphite)
This role installs graphite on Debian and RedHat systems.


Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

The default variables for this role are listed below. They are defined in defaults/main.yml`.

```yml
---

---
graphite_dir: "{{ dist_graphite_dir }}" #Check the OS file in vars
graphite_webapp: "{{ graphite_dir }}/webapp"
graphite_conf_dir: "{{ graphite_dir }}/conf"
graphite_storage_dir: "{{ graphite_dir }}/storage"
graphite_content_dir: "/usr/local/webapp/content"

graphite_rrd_dir: /var/lib/carbon/rrd
graphite_log_dir: /var/log/graphite-web/
graphite_index: '{{ graphite_storage_dir }}/index'

graphite_version: latest
graphite_use_nginx: true
graphite_secret_key: "SECRET_KEY"
graphite_host: localhost
graphite_port: 80
graphite_scheme: http
graphite_url: "{{ graphite_scheme }}://{{ graphite_host }}:{{ graphite_port }}"

graphite_uwsgi_sock_dir: /var/uwsgi
graphite_uwsgi_sock: '{{ graphite_uwsgi_sock_dir }}/graphite_uwsgi.sock'
graphite_uwsgi_pid: '{{ graphite_uwsgi_sock_dir }}/graphite_uwsgi.pid'

django_dir: "{{ dist_django_dir }}" #Check the proper file in vars

whisper_dir: /media/metrics/whisper/

whisper_cron_jobs:
  - name: "Remove old whisper data"
    cron_file: ansible_whisper_data_cleanup
    weekday: 0
    user: root
    job: "find {{ whisper_dir }} -type f -mtime +60 -name \\*.wsp -delete >> /var/log/ansible_whisper_data_cleanup.log 2>&1"

  - name: "Remove empty whisper dirs"
    cron_file: ansible_whisper_dir_cleanup
    user: root
    weekday: 0
    job: "find {{ whisper_dir }} -depth -type d -empty -delete >> /var/log/ansible_whisper_dir_cleanup.log 2>&1"


```

Dependencies
------------

- bobbyrenwick.pip
- jimbydamonk.ansible-libselinux-python
- cchurch.uwsgi
- geerlingguy.repo-epel (only for RedHat)
- geerlingguy.nginx

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache

Author Information
------------------
Mike Buzzetti
