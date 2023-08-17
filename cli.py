import typer
from typing import Optional
from utils import *
from UserInterface import UserInterface
from complete_cli import *
ui = None 
app = typer.Typer()
def CheckIntInput(input, str):
    for i in input:
        if not (i >= '0' and i <= '9'):
            ret = TestStandResult.NOT_ALLOWED
            print(ret.name, "value for" ,str,", should be interger")
            return ret
    return TestStandResult.OK

def openConfig():
    f = open("config.txt", "r")
    Lines = f.readlines()
    arr=[]
    for line in Lines:
        if not line:
            break
        val = "{}".format(line.strip())
        arr.append(val)

    if not arr:
        res:TestStandResult = TestStandResult.FAILURE
        print(res.name)
        f.close()
        return res
    f.close()
    return arr

def CheckHexIntInput(arr, str):
    size_arr = len(arr)
    if size_arr >= 2:
        first_part:str = arr[0] + arr[1]
        #check if hex
        if first_part == "0x" or first_part == '0X':
            if len(arr) < 3:
                ret =  TestStandResult.NOT_ALLOWED
                print(ret.name, "size too small of", str, " for hex value")
                return ret
            for i in range (2,len(arr)):
                if not ( (arr[i] >= '0' and arr[i] <= '9') or \
                        (arr[i] >= 'a' and arr[i] <='f') or \
                        (arr[i] >= 'A' and arr[i] <= 'F') ):
                    ret = TestStandResult.NOT_ALLOWED
                    print(ret.name, "value usb", str)
                    return ret
            ret = int(arr,16)
            return ret
    #value is int
    #value is also int but smaller than two
    ret = CheckIntInput(arr, str)
    if ret == TestStandResult.NOT_ALLOWED:
        print(ret.name, "value", str)
        return ret
    return int(arr,10)
                


    
@app.command()
def Setup(vid        = 0x0483, \
          pid        = 0x5740,\
          speed_usb  = 115200
        ):
    f = open("config.txt", "w")
    
    VID = PID = None
    ret = CheckHexIntInput(str(vid), "vid")
    if ret == TestStandResult.NOT_ALLOWED:
        f.close()
        return ret
    VID = ret
    
    ret = CheckHexIntInput(str(pid), "pid")
    if ret == TestStandResult.NOT_ALLOWED:
        f.close()
        return ret
    PID = ret
    
    ret = CheckHexIntInput(str(speed_usb), "speed_usb")
    if ret == TestStandResult.NOT_ALLOWED:
        f.close()
        return ret
    #s = speed_usb
   
    string = str(VID)+'\n'+str(PID)+'\n'+str(speed_usb)+'\n'
    f.write(string)
    f.close()
    ret = TestStandResult.OK
    print(ret.name,':',string)
    return ret

@app.command()
def CONFIG_USART(type:int    = None ,
    speed:int       = None,  
    clk_output:int = None,
    clk_lastbit:int = None,     
    clk_phase:int = None, 
    clk_polarity:int = None, 
    oversampling: int = None, 
    hardware_control: int = None, 
    tr_dir: int = None, 
    enable: int = None, 
    endianness_: int = None, 
    sync: int = None, 
    stop_bits: int = None, 
    parity_bit: int = None,
    datalenght: int = None
    ):
    type_:CONFIG = None
    clkOutput:Clockoutput = None
    clkLastbit:LastClockpulse = None
    clkPhase:Clockphase = None
    clkPolarity:Clockpolarity = None 
    overSampling:Oversampling = None
    hardwareControl:HardwareControl = None
    trDir: TranferDirection = None
    endianness_:Endianness = None
    sync_:Sync = None
    stopBits:StopBit = None
    parityBit:ParityBit = None
    dataLenght:DataLength = None

    if(type != None):
        if type >= 1 and type <= 4:
            type_ = CONFIG(type)
            print(type_.name)
        else:
            ret = TestStandResult.NOT_ALLOWED
            return ret
    if(speed != None):
        if(speed <= 0 or speed > 0xffffffff):
            ret = TestStandResult.NOT_ALLOWED
            print("speed cant be lower than 0")
            return ret
        else:
            print("speed: ", speed)
    if(clk_output != None):
        if(clk_output == 0 or clk_output == 1):
            clkOutput:Clockoutput = Clockoutput(clk_output)
            print("clk_output: ",clkOutput.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for clk_output")
            return TestStandResult.NOT_ALLOWED
    if(clk_lastbit != None):
        if(clk_lastbit == 0 or clk_lastbit == 1):
            clkLastbit = LastClockpulse(clk_lastbit)
            print("clock last bit: ",clkLastbit.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for clk last bit")
            return TestStandResult.NOT_ALLOWED
    if(clk_phase != None):
        if(clk_phase == 0 or clk_phase == 1):
            clkPhase = Clockphase(clk_phase)
            print("clock phase: ",clkPhase.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for clk phase")
            return TestStandResult.NOT_ALLOWED
    if(clk_polarity != None):
        if(clk_polarity == 0 or clk_polarity == 1):
            clkPolarity = Clockpolarity(clk_polarity)
            print("clock phase: ",clkPolarity.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for clkPolarity")
            return TestStandResult.NOT_ALLOWED
    if(oversampling != None):
        if(oversampling == 0 or oversampling == 1):
            overSampling = Oversampling(oversampling)
            print("clock phase: ",overSampling.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for oversampling")
            return TestStandResult.NOT_ALLOWED
    if(hardware_control != None):
        if(hardware_control == 0 or hardware_control == 1):
            hardwareControl = Clockoutput(hardware_control)
            print("clock phase: ",hardwareControl.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for hardwareControl")
            return TestStandResult.NOT_ALLOWED
    if(tr_dir != None):
        if(tr_dir >= 0 and tr_dir <= 3):
            trDir = TranferDirection(tr_dir)
            print("clock phase: ",trDir.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for trdir")
            return TestStandResult.NOT_ALLOWED
    if(enable != None):
        if(enable == 0 or enable == 1):
            print("enable: ",enable)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for enable")
            return TestStandResult.NOT_ALLOWED
    if(endianness_ != None):
        if(endianness_ == 0 or endianness_ == 1):
            endianness = Endianness(endianness_)
            print("clock phase: ",endianness.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for endianness")
            return TestStandResult.NOT_ALLOWED
    if(sync != None):
        if(sync == 0 or sync == 1):
            sync_ = Sync(sync)
            print("clock phase: ",sync_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for sync")
            return TestStandResult.NOT_ALLOWED
    if(stop_bits != None):
        if(stop_bits == 0 or stop_bits == 1):
            stopBits = StopBit(stop_bits)
            print("clock phase: ",stopBits.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for stop bits")
            return TestStandResult.NOT_ALLOWED

    if(parity_bit != None):
        if(parity_bit >= 0 or parity_bit <= 4):
            parityBit = ParityBit(parity_bit)
            print("clock phase: ",parityBit.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for parity bit")
            return TestStandResult.NOT_ALLOWED
    
    if(datalenght != None):
        if(datalenght == 0 or datalenght == 1):
            dataLenght = DataLength(datalenght)
            print("clock phase: ",dataLenght.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for data lenght")
            return TestStandResult.NOT_ALLOWED

    arr=openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.ConfigUSART(type_, speed, clkOutput, clkLastbit, clkPhase, \
        clkPolarity, overSampling, hardwareControl, trDir, enable,endianness_, sync_, stopBits, \
        parityBit, dataLenght)
    
@app.command()
def CONFIG_SPI(
        role:int=None,
        direction:int=None,
        datalength:int=None,
        clk_pol:int = None,
        clk_phase:int = None,
        nss:int = None,
        baudpre:int = None,
        endianness:int = None,
        ti_mode:int = None,
        enable:int = None,
    ):
    role_:Role = None
    direction_:SPI_direction = None
    dataLength:SPI_DataLength = None
    clkPol:Clockpolarity = None
    clkPhase:Clockphase = None
    nss_:NSS = None
    endianness_:Endianness = None
    baudPre:Baud_prescaler = None
    tiMode:TI_mode = None

    if(ti_mode != None):
        if(ti_mode == 0 or ti_mode == 1):
            tiMode = TI_mode(ti_mode)
            print("tiMode: ",tiMode.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for tiMode")
            return TestStandResult.NOT_ALLOWED
    if(role != None):
        if(role == 0 or role == 1):
            role_ = Role(role)
            print("role: ",role_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for role")
            return TestStandResult.NOT_ALLOWED
    if(nss != None):
        if(nss >= 0 and nss <=2):
            nss_ = NSS(nss)
            print("nss: ",nss_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for nss")
            return TestStandResult.NOT_ALLOWED
    if(baudpre != None):
        if(baudpre >= 0 and baudpre <=7):
            baudPre = Baud_prescaler(baudpre)
            print("baudpre: ",baudPre.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for baud prescaler")
            return TestStandResult.NOT_ALLOWED
    if(clk_phase != None):
        if(clk_phase == 0 or clk_phase == 1):
            clkPhase = Clockphase(clk_phase)
            print("clock phase: ",clkPhase.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for clk phase")
            return TestStandResult.NOT_ALLOWED
    if(clk_pol != None):
        if(clk_pol == 0 or clk_pol == 1):
            clkPol = Clockpolarity(clk_pol)
            print("clock pol: ",clkPol.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for clkPolarity")
            return TestStandResult.NOT_ALLOWED
   
    if(direction != None):
        if(direction >= 0 and direction <= 2):
            direction_ = SPI_direction(direction)
            print("direction: ",direction_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for trdir")
            return TestStandResult.NOT_ALLOWED
    if(enable != None):
        if(enable == 0 or enable == 1):
            print("enable: ",enable)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for enable")
            return TestStandResult.NOT_ALLOWED
    if(endianness != None):
        if(endianness == 0 or endianness == 1):
            endianness_ = Endianness(endianness)
            print("endianness: ",endianness_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for endianness")
            return TestStandResult.NOT_ALLOWED
    
    if(datalength != None):
        if(datalength == 0 or datalength == 1):
            dataLength = SPI_DataLength(datalength)
            print("clock phase: ",dataLength.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for data lenght")
            return TestStandResult.NOT_ALLOWED

    arr=openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.ConfigSPI(role_, direction_, dataLength, clkPol, clkPhase, nss_, \
        baudPre, endianness_,tiMode,enable)

@app.command()
def CONFIG_I2C(
        speed:int = None,
        own_addr:int = None,
        own_addr2:int = None,
        duty_cycle:int = None,
        role:int=None,
        addressing:int=None,
        dual:int=None,
        general_call:int=None,
        no_stretch:int=None,
        enable:int=None
    ):
    dutyCycle:Dutycycle = None
    role_:Role=None
    addressing_:I2C_addressing=None
    dual_:I2C_dualaddressing=None
    generalCall:I2C_generalcall=None
    noStretch:I2C_nostretch=None

    if(speed != None):
        if(speed <= 0 or speed > 0xffffffff):
            print(TestStandResult.NOT_ALLOWED.name,"value for speed")
            return TestStandResult.NOT_ALLOWED
        else:
            print("speed:", speed)
    if(own_addr != None):
        if(own_addr <= 0 or own_addr > 0xffffffff):
            print(TestStandResult.NOT_ALLOWED.name,"value for own_addr")
            return TestStandResult.NOT_ALLOWED
        else:
            print("own addr:", own_addr)

    if(own_addr2 != None):
        if(own_addr2 <= 0 or own_addr2 > 0xffffffff):
            print(TestStandResult.NOT_ALLOWED.name,"value for own_addr")
            return TestStandResult.NOT_ALLOWED
        else:
            print("own addr2:", own_addr2)

    if(duty_cycle != None):
        if(duty_cycle == 0 or duty_cycle == 1):
            dutyCycle = Dutycycle(duty_cycle)
            print("duty cyle: ",dutyCycle.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for duty cycle")
            return TestStandResult.NOT_ALLOWED
    if(role != None):
        if(role == 0 or role == 1):
            role_ = Role(role)
            print("role: ",role_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for role")
            return TestStandResult.NOT_ALLOWED
    if(addressing != None):
        if(addressing == 0 or addressing == 1):
            addressing_ = I2C_addressing(addressing)
            print("addressing: ",addressing_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for addressing")
            return TestStandResult.NOT_ALLOWED
    if(dual != None):
        if(dual == 0 or dual == 1):
            dual_ = I2C_dualaddressing(dual)
            print("dual: ",dual_.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for dual")
            return TestStandResult.NOT_ALLOWED
    if(general_call != None):
        if(general_call == 0 or general_call == 1):
            generalCall = I2C_generalcall(general_call)
            print("general call: ",generalCall.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for general call")
            return TestStandResult.NOT_ALLOWED
    if(no_stretch != None):
        if(no_stretch == 0 or no_stretch == 1):
            noStretch = I2C_nostretch(no_stretch)
            print("no stretch: ",noStretch.name)
        else:
            print(TestStandResult.NOT_ALLOWED.name,"value for no stretch")
            return TestStandResult.NOT_ALLOWED
    if(enable != None):
        if(enable < 0 or enable > 1):
            print(TestStandResult.NOT_ALLOWED.name,"value for enable")
            return TestStandResult.NOT_ALLOWED

    arr=openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.ConfigI2C(speed, own_addr, own_addr2, dutyCycle, role_,addressing_, 
                        dual_, generalCall, noStretch, enable)


@app.command()
def SEND_USART( number     = typer.Argument(1, help="Number of U(S)ART port [1-4]"), \
                data       = typer.Argument(0, help="data that should be send over U(S)ART protocol, text or array of bytes")
            ):
    if not (number >= '1' and number <= '4'):
        ret = TestStandResult.NOT_ALLOWED
        print("number is", ret.name)
        return ret

    n = SEND(int(number,10)+8)
    arr = openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.SendDataOverProtocol(n, data)

@app.command()
def SEND_SPI(data = typer.Argument(0, help="data that should be send over U(S)ART protocol, text or array of bytes")):
    n = SEND.SEND_SPI
    arr = openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.SendDataOverProtocol(n, data)

@app.command()
def SEND_I2C(data = typer.Argument(0, help="data that should be send over U(S)ART protocol, text or array of bytes")):
    n = SEND.SEND_I2C
    arr = openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.SendDataOverProtocol(n, data)

@app.command()
def RECEIVE_I2C():
    arr = openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.ReceiveDataOverProtocol(RECEIVE.I2C)

@app.command()
def RECEIVE_SPI():
    arr = openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.ReceiveDataOverProtocol(RECEIVE.SPI)

@app.command()
def RECEIVE_USART(number=typer.Argument(1, help="Number of U(S)ART port [1-4]")):

    if not (number >= '1' and number <= '4'):
        ret = TestStandResult.NOT_ALLOWED
        print("number is", ret.name)
        return ret
        
    n = RECEIVE(int(number,10)+16)
    arr = openConfig()
    if arr == TestStandResult.FAILURE:
        print("execute first \"setup\" command")
        return arr
    ui = UserInterface(int(arr[0]), int(arr[1]), int(arr[2]))
    return ui.ReceiveDataOverProtocol(n)

if __name__ == "__main__":
    app()
