import datetime
import random
import time

USERS = ["admin", "root", "goutham", "svc_deploy", "testuser"]
IPS = ["192.168.1.50", "10.0.0.15", "185.220.101.5", "192.168.1.105"]

def generate_log():
    timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
    event_type = random.choices(["SUCCESS", "FAILED_LOGIN", "PRIV_ESC"], weights=[0.6, 0.3, 0.1])[0]
    user = random.choice(USERS)
    ip = random.choice(IPS)

    if event_type == "FAILED_LOGIN":
        return f"{timestamp} my-domain-dc Workstation: WIN-DC01 EventID: 4625 Status: Audit Failure User: {user} SourceIP: {ip} Reason: Unknown user name or bad password."
    elif event_type == "PRIV_ESC":
        return f"{timestamp} my-domain-dc Workstation: WIN-DC01 EventID: 4672 Status: Audit Success User: {user} Privileges: SeDebugPrivilege Assigned."
    else:
        return f"{timestamp} my-domain-dc Workstation: WIN-DC01 EventID: 4624 Status: Audit Success User: {user} SourceIP: {ip} Authentication Package: Kerberos."

if __name__ == "__main__":
    with open("auth_events.log", "a") as f:
        for _ in range(50):
            log_entry = generate_log()
            print(log_entry)
            f.write(log_entry + "\n")
            time.sleep(0.1)