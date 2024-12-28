class DataMaster():
    def __init__(self):
        self.sync = "#?#\n"
        self.sync_ok = "!"
        self.StartStream = "#A#\n"
        self.StopStream = "#S#\n"
        self.SynchChannel = 0

        self.msg = []

        self.XData = []
        self.YData = []

        self.FunctionMaster = [
            "RowData",
            "VoltageDisplay"
        ]

    def DecodeMsg(self):
        temp = self.RowMsg.decode('utf8')
        if len(temp) > 0:
            if "#" in temp:
                self.msg = temp.split("#")
                del self.msg[0]

    def GenChannels(self):
        self.Channels = [f"Ch{ch}" for ch in range(self.SynchChannel)]

    def buildYdata(self):
        for _ in range(self.SynchChannel):
            self.YData.append([])

    def ClearData(self):
        self.RowMsg = ""
        self.msg = []
        self.Ydata = []