from win32com.client import DispatchWithEvents
from Tkinter import Tk

class handler:
    def __init__(self):
        self.whitelistAccount = ["BackupAdministrator"]
        self.whitelistProcess = ["csrss.exe","winlogon.exe","LogonUI.exe","explorer.exe"]
        
    def OnProcessStarted(self, process):
        if process.UserName not in self.whitelistAccount and process.Name not in self.whitelistProcess:
            process.Terminate()

    def OnProcessTerminated(self, process):
        self.prevProcess = []
      
manager = DispatchWithEvents('DeviareCOM.NktSpyMgr', handler)
manager.Initialize()

print "Freezing Processes"

root = Tk()
root.withdraw()
root.mainloop()
