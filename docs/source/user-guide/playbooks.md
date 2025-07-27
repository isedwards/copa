# Ansible Playbooks

`copa` seamlessly integrates with Ansible playbooks for configuration management and orchestration tasks.

## Playbook Integration

Any command in `toc.yml` that points to a `.yml` or `.yaml` file is executed as an Ansible playbook:

```yaml
commands:
  - deploy:
    - web: playbooks/deploy-web.yml
    - database: playbooks/deploy-db.yml
```

## Execution Method

`copa` uses `ansible-runner` to execute playbooks, providing:

- Clean execution environment
- Proper logging integration
- Error handling and reporting
- Output streaming

## Playbook Structure

Standard Ansible playbook structure works with `copa`:

```yaml
---
- name: Deploy web application
  hosts: web_servers
  become: yes
  
  vars:
    app_version: "{{ version | default('latest') }}"
    
  tasks:
    - name: Update application code
      git:
        repo: https://github.com/myorg/myapp.git
        dest: /opt/myapp
        version: "{{ app_version }}"
        
    - name: Template configuration file
      template:
        src: app.conf.j2
        dest: /etc/myapp/app.conf
      notify: restart app
      
  handlers:
    - name: restart app
      systemd:
        name: myapp
        state: restarted
```

## Jinja2 Templating

`copa` fully supports Ansible's Jinja2 templating capabilities:

### Variables
```yaml
vars:
  database_host: "{{ db_host | default('localhost') }}"
  debug_mode: "{{ environment == 'development' }}"
```

### Templates
```jinja2
# app.conf.j2
[database]
host = {{ database_host }}
port = {{ database_port | default(5432) }}

[app]
debug = {{ debug_mode | lower }}
log_level = {{ 'DEBUG' if debug_mode else 'INFO' }}
```

### Conditionals
```yaml
- name: Install development packages
  package:
    name: "{{ item }}"
  loop: "{{ dev_packages }}"
  when: environment == "development"
```

## Inventory Integration

`copa` works with standard Ansible inventory formats:

### Static Inventory
```ini
# inventory/hosts
[web_servers]
web1.example.com
web2.example.com

[db_servers]
db1.example.com

[all:vars]
ansible_user=deploy
```

### Dynamic Inventory
```python
#!/usr/bin/env python3
# inventory/dynamic.py
import json

inventory = {
    "web_servers": {
        "hosts": ["web1.example.com", "web2.example.com"]
    },
    "db_servers": {
        "hosts": ["db1.example.com"]
    }
}

print(json.dumps(inventory))
```

## Best Practices

### Playbook Organization
```
playbooks/
├── site.yml              # Main playbook
├── web.yml               # Web server playbook
├── database.yml          # Database playbook
├── group_vars/
│   ├── all.yml          # Variables for all hosts
│   └── web_servers.yml  # Variables for web servers
├── host_vars/
│   └── web1.example.com.yml  # Variables for specific host
└── templates/
    ├── nginx.conf.j2
    └── app.conf.j2
```

### Variable Management
- Use `group_vars/` for group-specific variables
- Use `host_vars/` for host-specific variables
- Keep sensitive data in Ansible Vault
- Use defaults in playbooks for fallback values

### Error Handling
```yaml
- name: Ensure service is running
  systemd:
    name: myapp
    state: started
  register: service_result
  failed_when: false
  
- name: Report service status
  debug:
    msg: "Service failed to start: {{ service_result.msg }}"
  when: service_result.failed
```

## Logging Integration

`copa` integrates playbook output with its logging system:

- Playbook tasks appear in Copa logs
- Verbosity levels control output detail
- Errors are captured and formatted consistently
- Debug information available with `-v`, `-vv` or `-vvv`
