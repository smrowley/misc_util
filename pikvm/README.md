# Ansible Collection - misc_utils.pikvm

Documentation for the collection.

Example playbook usage:

```yaml
---
- name: Interact with WebSocket using custom module
  hosts: localhost
  tasks:
    - name: Send key events via WebSocket
      my_namespace.my_collection.kvmd_websocket:
        uri: "wss://10.0.0.7/api/ws?stream=0"
        user: "admin"
        password: "admin"
        sleep_time: 0.05
        send_details:
          - { key: "Enter", state: true }
          - { key: "Enter", state: false }
```
