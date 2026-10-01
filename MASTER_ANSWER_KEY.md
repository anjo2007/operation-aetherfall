# OPERATION AETHERFALL // MASTER ANSWER KEY & ORGANIZER GUIDE

> **CONFIDENTIAL // COMPETITION HOST & ORGANIZER REFERENCE ONLY**  
> Do not distribute this document to contestants or players prior to competition completion.

---

## 1. THE COMPLETE NARRATIVE & RESOLUTION

### Background Story
- **Date & Setting:** October 1–2, 2026 at Nexus Dynamics headquarters, Building B, Room 304.
- **The Incident:** Dr. Elena Rostova, Chief Security Specialist, vanished suddenly from her locked office in Building B, Room 304.
- **The Initial Clues:** Her computer was left running an active countdown timer connected to an online public repository titled **Project Aether Archive**. An internal system purge was scheduled to trigger at midnight.
- **The Core Mystery:** Was Dr. Elena Rostova kidnapped by corporate rivals, or did she hide intentionally to expose an illegal mass surveillance program known as **SENTINEL-AI**?

### The Truth Revealed (End Game)
1. **Who was responsible?**  
   Senior Systems Engineer **John Vance** (Badge #9042) built and maintained the secret surveillance module embedded inside SENTINEL-AI, spying on employees and exfiltrating proprietary records.
2. **Was Elena kidnapped?**  
   **No.** Elena discovered John Vance’s illegal spyware and confronted him. When Vance tried to delete her files and stage her disappearance as a kidnapping, Elena went into hiding at an off-campus safehouse in Kerala, India.
3. **What was Operation Aetherfall?**  
   Elena’s contingency safety net—a meticulously designed trail of breadcrumbs across repository commits, incident logs, acoustic chimes, and floor schematics designed to allow investigators to reconstruct the evidence and stop the automated server wipe before midnight.
4. **Final Climax:**  
   Entering the final passcode stops the wipe and reveals Dr. Elena Rostova is alive and the truth is fully exposed.

---

## 2. STAGE-BY-STAGE SOLUTION WALKTHROUGH

### STAGE 1: The Hidden File & First Secret Key
* **Objective:** Identify the disguised file format and extract the first key fragment from Git commit history.
* **Clue 1 (The File `evidence_04`):**
  - On the README evidence board (`evidence_board.png`), four tags are shown: `01`, `02`, `04`, and `09`. Tag `04` is the only one marked with a red indicator.
  - In the file list, players find the extensionless binary file `evidence_04`.
  - Adding `.pdf` to the name (or inspecting file headers with `file` / PDF viewer) opens the official Cyber Crime Task Force Incident Report (`IR-2026-092`).
  - The report reveals:
    - Subject: Disappearance of Dr. Elena Rostova
    - Investigator: Agent John Vance
    - Dropped badge: `#9042` under Elena's desk
    - Room: `304`
    - Date: `October 2, 2026`
    - Workstation message: *"If you are reading this, Julian bypassed the system. Do not trust the morning backup."*
    - Critical protocol rule: *"The timer accepts the order used by the incident report."*
* **Clue 2 (Git Commit History in `main.py`):**
  - In `main.py`, a comment reads:
    ```python
    # Note: The morning backup is incomplete.
    # A backup shows what the present copy forgot.
    ```
  - Remembering the clue *"A backup shows what the present copy forgot"* and Elena's note *"Do not trust the morning backup"*, players run:
    ```bash
    git log -p main.py
    ```
  - Comparing commits reveals that John Vance’s commit (`refactor: morning backup sync - sanitized security tokens and logs`) deleted this line:
    ```python
    # recovery token: AETHER_
    ```
* **Stage 1 Solution:** First key fragment is **`AETHER_`**.

---

### STAGE 2: Finding the Inside Traitor & Combined Passcode
* **Objective:** Connect clues across issue reports to identify the traitor and build the authorization code.
* **Clue 1 (Issue #18 to Issue #42):**
  - Players review GitHub Issue #18: *“Camera 04: access report”*.
  - A comment by `@ghost_in_stack` reads:
    > **L**ogged unauthorized peripheral ping at 01:14 AM.  
    > **O**verride sequence originated from external gateway.  
    > **O**bserve the answer to life, the universe, and everything.  
    > **K**eep your eyes on the central reconciliation channel.
  - The first letters of the lines spell **LOOK**.
  - The *“answer to life, the universe, and everything”* is famously **42** (from *The Hitchhiker's Guide to the Galaxy*).
  - This points players to **Issue #42** without explicitly stating the phrase.
* **Clue 2 (Reconciling Logs in Issue #42):**
  - In Issue #42 (*“Investigation Reconciliation: Security Audit #42”*), players find:
    1. Chat timestamp date: **OCT 2** (OCT2)
    2. Security pass ID from logs: **9042** (belonging to Senior Engineer John Vance)
    3. Room location: **304**
  - The rule from the Incident Report states: *“The timer accepts the order used by the incident report”* (Date -> Badge -> Room).
* **Stage 2 Solution:** Combined traitor passcode is **`OCT2-9042-304`**.

---

### STAGE 3: Perimeter Vault & Hidden Audio Chimes
* **Objective:** Decrypt the encrypted vault using vehicle data and decode the acoustic chime transmission.
* **Clue 1 (Unlocking `stage2_vault.zip`):**
  - In `phone_log.txt`, the intercepted phone call transcript reads:
    > *ROSTOVA: I already backed up the records, John. Your car plate KL-08-CC-4912 is logged on camera 04.*
  - CCTV still frame `cam04_frame.png` confirms license plate **`KL-08-CC-4912`**.
  - Password to decrypt `stage2_vault.zip` is **`KL-08-CC-4912`**.
* **Clue 2 (Decoding the Audio Chimes):**
  - Inside the unzipped vault, players find `recordings/chime_transmission.wav`, `chime_cipher_grid.txt`, and `audio_spectrogram_hint.txt`.
  - The chimes play tone pairs matching a 5x5 grid (Tone 1=440Hz, Tone 2=523Hz, Tone 3=659Hz, Tone 4=784Hz, Tone 5=880Hz).
  - Tone pairs spell:
    - (4,3)=S, (3,4)=O, (4,3)=S  
    - [Pause]  
    - (1,1)=A, (1,5)=E, (4,4)=T, (2,3)=H, (1,5)=E, (4,2)=R  
    - Result: **`SOS AETHER`**.
* **Stage 3 Master Key Submission:**
  - Combining Stage 1 fragment (`AETHER_`) + Stage 2 traitor key (`OCT2-9042-304`):
  - **Full Combined Passcode:** **`AETHER_OCT2-9042-304`**
  - Submitting this into `python terminal.py` or `index.html` unlocks Stage 4.

---

### STAGE 4: Map Coordinates (Enhanced Multi-Layer Puzzle)
* **Objective:** Decrypt the multi-layer puzzle to discover the physical safehouse location.
* **Clue 1 (Metadata Inspection):**
  - Inspecting file properties / metadata chunks of `lab_photo.png` (or reading the sensor optical diagnostics in `system_diagnostics.log`) yields the incomplete Latitude tag:
    **`LAT_10.5276`** (10.5276° N).
* **Clue 2 (Grid & Blueprint Overlay):**
  - On the whiteboard in `lab_photo.png`, faint blue grid lines indicate calibration against Building B schematics.
  - Overlaying the whiteboard grid line onto the calibration baseline in `floor_blueprint.png` aligns exactly with:
    **`76.2144`** (76.2144° E).
* **Stage 4 Solution:**  
  Physical Coordinates: **`10.5276° N, 76.2144° E`**  
  *(Location Note: Pinpoints an industrial zone in Thrissur, Kerala, India — matching the Kerala vehicle registration `KL-08`).*

---

### STAGE 5: Stopping the Countdown & Climax
* **Objective:** Enter the final override at the safehouse terminal to halt the wipe and view the case resolution.
* **Procedure:**
  - Investigators navigate to `10.5276° N, 76.2144° E`.
  - Terminal displays: *"IF YOU FOUND THIS, YOU FOLLOWED THE TRAIL. DO NOT TRUST THE STORY YOU WERE GIVEN."*
  - Inputting the master key **`AETHER_OCT2-9042-304`** halts the wipe.
* **Final Resolution Screen:**
  ```text
  AETHERFALL PROTOCOL: COMPLETE
  EVIDENCE RECOVERED
  SERVER WIPE: STOPPED
  COPIES SAVED TO EXTERNAL SERVERS
  CASE STATUS: EXPOSED

  If you are seeing this, the evidence survived.
  You were never meant to find me.
  You were meant to find the truth.
  — E. ROSTOVA

  CASE CLOSED
  "YOU DIDN'T FIND ME. YOU FOUND WHAT I LEFT BEHIND."
  ```

---

## 3. SUMMARY QUICK CHEAT SHEET

| Stage | Puzzle Component | Answer / Key | Destination / Next Step |
| :---: | :--- | :--- | :--- |
| **1** | Extensionless file | `evidence_04` -> `evidence_04.pdf` | Reveals Incident Report IR-2026-092 |
| **1** | Commit diff in `main.py` | `AETHER_` | First passcode fragment |
| **2** | Issue 18 Acrostic + 42 | `LOOK` + `42` -> Look at Issue #42 | Opens Issue #42 reconciliation |
| **2** | Issue 42 Reconciled Code | `OCT2-9042-304` | Date + Badge + Room (Incident order) |
| **3** | Car License Plate | `KL-08-CC-4912` | Unlocks `stage2_vault.zip` |
| **3** | Acoustic Chime Audio | `SOS AETHER` | Audio intercept confirmation |
| **3** | Full Master Passcode | `AETHER_OCT2-9042-304` | Unlocks Stage 4 Geolocation |
| **4** | Exif / PNG Metadata | `10.5276` (Latitude) | North coordinate |
| **4** | Whiteboard + Blueprint | `76.2144` (Longitude) | East coordinate |
| **5** | Safehouse Terminal Override| `AETHER_OCT2-9042-304` | Stops Server Wipe -> CASE CLOSED |
