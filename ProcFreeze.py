from win32com.client import DispatchWithEvents
from Tkinter import Tk

class handler:
    def __init__(self):
        self.whitelistAccount = ["BackupAdministrator"]
        self.whitelistProcess = ["csrss.exe","winlogon.exe","LogonUI.exe","explorer.exe"]
        self.bypassProcess = []
        self.prevProcess = []
        
    def OnProcessStarted(self, process):
        if process.UserName not in self.whitelistAccount and process.Name not in self.whitelistProcess and not len(set(self.bypassProcess)&set(self.prevProcess)):
            process.Terminate()
        self.prevProcess.append(process.Name)

    def OnProcessTerminated(self, process):
        self.prevProcess = []
      
manager = DispatchWithEvents('DeviareCOM.NktSpyMgr', handler)
manager.Initialize()

print "Freezing Processes"

root = Tk()
root.withdraw()
root.mainloop()
