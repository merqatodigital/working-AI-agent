from resort_tools.reservation_tools import (
    check_room_availability,
    get_guest_profile,
    get_reservation,
    get_room_status,
    get_staff_on_shift,
    get_stock_level,
    set_store,
)
from resort_tools.staff_tools import (
    assign_task,
    create_task,
    draft_guest_reply,
    record_check_in,
    record_task_completion,
    update_room_status,
)
from resort_tools.approval_tools import (
    SENSITIVE_TOOLS,
    change_room_price,
    create_purchase_request,
    refund_guest,
)

READ_TOOLS = [
    get_reservation,
    check_room_availability,
    get_guest_profile,
    get_staff_on_shift,
    get_stock_level,
    get_room_status,
]

WRITE_TOOLS = [
    create_task,
    assign_task,
    draft_guest_reply,
    update_room_status,
    record_task_completion,
    record_check_in,
]

SENSITIVE_TOOLS_LIST = [
    refund_guest,
    create_purchase_request,
    change_room_price,
]

ALL_TOOLS = READ_TOOLS + WRITE_TOOLS + SENSITIVE_TOOLS_LIST

__all__ = [
    "set_store",
    "READ_TOOLS",
    "WRITE_TOOLS",
    "SENSITIVE_TOOLS_LIST",
    "SENSITIVE_TOOLS",
    "ALL_TOOLS",
]
