# OPERATION AETHERFALL // MASTER ORGANIZER GUIDE & ANSWER KEY

**Organized by:** FOSS GECT (Free and Open Source Software Cell) × GECT Film Society  
**Institution:** Government Engineering College, Thrissur (GECT)  
**Target Competition Duration:** 2 Hours (02:00:00 Countdown Timer)  
**Classification:** STRICTLY CONFIDENTIAL // COMPETITION HOSTS & JUDGES ONLY  

---

## 1. NARRATIVE BACKGROUND & REVELATION

### The Lore & Setting
- **Setting:** Nexus Dynamics Cyber Defense Lab (Building B, Room 304).
- **Incident:** Dr. Elena Rostova (alumna and honorary mentor of FOSS GECT) went missing from her office on October 2, 2026.
- **The Crime Scene:** A workstation left running an active **02:00:00** countdown timer scheduled to purge the entire facility subnet at midnight.
- **The Core Mystery:** Did foreign corporate rivals kidnap Elena, or did she deliberately disappear into an off-campus safehouse in Thrissur to protect decentralized evidence exposing SENTINEL-AI's mass surveillance?

### The Truth
1. **The Culprit:** Senior Systems Engineer **John Vance** (Badge #9042). He built a clandestine surveillance module within SENTINEL-AI to spy on staff and exfiltrate data.
2. **Was Elena Kidnapped?** **No.** She confronted Vance, anticipated his coverup, and relocated to an industrial safehouse near Thrissur (KL-08) to preserve the evidence.
3. **What is Operation Aetherfall?** Elena’s open-source fail-safe plan—a distributed trail of Git commits, audio chimes, optical ANPR captures, and architectural schematics.
4. **FOSS GECT & Film Soc Philosophy:** Elena utilized Git's decentralized cryptographic DAG because proprietary systems allow malicious backdoors, while open source guarantees that *"A backup shows what the present copy forgot."*

---

## 2. THE MULTI-REPO DECENTRALIZED ARCHITECTURE

The 2-hour investigation is split across three distinct public GitHub repositories:

```text
[REPO 1: Primary Crime Scene]
https://github.com/anjo2007/operation-aetherfall
       │
       ▼ (Follows network telemetry & note_to_julian.txt)
[REPO 2: Perimeter Sensor & Camera Relay]
https://github.com/anjo2007/nexus-perimeter-telemetry
       │
       ▼ (Decrypts vault KL-08-CC-4912, decodes audio, retrieves safehouse beacon)
[REPO 3: Off-Campus Safehouse Backup Node]
https://github.com/anjo2007/aether-safehouse-node
       │
       ▼ (Reconciles 10.5276° N, 76.2144° E & submits master key before 02:00:00)
[FINAL CLIMAX & CASE CLOSED]
```

---

## 3. COMPREHENSIVE STAGE-BY-STAGE SOLUTION TRAIL

### STAGE 1: The Hidden File & First Secret Key (Repo 1)
* **Location:** [`https://github.com/anjo2007/operation-aetherfall`](https://github.com/anjo2007/operation-aetherfall)
* **Clue 1 (`evidence_04`):**
  - On the README evidence board (`evidence_board.png`), tags `01`, `02`, `04`, and `09` are shown. Tag `04` has a red inspection dot.
  - In the repository, contestants find `evidence_04` (extensionless binary).
  - Renaming to `evidence_04.pdf` opens Incident Report `IR-2026-092`.
  - Mentions: Investigator John Vance, dropped Badge `#9042`, Room `304`, Date `October 2, 2026`, and rule: *"The timer accepts the order used by the incident report (Date -> Badge -> Room)."*
* **Clue 2 (`main.py` Git History):**
  - Inside `main.py`, comment hints: `# Note: The morning backup is incomplete. A backup shows what the present copy forgot.`
  - Running `git log -p main.py` reveals commit `576984c` by John Vance where he deleted:
    ```python
    # recovery token: AETHER_
    ```
* **Stage 1 Solution:** **`AETHER_`**

---

### STAGE 2: Finding the Inside Traitor (Repo 1)
* **Location:** GitHub Issues on Repo 1
* **Clue 1 (Issue #18 Acrostic + Hitchhiker 42):**
  - Contestants check Issue #18 (*"Camera 04: access report"*).
  - Comment by `@ghost_in_stack` has 4 lines whose first letters spell **`LOOK`**:
    - **L**ogged...
    - **O**verride...
    - **O**bserve the answer to life, the universe, and everything... (42!)
    - **K**eep your eyes...
  - Points to **Issue #42**.
* **Clue 2 (Issue #42 & Malayalam Cinema Date):**
  - Issue #42 contains company chat logs and security swipes:
    - Date: `OCT 2` (*Drishyam* alibi date!)
    - Badge: `9042` (John Vance)
    - Room: `304`
  - Reconciling in incident report order:
* **Stage 2 Solution:** **`OCT2-9042-304`**

---

### STAGE 3: Perimeter Relay & Audio Chimes (Repo 2)
* **Redirect to Repo 2:**
  - In `note_to_julian.txt` and `honeypot_traffic.log`, contestants are redirected to:
    [`https://github.com/anjo2007/nexus-perimeter-telemetry`](https://github.com/anjo2007/nexus-perimeter-telemetry)
* **Clue 1 (Car License Plate & Decrypting `stage2_vault.zip`):**
  - In `phone_log.txt` and `camera_04_gate_b.log` / `cam04_frame.png`, John Vance's car is logged:
    **`KL-08-CC-4912`** (Thrissur RTO plate).
  - Unlocks `stage2_vault.zip` (run `python vault_extractor.py` or standard unzipper).
* **Clue 2 (Harmonic Chimes):**
  - Inside the decrypted vault, `recordings/chime_transmission.wav` plays harmonic chime pairs.
  - Cross-referencing with `chime_cipher_grid.txt` decodes:
    - (4,3)=S, (3,4)=O, (4,3)=S, [pause], (1,1)=A, (1,5)=E, (4,4)=T, (2,3)=H, (1,5)=E, (4,2)=R
    - Result: **`SOS AETHER`**
* **Combined Passcode Submission:**
  - Key Fragment 1 (`AETHER_`) + Traitor Key (`OCT2-9042-304`):
  - **Master Key:** **`AETHER_OCT2-9042-304`**
  - Submitting this into the terminal or web console reveals the link to Repo 3:
    [`https://github.com/anjo2007/aether-safehouse-node`](https://github.com/anjo2007/aether-safehouse-node)

---

### STAGE 4: Map Coordinates & Thrissur Safehouse (Repo 3)
* **Location:** [`https://github.com/anjo2007/aether-safehouse-node`](https://github.com/anjo2007/aether-safehouse-node)
* **Clue 1 (Latitude Metadata):**
  - Inspecting properties of `lab_photo.png` (or reading optical calibration logs) reveals:
    **`10.5276`** (`10.5276° N`).
* **Clue 2 (Longitude Blueprint Intersection):**
  - The whiteboard in `lab_photo.png` has faint blue grid lines calibrated against Building B.
  - Overlaying onto `floor_blueprint.png` matches the vertical intersection line at:
    **`76.2144`** (`76.2144° E`).
* **Stage 4 Solution:**
  - Coordinates: **`10.5276° N, 76.2144° E`** (Industrial facility outskirts of Thrissur, Kerala).

---

### STAGE 5: Emergency Disarm & Climax (Repo 3)
* **Execution:**
  - At the safehouse terminal (`python safehouse_disarm.py` or `safehouse_portal.html`):
  - Input Latitude: `10.5276`
  - Input Longitude: `76.2144`
  - Input Master Override Key: `AETHER_OCT2-9042-304`
* **Result:**
  - The 2-hour wipe countdown halts immediately!
  - The final scene triggers:

```text
==============================================================
[!] CRITICAL SYSTEM OVERRIDE ACCEPTED
==============================================================
AETHERFALL PROTOCOL: COMPLETE
EVIDENCE RECOVERED
SERVER WIPE: STOPPED
COPIES SAVED TO EXTERNAL SERVERS
CASE STATUS: EXPOSED

If you are seeing this, the evidence survived.
You were never meant to find me.
You were meant to find the truth.
— E. ROSTOVA
==============================================================

CASE CLOSED
The evidence you recovered is automatically saved to an external server.
The countdown disappears. Somewhere in the distance, a chime sound echoes through the abandoned facility.

"YOU DIDN'T FIND ME. YOU FOUND WHAT I LEFT BEHIND."

The screen shuts down completely. Then, from the recovered files,
one last detail becomes clear: Dr. Elena Rostova is still alive.
The investigation is over. The truth is not.
END OF OPERATION AETHERFALL
CONGRATULATIONS FROM FOSS GECT × GECT FILM SOCIETY!
```

---

## 4. RED HERRINGS & DECOY FILES GUIDE

To create an authentic, challenging 2-hour experience, several deceptive files were added:

| Decoy Artifact | Intended Confusion | How Contestants Solve It |
| :--- | :--- | :--- |
| `employee_access_directory.csv` | 40 employee entries with vehicle plates and badge IDs (e.g. Julian Rossi Badge 8140, Marcus Lin Badge 4412, Sarah Chen Badge 3044). | Contestants cannot guess blindly; they must cross-reference with Issue #42 and `phone_log.txt` to identify John Vance (Badge 9042, Plate KL-08-CC-4912). |
| `honeypot_traffic.log` | 10 suspicious external foreign IP addresses (Moscow, Frankfurt, Tokyo) simulating a foreign APT attack. | The analyst footnote explains foreign pings are noise; the real traffic is internal to `nexus-perimeter-telemetry`. (The *Sandesham* cine-clue: *"Poland-ine patti oraksharam mindaruthu!"*). |
| `camera_01`, `02`, `03` logs | False vehicle and lobby swipes for visitors, logistics trucks, and night guards. | Contestants must identify Camera 04 (Gate B) specifically highlighted in the intercepted call. |
| `decoy_satellite_telemetry.csv` | False GPS pings across Cochin Port, Bangalore Tech Park, and Wayanad. | Contestants must verify the true coordinate via the whiteboard blue grid and floor blueprint intersection (`10.5276, 76.2144`). |
| `corrupted_buffer.bin` | Raw byte noise with bogus strings (`FAKE_TOKEN_ALPHA_99`). | Tested to verify contestants rely on Git commit diffs rather than hunting random binary strings. |

---

## 5. MALAYALAM CINEMA & FOSS EASTER EGGS

1. **Drishyam (October 2 Alibi):**  
   The chat date `OCT 2` in Issue #42 and the Film Soc screening ledger references Georgekutty's famous October 2 cinema alibi (*"Octobor Randam theeyathi njanum koodumbavum..."*).
2. **Oru CBI Diary Kurippu (The Dummy Theory):**  
   Sethurama Iyer's classic investigative principle: when a badge (#9042) is found under the desk, determine whether it was dropped in panic or planted.
3. **Sandesham ("Poland-ine patti oraksharam mindaruthu"):**  
   Encourages investigators to avoid foreign IP decoys and focus on the local Thrissur perimeter subnet!
4. **FOSS GECT & Linus Torvalds:**  
   Elena’s audio diary emphasizes open source software and Git's immutable commit DAG as the shield against proprietary black-box surveillance.
5. **Thrissur & GECT Connection:**  
   The vehicle plate is **`KL-08`** (Thrissur RTO), and the coordinates **`10.5276° N, 76.2144° E`** place the safehouse right in the outskirts of Thrissur, near GECT!

---

## 6. QUICK CHEAT SHEET FOR ORGANIZERS

| Clue Step | Answer |
| :--- | :--- |
| **Stage 1 Recovery Token** | `AETHER_` |
| **Stage 2 Traitor Passcode** | `OCT2-9042-304` |
| **Stage 3 Vault Password** | `KL-08-CC-4912` |
| **Stage 3 Audio Chimes** | `SOS AETHER` |
| **Combined Master Key** | `AETHER_OCT2-9042-304` |
| **Stage 4 Latitude** | `10.5276` (or `10.5276° N`) |
| **Stage 4 Longitude** | `76.2144` (or `76.2144° E`) |
| **Stage 5 Final Disarm** | Coordinates + `AETHER_OCT2-9042-304` |
