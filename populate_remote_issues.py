import subprocess
import time
import sys

REPO = "anjo2007/operation-aetherfall"

def run(cmd):
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if res.returncode != 0:
        print(f"[-] Error running: {cmd[:60]}... -> {res.stderr.strip()}")
    return res

def main():
    print(f"[*] Starting GitHub issues generation for {REPO}...")
    
    # 1 to 17
    for i in range(1, 18):
        title = f"Security Audit Check #{i:02d}: Facility Routine Verification"
        body = f"Automated background maintenance routine verification #{i} completed for Building B subnet."
        res = run(f'gh issue create --repo {REPO} --title "{title}" --body "{body}"')
        print(f"[+] Created #{i}: {res.stdout.strip()}")
        run(f'gh issue close {i} --repo {REPO}')
        time.sleep(0.4)

    # Issue 18: Camera 04: access report
    issue_18_title = "Camera 04: access report"
    issue_18_body = """### Automated Camera 04 Access Log

**Security Sensor Audit - October 2, 2026**

@ghost_in_stack commented:
**L**ogged unauthorized peripheral ping at 01:14 AM.  
**O**verride sequence originated from external gateway.  
**O**bserve the answer to life, the universe, and everything.  
**K**eep your eyes on the central reconciliation channel.  

*(Notice: The truth lies where life, the universe, and everything converge.)*
"""
    with open("temp_issue18.md", "w", encoding="utf-8") as f:
        f.write(issue_18_body)
    res = run(f'gh issue create --repo {REPO} --title "{issue_18_title}" --body-file temp_issue18.md')
    print(f"[+] Created Issue #18: {res.stdout.strip()}")
    time.sleep(0.4)

    # 19 to 41
    for i in range(19, 42):
        title = f"Perimeter Gateway Log #{i:02d}: Relay Synchronized"
        body = f"Routing table telemetry verification #{i} verified and archived."
        res = run(f'gh issue create --repo {REPO} --title "{title}" --body "{body}"')
        print(f"[+] Created #{i}: {res.stdout.strip()}")
        run(f'gh issue close {i} --repo {REPO}')
        time.sleep(0.4)

    # Issue 42: Investigation Reconciliation: Security Audit #42
    issue_42_title = "Investigation Reconciliation: Security Audit #42"
    issue_42_body = """# Investigation Reconciliation: Security Audit #42

Reconciliation audit thread for perimeter breach and workstation disappearance event in Room 304.

### Intercepted Messaging Log (Company Chat - General Security Operations)
```
@elena.r: Has anyone noticed the unusual outgoing internet activity on server AETHER-09?

@jvance: Probably just automated system updates, Elena. Don't worry about it. Go home.

@elena.r: System updates don't send 40GB of hidden data to an unknown location, John.

@mlin: Hey team, the security system flagged unauthorized access in Lab 304 at 10:15 PM. Who is in the building?

@jvance: I swiped in briefly to grab my jacket. Badge ID 9042. Everything is fine.

@elena.r: If anything happens to my workstation tonight, check the online project files. I left a safety net in main.py.

@sentinel-ai: [WARNING] User @elena.r disconnected unexpectedly.
```

### Reconciled Access Telemetry:
- **Incident Date Verified in Room Ledger:** `OCT 2`
- **Security Access Badge Identified:** `9042` (Belongs to Senior Engineer John Vance)
- **Breach Facility Location:** `Room 304` (Building B, Cyber Defense Lab)

> *Investigator Protocol Reminder:*  
> *The timer accepts the order used by the incident report.*  
> *(Incident Report standard registry format: Date Token -> Badge ID -> Room ID)*
"""
    with open("temp_issue42.md", "w", encoding="utf-8") as f:
        f.write(issue_42_body)
    res = run(f'gh issue create --repo {REPO} --title "{issue_42_title}" --body-file temp_issue42.md')
    print(f"[+] Created Issue #42: {res.stdout.strip()}")
    
    # Clean up temp files
    import os
    if os.path.exists("temp_issue18.md"): os.remove("temp_issue18.md")
    if os.path.exists("temp_issue42.md"): os.remove("temp_issue42.md")
    print("[*] All remote GitHub issues created successfully!")

if __name__ == "__main__":
    main()
