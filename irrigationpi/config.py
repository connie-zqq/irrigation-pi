rf_outlets_codes = {
    # outlet_num : (on_code, off_code)
    5: (9121756, 9121748)
}

water_pump_outlet_codes = rf_outlets_codes[5]

# Details could be found at: https://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html
water_pump_cron_settings = {
    "day": "*",
    "hour": 8,
    "minute": 30,
    "duration": 120,  # in seconds, self-defined config
}
