"""Modbus Client Common."""
from typing import Any, List, Tuple, Union, overload

import pymodbus.bit_read_message as pdu_bit_read
import pymodbus.bit_write_message as pdu_bit_write
import pymodbus.diag_message as pdu_diag
import pymodbus.file_message as pdu_file_msg
import pymodbus.mei_message as pdu_mei
import pymodbus.other_message as pdu_other_msg
import pymodbus.register_read_message as pdu_reg_read
import pymodbus.register_write_message as pdu_req_write
from pymodbus.constants import INTERNAL_ERROR
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse, ModbusRequest, ModbusResponse


class ModbusClientMixin:  # pylint: disable=too-many-public-methods
    """**ModbusClientMixin**.

    This is an interface class to facilitate the sending requests/receiving responses like read_coils.
    execute() allows to make a call with non-standard or user defined function codes (remember to add a PDU
    in the transport class to interpret the request/response).

    Simple modbus message call::

        response = client.read_coils(1, 10)
        # or
        response = await client.read_coils(1, 10)

    Advanced modbus message call::

        request = ReadCoilsRequest(1,10)
        response = client.execute(request)
        # or
        request = ReadCoilsRequest(1,10)
        response = await client.execute(request)

    .. tip::
        All methods can be used directly (synchronous) or
        with await <method> (asynchronous) depending on the client used.
    """

    def __init__(self):
        """Initialize."""

    @overload
    def execute(
        self, request: pdu_bit_read.ReadCoilsRequest
    ) -> Union[ExceptionResponse, pdu_bit_read.ReadCoilsResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_bit_read.ReadDiscreteInputsRequest
    ) -> Union[ExceptionResponse, pdu_bit_read.ReadDiscreteInputsResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_reg_read.ReadHoldingRegistersRequest
    ) -> Union[ExceptionResponse, pdu_reg_read.ReadHoldingRegistersResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_reg_read.ReadInputRegistersRequest
    ) -> Union[ExceptionResponse, pdu_reg_read.ReadInputRegistersResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_bit_write.WriteSingleCoilRequest
    ) -> Union[ExceptionResponse, pdu_bit_write.WriteSingleCoilResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_req_write.WriteSingleRegisterRequest
    ) -> Union[ExceptionResponse, pdu_req_write.WriteSingleRegisterResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_other_msg.ReadExceptionStatusRequest
    ) -> Union[ExceptionResponse, pdu_other_msg.ReadExceptionStatusResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnQueryDataRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnQueryDataResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.RestartCommunicationsOptionRequest
    ) -> Union[ExceptionResponse, pdu_diag.RestartCommunicationsOptionResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnDiagnosticRegisterRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnDiagnosticRegisterResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ChangeAsciiInputDelimiterRequest
    ) -> Union[ExceptionResponse, pdu_diag.ChangeAsciiInputDelimiterResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ForceListenOnlyModeRequest
    ) -> Union[ExceptionResponse, pdu_diag.ForceListenOnlyModeResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ClearCountersRequest
    ) -> Union[ExceptionResponse, pdu_diag.ClearCountersResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnBusMessageCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnBusMessageCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnBusCommunicationErrorCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnBusCommunicationErrorCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnBusExceptionErrorCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnBusExceptionErrorCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnSlaveMessageCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveMessageCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnSlaveNoResponseCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveNoResponseCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnSlaveNAKCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveNAKCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnSlaveBusyCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveBusyCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnSlaveBusCharacterOverrunCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveBusCharacterOverrunCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ReturnIopOverrunCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ReturnIopOverrunCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.ClearOverrunCountRequest
    ) -> Union[ExceptionResponse, pdu_diag.ClearOverrunCountResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_diag.GetClearModbusPlusRequest
    ) -> Union[ExceptionResponse, pdu_diag.GetClearModbusPlusResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_bit_write.WriteMultipleCoilsRequest
    ) -> Union[ExceptionResponse, pdu_bit_write.WriteMultipleCoilsResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_req_write.WriteMultipleRegistersRequest
    ) -> Union[ExceptionResponse, pdu_req_write.WriteMultipleRegistersResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_reg_read.ReadWriteMultipleRegistersRequest
    ) -> Union[ExceptionResponse, pdu_reg_read.ReadWriteMultipleRegistersResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_req_write.MaskWriteRegisterRequest
    ) -> Union[ExceptionResponse, pdu_req_write.MaskWriteRegisterResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_other_msg.GetCommEventCounterRequest
    ) -> Union[ExceptionResponse, pdu_other_msg.GetCommEventCounterResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_other_msg.GetCommEventLogRequest
    ) -> Union[ExceptionResponse, pdu_other_msg.GetCommEventLogResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_file_msg.ReadFileRecordRequest
    ) -> Union[ExceptionResponse, pdu_file_msg.ReadFileRecordResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_file_msg.WriteFileRecordRequest
    ) -> Union[ExceptionResponse, pdu_file_msg.WriteFileRecordResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_other_msg.ReportSlaveIdRequest
    ) -> Union[ExceptionResponse, pdu_other_msg.ReportSlaveIdResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_file_msg.ReadFifoQueueRequest
    ) -> Union[ExceptionResponse, pdu_file_msg.ReadFifoQueueResponse]:
        ...

    @overload
    def execute(
        self, request: pdu_mei.ReadDeviceInformationRequest
    ) -> Union[ExceptionResponse, pdu_mei.ReadDeviceInformationResponse]:
        ...

    def execute(self, request: ModbusRequest) -> ModbusResponse:
        """Execute request (code ???).

        :param request: Request to send
        :raises ModbusException:

        Call with custom function codes.

        .. tip::
            Response is not interpreted.
        """
        raise ModbusException(INTERNAL_ERROR)

    def read_coils(
        self, address: int, count: int = 1, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_bit_read.ReadCoilsResponse]:
        """Read coils (code 0x01).

        :param address: Start address to read from
        :param count: (optional) Number of coils to read
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_bit_read.ReadCoilsRequest(address, count, slave, **kwargs)
        )

    def read_discrete_inputs(
        self, address: int, count: int = 1, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_bit_read.ReadDiscreteInputsResponse]:
        """Read discrete inputs (code 0x02).

        :param address: Start address to read from
        :param count: (optional) Number of coils to read
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_bit_read.ReadDiscreteInputsRequest(address, count, slave, **kwargs)
        )

    def read_holding_registers(
        self, address: int, count: int = 1, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_reg_read.ReadHoldingRegistersResponse]:
        """Read holding registers (code 0x03).

        :param address: Start address to read from
        :param count: (optional) Number of coils to read
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_reg_read.ReadHoldingRegistersRequest(address, count, slave, **kwargs)
        )

    def read_input_registers(
        self, address: int, count: int = 1, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_reg_read.ReadInputRegistersResponse]:
        """Read input registers (code 0x04).

        :param address: Start address to read from
        :param count: (optional) Number of coils to read
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_reg_read.ReadInputRegistersRequest(address, count, slave, **kwargs)
        )

    def write_coil(
        self, address: int, value: bool, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_bit_write.WriteSingleCoilResponse]:
        """Write single coil (code 0x05).

        :param address: Address to write to
        :param value: Boolean to write
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_bit_write.WriteSingleCoilRequest(address, value, slave, **kwargs)
        )

    def write_register(
        self, address: int, value: int, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_req_write.WriteSingleRegisterResponse]:
        """Write register (code 0x06).

        :param address: Address to write to
        :param value: Value to write
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_req_write.WriteSingleRegisterRequest(address, value, slave, **kwargs)
        )

    def read_exception_status(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_other_msg.ReadExceptionStatusResponse]:
        """Read Exception Status (code 0x07).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_other_msg.ReadExceptionStatusRequest(slave, **kwargs))

    def diag_query_data(
        self, msg: bytearray, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnQueryDataResponse]:
        """Diagnose query data (code 0x08 sub 0x00).

        :param msg: Message to be returned
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnQueryDataRequest(msg, slave, **kwargs))

    def diag_restart_communication(
        self, toggle: bool, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.RestartCommunicationsOptionResponse]:
        """Diagnose restart communication (code 0x08 sub 0x01).

        :param toggle: True if toogled.
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_diag.RestartCommunicationsOptionRequest(toggle, slave, **kwargs)
        )

    def diag_read_diagnostic_register(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnDiagnosticRegisterResponse]:
        """Diagnose read diagnostic register (code 0x08 sub 0x02).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnDiagnosticRegisterRequest(slave, **kwargs))

    def diag_change_ascii_input_delimeter(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ChangeAsciiInputDelimiterResponse]:
        """Diagnose change ASCII input delimiter (code 0x08 sub 0x03).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ChangeAsciiInputDelimiterRequest(slave, **kwargs))

    def diag_force_listen_only(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ForceListenOnlyModeResponse]:
        """Diagnose force listen only (code 0x08 sub 0x04).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ForceListenOnlyModeRequest(slave, **kwargs))

    def diag_clear_counters(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ClearCountersResponse]:
        """Diagnose clear counters (code 0x08 sub 0x0A).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ClearCountersRequest(slave, **kwargs))

    def diag_read_bus_message_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnBusMessageCountResponse]:
        """Diagnose read bus message count (code 0x08 sub 0x0B).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnBusMessageCountRequest(slave, **kwargs))

    def diag_read_bus_comm_error_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnBusCommunicationErrorCountResponse]:
        """Diagnose read Bus Communication Error Count (code 0x08 sub 0x0C).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_diag.ReturnBusCommunicationErrorCountRequest(slave, **kwargs)
        )

    def diag_read_bus_exception_error_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnBusExceptionErrorCountResponse]:
        """Diagnose read Bus Exception Error Count (code 0x08 sub 0x0D).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_diag.ReturnBusExceptionErrorCountRequest(slave, **kwargs)
        )

    def diag_read_slave_message_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveMessageCountResponse]:
        """Diagnose read Slave Message Count (code 0x08 sub 0x0E).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnSlaveMessageCountRequest(slave, **kwargs))

    def diag_read_slave_no_response_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveNoResponseCountResponse]:
        """Diagnose read Slave No Response Count (code 0x08 sub 0x0F).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnSlaveNoResponseCountRequest(slave, **kwargs))

    def diag_read_slave_nak_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveNAKCountResponse]:
        """Diagnose read Slave NAK Count (code 0x08 sub 0x10).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnSlaveNAKCountRequest(slave, **kwargs))

    def diag_read_slave_busy_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveBusyCountResponse]:
        """Diagnose read Slave Busy Count (code 0x08 sub 0x11).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnSlaveBusyCountRequest(slave, **kwargs))

    def diag_read_bus_char_overrun_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnSlaveBusCharacterOverrunCountResponse]:
        """Diagnose read Bus Character Overrun Count (code 0x08 sub 0x12).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_diag.ReturnSlaveBusCharacterOverrunCountRequest(slave, **kwargs)
        )

    def diag_read_iop_overrun_count(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ReturnIopOverrunCountResponse]:
        """Diagnose read Iop overrun count (code 0x08 sub 0x13).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ReturnIopOverrunCountRequest(slave, **kwargs))

    def diag_clear_overrun_counter(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.ClearOverrunCountResponse]:
        """Diagnose Clear Overrun Counter and Flag (code 0x08 sub 0x14).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.ClearOverrunCountRequest(slave, **kwargs))

    def diag_getclear_modbus_response(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_diag.GetClearModbusPlusResponse]:
        """Diagnose Get/Clear modbus plus (code 0x08 sub 0x15).

        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_diag.GetClearModbusPlusRequest(slave, **kwargs))

    def diag_get_comm_event_counter(
        self, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_other_msg.GetCommEventCounterResponse]:
        """Diagnose get event counter (code 0x0B).

        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_other_msg.GetCommEventCounterRequest(**kwargs))

    def diag_get_comm_event_log(
        self, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_other_msg.GetCommEventLogResponse]:
        """Diagnose get event counter (code 0x0C).

        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_other_msg.GetCommEventLogRequest(**kwargs))

    def write_coils(
        self,
        address: int,
        values: Union[List[bool], bool],
        slave: int = 0,
        **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_bit_write.WriteMultipleCoilsResponse]:
        """Write coils (code 0x0F).

        :param address: Start address to write to
        :param values: List of booleans to write, or a single boolean to write
        :param slave: (optional) Modbus slave ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_bit_write.WriteMultipleCoilsRequest(address, values, slave, **kwargs)
        )

    def write_registers(
        self, address: int, values: Union[List[int], int], slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_req_write.WriteMultipleRegistersResponse]:
        """Write registers (code 0x10).

        :param address: Start address to write to
        :param values: List of values to write, or a single value to write
        :param slave: (optional) Modbus slave unit ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_req_write.WriteMultipleRegistersRequest(
                address, values, slave, **kwargs
            )
        )

    def report_slave_id(
        self, slave: int = 0, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_other_msg.ReportSlaveIdResponse]:
        """Report slave ID (code 0x11).

        :param slave: (optional) Modbus slave unit ID
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_other_msg.ReportSlaveIdRequest(slave, **kwargs))

    def read_file_record(
        self, records: List[Tuple], **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_file_msg.ReadFileRecordResponse]:
        """Read file record (code 0x14).

        :param records: List of (Reference type, File number, Record Number, Record Length)
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_file_msg.ReadFileRecordRequest(records, **kwargs))

    def write_file_record(
        self, records: List[Tuple], **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_file_msg.WriteFileRecordResponse]:
        """Write file record (code 0x15).

        :param records: List of (Reference type, File number, Record Number, Record Length)
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(pdu_file_msg.WriteFileRecordRequest(records, **kwargs))

    def mask_write_register(
        self,
        address: int = 0x0000,
        and_mask: int = 0xFFFF,
        or_mask: int = 0x0000,
        **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_req_write.MaskWriteRegisterResponse]:
        """Mask write register (code 0x16).

        :param address: The mask pointer address (0x0000 to 0xffff)
        :param and_mask: The and bitmask to apply to the register address
        :param or_mask: The or bitmask to apply to the register address
        :param kwargs: (optional) Experimental parameters.
        :raises ModbusException:
        """
        return self.execute(
            pdu_req_write.MaskWriteRegisterRequest(address, and_mask, or_mask, **kwargs)
        )

    def readwrite_registers(
        self,
        read_address: int = 0,
        read_count: int = 0,
        write_address: int = 0,
        values: Union[List[int], int] = 0,
        slave: int = 0,
        **kwargs
    ) -> Union[ExceptionResponse, pdu_reg_read.ReadWriteMultipleRegistersResponse]:
        """Read/Write registers (code 0x17).

        :param read_address: The address to start reading from
        :param read_count: The number of registers to read from address
        :param write_address: The address to start writing to
        :param values: List of values to write, or a single value to write
        :param slave: (optional) Modbus slave unit ID
        :param kwargs:
        :raises ModbusException:
        """
        return self.execute(
            pdu_reg_read.ReadWriteMultipleRegistersRequest(
                read_address=read_address,
                read_count=read_count,
                write_address=write_address,
                values=values,
                unit=slave,
                **kwargs
            )
        )

    def read_fifo_queue(
        self, address: int = 0x0000, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_file_msg.ReadFifoQueueResponse]:
        """Read FIFO queue (code 0x18).

        :param address: The address to start reading from
        :param kwargs:
        :raises ModbusException:
        """
        return self.execute(pdu_file_msg.ReadFifoQueueRequest(address, **kwargs))

    # code 0x2B sub 0x0D: CANopen General Reference Request and Response, NOT IMPLEMENTED

    def read_device_information(
        self, read_code: int = None, object_id: int = 0x00, **kwargs: Any
    ) -> Union[ExceptionResponse, pdu_mei.ReadDeviceInformationResponse]:
        """Read FIFO queue (code 0x2B sub 0x0E).

        :param read_code: The device information read code
        :param object_id: The object to read from
        :param kwargs:
        :raises ModbusException:
        """
        return self.execute(
            pdu_mei.ReadDeviceInformationRequest(read_code, object_id, **kwargs)
        )
