from win32com.client import DispatchWithEvents
from Tkinter import Tk

whitelist = []

class handler:
    def OnProcessStarted(self, process):
        print "{} started {}({})\n".format(process.UserName,process.Name,process.Id)
        
    def OnProcessTerminated(self, process):
        print "\t\t\t\t\t\t{}({})\n".format(process.Name,process.Id)
      
manager = DispatchWithEvents('DeviareCOM.NktSpyMgr', handler)
manager.Initialize()

root = Tk()
root.withdraw()
root.mainloop()
