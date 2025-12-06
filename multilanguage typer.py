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

# Configuration
TYPING_SPEED_MIN = 0.05  # Minimum delay between characters (seconds)
TYPING_SPEED_MAX = 0.15  # Maximum delay between characters (seconds)
LINE_BREAK_DELAY = 0.1   # Additional delay for line breaks
INDENT_DELAY = 0.05      # Delay for indentation


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
            time.sleep(0.02)  # Small delay for auto-complete to trigger
            pyautogui.press('delete')  # Delete the auto-completed closing bracket


def type_with_indentation(text: str):
    """
    Type text character-by-character exactly as provided.
    Handles LeetCode's auto-indentation properly.
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
                # Wait for LeetCode to apply auto-indent
                time.sleep(0.12)
                
                # Clear auto-indentation using Ctrl+A on the line, then retype
                # Select from current position to start of line
                pyautogui.hotkey('shift', 'home')
                time.sleep(0.02)
                
                # Delete selection (only whitespace should be selected)
                pyautogui.press('backspace')
                time.sleep(0.02)
                
                # Type our correct indentation
                pyautogui.write(' ' * indent_count, interval=0.01)
                
                # Skip the spaces we just handled
                i = j


def countdown(seconds: int = 3):
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
    
    # Check if running on Windows
    import platform
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
    countdown(3)
    
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

