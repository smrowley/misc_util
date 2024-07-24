from ansible.module_utils.basic import AnsibleModule
import websocket
import ssl
import time

def send_key_event(ws, key, state, sleep_time):
    ws.send('{"event_type": "key", "event": {"key": "%s", "state": %s}}' % (key, str(state).lower()))
    time.sleep(sleep_time)

def run_module():
    module_args = dict(
        uri=dict(type='str', required=True),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True),
        sleep_time=dict(type='float', required=False, default=0.05),
        send_details=dict(type='list', required=True, elements='dict')
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    uri = module.params['uri']
    user = module.params['user']
    password = module.params['password']
    sleep_time = module.params['sleep_time']
    send_details = module.params['send_details']

    headers = {"X-KVMD-User": user, "X-KVMD-Passwd": password}

    try:
        ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
        ws.connect(uri, header=headers)

        for detail in send_details:
            key = detail.get('key')
            state = detail.get('state')
            send_key_event(ws, key, state, sleep_time)

        ws.close()
        result['changed'] = True
        result['message'] = 'Key events sent successfully'
    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()