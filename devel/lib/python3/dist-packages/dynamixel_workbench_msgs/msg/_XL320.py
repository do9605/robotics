# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dynamixel_workbench_msgs/XL320.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class XL320(genpy.Message):
  _md5sum = "f4c9a1069d9176eaf1948e4f20082d40"
  _type = "dynamixel_workbench_msgs/XL320"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# This message is compatible with control table of Dynamixel XL Series (XL320)
# If you want to specific information about control table, please follow the link (http://emanual.robotis.com/)

uint16 Model_Number
uint8  Firmware_Version
uint8  ID
uint8  Baud_Rate
uint8  Return_Delay_Time
uint16 CW_Angle_Limit
uint16 CCW_Angle_Limit
uint8  Control_Mode
uint8  Temperature_Limit
uint8  Min_Voltage_Limit
uint8  Max_Voltage_Limit
uint16 Max_Torque
uint8  Status_Return_Level
uint8  Shutdown

uint8  Torque_Enable
uint8  LED
uint8  D_gain
uint8  I_gain
uint8  P_gain
uint16 Goal_Position
uint16 Moving_Speed
uint16 Torque_Limit
uint16 Present_Position
uint16 Present_Speed
uint16 Present_Load
uint8  Present_Voltage
uint8  Present_Temperature
uint8  Registered
uint8  Moving
uint8  Hardware_Error_Status
uint16 Punch
"""
  __slots__ = ['Model_Number','Firmware_Version','ID','Baud_Rate','Return_Delay_Time','CW_Angle_Limit','CCW_Angle_Limit','Control_Mode','Temperature_Limit','Min_Voltage_Limit','Max_Voltage_Limit','Max_Torque','Status_Return_Level','Shutdown','Torque_Enable','LED','D_gain','I_gain','P_gain','Goal_Position','Moving_Speed','Torque_Limit','Present_Position','Present_Speed','Present_Load','Present_Voltage','Present_Temperature','Registered','Moving','Hardware_Error_Status','Punch']
  _slot_types = ['uint16','uint8','uint8','uint8','uint8','uint16','uint16','uint8','uint8','uint8','uint8','uint16','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint16','uint16','uint16','uint16','uint16','uint16','uint8','uint8','uint8','uint8','uint8','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Model_Number,Firmware_Version,ID,Baud_Rate,Return_Delay_Time,CW_Angle_Limit,CCW_Angle_Limit,Control_Mode,Temperature_Limit,Min_Voltage_Limit,Max_Voltage_Limit,Max_Torque,Status_Return_Level,Shutdown,Torque_Enable,LED,D_gain,I_gain,P_gain,Goal_Position,Moving_Speed,Torque_Limit,Present_Position,Present_Speed,Present_Load,Present_Voltage,Present_Temperature,Registered,Moving,Hardware_Error_Status,Punch

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(XL320, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Model_Number is None:
        self.Model_Number = 0
      if self.Firmware_Version is None:
        self.Firmware_Version = 0
      if self.ID is None:
        self.ID = 0
      if self.Baud_Rate is None:
        self.Baud_Rate = 0
      if self.Return_Delay_Time is None:
        self.Return_Delay_Time = 0
      if self.CW_Angle_Limit is None:
        self.CW_Angle_Limit = 0
      if self.CCW_Angle_Limit is None:
        self.CCW_Angle_Limit = 0
      if self.Control_Mode is None:
        self.Control_Mode = 0
      if self.Temperature_Limit is None:
        self.Temperature_Limit = 0
      if self.Min_Voltage_Limit is None:
        self.Min_Voltage_Limit = 0
      if self.Max_Voltage_Limit is None:
        self.Max_Voltage_Limit = 0
      if self.Max_Torque is None:
        self.Max_Torque = 0
      if self.Status_Return_Level is None:
        self.Status_Return_Level = 0
      if self.Shutdown is None:
        self.Shutdown = 0
      if self.Torque_Enable is None:
        self.Torque_Enable = 0
      if self.LED is None:
        self.LED = 0
      if self.D_gain is None:
        self.D_gain = 0
      if self.I_gain is None:
        self.I_gain = 0
      if self.P_gain is None:
        self.P_gain = 0
      if self.Goal_Position is None:
        self.Goal_Position = 0
      if self.Moving_Speed is None:
        self.Moving_Speed = 0
      if self.Torque_Limit is None:
        self.Torque_Limit = 0
      if self.Present_Position is None:
        self.Present_Position = 0
      if self.Present_Speed is None:
        self.Present_Speed = 0
      if self.Present_Load is None:
        self.Present_Load = 0
      if self.Present_Voltage is None:
        self.Present_Voltage = 0
      if self.Present_Temperature is None:
        self.Present_Temperature = 0
      if self.Registered is None:
        self.Registered = 0
      if self.Moving is None:
        self.Moving = 0
      if self.Hardware_Error_Status is None:
        self.Hardware_Error_Status = 0
      if self.Punch is None:
        self.Punch = 0
    else:
      self.Model_Number = 0
      self.Firmware_Version = 0
      self.ID = 0
      self.Baud_Rate = 0
      self.Return_Delay_Time = 0
      self.CW_Angle_Limit = 0
      self.CCW_Angle_Limit = 0
      self.Control_Mode = 0
      self.Temperature_Limit = 0
      self.Min_Voltage_Limit = 0
      self.Max_Voltage_Limit = 0
      self.Max_Torque = 0
      self.Status_Return_Level = 0
      self.Shutdown = 0
      self.Torque_Enable = 0
      self.LED = 0
      self.D_gain = 0
      self.I_gain = 0
      self.P_gain = 0
      self.Goal_Position = 0
      self.Moving_Speed = 0
      self.Torque_Limit = 0
      self.Present_Position = 0
      self.Present_Speed = 0
      self.Present_Load = 0
      self.Present_Voltage = 0
      self.Present_Temperature = 0
      self.Registered = 0
      self.Moving = 0
      self.Hardware_Error_Status = 0
      self.Punch = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_H4B2H4BH7B6H5BH().pack(_x.Model_Number, _x.Firmware_Version, _x.ID, _x.Baud_Rate, _x.Return_Delay_Time, _x.CW_Angle_Limit, _x.CCW_Angle_Limit, _x.Control_Mode, _x.Temperature_Limit, _x.Min_Voltage_Limit, _x.Max_Voltage_Limit, _x.Max_Torque, _x.Status_Return_Level, _x.Shutdown, _x.Torque_Enable, _x.LED, _x.D_gain, _x.I_gain, _x.P_gain, _x.Goal_Position, _x.Moving_Speed, _x.Torque_Limit, _x.Present_Position, _x.Present_Speed, _x.Present_Load, _x.Present_Voltage, _x.Present_Temperature, _x.Registered, _x.Moving, _x.Hardware_Error_Status, _x.Punch))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 42
      (_x.Model_Number, _x.Firmware_Version, _x.ID, _x.Baud_Rate, _x.Return_Delay_Time, _x.CW_Angle_Limit, _x.CCW_Angle_Limit, _x.Control_Mode, _x.Temperature_Limit, _x.Min_Voltage_Limit, _x.Max_Voltage_Limit, _x.Max_Torque, _x.Status_Return_Level, _x.Shutdown, _x.Torque_Enable, _x.LED, _x.D_gain, _x.I_gain, _x.P_gain, _x.Goal_Position, _x.Moving_Speed, _x.Torque_Limit, _x.Present_Position, _x.Present_Speed, _x.Present_Load, _x.Present_Voltage, _x.Present_Temperature, _x.Registered, _x.Moving, _x.Hardware_Error_Status, _x.Punch,) = _get_struct_H4B2H4BH7B6H5BH().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_H4B2H4BH7B6H5BH().pack(_x.Model_Number, _x.Firmware_Version, _x.ID, _x.Baud_Rate, _x.Return_Delay_Time, _x.CW_Angle_Limit, _x.CCW_Angle_Limit, _x.Control_Mode, _x.Temperature_Limit, _x.Min_Voltage_Limit, _x.Max_Voltage_Limit, _x.Max_Torque, _x.Status_Return_Level, _x.Shutdown, _x.Torque_Enable, _x.LED, _x.D_gain, _x.I_gain, _x.P_gain, _x.Goal_Position, _x.Moving_Speed, _x.Torque_Limit, _x.Present_Position, _x.Present_Speed, _x.Present_Load, _x.Present_Voltage, _x.Present_Temperature, _x.Registered, _x.Moving, _x.Hardware_Error_Status, _x.Punch))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 42
      (_x.Model_Number, _x.Firmware_Version, _x.ID, _x.Baud_Rate, _x.Return_Delay_Time, _x.CW_Angle_Limit, _x.CCW_Angle_Limit, _x.Control_Mode, _x.Temperature_Limit, _x.Min_Voltage_Limit, _x.Max_Voltage_Limit, _x.Max_Torque, _x.Status_Return_Level, _x.Shutdown, _x.Torque_Enable, _x.LED, _x.D_gain, _x.I_gain, _x.P_gain, _x.Goal_Position, _x.Moving_Speed, _x.Torque_Limit, _x.Present_Position, _x.Present_Speed, _x.Present_Load, _x.Present_Voltage, _x.Present_Temperature, _x.Registered, _x.Moving, _x.Hardware_Error_Status, _x.Punch,) = _get_struct_H4B2H4BH7B6H5BH().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_H4B2H4BH7B6H5BH = None
def _get_struct_H4B2H4BH7B6H5BH():
    global _struct_H4B2H4BH7B6H5BH
    if _struct_H4B2H4BH7B6H5BH is None:
        _struct_H4B2H4BH7B6H5BH = struct.Struct("<H4B2H4BH7B6H5BH")
    return _struct_H4B2H4BH7B6H5BH
