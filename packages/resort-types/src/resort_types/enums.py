from enum import Enum


class Department(str, Enum):
    GUEST_RELATIONS = "guest_relations"
    RESERVATIONS = "reservations"
    FRONT_DESK = "front_desk"
    HOUSEKEEPING = "housekeeping"
    MAINTENANCE = "maintenance"
    STAFF = "staff"
    INVENTORY = "inventory"
    PURCHASING = "purchasing"
    FINANCE = "finance"


class TaskStatus(str, Enum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Priority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class RoomType(str, Enum):
    STANDARD = "standard"
    DELUXE = "deluxe"
    SUITE = "suite"
    VILLA = "villa"


class RoomStatus(str, Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    CLEANING = "cleaning"
    MAINTENANCE = "maintenance"
    OUT_OF_ORDER = "out_of_order"


class ReservationStatus(str, Enum):
    CONFIRMED = "confirmed"
    CHECKED_IN = "checked_in"
    CHECKED_OUT = "checked_out"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"


class ApprovalType(str, Enum):
    REFUND = "refund"
    PRICE_CHANGE = "price_change"
    DELETE_BOOKING = "delete_booking"
    FINANCIAL_ENTRY = "financial_entry"
    PURCHASE_APPROVAL = "purchase_approval"
    SUPPLIER_PAYMENT = "supplier_payment"


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"


class IntentType(str, Enum):
    GUEST_REQUEST = "guest_request"
    BOOKING_INQUIRY = "booking_inquiry"
    MAINTENANCE_REQUEST = "maintenance_request"
    COMPLAINT = "complaint"
    INFORMATION_REQUEST = "information_request"
    FINANCIAL_QUESTION = "financial_question"
    STAFF_COORDINATION = "staff_coordination"
    INVENTORY_CHECK = "inventory_check"
    GENERAL = "general"
