expected_output = {
    1: {
        "groupname": "2c",
        "sec_model": "v1",
        "contextname": "none",
        "storage_type": "volatile",
        "readview": "none",
        "writeview": "none",
        "notifyview": "*tv.FFFF58bf.eaFF58bf.eaFFFFFF.F",
        "row_status": {"status": "active"},
    },
    2: {
        "groupname": "2c",
        "sec_model": "v2c",
        "contextname": "none",
        "storage_type": "volatile",
        "readview": "none",
        "writeview": "none",
        "notifyview": "*tv.FFFF58bf.eaFF58bf.eaFFFFFF.F",
        "row_status": {"status": "active"},
    },
    3: {
        "groupname": "ag-ro",
        "sec_model": "v1",
        "contextname": "none",
        "storage_type": "volatile",
        "readview": "v1default",
        "writeview": "none",
        "notifyview": "*tv.FFFF58bf.eaFF58bf.eaFFFFFF.F",
        "row_status": {"status": "active"},
    },
    4: {
        "groupname": "ag-ro",
        "sec_model": "v3 auth",
        "contextname": "none",
        "storage_type": "nonvolatile",
        "readview": "v1default",
        "writeview": "none",
        "notifyview": "none",
        "row_status": {"status": "active"},
    },
    5: {
        "groupname": "ag-ro",
        "sec_model": "v3 priv",
        "contextname": "none",
        "storage_type": "nonvolatile",
        "readview": "v1default",
        "writeview": "none",
        "notifyview": "none",
        "row_status": {"status": "active"},
    },
    6: {
        "groupname": "ag-rw",
        "sec_model": "v2c",
        "contextname": "none",
        "storage_type": "volatile",
        "readview": "v1default",
        "writeview": "v1default",
        "notifyview": "none",
        "row_status": {"status": "active", "access_list": "snmp-servers"},
    },
    7: {
        "groupname": "IMI",
        "sec_model": "v2c",
        "contextname": "none",
        "storage_type": "permanent",
        "readview": "*ilmi",
        "writeview": "*ilmi",
        "notifyview": "none",
        "row_status": {"status": "active"},
    },
    8: {
        "groupname": "AlfaV",
        "sec_model": "v2c",
        "contextname": "none",
        "storage_type": "permanent",
        "readview": "v1default",
        "writeview": "none",
        "notifyview": "none",
        "row_status": {"status": "active", "access_list": "90"},
    },
    9: {
        "groupname": "ag-rw",
        "sec_model": "v1",
        "readview": "v1default",
        "writeview": "v1default",
        "notifyview": "none",
        "row_status": {"status": "active", "access_list": "snmp-servers"},
    },
    10: {
        "groupname": "2c",
        "sec_model": "v2c",
        "readview": "none",
        "writeview": "none",
        "notifyview": "*tv.FFFF58bf.eaFF58bf.eaFFFFFF.F",
        "row_status": {"status": "active"},
    },
}
