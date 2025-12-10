#!/usr/bin/env python3
"""
Multi-Language Code Typer - Windows Edition
Simulates human typing from clipboard
Perfectly preserves indentation for LeetCode content (Python, Java, C++, etc.)
Optimized for Windows operating system
Requires Python 3.7 or higher
"""

import pyperclip
import pyautogui
import time
import random
import sys
from typing import Optional

# Safety: Add a small delay between actions
pyautogui.PAUSE = 0.01

# Configuration
TYPING_SPEED_MIN = 0.01  # Minimum delay between characters (seconds)
TYPING_SPEED_MAX = 0.03  # Maximum delay between characters (seconds)
LINE_BREAK_DELAY = 0.06  # Additional delay for line breaks (increased for Java compatibility)
INDENT_DELAY = 0.01      # Delay for indentation


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
    NOTE: Newlines are handled in type_with_indentation(), not here.
    """
    # Random delay to simulate human typing
    delay = random.uniform(TYPING_SPEED_MIN, TYPING_SPEED_MAX)
    
    # Slightly longer delay after punctuation
    if prev_char and prev_char in '.,;:!?':
        delay += random.uniform(0.02, 0.05)
    
    time.sleep(delay)
    
    # Handle special characters
    if char == '\t':
        # Convert tabs to spaces (4 spaces)
        pyautogui.write('    ', interval=INDENT_DELAY)
    elif char == ' ':
        pyautogui.press('space')
    else:
        # Type the character
        pyautogui.write(char, interval=0)
        
        # LeetCode auto-completes brackets/quotes - delete the auto-completed character
        if char in '{[("\'':
            time.sleep(0.02)  # Small delay for auto-complete to trigger
            pyautogui.press('delete')  # Delete the auto-completed closing bracket
            # Extra delay after braces for Java (they affect auto-indent)
            if char == '{':
                time.sleep(0.01)


def type_with_indentation(text: str):
    """
    Type text character-by-character exactly as provided.
    Handles LeetCode's auto-indentation properly.
    Works for Python, Java, C++, JavaScript, and other languages.
    STRATEGY: After every Enter, wipe whatever auto-indent exists, then type the
    exact indentation from the source. Uses a temporary space so the newline
    itself is never deleted, even when no indent is needed (common in Java).
    """
    prev_char = None
    i = 0
    
    while i < len(text):
        char = text[i]
        
        # Special handling for newlines
        if char == '\n':
            # Look ahead to see how many spaces follow
            indent_count = 0
            j = i + 1
            while j < len(text) and text[j] == ' ':
                indent_count += 1
                j += 1
            
            # Type Enter
            pyautogui.press('enter')
            time.sleep(0.08)
            
            # Wait for LeetCode/IDE to apply its auto-indent
            time.sleep(0.12)
            
            # Insert a temporary space so we can safely select/backspace
            pyautogui.press('space')
            time.sleep(0.01)
            
            # Select from cursor back to start of line (auto-indent + temp space)
            pyautogui.keyDown('shift')
            time.sleep(0.01)
            pyautogui.press('home')
            time.sleep(0.03)
            pyautogui.keyUp('shift')
            time.sleep(0.01)
            
            # Delete the selection (removes auto-indent, preserves newline)
            pyautogui.press('backspace')
            time.sleep(0.04)
            
            # Stabilize cursor at column 0
            time.sleep(0.02)
            
            # Now type our correct indentation
            if indent_count > 0:
                for _ in range(indent_count):
                    pyautogui.press('space')
                    time.sleep(0.006)
            
            # Skip past the newline and spaces we just handled
            i = j
            prev_char = ' ' if indent_count > 0 else '\n'
        else:
            # Type regular characters normally
            human_type_char(char, prev_char)
            prev_char = char
            i += 1


def countdown(seconds: int = 2):
    """Countdown before starting to type."""
    print(f"Starting in {seconds} seconds...")
    for i in range(seconds, 0, -1):
        print(f"{i}...", end=' ', flush=True)
        time.sleep(1)
    print("\nTyping started! Switch to your target window now.")


def main():
    """Main function."""
    print("Multi-Language Code Typer - Windows Edition (LeetCode)")
    print("Supports: Python, Java, C++, JavaScript, and more")
    print("=" * 60)
    
    # Check Python version
    import platform
    python_version = sys.version_info
    if python_version < (3, 7):
        print(f"ERROR: Python 3.7 or higher is required.")
        print(f"Current version: {python_version.major}.{python_version.minor}.{python_version.micro}")
        sys.exit(1)
    
    # Check if running on Windows
    if platform.system() != 'Windows':
        print("WARNING: This script is optimized for Windows.")
        print(f"Detected OS: {platform.system()}")
        response = input("Continue anyway? (y/n): ").strip().lower()
        if response != 'y':
            print("Cancelled. Use the Mac/Linux version for other operating systems.")
            sys.exit(0)
    
    # Get content from clipboard
    print("Reading from clipboard...")
    content = get_clipboard_content()
    
    # Normalize indentation
    content = normalize_indentation(content)
    
    print(f"Content length: {len(content)} characters")
    print(f"Number of lines: {content.count(chr(10)) + 1}")
    print("\nPreview (first 200 chars):")
    print("-" * 50)
    print(content[:200] + ("..." if len(content) > 200 else ""))
    print("-" * 50)
    
    # Ask for confirmation
    response = input("\nProceed with typing? (y/n): ").strip().lower()
    if response != 'y':
        print("Cancelled.")
        sys.exit(0)
    
    # Countdown
    countdown(2)
    
    # Type the content
    try:
        type_with_indentation(content)
        print("\n✓ Typing completed!")
    except KeyboardInterrupt:
        print("\n\nTyping interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nError during typing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

