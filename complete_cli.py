from utils import *
def complete_endianness():
    return [Endianness.LSB, Endianness.MSB]
def complete_dataLength():
    return [DataLength.EIGHT, DataLength.NINE]
def complete_sync():
    return [Sync.Synchronous, Sync.Asynchronous]
def complete_hardwarecontrol():
    return [HardwareControl.HWC_NONE, HardwareControl.HWC_RTS, HardwareControl.HWC_CTS, HardwareControl.HWC_RTS]
def complete_transferdirection():
    return [TranferDirection.Trans_None, TranferDirection.Trans_RX, TranferDirection.Trans_TX, TranferDirection.Trans_TX_RX]
def complete_stopbit():
    return [StopBit.Stop_One, StopBit.Stop_Two, StopBit.Stop_Half, StopBit.Stop_OneandHalf]
def complete_paritybit():
    return [ParityBit.Par_Odd, ParityBit.Par_Even, ParityBit.Par_None]
