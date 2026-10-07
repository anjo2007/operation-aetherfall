#!/usr/bin/env python3
"""
OPERATION AETHERFALL // CYBER CRIME TASK FORCE INVESTIGATION TERMINAL
Case File: CCTF-2026-092
Nexus Dynamics - Room 304 Incident

Interactive disarm console and clue verification engine for players.
"""

import sys
import os
import time
import zipfile
import re

BANNER = r"""
================================================================================
  ______  _____  ______ _____         _______ _____  ______ __   __
 |  ____|/ ____|/ ____|  __ \     /\|__   __|  __ \|  ____|\ \ / /
 | |__  | (___ | |    | |__) |   /  \  | |  | |__) | |__   \ V / 
 |  __|  \___ \| |    |  _  /   / /\ \ | |  |  _  /|  __|   > <  
 | |____ ____) | |____| | \ \  / ____ \| |  | | \ \| |____ / . \ 
 |______|_____/ \_____|_|  \_\/_/    \_\_|  |_|  \_\______/_/ \_\
================================================================================
  OPERATION AETHERFALL // CYBER CRIME TASK FORCE (CCTF) INVESTIGATION CONSOLE
  FACILITY: NEXUS DYNAMICS - BUILDING B - ROOM 304
  INCIDENT DATE: OCTOBER 2, 2026
================================================================================
"""

COUNTDOWN_HOURS = 2
COUNTDOWN_MINUTES = 0
COUNTDOWN_SECONDS = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_status(completed_stages):
    stages = [
        ("STAGE 1", "The Hidden File & First Secret Key", 1 in completed_stages),
        ("STAGE 2", "Inside Traitor & Security Ledger", 2 in completed_stages),
        ("STAGE 3", "Perimeter Vault & Acoustic Chimes", 3 in completed_stages),
        ("STAGE 4", "Forensic Lab Coordinates", 4 in completed_stages),
        ("STAGE 5", "Safehouse Server Wipe Disarm", 5 in completed_stages),
    ]
    print("\n[INVESTIGATION DOSSIER STATUS]")
    print("-" * 75)
    for tag, name, done in stages:
        status_box = "[ VERIFIED // COMPLETE ]" if done else "[ PENDING INVESTIGATION ]"
        color = "\033[92m" if done else "\033[93m"
        reset = "\033[0m"
        print(f" {tag}: {name:<40} {color}{status_box}{reset}")
    print("-" * 75)

def stage_1_flow(completed_stages):
    print("\n" + "=" * 75)
    print("STAGE 1: THE HIDDEN FILE & FIRST SECRET KEY")
    print("=" * 75)
    print("Dossier Brief:")
    print("  - Examine the evidence board (evidence_board.png).")
    print("  - Locate the marked evidence item in the file system (evidence_04).")
    print("  - Inspect the commit history of main.py for sanitized tokens.")
    print("    Hint: 'A backup shows what the present copy forgot.'")
    print("-" * 75)
    
    val = input("\nEnter recovery token fragment found in main.py commit history: ").strip()
    if val.upper() == "AETHER_":
        print("\n\033[92m[+] SUCCESS: Token fragment verified: AETHER_\033[0m")
        print("[+] Dr. Elena Rostova's primary recovery prefix authenticated.")
        completed_stages.add(1)
    else:
        print("\n\033[91m[-] ERROR: Invalid recovery token fragment.\033[0m")
        print("[-] Check the git log of main.py: compare before John Vance's morning backup commit.")

def stage_2_flow(completed_stages):
    print("\n" + "=" * 75)
    print("STAGE 2: FINDING THE INSIDE TRAITOR")
    print("=" * 75)
    print("Dossier Brief:")
    print("  - Issue #18 contains a note from @ghost_in_stack pointing to Issue #42.")
    print("  - In Issue #42, reconcile:")
    print("      * Chat Date")
    print("      * Security Badge ID")
    print("      * Target Room Number")
    print("  - The Incident Report states: 'The timer accepts the order used by the incident report.'")
    print("    Format: [Date]-[Badge]-[Room]")
    print("-" * 75)
    
    val = input("\nEnter reconciled passcode (Format: DATE-BADGE-ROOM): ").strip()
    # Normalize input
    clean_val = val.replace(" ", "").upper()
    if clean_val == "OCT2-9042-304" or clean_val == "OCT02-9042-304":
        print("\n\033[92m[+] SUCCESS: Inside traitor identified: Senior Engineer John Vance (Badge #9042)!\033[0m")
        print("[+] Reconciled authorization key accepted: OCT2-9042-304")
        completed_stages.add(2)
    else:
        print("\n\033[91m[-] ERROR: Passcode incorrect.\033[0m")
        print("[-] Ensure you combine: Date (OCT2) + Badge (9042) + Room (304).")

def stage_3_flow(completed_stages):
    print("\n" + "=" * 75)
    print("STAGE 3: PERIMETER VAULT & HIDDEN AUDIO CHIMES")
    print("=" * 75)
    print("Dossier Brief:")
    print("  - Inspect phone_log.txt and cam04_frame.png for the vehicle license plate.")
    print("  - Decrypt stage2_vault.zip using the license plate password.")
    print("  - Analyze recordings/chime_transmission.wav against chime_cipher_grid.txt.")
    print("  - Combine Key Fragment 1 (AETHER_) with Traitor Key (OCT2-9042-304).")
    print("-" * 75)

    # Sub-challenge 3A: License plate check
    plate = input("Enter vehicle license plate to unlock stage2_vault.zip: ").strip().upper().replace(" ", "")
    if plate == "KL-08-CC-4912" or plate == "KL08CC4912":
        print("\n\033[92m[+] VAULT UNLOCKED: stage2_vault.zip decrypted.\033[0m")
        print("[+] Audio transmission and acoustic grid extracted.")
    else:
        print("\n\033[91m[-] ACCESS DENIED: Incorrect vehicle license plate.\033[0m")
        print("[-] Check phone_log.txt or inspect the ANPR box on cam04_frame.png.")
        return

    # Sub-challenge 3B: Audio chimes solution
    chime_sol = input("\nEnter decoded message from audio chime transmission (SOS ???): ").strip().upper()
    if "SOS" in chime_sol and "AETHER" in chime_sol:
        print("\n\033[92m[+] ACOUSTIC CIPHER VERIFIED: 'SOS AETHER' decoded.\033[0m")
    else:
        print("\n\033[93m[!] Note: Audio chimes spell 'SOS AETHER'. Proceeding to combined key submission...\033[0m")

    # Sub-challenge 3C: Full passcode submission
    full_key = input("\nEnter full combined master key (Stage 1 Key + Stage 2 Key): ").strip().upper()
    if full_key == "AETHER_OCT2-9042-304":
        print("\n\033[92m[+] FULL MASTER KEY ACCEPTED: AETHER_OCT2-9042-304\033[0m")
        print("[+] Access granted to Stage 4 forensic geolocation grid!")
        print("\033[96m[!] OFFCAMPUS SAFEHOUSE BEACON LOCATED: https://github.com/anjo2007/aether-safehouse-node\033[0m")
        completed_stages.add(3)
    else:
        print("\n\033[91m[-] ERROR: Passcode mismatch. Combine [AETHER_] + [OCT2-9042-304].\033[0m")

def stage_4_flow(completed_stages):
    print("\n" + "=" * 75)
    print("STAGE 4: FORENSIC LAB COORDINATES")
    print("=" * 75)
    print("Dossier Brief:")
    print("  - Inspect lab_photo.png metadata properties for the Latitude tag.")
    print("    (Or review optical calibration notes in system_diagnostics.log).")
    print("  - Highlight the faint blue grid lines on the whiteboard in lab_photo.png.")
    print("  - Overlay them onto floor_blueprint.png to identify the Longitude intersect.")
    print("-" * 75)

    lat_input = input("Enter recovered Latitude (e.g., 10.5276): ").strip().replace("LAT_", "").replace("°N", "").replace("N", "").strip()
    lon_input = input("Enter recovered Longitude (e.g., 76.2144): ").strip().replace("LON_", "").replace("°E", "").replace("E", "").strip()
    
    is_lat_valid = "10.5276" in lat_input
    is_lon_valid = "76.2144" in lon_input
    
    if is_lat_valid and is_lon_valid:
        print("\n\033[92m[+] GEOLOCATION LOCK CONFIRMED: 10.5276° N, 76.2144° E\033[0m")
        print("[+] Target facility identified: Abandoned Industrial Safehouse, Kerala.")
        print("[+] External backup server beacon detected on site!")
        completed_stages.add(4)
    else:
        print("\n\033[91m[-] COORDINATES REJECTED.\033[0m")
        if not is_lat_valid:
            print("[-] Latitude tag invalid. Check lab_photo.png metadata tag: LAT_10.5276.")
        if not is_lon_valid:
            print("[-] Longitude invalid. Check whiteboard blue line on floor_blueprint.png: 76.2144.")

def stage_5_flow(completed_stages):
    print("\n" + "=" * 75)
    print("STAGE 5: STOPPING THE COUNTDOWN & FINAL RESOLUTION")
    print("=" * 75)
    print("Field Operation Report:")
    print("  Investigators have arrived at the safehouse outside campus (10.5276° N, 76.2144° E).")
    print("  Inside, a single terminal screen is illuminated:")
    print('  "IF YOU FOUND THIS, YOU FOLLOWED THE TRAIL. DO NOT TRUST THE STORY YOU WERE GIVEN."')
    print("  Server wipe countdown is counting down the final seconds!")
    print("-" * 75)
    
    final_auth = input("\nEnter FINAL OVERRIDE PASSCODE to stop server wipe: ").strip().upper()
    if final_auth == "AETHER_OCT2-9042-304" or final_auth == "AETHERFALL":
        completed_stages.add(5)
        run_climax_sequence()
    else:
        print("\n\033[91m[-] INVALID OVERRIDE CODE.\033[0m")
        print("[-] Enter master key: AETHER_OCT2-9042-304")

def run_climax_sequence():
    clear()
    print("\n\033[92m" + "=" * 75)
    print("[!] TRANSMITTING EMERGENCY OVERRIDE TO SENTINEL-AI DAEMON...")
    print("=" * 75 + "\033[0m")
    time.sleep(1.2)
    
    typewriter("\nAUTHENTICATING OPERATOR CREDENTIALS...", 0.02)
    time.sleep(0.6)
    typewriter("DISARMING AUTO-PURGE SCRIPT IN NODE SEC-B-09...", 0.02)
    time.sleep(0.6)
    typewriter("ISOLATING SENTINEL-AI SURVEILLANCE MODULES...", 0.02)
    time.sleep(0.8)

    print("\n" + "\033[96m" + "=" * 75)
    typewriter("AETHERFALL PROTOCOL: COMPLETE", 0.02)
    typewriter("EVIDENCE RECOVERED", 0.02)
    typewriter("SERVER WIPE: STOPPED", 0.02)
    typewriter("COPIES SAVED TO EXTERNAL SERVERS", 0.02)
    typewriter("CASE STATUS: EXPOSED", 0.02)
    print("=" * 75 + "\033[0m")
    time.sleep(1.0)

    print("\n\033[93m" + "-" * 75)
    typewriter("If you are seeing this, the evidence survived.", 0.025)
    typewriter("You were never meant to find me.", 0.025)
    typewriter("You were meant to find the truth.", 0.025)
    typewriter("— E. ROSTOVA", 0.03)
    print("-" * 75 + "\033[0m\n")
    time.sleep(2.0)

    print("\033[90m[The monitor goes black.]\033[0m")
    time.sleep(1.5)
    print("\033[90m[For a few seconds, nobody speaks. Then a final message appears:]\033[0m\n")
    time.sleep(1.5)

    print("\033[92m" + "*" * 75)
    print("                             CASE  CLOSED")
    print("*" * 75 + "\033[0m")
    time.sleep(1.0)
    typewriter("The evidence you recovered is automatically saved to an external server.", 0.02)
    typewriter("The countdown disappears.", 0.02)
    typewriter("Somewhere in the distance, a chime sound echoes through the abandoned facility.", 0.02)
    print()
    typewriter('"YOU DIDN\'T FIND ME. YOU FOUND WHAT I LEFT BEHIND."', 0.035)
    print()
    typewriter("The screen shuts down completely. Then, from the recovered files,", 0.02)
    typewriter("one last detail becomes clear: Dr. Elena Rostova is still alive.", 0.02)
    typewriter("The investigation is over. The truth is not.", 0.025)
    print("\n\033[92m======================= END OF OPERATION AETHERFALL =======================\033[0m\n")

def main():
    completed_stages = set()
    while True:
        clear()
        print(BANNER)
        print_status(completed_stages)
        
        print("\nCOMMANDS:")
        print("  1 - Stage 1: Verify First Key Fragment (evidence_04 & main.py)")
        print("  2 - Stage 2: Verify Traitor Key (Issue 18 -> Issue 42)")
        print("  3 - Stage 3: Unlock Vault & Audio Chimes (cam04 & stage2_vault.zip)")
        print("  4 - Stage 4: Verify Map Coordinates (lab_photo.png & floor_blueprint)")
        print("  5 - Stage 5: Disarm Server Wipe at Safehouse")
        print("  0 - Exit Terminal")
        
        choice = input("\nSelect Investigation Action (0-5): ").strip()
        
        if choice == "1":
            stage_1_flow(completed_stages)
            input("\nPress Enter to return to main terminal...")
        elif choice == "2":
            stage_2_flow(completed_stages)
            input("\nPress Enter to return to main terminal...")
        elif choice == "3":
            stage_3_flow(completed_stages)
            input("\nPress Enter to return to main terminal...")
        elif choice == "4":
            stage_4_flow(completed_stages)
            input("\nPress Enter to return to main terminal...")
        elif choice == "5":
            stage_5_flow(completed_stages)
            if 5 in completed_stages:
                break
            input("\nPress Enter to return to main terminal...")
        elif choice == "0":
            print("\nClosing CCTF terminal session. Keep investigating.")
            break
        else:
            print("\nInvalid selection. Choose 0-5.")
            time.sleep(1)

if __name__ == "__main__":
    main()
