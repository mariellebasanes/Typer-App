#!/usr/bin/env python3
"""
Multi-Language Code Typer - Windows Edition
Simulates human typing from clipboard
Perfectly preserves indentation for LeetCode content (Python, Java, C++, etc.)
Optimized for Windows operating system
"""

import pyperclip
import pyautogui
import time
import random
import sys
from typing import Optional

# Safety: Add a small delay between actions
pyautogui.PAUSE = 0.01

# Configuration - Default Mode (Fast & Reliable)
TYPING_SPEED_MIN = 0.05  # Minimum delay between characters (seconds)
TYPING_SPEED_MAX = 0.15  # Maximum delay between characters (seconds)
LINE_BREAK_DELAY = 0.15  # Additional delay for line breaks
INDENT_DELAY = 0.05      # Delay for indentation
AUTO_INDENT_WAIT = 0.15  # Wait time for LeetCode's auto-indent to trigger
SHIFT_HOME_DELAY = 0.03  # Delay after Shift+Home selection
BACKSPACE_DELAY = 0.03   # Delay after backspace
BRACKET_DELETE_DELAY = 0.02  # Delay for bracket auto-complete deletion

# Timing Presets
TIMING_PRESETS = {
    'fast': {
        'LINE_BREAK_DELAY': 0.12,
        'AUTO_INDENT_WAIT': 0.12,
        'SHIFT_HOME_DELAY': 0.02,
        'BACKSPACE_DELAY': 0.02,
        'description': 'Fast mode - works on most modern systems'
    },
    'normal': {
        'LINE_BREAK_DELAY': 0.15,
        'AUTO_INDENT_WAIT': 0.15,
        'SHIFT_HOME_DELAY': 0.03,
        'BACKSPACE_DELAY': 0.03,
        'description': 'Normal mode - balanced speed and reliability (Default)'
    },
    'safe': {
        'LINE_BREAK_DELAY': 0.25,
        'AUTO_INDENT_WAIT': 0.30,
        'SHIFT_HOME_DELAY': 0.05,
        'BACKSPACE_DELAY': 0.05,
        'description': 'Safe mode - for slower systems or experiencing issues'
    },
    'ultra_safe': {
        'LINE_BREAK_DELAY': 0.35,
        'AUTO_INDENT_WAIT': 0.40,
        'SHIFT_HOME_DELAY': 0.08,
        'BACKSPACE_DELAY': 0.08,
        'description': 'Ultra Safe mode - maximum reliability, slower typing'
    }
}


def get_clipboard_content() -> str:
    """Get content from clipboard."""
    try:
        content = pyperclip.paste()
        if not content:
            print("Clipboard is empty!")
            sys.exit(1)
        return content
    except Exception as e:
        print(f"Error reading clipboard: {e}")
        sys.exit(1)


def normalize_indentation(text: str) -> str:
    """
    Normalize indentation to spaces (standard for most languages).
    Converts tabs to 4 spaces and preserves relative indentation.
    Works for Python, Java, C++, JavaScript, and other languages.
    """
    lines = text.split('\n')
    normalized_lines = []
    
    for line in lines:
        # Count leading whitespace (both spaces and tabs)
        stripped = line.lstrip()
        leading = line[:len(line) - len(stripped)]
        
        # Convert tabs to 4 spaces
        leading_normalized = leading.replace('\t', '    ')
        
        # Reconstruct line with normalized indentation
        normalized_lines.append(leading_normalized + stripped)
    
    return '\n'.join(normalized_lines)


def human_type_char(char: str, prev_char: Optional[str] = None):
    """
    Type a single character with human-like variation.
    Handles special characters, indentation, and auto-complete properly.
    """
    # Random delay to simulate human typing
    delay = random.uniform(TYPING_SPEED_MIN, TYPING_SPEED_MAX)
    
    # Longer delay after punctuation
    if prev_char and prev_char in '.,;:!?':
        delay += random.uniform(0.1, 0.3)
    
    time.sleep(delay)
    
    # Handle special characters
    if char == '\n':
        pyautogui.press('enter')
        time.sleep(LINE_BREAK_DELAY)
    elif char == '\t':
        # Convert tabs to spaces (4 spaces)
        pyautogui.write('    ', interval=INDENT_DELAY)
    elif char == ' ':
        pyautogui.press('space')
    else:
        # Type the character
        pyautogui.write(char, interval=0)
        
        # LeetCode auto-completes brackets/quotes - delete the auto-completed character
        if char in '{[("\'':
            time.sleep(BRACKET_DELETE_DELAY)  # Small delay for auto-complete to trigger
            pyautogui.press('delete')  # Delete the auto-completed closing bracket


def type_with_indentation(text: str):
    """
    Type text character-by-character exactly as provided.
    Handles LeetCode's auto-indentation properly with improved reliability.
    Works for Python, Java, C++, JavaScript, and other languages.
    """
    prev_char = None
    i = 0
    
    while i < len(text):
        char = text[i]
        
        # Type the character
        human_type_char(char, prev_char)
        prev_char = char
        i += 1
        
        # After a newline, handle indentation specially
        if char == '\n' and i < len(text):
            # Count how many spaces follow the newline (our desired indentation)
            indent_count = 0
            j = i
            while j < len(text) and text[j] == ' ':
                indent_count += 1
                j += 1
            
            # If there's indentation coming, clear LeetCode's auto-indent and type ours
            if indent_count > 0:
                # Wait for LeetCode to apply auto-indent (configurable timing)
                time.sleep(AUTO_INDENT_WAIT)
                
                # Method 1: Use Shift+Home to select auto-indent
                # This selects from cursor backwards to line start
                pyautogui.hotkey('shift', 'home')
                time.sleep(SHIFT_HOME_DELAY)
                
                # Delete the selected auto-indentation
                pyautogui.press('backspace')
                time.sleep(BACKSPACE_DELAY)
                
                # Type our correct indentation
                pyautogui.write(' ' * indent_count, interval=0.01)
                
                # Skip the spaces we just handled
                i = j
            else:
                # No indentation needed, but still wait a bit for stability
                time.sleep(0.05)


def countdown(seconds: int = 5):
    """Countdown before starting to type."""
    print(f"\n⏱️  Starting in {seconds} seconds... Switch to LeetCode editor now!")
    for i in range(seconds, 0, -1):
        print(f"   {i}...", end=' ', flush=True)
        time.sleep(1)
    print("\n\n🚀 Typing started! Do not touch your keyboard or mouse...\n")


def apply_timing_preset(preset_name: str):
    """Apply a timing preset configuration."""
    global LINE_BREAK_DELAY, AUTO_INDENT_WAIT, SHIFT_HOME_DELAY, BACKSPACE_DELAY
    
    preset = TIMING_PRESETS.get(preset_name, TIMING_PRESETS['normal'])
    LINE_BREAK_DELAY = preset['LINE_BREAK_DELAY']
    AUTO_INDENT_WAIT = preset['AUTO_INDENT_WAIT']
    SHIFT_HOME_DELAY = preset['SHIFT_HOME_DELAY']
    BACKSPACE_DELAY = preset['BACKSPACE_DELAY']
    
    print(f"✓ Applied '{preset_name}' mode: {preset['description']}")


def main():
    """Main function."""
    print("=" * 70)
    print("  Multi-Language Code Typer - Windows Edition (LeetCode)")
    print("  Supports: Python, Java, C++, JavaScript, and more")
    print("=" * 70)
    
    # Check if running on Windows
    import platform
    if platform.system() != 'Windows':
        print("\n⚠️  WARNING: This script is optimized for Windows.")
        print(f"Detected OS: {platform.system()}")
        response = input("Continue anyway? (y/n): ").strip().lower()
        if response != 'y':
            print("Cancelled. Use the Mac/Linux version for other operating systems.")
            sys.exit(0)
    
    # Timing mode selection
    print("\n📊 TIMING MODE SELECTION")
    print("-" * 70)
    print("Choose a mode (especially if you're experiencing one-liner issues):\n")
    print("  1. Fast Mode     - Works on most modern systems (fastest)")
    print("  2. Normal Mode   - Balanced speed and reliability (DEFAULT) ⭐")
    print("  3. Safe Mode     - For slower systems or one-liner issues")
    print("  4. Ultra Safe    - Maximum reliability (slowest, but most reliable)")
    print()
    
    mode_choice = input("Select mode [1-4] or press Enter for Normal (2): ").strip()
    
    mode_map = {
        '1': 'fast',
        '2': 'normal',
        '3': 'safe',
        '4': 'ultra_safe',
        '': 'normal'  # Default
    }
    
    selected_mode = mode_map.get(mode_choice, 'normal')
    apply_timing_preset(selected_mode)
    print()
    
    # Get content from clipboard
    print("📋 Reading from clipboard...")
    content = get_clipboard_content()
    
    # Normalize indentation
    content = normalize_indentation(content)
    
    print(f"✓ Content loaded successfully!")
    print(f"   - Length: {len(content)} characters")
    print(f"   - Lines: {content.count(chr(10)) + 1}")
    print("\n📄 Preview (first 200 chars):")
    print("-" * 70)
    print(content[:200] + ("..." if len(content) > 200 else ""))
    print("-" * 70)
    
    # Important tips
    print("\n💡 IMPORTANT TIPS:")
    print("   • Clear your LeetCode editor completely before starting")
    print("   • Position cursor at the beginning of the editor")
    print("   • Don't touch keyboard/mouse while typing is in progress")
    print("   • Press Ctrl+C anytime to stop")
    
    # Ask for confirmation
    response = input("\n▶️  Proceed with typing? (y/n): ").strip().lower()
    if response != 'y':
        print("Cancelled.")
        sys.exit(0)
    
    # Countdown
    countdown(5)
    
    # Type the content
    try:
        type_with_indentation(content)
        print("\n✅ Typing completed successfully!")
        print("\nIf the output looks incorrect:")
        print("   • Try a slower mode (Safe or Ultra Safe)")
        print("   • Make sure LeetCode editor was completely cleared")
        print("   • Check your browser performance (close other tabs)")
    except KeyboardInterrupt:
        print("\n\n⚠️  Typing interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error during typing: {e}")
        print("\nTroubleshooting:")
        print("   • Try running again with 'Safe Mode' or 'Ultra Safe Mode'")
        print("   • Ensure Python and dependencies are up to date")
        sys.exit(1)


if __name__ == "__main__":
    main()

