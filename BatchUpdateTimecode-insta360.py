#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DaVinci Resolve Timecode Setter for Insta360 X4
Extracts HH:MM:SS from filename and sets as timecode
"""

import sys
import re

# Alternative import method for macOS
def GetResolve():
    try:
        # Windows/Linux method
        import DaVinciResolveScript as bmd
        return bmd.scriptapp("Resolve")
    except ImportError:
        # macOS method
        import imp
        dvr_script = imp.load_source('DaVinciResolveScript',
            '/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/DaVinciResolveScript.py')
        return dvr_script.scriptapp("Resolve")

# Get the current project and media pool
resolve = GetResolve()

if not resolve:
    print("ERROR: Could not connect to DaVinci Resolve")
    print("Make sure DaVinci Resolve is running")
    sys.exit(1)

projectManager = resolve.GetProjectManager()
currentProject = projectManager.GetCurrentProject()

if not currentProject:
    print("ERROR: No project is currently open")
    sys.exit(1)

mediaPool = currentProject.GetMediaPool()

# Get selected clips from the Media Pool
clips = mediaPool.GetSelectedClips()

if not clips:
    print("⚠ ERROR: No clips selected in Media Pool")
    print("Please select one or more clips and run the script again.")
else:
    print(f"Found {len(clips)} selected clip(s)")
    print("-" * 60)

    # Process each clip
    success_count = 0
    failed_count = 0

    for clip in clips:
        clip_name = clip.GetClipProperty('File Name')

        # Extract time from filename using regex
        # Pattern: VID_YYYYMMDD_HHMMSS_XX_XXX.mp4
        match = re.search(r'_(\d{6})_', clip_name)

        if not match:
            print(f"⚠ SKIPPED: {clip_name}")
            print(f" Could not find HH:MM:SS pattern in filename")
            failed_count += 1
            continue

        try:
            time_str = match.group(1)  # Extract HHMMSS

            # Convert HHMMSS to HH:MM:SS:00
            hours = time_str[0:2]
            minutes = time_str[2:4]
            seconds = time_str[4:6]
            new_timecode = f"{hours}:{minutes}:{seconds}:00"

            if clip.SetClipProperty('Start TC', new_timecode):
                print(f"✓ SUCCESS: {clip_name}")
                print(f" Extracted Time: {time_str} → {new_timecode}")
                success_count += 1
            else:
                print(f"✗ FAILED: {clip_name} - SetClipProperty returned False")
                failed_count += 1

        except Exception as e:
            print(f"✗ ERROR: {clip_name} - {str(e)}")
            failed_count += 1

    print("-" * 60)
    print(f"Processing complete:")
    print(f" Success: {success_count}")
    print(f" Failed: {failed_count}")
    print(f" Total: {len(clips)}")
