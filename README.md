# dfm
docker run --network="host" --rm flask
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

