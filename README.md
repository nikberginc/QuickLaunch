# QuickLaunch 🎮

**Completed:** October 31, 2025

QuickLaunch is a lightweight Windows automation utility developed in Python. The program was created to simplify my Minecraft gaming setup by automatically checking and launching multiple applications instead of opening each one manually.

The script checks whether specific applications are already running and attempts to launch them if they are not detected.

I developed this project to explore Python automation, process management, and launching Windows applications programmatically.

## Features

- **Automatic application launching:** Opens multiple applications through a single script.
- **Process detection:** Checks whether applications are already running before attempting to launch them.
- **Minecraft integration:** Launches Minecraft if neither Minecraft Launcher nor Minecraft for Windows is detected.
- **Browser integration:** Opens a predefined webpage when Brave Browser is not already running.
- **ASUS GlideX integration:** Automatically launches GlideX if it is not running.
- **Startup delays:** Uses short delays between application checks.
- **Simple configuration:** Application identifiers and website URLs can be modified directly in the Python code.
- **Lightweight execution:** Runs through the terminal without requiring a graphical interface.

## Requirements

- Windows 10 or Windows 11
- Python 3
- `psutil`
- The applications you want to launch must be installed.

The project also uses Python's built-in modules:

- `webbrowser`
- `subprocess`
- `time`

## Installation

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the directory containing `Minecraft-Setup.py`.
4. Install the required library:

   ```bash
   python -m pip install psutil
   ```

5. Run the program:

   ```bash
   python Minecraft-Setup.py
   ```

The script automatically checks the configured applications and attempts to launch any that are not already running.

## How to Use

The application does not require any additional user input.

Once executed, it performs the following actions:

1. Checks whether Brave Browser is running.
2. If Brave is not detected, opens the configured webpage in the system's default browser.
3. Waits one second.
4. Checks whether Minecraft Launcher or Minecraft for Windows is running.
5. If neither is detected, attempts to launch Minecraft through Windows.
6. Waits another second.
7. Checks whether ASUS GlideX is running.
8. If GlideX is not detected, attempts to launch it.

After all checks are completed, the script finishes execution.



## How It Works

### 1. Detecting Running Applications

The program uses the `psutil` library to inspect active processes.

For example, the following code checks whether Brave Browser is running:

```python
if "brave.exe" in (p.name() for p in psutil.process_iter()):
    print("Brave browser is already running... ")
```

If the specified process is detected, the program skips its corresponding launch command.

This helps avoid unnecessarily launching applications that are already open.

### 2. Opening a Website

If Brave Browser is not detected, the program uses Python's built-in `webbrowser` module:

```python
webbrowser.open("https://example.com")
```

This opens the specified website in the system's default browser.

**Note:** The default browser does not necessarily have to be Brave. The current script checks for Brave but uses Windows' default browser configuration when opening the website.

The website URL can be customized by editing the Python file.

### 3. Launching Minecraft

The script checks whether Minecraft Launcher or Minecraft for Windows is already running:

```python
if any(
    p.name() in ("MinecraftLauncher.exe", "Minecraft.Windows.exe")
    for p in psutil.process_iter()
):
    print("some form of Minecraft is already running... ")
```

If neither process is detected, the program attempts to launch Minecraft using a Windows application identifier.

```python
subprocess.Popen(
    "explorer.exe shell:AppsFolder\\Microsoft.4297127D64EC6_8wekyb3d8bbwe!Minecraft"
)
```

This command asks Windows Explorer to open the application registered under that identifier.

### 4. Launching ASUS GlideX

The program uses a similar approach for ASUS GlideX.

First, it checks whether the application is already running:

```python
if "GlideX.exe" in (p.name() for p in psutil.process_iter()):
    print("GlideX is already running... ")
```

If GlideX is not detected, the script attempts to start it using its Windows application identifier.

This allows the program to launch the application without manually locating its executable.

### 5. Startup Delays

The application uses:

```python
time.sleep(1)
```

This creates a one-second pause between application checks.

Although the launch commands are executed sequentially, the applications themselves can continue starting in the background.

## Project Structure

```text
QuickLaunch/
├── Minecraft-Setup.py
├── .gitignore
└── README.md
```

The project contains a single Python source file responsible for detecting and launching the configured applications.

## Known Limitations

- **Windows-specific:** The application launch commands rely on Windows Explorer and `shell:AppsFolder` identifiers.
- **Fixed application selection:** The script is currently configured for Brave, Minecraft, and ASUS GlideX.
- **Hardcoded configuration:** Changing the selected applications or website requires modifying the Python source code.
- **Process-name detection:** The program relies on executable names, which may differ between versions or installations.
- **Default-browser behavior:** The website opens in the system's default browser, not necessarily Brave.
- **Limited error handling:** The script does not comprehensively handle missing applications, inaccessible processes, or failed launch commands.
- **No graphical interface:** The application is controlled entirely through its Python script.

## Development Note

QuickLaunch was developed as a small personal automation project to make preparing for Minecraft gaming sessions faster and more convenient.

Although relatively simple, the project allowed me to experiment with detecting active processes, interacting with Windows applications, opening webpages, and automating repetitive computer tasks.

It demonstrates practical uses of Python libraries and basic operating-system automation.


**Author:** [Nik Berginc](https://github.com/nikberginc)
