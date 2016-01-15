from win32com.client import DispatchWithEvents
from Tkinter import Tk

whitelist = []

class handler:
    def OnProcessStarted(self, process):
        if process.Name not in whitelist:
            process.Terminate()
      
manager = DispatchWithEvents('DeviareCOM.NktSpyMgr', handler)
manager.Initialize()

print "Freezing Processes"

root = Tk()
root.withdraw()
root.mainloop()
