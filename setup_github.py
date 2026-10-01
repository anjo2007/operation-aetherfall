#!/usr/bin/env python3
"""
OPERATION AETHERFALL // GITHUB REPOSITORY & ISSUES SETUP SCRIPT
Nexus Dynamics Investigation

This script automates:
1. Setting up the Git commit history with realistic timestamps, authors, and deleted token.
2. Creating a public/private GitHub repository via `gh` CLI (if selected).
3. Populating GitHub issues (including Issue #18 with LOOK/@ghost_in_stack and Issue #42).
"""

import os
import subprocess
import sys
import time

def run(cmd, env=None):
    res = subprocess.run(cmd, shell=True, text=True, capture_output=True, env=env)
    if res.returncode != 0:
        print(f"[-] Command failed: {cmd}\n[-] Error: {res.stderr}")
    return res

def setup_git_history():
    print("[*] Initializing local Git repository with chronological lore commits...")
    
    # Backup current files before staging
    main_py_final = open("main.py", "r", encoding="utf-8").read()
    
    run("git init")
    run("git config user.name \"Dr. Elena Rostova\"")
    run("git config user.email \"e.rostova@nexusdynamics.internal\"")
    
    # Commit 1: Initial creation of main.py
    commit1_main = """# ==============================================================================
# PROJECT AETHER ARCHIVE - SYSTEM DAEMON
# Nexus Dynamics | Cyber Defense Division
# Author: Dr. Elena Rostova (Lead Security Specialist)
# ==============================================================================

import sys
import os
import time

SERVER_WIPE_ACTIVE = False
TARGET_NODE = "AETHER-09"
"""
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(commit1_main)
        
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = "Dr. Elena Rostova"
    env["GIT_AUTHOR_EMAIL"] = "e.rostova@nexusdynamics.internal"
    env["GIT_AUTHOR_DATE"] = "2026-09-24T14:15:00"
    env["GIT_COMMITTER_NAME"] = "Dr. Elena Rostova"
    env["GIT_COMMITTER_EMAIL"] = "e.rostova@nexusdynamics.internal"
    env["GIT_COMMITTER_DATE"] = "2026-09-24T14:15:00"
    
    run("git add main.py", env=env)
    run("git commit -m \"feat: initial commit for Project Aether Archive core modules\"", env=env)

    # Commit 2: Dr. Elena Rostova adds emergency failsafe recovery token
    commit2_main = """# ==============================================================================
# PROJECT AETHER ARCHIVE - SYSTEM DAEMON
# Nexus Dynamics | Cyber Defense Division
# Author: Dr. Elena Rostova (Lead Security Specialist)
# ==============================================================================

import sys
import os
import time

# ==============================================================================
# EMERGENCY SYSTEM RECOVERY HOOK
# recovery token: AETHER_
# Author: Dr. Elena Rostova
# ==============================================================================

SERVER_WIPE_ACTIVE = True
TARGET_NODE = "AETHER-09"
"""
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(commit2_main)
        
    env["GIT_AUTHOR_NAME"] = "Dr. Elena Rostova"
    env["GIT_AUTHOR_EMAIL"] = "e.rostova@nexusdynamics.internal"
    env["GIT_AUTHOR_DATE"] = "2026-09-28T17:40:00"
    env["GIT_COMMITTER_NAME"] = "Dr. Elena Rostova"
    env["GIT_COMMITTER_EMAIL"] = "e.rostova@nexusdynamics.internal"
    env["GIT_COMMITTER_DATE"] = "2026-09-28T17:40:00"
    
    run("git add main.py", env=env)
    run("git commit -m \"sec: add emergency failsafe recovery hook and telemetry watchdog\"", env=env)

    # Commit 3: John Vance removes the token and adds Note: The morning backup is incomplete.
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(main_py_final)
        
    env["GIT_AUTHOR_NAME"] = "John Vance"
    env["GIT_AUTHOR_EMAIL"] = "j.vance@nexusdynamics.internal"
    env["GIT_AUTHOR_DATE"] = "2026-10-01T23:10:00"
    env["GIT_COMMITTER_NAME"] = "John Vance"
    env["GIT_COMMITTER_EMAIL"] = "j.vance@nexusdynamics.internal"
    env["GIT_COMMITTER_DATE"] = "2026-10-01T23:10:00"
    
    run("git add main.py", env=env)
    run("git commit -m \"refactor: morning backup sync - sanitized security tokens and logs\"", env=env)

    # Commit 4: Dr. Elena Rostova stages emergency forensic evidence
    env["GIT_AUTHOR_NAME"] = "Dr. Elena Rostova"
    env["GIT_AUTHOR_EMAIL"] = "e.rostova@nexusdynamics.internal"
    env["GIT_AUTHOR_DATE"] = "2026-10-02T01:25:00"
    env["GIT_COMMITTER_NAME"] = "Dr. Elena Rostova"
    env["GIT_COMMITTER_EMAIL"] = "e.rostova@nexusdynamics.internal"
    env["GIT_COMMITTER_DATE"] = "2026-10-02T01:25:00"
    
    run("git add evidence_04 evidence_board.png cam04_frame.png phone_log.txt stage2_vault.zip lab_photo.png floor_blueprint.png system_diagnostics.log issues/", env=env)
    run("git commit -m \"CRITICAL: Stage emergency evidence archive and forensic snapshot\"", env=env)

    # Commit 5: Sentinel-AI Daemon locks down system
    env["GIT_AUTHOR_NAME"] = "SENTINEL-AI Daemon"
    env["GIT_AUTHOR_EMAIL"] = "sentinel@nexusdynamics.internal"
    env["GIT_AUTHOR_DATE"] = "2026-10-02T01:50:00"
    env["GIT_COMMITTER_NAME"] = "SENTINEL-AI Daemon"
    env["GIT_COMMITTER_EMAIL"] = "sentinel@nexusdynamics.internal"
    env["GIT_COMMITTER_DATE"] = "2026-10-02T01:50:00"
    
    run("git add README.md terminal.py index.html MASTER_ANSWER_KEY.md setup_github.py generate_all_assets.py", env=env)
    run("git commit -m \"LOCKDOWN: Unauthorized terminal breach detected - server wipe countdown armed\"", env=env)

    print("[+] Git commit history successfully created.")
    log = run("git log --oneline").stdout
    print("[*] Current git log:\n" + log)

def push_to_github(repo_name="operation-aetherfall", is_public=True):
    print(f"[*] Checking GitHub CLI status...")
    auth_check = run("gh auth status")
    if auth_check.returncode != 0:
        print("[-] GitHub CLI is not authenticated. Please run: gh auth login")
        return False

    visibility = "--public" if is_public else "--private"
    print(f"[*] Creating remote repository '{repo_name}' on GitHub ({visibility})...")
    create_res = run(f"gh repo create {repo_name} {visibility} --source=. --remote=origin --push")
    if create_res.returncode == 0:
        print(f"[+] Repository created and pushed successfully to GitHub!")
        return True
    else:
        print(f"[!] Repo creation output: {create_res.stderr or create_res.stdout}")
        return False

def populate_github_issues():
    print("[*] Populating sequential GitHub issues (1 to 42)...")
    
    # Issue 1 to 17: Closed maintenance tickets
    for i in range(1, 18):
        title = f"Routine Subsystem Audit Ticket #{i:02d}"
        body = f"Automated maintenance routine check #{i} completed for Building B subnet."
        run(f"gh issue create --title \"{title}\" --body \"{body}\"")
        run(f"gh issue close {i}")
        time.sleep(0.5)

    # Issue 18: Camera 04: access report
    issue_18_body = """### Automated Camera 04 Access Log

**Security Sensor Audit - October 2, 2026**

@ghost_in_stack commented:
**L**ogged unauthorized peripheral ping at 01:14 AM.  
**O**verride sequence originated from external gateway.  
**O**bserve the answer to life, the universe, and everything.  
**K**eep your eyes on the central reconciliation channel.  

*(Notice: The truth lies where life, the universe, and everything converge.)*
"""
    run(f"gh issue create --title \"Camera 04: access report\" --body \"{issue_18_body}\"")
    print("[+] Created Issue #18: Camera 04: access report")

    # Issue 19 to 41: Closed tickets
    for i in range(19, 42):
        title = f"Internal Network Ticket #{i:02d}"
        body = f"Gateway routing table verification #{i} logged."
        run(f"gh issue create --title \"{title}\" --body \"{body}\"")
        run(f"gh issue close {i}")
        time.sleep(0.5)

    # Issue 42: Investigation Reconciliation: Security Audit #42
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
    run(f"gh issue create --title \"Investigation Reconciliation: Security Audit #42\" --body \"{issue_42_body}\"")
    print("[+] Created Issue #42: Investigation Reconciliation: Security Audit #42")

if __name__ == "__main__":
    setup_git_history()
    if len(sys.argv) > 1 and sys.argv[1] == "--push":
        repo_name = sys.argv[2] if len(sys.argv) > 2 else "operation-aetherfall"
        if push_to_github(repo_name):
            populate_github_issues()
