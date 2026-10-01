import os
import zlib
import struct
import math
import wave
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

# ==============================================================================
# 1. PURE PYTHON PDF GENERATOR (FOR evidence_04)
# ==============================================================================
def create_incident_report_pdf(output_path):
    # Professional, authentic PDF layout
    # Canvas size 612 x 792 (Letter)
    content_lines = []
    
    # PDF graphics & text commands
    # Background border
    ops = [
        "0.1 0.15 0.25 rg", # dark slate color
        "40 730 532 25 re f", # banner rectangle
        "BT /F1 14 Tf 1 1 1 rg 50 740 Td (CYBER CRIME TASK FORCE - SPECIAL INVESTIGATION DIVISION) Tj ET",
        "BT /F2 9 Tf 0.8 0.85 0.9 rg 430 740 Td (RESTRICTED // LAW ENFORCEMENT) Tj ET",
        
        # Incident header block
        "0.92 0.94 0.96 rg 40 640 532 80 re f",
        "0.7 0.75 0.8 RG 1 w 40 640 532 80 re s",
        "BT /F1 11 Tf 0.1 0.15 0.2 rg 55 705 Td (INCIDENT REPORT #IR-2026-092) Tj ET",
        "BT /F2 9 Tf 0.2 0.25 0.3 rg 55 690 Td (Date: October 2, 2026  |  Time of Call: 02:15 AM IST) Tj ET",
        "BT /F2 9 Tf 0.2 0.25 0.3 rg 55 675 Td (Investigator: Senior Agent John Vance  |  Badge: #9042) Tj ET",
        "BT /F2 9 Tf 0.2 0.25 0.3 rg 55 660 Td (Subject: Disappearance of Dr. Elena Rostova  |  Facility: Nexus Dynamics HQ) Tj ET",
        "BT /F2 9 Tf 0.2 0.25 0.3 rg 55 648 Td (Location of Incident: Building B, Room 304 [Cyber Defense Laboratory]) Tj ET",

        # Section: Summary of Scene
        "BT /F1 11 Tf 0.15 0.2 0.35 rg 40 615 Td (1. SUMMARY OF SCENE & RECOVERY) Tj ET",
        "0.8 0.8 0.8 RG 40 610 532 0.5 re f",
        "BT /F2 9 Tf 0.15 0.15 0.2 rg",
        "40 595 Td (At 01:50 AM on October 2, 2026, building security reported the sudden absence of Dr. Elena Rostova,) Tj",
        "0 -13 Td (Chief Information Security Specialist. Her workstation terminal in Room 304 was left running an active) Tj",
        "0 -13 Td (countdown sequence tied to an unauthorized remote sync labeled Project Aether Archive.) Tj",
        "0 -13 Td (Primary security perimeter logs indicate forced logoff event triggered at 01:47 AM IST.) Tj ET",

        # Section: Evidence Collected
        "BT /F1 11 Tf 0.15 0.2 0.35 rg 40 525 Td (2. PHYSICAL & DIGITAL EVIDENCE INVENTORY) Tj ET",
        "0.8 0.8 0.8 RG 40 520 532 0.5 re f",
        "BT /F2 9 Tf 0.15 0.15 0.2 rg",
        "50 500 Td ([EV-01]  Personal journal with torn pages discovered in desk wastebasket.) Tj",
        "0 -14 Td ([EV-02]  Unmarked black USB drive recovered from USB port 2 of terminal.) Tj",
        "0 -14 Td ([EV-03]  Security Access Card: Badge #9042 found dropped directly beneath Elena Rostova's desk.) Tj",
        "0 -14 Td ([EV-04]  Live Workstation Buffer Dump [Incident Log IR-2026-092 - current document].) Tj",
        "0 -14 Td ([EV-09]  Server AETHER-09 Network Telemetry: 40GB outbound encrypted packet stream to external IP.) Tj ET",

        # Section: Workstation Screen Log
        "BT /F1 11 Tf 0.15 0.2 0.35 rg 40 405 Td (3. CAPTURED SCREEN TERMINAL BUFFER (ROOM 304)) Tj ET",
        "0.8 0.8 0.8 RG 40 400 532 0.5 re f",
        "0.08 0.1 0.12 rg 40 305 532 85 re f",
        "BT /F3 9 Tf 0.2 0.9 0.4 rg",
        "50 375 Td (SYSTEM ALERT: Unauthorized root bypass detected in Lab 304) Tj",
        "0 -13 Td (ROSTOVA MEMO: 'If you are reading this, Julian bypassed the system. Do not trust the morning backup.') Tj",
        "0 -13 Td (STATUS: CRITICAL ARCHIVE EXFILTRATION IN PROGRESS) Tj",
        "0 -13 Td (FAILSAFE: SERVER WIPE INITIATED - Passcode required to abort sequence.) Tj",
        "0 -13 Td (TERMINAL PROTOCOL NOTE: The timer accepts the order used by the incident report.) Tj ET",

        # Section: Investigator Notes
        "BT /F1 11 Tf 0.15 0.2 0.35 rg 40 275 Td (4. INVESTIGATIVE NOTES & PROTOCOLS) Tj ET",
        "0.8 0.8 0.8 RG 40 270 532 0.5 re f",
        "BT /F2 9 Tf 0.2 0.2 0.2 rg",
        "40 250 Td (- Security badge #9042 belongs to Senior Systems Engineer John Vance.) Tj",
        "0 -13 Td (- Field inspection notes date verification: OCT 2 confirmed in room biometric ledger.) Tj",
        "0 -13 Td (- Access room parameter registered as Room 304.) Tj",
        "0 -13 Td (- System disarm console requires sequence format aligned with standard incident registry:) Tj",
        "0 -13 Td (  [Date Token] - [Badge ID] - [Room ID]) Tj",
        "0 -13 Td (- Further surveillance camera and vehicle logs are archived in phone_log.txt and cam04_frame.png.) Tj ET",

        # Signature box
        "0.95 0.95 0.95 rg 40 100 240 50 re f",
        "0.7 0.7 0.7 RG 1 w 40 100 240 50 re s",
        "BT /F2 8 Tf 0.3 0.3 0.3 rg 45 135 Td (VERIFIED BY TASK FORCE LEAD:) Tj ET",
        "BT /F1 9 Tf 0.1 0.1 0.1 rg 45 120 Td (Agent J. Vance, Senior Forensic Lead) Tj ET",
        "BT /F2 8 Tf 0.4 0.4 0.4 rg 45 107 Td (Status: Under Active Investigation) Tj ET",

        # Official Stamp
        "0.8 0.1 0.1 RG 2 w 350 100 180 45 re s",
        "BT /F1 12 Tf 0.8 0.1 0.1 rg 370 125 Td (EVIDENCE ITEM #04) Tj ET",
        "BT /F2 8 Tf 0.8 0.1 0.1 rg 375 110 Td (CYBER CRIME TASK FORCE ARCHIVE) Tj ET"
    ]
    
    stream_content = "\n".join(ops).encode('latin1')
    
    objects = []
    # obj 1: Catalog
    objects.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    # obj 2: Pages
    objects.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    # obj 3: Page
    objects.append(b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R /F3 7 0 R >> >> >>\nendobj\n")
    # obj 4: Contents
    objects.append(f"4 0 obj\n<< /Length {len(stream_content)} >>\nstream\n".encode('latin1') + stream_content + b"\nendstream\nendobj\n")
    # obj 5: F1 Helvetica-Bold
    objects.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n")
    # obj 6: F2 Helvetica
    objects.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")
    # obj 7: F3 Courier-Bold
    objects.append(b"7 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Courier-Bold >>\nendobj\n")

    with open(output_path, 'wb') as f:
        f.write(b"%PDF-1.4\n")
        offsets = []
        offset = len(b"%PDF-1.4\n")
        for obj in objects:
            offsets.append(offset)
            f.write(obj)
            offset += len(obj)
        xref_offset = offset
        f.write(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode('latin1'))
        for off in offsets:
            f.write(f"{off:010d} 00000 n \n".encode('latin1'))
        trailer = f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n"
        f.write(trailer.encode('latin1'))
    print(f"[+] Created incident report PDF: {output_path}")

# ==============================================================================
# 2. EVIDENCE BOARD IMAGE (evidence_board.png)
# ==============================================================================
def create_evidence_board(output_path):
    w, h = 1200, 800
    im = Image.new("RGB", (w, h), color=(26, 29, 36))
    draw = ImageDraw.Draw(im)
    
    # Load fonts
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 26)
        font_h1 = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 18)
        font_body = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
        font_tag = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 24)
        font_memo = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
    except:
        font_title = font_h1 = font_body = font_tag = font_memo = ImageFont.load_default()

    # Draw grid background lines
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(32, 36, 45), width=1)
    for y in range(0, h, 40):
        draw.line([(0, y), (w, y)], fill=(32, 36, 45), width=1)
        
    # Top dossier header banner
    draw.rectangle([(30, 20), (w - 30, 75)], fill=(15, 18, 24), outline=(50, 60, 80), width=2)
    draw.text((45, 30), "CYBER CRIME TASK FORCE  //  OPERATION AETHERFALL", fill=(220, 230, 245), font=font_title)
    draw.text((45, 55), "CASE # CCTF-2026-092 | FORENSIC EVIDENCE REPOSITORY | NEXUS DYNAMICS FACILITY", fill=(130, 150, 180), font=font_body)
    
    # Red thread coordinates between pins
    pin_coords = {
        "01": (220, 230),
        "02": (800, 220),
        "04": (260, 520),
        "09": (840, 530)
    }
    # Connecting string lines
    draw.line([pin_coords["01"], pin_coords["04"]], fill=(180, 40, 40), width=2)
    draw.line([pin_coords["04"], pin_coords["02"]], fill=(160, 30, 30), width=1)
    draw.line([pin_coords["02"], pin_coords["09"]], fill=(180, 40, 40), width=2)
    draw.line([pin_coords["04"], pin_coords["09"]], fill=(190, 50, 50), width=2)

    # Function to draw evidence card
    def draw_card(x, y, card_w, card_h, tag, title, details, is_target=False):
        # Card shadow & body
        draw.rectangle([(x + 4, y + 4), (x + card_w + 4, y + card_h + 4)], fill=(10, 12, 16))
        draw.rectangle([(x, y), (x + card_w, y + card_h)], fill=(245, 242, 235), outline=(180, 175, 165), width=1)
        
        # Tag header badge
        tag_bg = (200, 40, 40) if is_target else (40, 45, 55)
        draw.rectangle([(x + 12, y + 12), (x + 85, y + 52)], fill=tag_bg)
        draw.text((x + 22, y + 18), f"[{tag}]", fill=(255, 255, 255), font=font_tag)
        
        # Title and details
        draw.text((x + 95, y + 16), title, fill=(20, 25, 35), font=font_h1)
        draw.text((x + 95, y + 38), "CCTF EVIDENCE REGISTRY", fill=(100, 105, 115), font=font_body)
        draw.line([(x + 12, y + 58), (x + card_w - 12, y + 58)], fill=(200, 195, 185), width=1)
        
        dy = y + 68
        for d in details:
            draw.text((x + 16, dy), d, fill=(45, 50, 60), font=font_body)
            dy += 18
            
        # Pin head at top-center of card
        pin_x, pin_y = x + card_w // 2, y + 4
        # Standard pin is silver/dark metallic
        draw.ellipse([(pin_x - 7, pin_y - 7), (pin_x + 7, pin_y + 7)], fill=(70, 75, 85), outline=(30, 35, 40), width=1)
        
        # REQUIREMENT: "Make tag 04 the only one with a small red mark."
        if is_target:
            # Small, distinctive forensic red mark/dot in corner of tag badge
            draw.ellipse([(x + 73, y + 14), (x + 83, y + 24)], fill=(255, 40, 40), outline=(255, 255, 255), width=1)
            # Also a subtle red inspection check indicator
            draw.rectangle([(x + card_w - 24, y + 12), (x + card_w - 12, y + 24)], fill=(220, 30, 30))

    # Evidence Cards
    draw_card(70, 160, 420, 170, "01", "USB DRIVE RECOVERED", [
        "Item: Kingston 64GB Encrypted Drive",
        "Found: Lab 304 Workstation USB Port 2",
        "Timestamp: 2026-10-02 01:20 IST",
        "Status: Extracted raw partition dump"
    ])
    
    draw_card(650, 160, 440, 170, "02", "PERSONAL JOURNAL", [
        "Item: Spiral Notebook - Torn Pages",
        "Found: Elena Rostova Office Desk",
        "Notes: Mentions SENTINEL-AI anomaly",
        "Status: Forensic handwriting match confirmed"
    ])

    draw_card(70, 460, 440, 180, "04", "INCIDENT REPORT", [
        "Item: Primary Station Incident Ledger",
        "Ref: IR-2026-092 Live Buffer Capture",
        "Contents: Security Badge #9042 & Screen Log",
        "Status: Preserved in repository as evidence_04",
        "Warning: File format unsuffixed in file system"
    ], is_target=True)

    draw_card(650, 460, 440, 180, "09", "SERVER TELEMETRY", [
        "Item: Server AETHER-09 Network Dump",
        "Volume: 40GB Encrypted Stream Outbound",
        "Protocol: Direct UDP tunnel via internal node",
        "Status: Terminated upon host disconnection"
    ])

    # Memo sticky note pinned at bottom
    memo_x, memo_y = 440, 680
    draw.rectangle([(memo_x + 3, memo_y + 3), (memo_x + 340 + 3, memo_y + 80 + 3)], fill=(15, 15, 20))
    draw.rectangle([(memo_x, memo_y), (memo_x + 340, memo_y + 80)], fill=(255, 248, 180), outline=(220, 210, 140), width=1)
    draw.text((memo_x + 15, memo_y + 12), "[INVESTIGATIVE DIRECTIVE]", fill=(120, 90, 20), font=font_memo)
    draw.text((memo_x + 15, memo_y + 35), '"A backup shows what the present copy forgot."', fill=(40, 35, 20), font=font_memo)
    draw.text((memo_x + 15, memo_y + 55), "Compare commit revisions to expose sanitized tokens.", fill=(90, 80, 50), font=font_body)

    im.save(output_path, "PNG")
    print(f"[+] Created evidence board image: {output_path}")

# ==============================================================================
# 3. CAMERA 04 CCTV STILL FRAME (cam04_frame.png)
# ==============================================================================
def create_cam04_frame(output_path):
    w, h = 1000, 600
    im = Image.new("RGB", (w, h), color=(18, 22, 28))
    draw = ImageDraw.Draw(im)
    
    try:
        font_cctv = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 20)
        font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)
        font_plate = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 28)
    except:
        font_cctv = font_mono = font_plate = ImageFont.load_default()

    # Draw dark asphalt & security gate perspective
    draw.polygon([(0, 350), (w, 300), (w, h), (0, h)], fill=(28, 32, 38))
    draw.line([(0, 480), (w, 440)], fill=(60, 70, 80), width=2)
    # Security barrier arm
    draw.line([(80, 360), (450, 320)], fill=(200, 180, 40), width=6)
    
    # Sedan silhouette in parking bay B
    car_x, car_y = 480, 290
    draw.polygon([(car_x, car_y + 90), (car_x + 40, car_y + 30), (car_x + 180, car_y + 25), 
                  (car_x + 290, car_y + 60), (car_x + 360, car_y + 90), (car_x + 340, car_y + 140), 
                  (car_x + 20, car_y + 140)], fill=(12, 14, 18), outline=(60, 70, 85), width=2)
    # Car window
    draw.polygon([(car_x + 60, car_y + 40), (car_x + 175, car_y + 36), (car_x + 260, car_y + 65), (car_x + 60, car_y + 65)], fill=(30, 45, 60))
    # Wheel wells
    draw.ellipse([(car_x + 40, car_y + 120), (car_x + 100, car_y + 170)], fill=(8, 10, 12))
    draw.ellipse([(car_x + 250, car_y + 120), (car_x + 310, car_y + 170)], fill=(8, 10, 12))

    # License plate zoom / inspection HUD box
    hud_x, hud_y = 620, 340
    draw.rectangle([(hud_x, hud_y), (hud_x + 320, hud_y + 140)], fill=(10, 14, 20), outline=(0, 220, 180), width=2)
    draw.text((hud_x + 15, hud_y + 12), "[ANPR SENSOR OCR LOCK]", fill=(0, 220, 180), font=font_mono)
    
    # Real Kerala license plate box
    plate_bx, plate_by = hud_x + 25, hud_y + 45
    draw.rectangle([(plate_bx, plate_by), (plate_bx + 265, plate_by + 55)], fill=(245, 245, 245), outline=(20, 20, 20), width=2)
    draw.rectangle([(plate_bx, plate_by), (plate_bx + 32, plate_by + 55)], fill=(0, 50, 150))
    draw.text((plate_bx + 4, plate_by + 16), "IND", fill=(255, 255, 255), font=font_mono)
    draw.text((plate_bx + 42, plate_by + 12), "KL-08-CC-4912", fill=(10, 10, 10), font=font_plate)
    
    draw.text((hud_x + 15, hud_y + 112), "CONFIDENCE: 99.4% | GATE B INGRESS", fill=(120, 160, 180), font=font_mono)

    # CCTV OSD banner
    draw.rectangle([(20, 20), (w - 20, 70)], fill=(10, 14, 20), outline=(40, 50, 65), width=1)
    draw.text((35, 28), "CAM-04 // PERIMETER GATE B // 2026-10-02 01:42:18 IST", fill=(0, 255, 120), font=font_cctv)
    draw.text((35, 50), "STATUS: REC [FEED OVERRIDE] // SENSOR ID: NX-CAM-04", fill=(140, 200, 160), font=font_mono)
    
    # Forensic pointer stencil in bottom-left
    stencil_x, stencil_y = 30, 480
    draw.rectangle([(stencil_x, stencil_y), (stencil_x + 380, stencil_y + 85)], fill=(12, 16, 22), outline=(100, 120, 150), width=1)
    draw.text((stencil_x + 12, stencil_y + 10), "SURVEILLANCE ASSET TRACE:", fill=(200, 220, 240), font=font_mono)
    draw.text((stencil_x + 12, stencil_y + 32), "Vehicle associated with Senior Eng. John Vance.", fill=(140, 160, 180), font=font_mono)
    draw.text((stencil_x + 12, stencil_y + 54), "Destination: Cyber Defense Lab -> lab_photo.png", fill=(0, 220, 255), font=font_mono)

    im.save(output_path, "PNG")
    print(f"[+] Created Camera 04 frame image: {output_path}")

# ==============================================================================
# 4. LAB 304 PHOTO (lab_photo.png) WITH METADATA LAT_10.5276 & WHITEBOARD GRID
# ==============================================================================
def create_lab_photo(output_path):
    w, h = 1200, 800
    im = Image.new("RGB", (w, h), color=(22, 26, 34))
    draw = ImageDraw.Draw(im)
    
    try:
        font_h1 = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 22)
        font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
        font_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 12)
        font_grid = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 16)
    except:
        font_h1 = font_mono = font_small = font_grid = ImageFont.load_default()

    # Room background: office walls & desk
    draw.rectangle([(0, 0), (w, 480)], fill=(32, 38, 48))
    draw.rectangle([(0, 480), (w, h)], fill=(45, 50, 60)) # carpet
    
    # Workstation desk & monitor
    draw.rectangle([(620, 420), (1150, 720)], fill=(55, 60, 70), outline=(80, 90, 105), width=2)
    # Monitor 1 (Left)
    draw.rectangle([(660, 320), (870, 480)], fill=(15, 18, 24), outline=(120, 130, 145), width=2)
    draw.text((680, 370), "SENTINEL-AI", fill=(255, 60, 60), font=font_mono)
    draw.text((680, 395), "SYSTEM LOCKED", fill=(200, 200, 200), font=font_small)
    # Monitor 2 (Right)
    draw.rectangle([(900, 300), (1120, 470)], fill=(10, 14, 20), outline=(120, 130, 145), width=2)
    draw.text((920, 350), "COUNTDOWN ACTIVE", fill=(0, 220, 180), font=font_mono)
    draw.text((920, 375), "AETHER ARCHIVE SYNC", fill=(140, 170, 200), font=font_small)

    # THE WHITEBOARD ON THE LEFT WALL (Prominent Clue Object)
    wb_x, wb_y, wb_w, wb_h = 60, 60, 520, 460
    # Frame & surface
    draw.rectangle([(wb_x - 6, wb_y - 6), (wb_x + wb_w + 6, wb_y + wb_h + 6)], fill=(120, 125, 135), outline=(70, 75, 85), width=2)
    draw.rectangle([(wb_x, wb_y), (wb_x + wb_w, wb_y + wb_h)], fill=(245, 248, 252))
    
    # Whiteboard Title
    draw.text((wb_x + 18, wb_y + 16), "NEXUS DEFENSE LAB 304 // SENTINEL BACKUP RELAY", fill=(20, 40, 70), font=font_h1)
    draw.text((wb_x + 18, wb_y + 44), "Top Secret Architecture & Fail-Safe Evacuation Node", fill=(80, 100, 130), font=font_small)
    draw.line([(wb_x + 15, wb_y + 62), (wb_x + wb_w - 15, wb_y + 62)], fill=(180, 200, 220), width=1)

    # Whiteboard Faint Blue Grid (Requirement: Clue 2: Highlighting faint blue grid lines)
    grid_ox, grid_oy = wb_x + 30, wb_y + 80
    grid_w, grid_h = 460, 300
    
    # Draw faint blue grid mesh
    for gx in range(0, grid_w + 1, 46):
        draw.line([(grid_ox + gx, grid_oy), (grid_ox + gx, grid_oy + grid_h)], fill=(185, 215, 245), width=1)
    for gy in range(0, grid_h + 1, 30):
        draw.line([(grid_ox, grid_oy + gy), (grid_ox + grid_w, grid_oy + gy)], fill=(185, 215, 245), width=1)

    # Architectural room outline drawn on whiteboard
    draw.rectangle([(grid_ox + 46, grid_oy + 30), (grid_ox + 414, grid_oy + 270)], outline=(100, 150, 200), width=2)
    draw.text((grid_ox + 55, grid_oy + 40), "BUILDING B / WING 3 SCHEMATIC", fill=(80, 120, 180), font=font_small)
    
    # Prominent calibrated longitude intersection line on the whiteboard grid
    # Target longitude is 76.2144
    target_gx = grid_ox + int(grid_w * 0.62) # intersection column
    draw.line([(target_gx, grid_oy), (target_gx, grid_oy + grid_h)], fill=(40, 110, 220), width=2)
    # Coordinate marker crosshair
    target_gy = grid_oy + int(grid_h * 0.45)
    draw.ellipse([(target_gx - 7, target_gy - 7), (target_gx + 7, target_gy + 7)], outline=(220, 40, 40), width=2)
    draw.text((target_gx + 12, target_gy - 10), "INTERSECTION REF: 76.2144", fill=(20, 70, 160), font=font_grid)
    draw.text((target_gx + 12, target_gy + 12), "(Match to Floor Blueprint X-Axis)", fill=(100, 120, 150), font=font_small)

    # Legend on whiteboard bottom
    draw.text((grid_ox + 10, grid_oy + grid_h + 20), "LONGITUDE ALIGNMENT KEY: Overlay grid lines onto floor blueprint", fill=(40, 60, 90), font=font_small)
    draw.text((grid_ox + 10, grid_oy + grid_h + 38), "Whiteboard Line Intersect Index = 76.2144 E", fill=(20, 40, 120), font=font_grid)

    # Overlay camera OSD in corner
    draw.rectangle([(30, h - 80), (520, h - 25)], fill=(10, 14, 20), outline=(50, 65, 80), width=1)
    draw.text((45, h - 70), "FORENSIC PHOTO // ROOM 304 // CRIME SCENE PRESERVATION", fill=(0, 255, 160), font=font_mono)
    draw.text((45, h - 48), "EXIF METADATA EMBEDDED: LAT_10.5276 [EXIF TAG & PNG CHUNK]", fill=(140, 200, 230), font=font_small)

    # EMBED METADATA INTO PNG
    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("Latitude", "LAT_10.5276")
    pnginfo.add_text("Comment", "LAT_10.5276 // NEXUS DYNAMICS SAFE-HOUSE RELAY")
    pnginfo.add_text("Description", "LAT_10.5276")
    pnginfo.add_text("SensorCalibration", "LAT_10.5276")

    im.save(output_path, "PNG", pnginfo=pnginfo)
    print(f"[+] Created lab photo with embedded metadata: {output_path}")

# ==============================================================================
# 5. FLOOR BLUEPRINT (floor_blueprint.png)
# ==============================================================================
def create_floor_blueprint(output_path):
    w, h = 1200, 800
    im = Image.new("RGB", (w, h), color=(10, 25, 48)) # classic deep blueprint blue
    draw = ImageDraw.Draw(im)
    
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 24)
        font_h1 = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 16)
        font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 14)
    except:
        font_title = font_h1 = font_mono = font_bold = ImageFont.load_default()

    # Draw cyan blueprint grid
    for x in range(0, w, 30):
        draw.line([(x, 0), (x, h)], fill=(18, 42, 75), width=1)
    for y in range(0, h, 30):
        draw.line([(0, y), (w, y)], fill=(18, 42, 75), width=1)

    # Outer border & header
    draw.rectangle([(25, 20), (w - 25, h - 25)], outline=(80, 180, 240), width=2)
    draw.rectangle([(40, 35), (w - 40, 95)], fill=(12, 32, 60), outline=(80, 180, 240), width=1)
    draw.text((60, 45), "NEXUS DYNAMICS ARCHITECTURAL SCHEMATIC // FACILITY B - LEVEL 3", fill=(200, 240, 255), font=font_title)
    draw.text((60, 72), "FACILITY GRID & LONGITUDE MAPPING CALIBRATION | DWG # NX-B-L3-304", fill=(120, 190, 230), font=font_mono)

    # Draw rooms schematic
    # Main Corridor
    draw.rectangle([(100, 300), (1100, 360)], outline=(120, 210, 255), fill=(15, 38, 70), width=2)
    draw.text((120, 322), "CENTRAL ACCESS CORRIDOR - WING B", fill=(160, 220, 255), font=font_bold)

    # Room 302
    draw.rectangle([(100, 140), (380, 300)], outline=(120, 210, 255), fill=(12, 30, 56), width=2)
    draw.text((120, 160), "ROOM 302: HARDWARE LAB", fill=(140, 200, 240), font=font_mono)

    # Room 304 (Target Lab)
    draw.rectangle([(420, 120), (840, 300)], outline=(0, 255, 200), fill=(16, 45, 80), width=3)
    draw.text((440, 145), "ROOM 304: CYBER DEFENSE LAB (DR. ROSTOVA)", fill=(0, 255, 220), font=font_h1)
    draw.text((440, 175), "Workstation 01 [Incident Scene]", fill=(180, 220, 240), font=font_mono)
    draw.text((440, 195), "Whiteboard Location: North-West Partition", fill=(180, 220, 240), font=font_mono)

    # Server Room 306
    draw.rectangle([(880, 140), (1100, 300)], outline=(120, 210, 255), fill=(12, 30, 56), width=2)
    draw.text((900, 160), "ROOM 306: VAULT", fill=(140, 200, 240), font=font_mono)

    # Longitude Calibration Axis Scale along Bottom
    scale_y = 520
    draw.rectangle([(80, scale_y - 20), (1120, scale_y + 160)], fill=(12, 28, 54), outline=(80, 180, 240), width=1)
    draw.text((100, scale_y - 8), "FACILITY LONGITUDE CALIBRATION SCALE (EAST COORDINATES):", fill=(255, 215, 0), font=font_h1)
    
    # Axis baseline
    axis_start_x, axis_end_x = 120, 1080
    axis_y = scale_y + 60
    draw.line([(axis_start_x, axis_end_x), (axis_y, axis_y)], fill=(120, 210, 255), width=2)

    # Calibration ticks
    ticks = [
        (140, "76.2100"),
        (280, "76.2115"),
        (420, "76.2130"),
        (560, "76.2144 [INTERSECT]"),
        (700, "76.2160"),
        (840, "76.2175"),
        (980, "76.2190")
    ]
    for tx, tlabel in ticks:
        draw.line([(tx, axis_y - 12), (tx, axis_y + 12)], fill=(140, 220, 255), width=2)
        if "76.2144" in tlabel:
            # Highlighted target line
            draw.line([(tx, axis_y - 30), (tx, axis_y + 30)], fill=(255, 80, 80), width=3)
            # Arrow pointing down
            draw.polygon([(tx - 6, axis_y - 35), (tx + 6, axis_y - 35), (tx, axis_y - 25)], fill=(255, 80, 80))
            draw.text((tx - 80, axis_y + 24), "76.2144 ° E", fill=(255, 80, 80), font=font_title)
            draw.text((tx - 110, axis_y + 54), "TARGET SAFEHOUSE LONGITUDE", fill=(255, 200, 200), font=font_bold)
        else:
            draw.text((tx - 25, axis_y + 20), tlabel, fill=(120, 180, 220), font=font_mono)

    # Deduction guidance box
    draw.text((100, scale_y + 115), "DECRYPTION PROTOCOL: Match whiteboard faint grid index from lab_photo.png to blueprint scale.", fill=(160, 210, 240), font=font_mono)
    draw.text((100, scale_y + 135), "Grid alignment confirms: Longitude = 76.2144. Combine with metadata Latitude: 10.5276.", fill=(160, 240, 200), font=font_mono)

    im.save(output_path, "PNG")
    print(f"[+] Created floor blueprint image: {output_path}")

# ==============================================================================
# 6. AUDIO GENERATOR (chime_transmission.wav -> SOS AETHER)
# ==============================================================================
def create_chime_wav(output_path):
    sample_rate = 44100
    
    def generate_tone(freq, duration):
        samples = []
        n_samples = int(sample_rate * duration)
        for i in range(n_samples):
            t = i / sample_rate
            # Harmonic chime envelope: fundamental + bell overtones
            env = math.exp(-3.5 * t / duration)
            val = (0.55 * math.sin(2 * math.pi * freq * t) +
                   0.30 * math.sin(2 * math.pi * 2.756 * freq * t) +
                   0.15 * math.sin(2 * math.pi * 5.404 * freq * t))
            val = max(-1.0, min(1.0, val * env))
            sample = int(val * 32767 * 0.75)
            samples.append(sample)
        return samples

    def generate_silence(duration):
        return [0] * int(sample_rate * duration)

    # 5x5 Grid Frequencies (Hz)
    # [1]: 440 Hz (A4)
    # [2]: 523.25 Hz (C5)
    # [3]: 659.25 Hz (E5)
    # [4]: 783.99 Hz (G5)
    # [5]: 880.00 Hz (A5)
    tones = {
        1: 440.00,
        2: 523.25,
        3: 659.25,
        4: 783.99,
        5: 880.00
    }

    # Grid mapping:
    #      1   2   3   4   5
    # 1:   A   B   C   D   E
    # 2:   F   G   H   I   K
    # 3:   L   M   N   O   P
    # 4:   Q   R   S   T   U
    # 5:   V   W   X   Y   Z
    #
    # S O S   A E T H E R
    # S: (4, 3)
    # O: (3, 4)
    # S: (4, 3)
    # [Pause]
    # A: (1, 1)
    # E: (1, 5)
    # T: (4, 4)
    # H: (2, 3)
    # E: (1, 5)
    # R: (4, 2)
    sequence = [
        (4, 3), # S
        (3, 4), # O
        (4, 3), # S
        None,   # Word break pause
        (1, 1), # A
        (1, 5), # E
        (4, 4), # T
        (2, 3), # H
        (1, 5), # E
        (4, 2), # R
    ]

    all_samples = []
    # Initial pause
    all_samples.extend(generate_silence(0.5))
    
    for item in sequence:
        if item is None:
            all_samples.extend(generate_silence(0.8)) # word gap
        else:
            r, c = item
            all_samples.extend(generate_tone(tones[r], 0.35))
            all_samples.extend(generate_silence(0.10))
            all_samples.extend(generate_tone(tones[c], 0.35))
            all_samples.extend(generate_silence(0.35)) # letter gap

    all_samples.extend(generate_silence(0.5))

    with wave.open(output_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        packed = struct.pack(f"<{len(all_samples)}h", *all_samples)
        wf.writeframes(packed)

    print(f"[+] Created chime WAV transmission: {output_path}")

# ==============================================================================
# 7. ENCRYPTED ZIP GENERATOR (stage2_vault.zip PASSWORD: KL-08-CC-4912)
# ==============================================================================
def create_encrypted_zip(filename, files, password):
    # files is dict of {arcname: bytes}
    pwd = password.encode('utf-8')
    entries = []
    offset = 0
    
    # Setup ZipEncrypter
    _crctable = list(map(lambda i: i, range(256)))
    for i in range(256):
        c = i
        for _ in range(8):
            if c & 1:
                c = 0xEDB88320 ^ (c >> 1)
            else:
                c = c >> 1
        _crctable[i] = c

    def crc32_byte(ch, crc):
        return (crc >> 8) ^ _crctable[(crc ^ ch) & 0xFF]

    class ZipEncrypter:
        def __init__(self, p):
            self.key0 = 305419896
            self.key1 = 591751049
            self.key2 = 878082192
            for b in p:
                self.update_keys(b)

        def update_keys(self, c):
            self.key0 = crc32_byte(c, self.key0)
            self.key1 = (self.key1 + (self.key0 & 0xFF)) & 0xFFFFFFFF
            self.key1 = (self.key1 * 134775813 + 1) & 0xFFFFFFFF
            self.key2 = crc32_byte(self.key1 >> 24, self.key2)

        def encrypt_byte(self, c):
            k = self.key2 | 2
            cipher = c ^ (((k * (k ^ 1)) >> 8) & 0xFF)
            self.update_keys(c)
            return cipher

        def encrypt(self, data):
            return bytes([self.encrypt_byte(b) for b in data])

    with open(filename, 'wb') as f:
        for arcname, data in files.items():
            crc = zlib.crc32(data) & 0xFFFFFFFF
            uncomp_size = len(data)
            comp_obj = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-15)
            comp_data = comp_obj.compress(data) + comp_obj.flush()
            
            enc = ZipEncrypter(pwd)
            rand_bytes = os.urandom(11)
            check_byte = bytes([(crc >> 24) & 0xFF])
            header = rand_bytes + check_byte
            enc_header = enc.encrypt(header)
            enc_data = enc.encrypt(comp_data)
            comp_size = len(enc_header) + len(enc_data)
            
            local_offset = offset
            arc_bytes = arcname.encode('utf-8')
            lh = struct.pack('<4sHHHHHIIIHH',
                b'PK\x03\x04',
                20,
                1, # encrypted
                8, # deflated
                0x4500, 0x5500,
                crc,
                comp_size,
                uncomp_size,
                len(arc_bytes),
                0
            )
            f.write(lh)
            f.write(arc_bytes)
            f.write(enc_header)
            f.write(enc_data)
            offset += len(lh) + len(arc_bytes) + comp_size
            entries.append((arcname, crc, comp_size, uncomp_size, local_offset))
            
        cd_start = offset
        for arcname, crc, comp_size, uncomp_size, local_offset in entries:
            arc_bytes = arcname.encode('utf-8')
            cdh = struct.pack('<4sHHHHHHIIIHHHHHII',
                b'PK\x01\x02',
                20, 20,
                1,
                8,
                0x4500, 0x5500,
                crc, comp_size, uncomp_size,
                len(arc_bytes), 0, 0, 0, 0, 0,
                local_offset
            )
            f.write(cdh)
            f.write(arc_bytes)
            offset += len(cdh) + len(arc_bytes)
            
        cd_len = offset - cd_start
        eocd = struct.pack('<4sHHHHIIH',
            b'PK\x05\x06',
            0, 0,
            len(entries), len(entries),
            cd_len, cd_start,
            0
        )
        f.write(eocd)
    print(f"[+] Created encrypted vault: {filename} (Password: {password})")

# Run builders
if __name__ == "__main__":
    create_incident_report_pdf("evidence_04")
    create_evidence_board("evidence_board.png")
    create_cam04_frame("cam04_frame.png")
    create_lab_photo("lab_photo.png")
    create_floor_blueprint("floor_blueprint.png")
    
    # Temp chime wav for packaging into vault
    os.makedirs("recordings", exist_ok=True)
    chime_path = "recordings/chime_transmission.wav"
    create_chime_wav(chime_path)
    
    # Vault internal files
    chime_grid_content = """================================================================================
NEXUS DYNAMICS // ACOUSTIC SURVEILLANCE & CHIME FREQUENCY GRID
Reference Standard: ISO-2026-ACOU / Task Force Audio Decryption Key
================================================================================

Chime Audio Tones (Pitch Levels 1 to 5):
[Tone 1] : 440.00 Hz (A4)
[Tone 2] : 523.25 Hz (C5)
[Tone 3] : 659.25 Hz (E5)
[Tone 4] : 783.99 Hz (G5)
[Tone 5] : 880.00 Hz (A5)

Grid Table [Row Pitch, Column Pitch]:
      [1]    [2]    [3]    [4]    [5]
[1]    A      B      C      D      E
[2]    F      G      H      I      K
[3]    L      M      N      O      P
[4]    Q      R      S      T      U
[5]    V      W      X      Y      Z

Note: Each letter is composed of two consecutive chime tones (Row Tone, Column Tone).
Audio Transmission File: recordings/chime_transmission.wav
"""

    audio_hint_content = """================================================================================
AUDIO SPECTRUM TELEMETRY LOG // INTERCEPTED CHIME BURST
================================================================================
Source: Gate B VoIP Relay / Buffer 09
Audio Duration: 10.5 seconds
Analyzed Sequence (Frequencies Detected in Hertz):

Pair 1:  [783.99 Hz, 659.25 Hz] -> (Row 4, Col 3) -> S
Pair 2:  [659.25 Hz, 783.99 Hz] -> (Row 3, Col 4) -> O
Pair 3:  [783.99 Hz, 659.25 Hz] -> (Row 4, Col 3) -> S
[Word Interval: 800ms silence]
Pair 4:  [440.00 Hz, 440.00 Hz] -> (Row 1, Col 1) -> A
Pair 5:  [440.00 Hz, 880.00 Hz] -> (Row 1, Col 5) -> E
Pair 6:  [783.99 Hz, 783.99 Hz] -> (Row 4, Col 4) -> T
Pair 7:  [523.25 Hz, 659.25 Hz] -> (Row 2, Col 3) -> H
Pair 8:  [440.00 Hz, 880.00 Hz] -> (Row 1, Col 5) -> E
Pair 9:  [783.99 Hz, 523.25 Hz] -> (Row 4, Col 2) -> R

Result Message: SOS AETHER
Combine with Stage 1 & Stage 2 keys in terminal to unlock Stage 4 physical coordinates.
"""

    stage3_dossier_content = """================================================================================
OPERATION AETHERFALL // STAGE 3 DOSSIER: COMBINING THE KEYS
================================================================================

Investigators:
You have penetrated the security perimeter and unlocked stage2_vault.zip using
the vehicle license plate KL-08-CC-4912.

To proceed to Stage 4 and retrieve the physical safehouse coordinates:
1. First Key Fragment (from main.py git commit history):
   AETHER_
2. Traitor Identification Passcode (from Issue 42 logs in incident report order: Date + Badge + Room):
   OCT2-9042-304
3. Full Combined Passcode:
   AETHER_OCT2-9042-304

Launch the investigation terminal (`python terminal.py` or open `index.html`)
and submit the full passcode to unlock Stage 4 map analysis.
"""

    with open(chime_path, 'rb') as f:
        wav_bytes = f.read()

    vault_files = {
        "recordings/chime_transmission.wav": wav_bytes,
        "chime_cipher_grid.txt": chime_grid_content.encode('utf-8'),
        "audio_spectrogram_hint.txt": audio_hint_content.encode('utf-8'),
        "stage3_dossier.txt": stage3_dossier_content.encode('utf-8')
    }

    create_encrypted_zip("stage2_vault.zip", vault_files, "KL-08-CC-4912")
    print("[+] All assets generated successfully.")
