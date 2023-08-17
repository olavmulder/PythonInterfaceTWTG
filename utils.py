from enum import Enum
#check van het gebruik van library

class TestStandResult(Enum):
    UNKNOWN = 0
    OK = 1
    DUT_NOT_ACCESSIBLE = -1
    NOT_ALLOWED = -2
    FAILURE = -3
    DATA = -4


class Endianness(Enum):
    LSB = 0
    MSB = 1

class DataLength(Enum):
    EIGHT = 0
    NINE = 1 
 
class Sync(Enum):
    Synchronous = 0
    Asynchronous = 1

class HardwareControl(Enum):
    HWC_NONE = 0
    HWC_RTS = 1
    HWC_CTS = 2
    HWC_RTS_CTS = 3

class TranferDirection(Enum):
    Trans_None = 0
    Trans_RX = 1
    Trans_TX = 2
    Trans_TX_RX = 3

class StopBit(Enum):
    Stop_One = 0
    Stop_Two = 1
    Stop_Half = 2
    Stop_OneandHalf = 3

class ParityBit(Enum):
    Par_Odd = 2
    Par_Even = 1
    Par_None = 0

class Oversampling(Enum):
    Over_16 = 1
    Over_8 = 0

class Clockphase(Enum):
    Clkphase_Two = 1
    Clkphase_One = 0

class Clockpolarity(Enum):
    Clkpol_High = 1
    Clkpol_Low = 0

class Clockoutput(Enum):
    Clkout_Enable = 1
    Clkout_Disable = 0

class LastClockpulse(Enum):
    Lastpulse_No_Output = 0
    Lastpulse_Output = 1

class NSS(Enum):
    NSS_Soft = 0
    NSS_HardInput = 1
    NSS_HardOutput = 2

class Role(Enum):
    Role_Master = 0
    Role_Slave = 1

class Baud_prescaler(Enum):
    Pre_2 = 0
    Pre_4 = 1
    Pre_8 = 2
    Pre_16 = 3
    Pre_32 = 4
    Pre_64 = 5
    Pre_128 = 6
    Pre_256 = 7
class SPI_direction(Enum):
    Dir_One_Line = 0
    Dir_Two_Line = 1
    Dir_Two_Line_RXONLY = 2

class TI_mode(Enum):
    TI_Off = 0
    TI_On = 1

class SPI_DataLength(Enum):
    SPI_Len_Eight = 0
    SPI_Len_Sixteen = 1


class I2C_addressing(Enum):
	addr_7 = 0
	addr_10 = 1

class I2C_dualaddressing(Enum):
	Dual_Off = 0
	Dual_On = 1

class I2C_generalcall(Enum):
	Gen_Off = 0
	Gen_On = 1

class I2C_nostretch(Enum):
	NoStretch_Off = 0
	NoStretch_On = 1

class Dutycycle(Enum):
	Duty_2 = 0
	Duty_16_9 = 1

class CONFIG(Enum):
    CONFIG_USART1 = 1
    CONFIG_USART2 = 2
    CONFIG_USART3 = 3
    CONFIG_USART4 = 4
    CONFIG_SPI    = 5
    CONFIG_I2C    = 6
    CONFIG_IO     = 7
    CONFIG_TWO_QUADRANT = 8

class SEND(Enum):
    SEND_USART1 = 9
    SEND_USART2 = 10
    SEND_USART3 = 11
    SEND_USART4 = 12
    SEND_SPI    = 13
    SEND_I2C    = 14
    SEND_CAN    = 15
    SEND_LVDS   = 16

class RECEIVE(Enum):
    RECEIVE_USART1 = 17
    RECEIVE_USART2 = 18
    RECEIVE_USART3 = 19
    RECEIVE_USART4 = 20
    RECEIVE_SPI    = 21
    RECEIVE_I2C    = 22
    RECEIVE_CAN    = 23
    RECEIVE_LVDS   = 24



def HandleCommand(command):
    if command <=8:
        res:CONFIG = CONFIG(command)
    elif command >= 9 and command <=16:
        res:SEND = SEND(command)
    elif command >= 17 and command <= 24:
        res:RECEIVE = RECEIVE(command)
    return res





