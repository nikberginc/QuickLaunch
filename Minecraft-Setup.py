#this will launch minecraft launcher and brave browser(default browser) with a specific URL
import psutil
import webbrowser
import subprocess
import time


#checks and opens Brave -- example.com
if "brave.exe" in (p.name() for p in psutil.process_iter()):
    print("Brave browser is already running... ")

else:
    webbrowser.open("https://example.com")


time.sleep(1)


#checks and opens Minecraft Launcher
if any(p.name() in ("MinecraftLauncher.exe", "Minecraft.Windows.exe") for p in psutil.process_iter()):
    print("some form of Minecraft is already running... ")

else:
    subprocess.Popen("explorer.exe shell:AppsFolder\\Microsoft.4297127D64EC6_8wekyb3d8bbwe!Minecraft")


time.sleep(1)


#checks and opens GlideX
if "GlideX.exe" in (p.name() for p in psutil.process_iter()):
    print("GlideX is already running... ")

else:
    subprocess.Popen("explorer.exe shell:AppsFolder\\B9ECED6F.Glidex_qmba6cd70vzyy!App")


