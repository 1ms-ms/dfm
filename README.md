# dfm
ansible-playbook server.yml -e @config_file.yml
```
.
├── ansible.cfg
├── ansible.pem
├── config.sql
├── config_file.yml
├── roles
│   ├── docker
│   │   └── tasks
│   │       └── main.yml
│   ├── maria_db
│   │   ├── tasks
│   │   │   └── main.yml
│   │   └── templates
│   │       └── template.j2
│   └── server
│       └── tasks
│           └── main.yml
└── server.yml
```

