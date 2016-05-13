import wx
import threading
import time

import wx.lib.plot as plot

from Core.Info.performance import PerformanceInfo
from Core.Info.system import SystemInfo

threading._DummyThread._Thread__stop = lambda x: 42
p=PerformanceInfo()
s=SystemInfo()
########################################################################

########################################################################




########################################################################
class Prototype(wx.Frame):


      global tag

      #----------------------------------------------------------------------
      def __init__(self, parent, title):
           wx.Frame.__init__(self, None, title="Test Tools", size=(300,300))
           self.data = []
           self.tag=None
           self.UI()
           self.Centre()
           self.Show()

      #----------------------------------------------------------------------
      def UI(self):
           panel = wx.Panel(self,-1)
           vbox = wx.BoxSizer(wx.VERTICAL)
           hbox0 = wx.BoxSizer(wx.HORIZONTAL)
           l0 = wx.StaticText(panel, -1, "packName")
           hbox0.Add(l0, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           self.t0 = wx.TextCtrl(panel,size=(200,20),style =wx.TE_LEFT)
           hbox0.Add(self.t0,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           vbox.Add(hbox0)
           hbox1 = wx.BoxSizer(wx.HORIZONTAL)
           l1 = wx.StaticText(panel, -1, "catchTime")
           hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           self.t1 = wx.TextCtrl(panel)
           self.t1.SetMaxLength(3)
           hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           vbox.Add(hbox1)
           hbox2 = wx.BoxSizer(wx.HORIZONTAL)
           l2 = wx.StaticText(panel, -1, "lautchTime")
           hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5)
           self.t2 = wx.TextCtrl(panel)
           self.t2.SetMaxLength(10)
           hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           vbox.Add(hbox2)
           hbox3 = wx.BoxSizer(wx.HORIZONTAL)
           self.t3 = wx.TextCtrl(panel,size = (300,100),style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_CENTER)
           hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           vbox.Add(hbox3)
           hbox4 = wx.BoxSizer(wx.HORIZONTAL)
           self.btn1 = wx.Button(panel, label = "Start")
           self.btn2 = wx.Button(panel, label = "Clear")
           self.btn3 = wx.Button(panel, label = "Show")
           hbox4.Add(self.btn1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           self.btn1.Bind(wx.EVT_BUTTON, self.OnStart, self.btn1)
           hbox4.Add(self.btn2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           self.btn2.Bind(wx.EVT_BUTTON, self.OnClear, self.btn2)
           hbox4.Add(self.btn3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           self.btn3.Bind(wx.EVT_BUTTON, self.OnDraw, self.btn3)
           vbox.Add(hbox4)
           hbox5 = wx.BoxSizer(wx.HORIZONTAL)
           self.t4 = wx.TextCtrl(panel,size = (300,50),style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_CENTER)
           hbox5.Add(self.t4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
           vbox.Add(hbox5)
           panel.SetSizer(vbox)
           menuBar = wx.MenuBar()
           menu1 = wx.Menu()
           menu1.Append(101, "&CPU", "",wx.ITEM_RADIO)
           self.Bind(wx.EVT_MENU, self.Menu101, id=101)
           menu1.Append(102, "&MEM", "",wx.ITEM_RADIO)
           self.Bind(wx.EVT_MENU, self.Menu102, id=102)
           menu1.Append(103, "&TIME", "",wx.ITEM_RADIO)
           self.Bind(wx.EVT_MENU, self.Menu103, id=103)
           menu1.Append(104, "&FLOW", "",wx.ITEM_RADIO)
           self.Bind(wx.EVT_MENU, self.Menu104, id=104)
           menu1.AppendSeparator()
           menu1.Append(201, "&Close", "")
           self.Bind(wx.EVT_MENU, self.OnClose, id=201)
           # Add menu to the menu bar
           menuBar.Append(menu1, "&Performance")
           self.SetMenuBar(menuBar)
           self.Centre()
           self.Show()
      #----------------------------------------------------------------------

      def Menu101(self,event):
           self.tag="cpu"

      def Menu102(self,event):
           self.tag="mem"

      def Menu103(self,event):
           self.tag="time"

      def Menu104(self,event):
           self.tag="flow"

      def OnClose(self,event):
           self.Close()

      #----------------------------------------------------------------------
      def OnStart(self,event):
           #or isinstance(self.t1.GetValue().encode("utf-8"),str)
           self.t3.Clear()
           self.t4.Clear()
           self.data=[]
           if self.tag is None:
               dlg=wx.MessageDialog(None,"Please Select Performance", "Warining" ,wx.OK | wx.ICON_WARNING)
               if dlg.ShowModal()==wx.ID_OK:
                   return
           if self.t0.GetValue().encode("utf-8") is '' :
               dlg=wx.MessageDialog(None,"Please Entry packName", "Error" ,wx.OK | wx.ICON_ERROR)
               if dlg.ShowModal()==wx.ID_OK:
                    self.t1.Clear()
                    return
           if self.t1.GetValue().encode("utf-8") is '' :
               dlg=wx.MessageDialog(None,"Please Entry catchTime", "Error" ,wx.OK | wx.ICON_ERROR)
               if dlg.ShowModal()==wx.ID_OK:
                    self.t1.Clear()
                    return
           if self.t2.GetValue().encode("utf-8") is '' :
               dlg=wx.MessageDialog(None,"Please Entry lauchTime", "Error" ,wx.OK | wx.ICON_ERROR)
               if dlg.ShowModal()==wx.ID_OK:
                    self.t2.Clear()
                    return
           self.packageName=self.t0.GetValue()
           if self.tag=="mem":
               threading._start_new_thread(self.memTread,())
               threading._start_new_thread(self.typeMemAvg,())
           elif self.tag=="cpu":
               threading._start_new_thread(self.cpuTread,())
               threading._start_new_thread(self.typeCpuAvg,())
           elif self.tag=="time":
               dlg=wx.MessageDialog(None,"Sorry! Time is not dev.Wait for new version", "Info" ,wx.OK | wx.ICON_MASK)
               if dlg.ShowModal()==wx.ID_OK:
                    return
               #threading._start_new_thread(self.memTread,())
           else:
               dlg=wx.MessageDialog(None,"Sorry! Flow is not dev.Wait for new version", "Info" ,wx.OK | wx.ICON_ERROR)
               if dlg.ShowModal()==wx.ID_OK:
                    return



           #rint self.getAVG(self.t3.GetValue())
           #print self.getFlow()
      def typeMemAvg(self):
               time.sleep(int(self.t2.GetValue())+1)
               self.t4.SetValue("Mem avg is "+ str(self.getMemAvg(self.t3.GetValue())))

      def typeCpuAvg(self):
               time.sleep(int(self.t2.GetValue())+1)
               self.t4.SetValue("Cpu avg is "+ str(self.getCpuAvg(self.t3.GetValue())))

      def  OnClear(self,event):
           
           self.t3.Clear()
           self.data=[]

      def getFlow(self):
           if self.chargeDevice():
              raise Exception("device not found")
           sflow=p.getCurFlowFromProc(self.packageName)
           i=int(self.t2.GetValue())/int(self.t1.GetValue())
           while i>0:
               i=i-1
               time.sleep(int(self.t1.GetValue()))
           eflow=p.getCurFlowFromProc(self.packageName)
           flow=eflow-sflow
           return flow


      def memTread(self):
           i=int(self.t2.GetValue())/int(self.t1.GetValue())
           while i>0:
               i=i-1
               threading._start_new_thread(self.getMemData,())
               time.sleep(int(self.t1.GetValue()))

      def cpuTread(self):
           i=int(self.t2.GetValue())/int(self.t1.GetValue())
           while i>0:
               i=i-1
               threading._start_new_thread(self.getCpuData(),())
               time.sleep(int(self.t1.GetValue()))

      def chargeDevice(self):
          flag=False
          dlist=s.getDeviceIDlist()
          print dlist
          if len(dlist) ==0:
              flag=True
              return flag
          return flag



      def getMemData(self):
          tmp=p.getMemFromDump(self.packageName)
          if self.chargeDevice():
              raise Exception("device not found")
          if tmp == "error" :
              raise Exception(self.packageName+" is not found")
          else:
              self.data.append((self.getTextNo(),int(tmp)))
             # wx.CallAfter(self.t3.AppendText, tmp+"\n")
              self.t3.AppendText(tmp+"\n")


      def getTextNo(self):
          tmp=self.t3.GetValue().split("\n")
          l=len(tmp)
          return l

      def getCpuData(self):
           tmp=p.getCpuFromDump(self.packageName)
           if self.chargeDevice():
              raise Exception("device not found")
           if tmp =='':
               raise Exception(self.packageName+" is not found")
           else:
               self.data=tmp[0]
               self.t3.AppendText(tmp[0]+"\n")




      def getMemAvg(self,value):
           if value is None or "":
               raise Exception('value is none')
           else:
               tmp=value.split("\n")
               temp=tmp[:len(tmp)-1]
               sum=0
               for x in temp:
                    sum=sum+int(x)
               avg=sum/len(temp)
               return avg

      def getCpuAvg(self,value):
           if value is None or "":
               raise Exception('value is none')
           else:
               tmp=value.split("\n")
               temp=tmp[:len(tmp)-1]
               sum=0.0
               for x in temp:
                    j=x.split("%")[0]
                    sum=sum+float(j)
               avg=str(sum/len(temp))+"%"
               return avg


      def OnDraw(self, event):

           frm = wx.Frame(self, -1, 'demo', size=(600, 450))
           client = plot.PlotCanvas(frm)
           line = plot.PolyLine(self.data, colour='pink', width=5, \
                             legend='value')
           gc = plot.PlotGraphics([line], 'demo', 'X', 'Y')
           client.Draw(gc,xAxis=(0,self.getTextNo()),yAxis=(0,200000))
           frm.Show()

#----------------------------------------------------------------------
app = wx.App(False)
desiredSize = wx.Size(400,300)

Prototype(None, title='')
app.MainLoop()