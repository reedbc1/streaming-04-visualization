"""src/streaming/data_validation/data_contract_reed.py.

Reed-specific data contract additions for consumed sales output.

This module leaves the case example untouched and overrides the consumed
field order so enriched messages include product_name from products.csv.
"""

# === DECLARE IMPORTS ===

from typing import Final

from streaming.data_validation.data_contract_case import (
    ALLOWED_CURRENCY_CODES,
    ALLOWED_DEVICE_TYPES,
    ALLOWED_PAYMENT_METHODS,
    ALLOWED_REFERRAL_SOURCES,
    CURRENCIES_REQUIRED_FIELDS,
    DISCOUNT_CODES_REQUIRED_FIELDS,
    PRODUCTS_REQUIRED_FIELDS,
    REGIONS_REQUIRED_FIELDS,
    REJECTED_SALES_FIELDNAMES,
    SALES_OPTIONAL_FIELDS,
    SALES_REQUIRED_FIELDS,
    VALID_SALES_FIELDNAMES,
    keep_sales_fields,
    validate_required_fields,
    validate_sale_record,
)

# === DECLARE EXPORTS ===

__all__ = [
    "ALLOWED_CURRENCY_CODES",
    "ALLOWED_DEVICE_TYPES",
    "ALLOWED_PAYMENT_METHODS",
    "ALLOWED_REFERRAL_SOURCES",
    "CONSUMED_FIELDNAMES",
    "CURRENCIES_REQUIRED_FIELDS",
    "DISCOUNT_CODES_REQUIRED_FIELDS",
    "PRODUCTS_REQUIRED_FIELDS",
    "REGIONS_REQUIRED_FIELDS",
    "REJECTED_SALES_FIELDNAMES",
    "SALES_OPTIONAL_FIELDS",
    "SALES_REQUIRED_FIELDS",
    "VALID_SALES_FIELDNAMES",
    "keep_sales_fields",
    "validate_required_fields",
    "validate_sale_record",
]

# === OUTPUT FIELD ORDER ===

CONSUMED_FIELDNAMES: Final[list[str]] = [
    *SALES_REQUIRED_FIELDS,
    "product_name",
    "subtotal",
    "tax_amount",
    "total",
    "_kafka_key",
    "_kafka_partition",
    "_kafka_offset",
]
