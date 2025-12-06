# LeetCode Typer - Multi-Language Code Typer

A Windows-optimized tool that simulates human typing from your clipboard, perfect for typing code into LeetCode or other coding platforms. Supports Python, Java, C++, JavaScript, and more!

## 🚀 Quick Start

### Option 1: One-Click Install & Run (Easiest)
1. Double-click **`INSTALL_AND_RUN.bat`**
2. Follow the prompts
3. Done! ✨

### Option 2: Manual Installation
1. Double-click **`setup.bat`** to install dependencies
2. Double-click **`run.bat`** to launch the app

## 📋 Requirements

- **Windows 10/11**
- **Python 3.7+** (Download from [python.org](https://www.python.org/downloads/))
  - ⚠️ During Python installation, check **"Add Python to PATH"**

## 🎯 How to Use

1. **Copy your code** to the clipboard (Ctrl+C)
2. **Run the application** using `run.bat` or `INSTALL_AND_RUN.bat`
3. **Review the preview** and confirm with `y`
4. **Switch to your target window** (e.g., LeetCode editor) during the 3-second countdown
5. **Sit back** and watch the code being typed automatically!

## ✨ Features

- ✅ **Multi-language support**: Python, Java, C++, JavaScript, and more
- ✅ **Perfect indentation**: Handles LeetCode's auto-indentation intelligently
- ✅ **Human-like typing**: Random delays and natural typing speed
- ✅ **Auto-complete handling**: Automatically manages LeetCode's bracket auto-completion
- ✅ **Safe and reliable**: Keyboard interrupt supported (Ctrl+C to stop)

## 📦 Dependencies

- `pyperclip` - Clipboard access
- `PyAutoGUI` - Keyboard automation

These are automatically installed by `setup.bat` or `INSTALL_AND_RUN.bat`.

## 🛠️ Files Overview

| File | Description |
|------|-------------|
| `INSTALL_AND_RUN.bat` | One-click installer and launcher |
| `setup.bat` | Install dependencies only |
| `run.bat` | Run the application |
| `FIX_ONE_LINER.bat` | 🔧 Fix for one-liner issue (automatic timing adjustment) |
| `multilanguage typer.py` | Main Python script |
| `requirements.txt` | Python dependencies list |
| `config_slow.txt` | Manual configuration for slower systems |

## ⚠️ Troubleshooting

### "Python is not installed" error
- Install Python from [python.org](https://www.python.org/downloads/)
- During installation, **check "Add Python to PATH"**
- Restart your computer after installation

### Dependencies won't install
- Check your internet connection
- Run Command Prompt as Administrator
- Manually run: `python -m pip install pyperclip pyautogui`

### Code appears as one line (one-liner issue)
**This happens when timing is too fast for your system/browser:**

**Solution 1 (Easiest):**
- When prompted "Experiencing one-liner issues? Increase delay?", type `y`
- This increases timing automatically

**Solution 2 (Manual):**
- Open `multilanguage typer.py`
- Find line ~23: `AUTO_INDENT_WAIT = 0.15`
- Change to: `AUTO_INDENT_WAIT = 0.25` or `0.3`
- Save and run again

**Solution 3 (Browser):**
- Try a different browser (Chrome, Firefox, Edge)
- Some browsers handle LeetCode's auto-indent differently

### Code indentation is wrong
- Make sure you're using the LeetCode editor (not a plain text editor)
- Clear the editor completely before running the script
- Ensure your source code has proper indentation
- Position cursor at the beginning of the editor

### Extra brackets appearing
- This is now handled automatically
- If still happening, make sure you're using the latest version
- Try increasing the delay (see one-liner solution above)

## 📝 Tips

- **Test with simple code first** before trying complex solutions
- **Clear the LeetCode editor** before starting
- **Position your cursor** at the beginning of the editor
- **Don't touch your keyboard/mouse** while the script is running

## 🔒 Safety

- The script only types what's in your clipboard
- Press **Ctrl+C** anytime to stop the typing
- A 3-second countdown gives you time to switch windows

## 💡 Best Practices

1. Format your code properly before copying
2. Use consistent indentation (spaces recommended)
3. Test on a blank notepad first if unsure
4. Keep your system responsive - close unnecessary applications

## 📄 License

Free to use for personal and educational purposes.

## 🤝 Support

If you encounter issues:
1. Check the Troubleshooting section above
2. Ensure Python and dependencies are installed correctly
3. Verify your code formatting in the clipboard

---

**Enjoy coding! 🎉**

