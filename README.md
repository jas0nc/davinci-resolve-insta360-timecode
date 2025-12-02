# DaVinci Resolve Insta360 Timecode Batch Updater

Automatically extract and set timecode metadata from Insta360 video filenames in DaVinci Resolve.

## Overview

This Python script automates the tedious process of setting timecode for Insta360 footage in DaVinci Resolve. Instead of manually entering timecode for each clip, the script intelligently parses the timestamp embedded in your Insta360 filenames and applies it as the Start Timecode in your media pool.

### Why This Matters

Insta360 videos follow a consistent naming convention that includes the filming date and precise time. This script leverages that metadata to automatically populate accurate timecode information, which is essential for:
- Syncing multi-camera footage
- Maintaining accurate timeline references
- Streamlining post-production workflows
- Batch processing large footage libraries

## Features

✅ **Automatic Timecode Extraction** - Parses HH:MM:SS from Insta360 filenames  
✅ **Batch Processing** - Update multiple clips in one operation  
✅ **Cross-Platform Support** - Works on Windows, macOS, and Linux  
✅ **Error Handling** - Detailed logging for successful and failed operations  
✅ **Non-Destructive** - Only modifies timecode metadata, not media files  
✅ **User-Friendly Output** - Clear feedback on what was processed  

## Filename Pattern

This script works with Insta360 filenames in this format:

```
VID_YYYYMMDD_HHMMSS_XX_YYY.mp4
VID_20251130_104916_00_004.mp4
VID_20251130_111242_00_005.mp4
VID_20251130_133049_00_016_017.mp4
```

Where:
- `YYYYMMDD` = Date (film date)
- `HHMMSS` = Time in 24-hour format (this becomes your timecode)
- `XX` = Audio channel indicator
- `YYY` = Clip sequence number

## Requirements

- **DaVinci Resolve** (version 18.0 or later recommended)
- **Python 3.6+** (typically included with DaVinci Resolve)
- Media clips in your DaVinci Resolve project with Insta360 naming convention

## Installation

### Step 1: Locate Your Scripts Folder

**Windows:**
```
%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility
```
Quick access: Press `Win + R`, paste the path above, press Enter

**macOS:**
```
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility
```
Quick access: Open Finder → `Cmd + Shift + G` → paste the path above

**Linux:**
```
~/.local/share/DaVinciResolve/Fusion/Scripts/Utility
```

### Step 2: Download and Save the Script

1. Download `BatchUpdateTimecode_Insta360.py` from this repository
2. Place it in the `Utility` folder (see Step 1)
3. Restart DaVinci Resolve completely

### Step 3: Verify Installation

1. Open DaVinci Resolve
2. Go to **Workspace → Scripts → Utility**
3. You should see "BatchUpdateTimecode_Insta360" in the menu

## Usage

1. **Import Your Footage**
   - Import Insta360 video files into your DaVinci Resolve Media Pool
   - Ensure filenames follow the `VID_YYYYMMDD_HHMMSS_XX_YYY.mp4` pattern

2. **Select Clips**
   - In the Media Pool, select one or more clips you want to update
   - You can multi-select by holding `Ctrl` (Windows) or `Cmd` (macOS)

3. **Run the Script**
   - Go to **Workspace → Scripts → Utility → BatchUpdateTimecode_Insta360**
   - The script will process your selected clips

4. **Review Results**
   - Check the script output in the console for success/failure messages
   - Verify timecode was applied correctly (check **Clip Properties**)

### Example Output

```
Found 3 selected clip(s)
------------------------------------------------------------
✓ SUCCESS: VID_20251130_104916_00_004.mp4
  Extracted Time: 10:49:16
  New Timecode: 10:49:16:00

✓ SUCCESS: VID_20251130_111242_00_005.mp4
  Extracted Time: 11:12:42
  New Timecode: 11:12:42:00

✓ SUCCESS: VID_20251130_133049_00_016_017.mp4
  Extracted Time: 13:30:49
  New Timecode: 13:30:49:00

------------------------------------------------------------
Processing complete:
 Success: 3
 Failed: 0
 Total: 3
```

## Troubleshooting

### Script Doesn't Appear in Menu

- **Solution 1:** Ensure the script is in the correct `Utility` subfolder (not just the parent `Scripts` folder)
- **Solution 2:** Restart DaVinci Resolve completely
- **Solution 3:** Check file extension is `.py` (not `.txt`)

### "No Clips Selected" Error

- Make sure you have clips selected in the Media Pool
- Click on a clip to highlight it before running the script

### Timecode Not Updating

- Verify your filenames match the Insta360 pattern: `VID_YYYYMMDD_HHMMSS_XX_YYY.mp4`
- Check that the date/time portion is valid (not corrupted filenames)
- Ensure clips are stored in the Media Pool (not just in bins on the timeline)

### "Could Not Connect to DaVinci Resolve"

- Make sure DaVinci Resolve is open and running
- Try restarting DaVinci Resolve
- Check that Python scripting is enabled in Preferences

## How It Works

The script performs these steps:

1. **Connects to DaVinci Resolve** via the Scripting API
2. **Gets Selected Clips** from your Media Pool
3. **Parses Filename** using regex to extract the HHMMSS timestamp
4. **Converts Timecode** from HHMMSS to HH:MM:SS:00 format (DaVinci Resolve standard)
5. **Sets Start TC** property on each clip
6. **Reports Results** with detailed success/failure information

## Technical Details

### Timecode Format

- **Input:** `HHMMSS` (e.g., `104916` = 10:49:16)
- **Output:** `HH:MM:SS:00` (e.g., `10:49:16:00`)
- The `:00` represents frames at 24fps (DaVinci Resolve standard)

### Regex Pattern

```python
r'VID_\d{8}_(\d{2})(\d{2})(\d{2})_\d{2}_\d{3}'
```

This extracts the first occurrence of 6 consecutive digits after the date.

## Platform-Specific Notes

### Windows
- Uses standard environment variables for path resolution
- Supports both user-level and system-level script installations

### macOS
- Requires special import method for DaVinciResolveScript module
- May need full disk access permissions for script access

### Linux
- Works with DaVinci Resolve installation in standard locations
- Supports both user (`~/.local/share`) and system (`/opt/resolve`) paths

## Related Resources

- [DaVinci Resolve Python API Documentation](https://www.blackmagicdesign.com/developer/product/davinci-resolve/)
- [DaVinci Resolve Official Support](https://www.blackmagicdesign.com/support/)
- [Insta360 Official Documentation](https://www.insta360.com/)

## Contributing

Found a bug or have suggestions? Feel free to open an issue or submit a pull request!

## License

This script is provided as-is for personal and commercial use. Modify and distribute as needed.

## Disclaimer

This script modifies metadata in your DaVinci Resolve project. Always test on a backup project first. The author is not responsible for any data loss or project corruption.

---

**Happy editing! 🎬**