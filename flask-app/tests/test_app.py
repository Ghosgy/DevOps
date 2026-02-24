from app import calculate_race_times, format_time
import pytest

def test_format_time():
    assert format_time(0) == "0:00"
    assert format_time(1) == "1:00"
    assert format_time(10) == "10:00"
    assert format_time(60) == "1:00:00"
    assert format_time(181) == "3:01:00"
    assert format_time(611) == "10:11:00"

def test_calculate_race_times():
    # pace per km is 5 min
    #TODO: complete the dict with the expected times
    distance_result = {
        "5K": "25:00",
        "10K": "50:00",
        "Half Marathon": "",
        "Marathon": ""
    }

    def test_format_time():
        assert format_time(0) == "0:00"
        assert format_time(1) == "1:00"
        assert format_time(10) == "10:00"
        assert format_time(60) == "1:00:00"
        assert format_time(181) == "3:01:00"
        assert format_time(611) == "10:11:00"

    def test_calculate_race_times_pace_5():
        # pace per km is 5 min
        distance_result = {
            "5K": "25:00",
            "10K": "50:00",
            "Half Marathon": "1:45:00",  # 21.0975 km * 5 = 105.4875 -> ~105 min -> 1:45:00
            "Marathon": "3:31:00"        # 42.195 km * 5 = 210.975 -> ~211 min -> 3:31:00
        }
        assert calculate_race_times(5) == distance_result

    def test_calculate_race_times_zero_pace():
        # zero pace should produce zero times (no movement)
        expected = {
            "5K": "0:00",
            "10K": "0:00",
            "Half Marathon": "0:00",
            "Marathon": "0:00"
        }
        assert calculate_race_times(0) == expected

    def test_calculate_race_times_negative_pace_raises():
        # negative pace is invalid
        with pytest.raises(ValueError):
            calculate_race_times(-5)

    def test_calculate_race_times_empty_or_invalid_inputs_raise():
        # None, empty string, or other non-numeric inputs should raise
        for bad in (None, "", [], {}):
            with pytest.raises((TypeError, ValueError)):
                calculate_race_times(bad)
