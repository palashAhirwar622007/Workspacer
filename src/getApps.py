import psutil as psu
import win32gui as w32g
import win32process as w32p

# Blacklist of background/system apps to filter out
BACKGROUND_APPS = {
    'PowerToys.QuickAccess.exe',
    'NVIDIA Overlay.exe',
    'Nahimic3.exe',
    'ApplicationFrameHost.exe',
    'TextInputHost.exe',
    'explorer.exe',
    'svchost.exe',
    'csrss.exe',
    'lsass.exe',
    'wininit.exe',
    'services.exe',
    'lsm.exe',
    'dwm.exe',
    'taskhostw.exe',
    'conhost.exe',
    'spoolsv.exe',
    'rundll32.exe',
    'SearchIndexer.exe',
    'MicrosoftEdgeUpdate.exe',
    'RuntimeBroker.exe',
    'sihost.exe',
    'CTAudioService.exe',
    'WmiPrvSE.exe',
    'Microsoft.CmdPal.UI.exe',
}

def getRunningApps():
    appNames = []
    appPaths = []
    
    def callback(hwnd, extra):
        if w32g.IsWindowVisible(hwnd):
            title = w32g.GetWindowText(hwnd)
            if title:
                try:
                    _, pid = w32p.GetWindowThreadProcessId(hwnd)
                    proc = psu.Process(pid)
                    app_name = proc.name()

                    app_path = proc.exe()

                    if app_name not in BACKGROUND_APPS:
                        appNames.append(app_name)
                        appPaths.append(app_path)
                except:
                    pass
        return True
    
    w32g.EnumWindows(callback, None)
    # return list(apps)
    return appNames, appPaths

def getPathsFromFile(filepath):
    """Get PATHS from saved workspace file"""

    paths = []

    with open(filepath) as f:
        for x in f:
            y = x.index(":")
            z = x[y+1:]
            paths.append(z.strip())
            # print(z)
    
    return paths

def getNamesFromFile(filepath):

    """Get NAMES from saved workspace file"""

    names = []

    with open(filepath) as f:
        for row in f:
            colonIndex = row.index(":")
            nam = row[:colonIndex]
            names.append(nam.strip())

    return names

