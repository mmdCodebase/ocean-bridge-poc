from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse
from unittest.mock import patch
import pytest
import json
import sys
from requests import Response
from app.main import app  # Import your FastAPI app here

client = TestClient(app)

def mock_validate_token():
    return True  # Simulate successful token validation

def mock_perform_data_validation_failure(*args, **kwargs):
    raise Exception("Simulated BLAT process failure")

def mock_parse_cookies(cookies):
    return {"auth_token": "dummy_token", "session_id": "dummy_session_id"}

def mock_asi_nvo_success_response(*args, **kwargs):
    messages = [{"message_type": "INFO", "message": "ASI-NVO process succeeded."}]
    response = Response()
    response.status_code=200, 
    return response.json()

@pytest.fixture
def action_navigation_request():
    return {
    "page_keys": "{\"ws_key\":\"\"}",
    "actionable_attributes": "{\"actionable_location\":\"data_grid_toolbar\",\"action_type\":\"action\",\"special_button_type\":\"save\",\"button_scope\":\"backend\",\"is_action_refresh_when_complete\":true,\"form_field_attributes\":null,\"data_grid_toolbar_attributes\":{\"rows_sent_type\":\"all\",\"is_row_key_values_required\":false,\"rows_type\":\"multiple\"},\"data_grid_row_attributes\":null,\"navigation_attributes\":null,\"info_only_attributes\":{\"action_id\":\"de3def9f-f29e-4b52-8892-a0abd4688ec4\",\"action_from_ws_id\":\"1aa6a75a-011a-4991-a3b8-fdca96db20a5\",\"action_from_page_keys\":null,\"action_from_form_id\":\"00000000-0000-0000-0000-000000000000\",\"action_from_data_grid_id\":\"c7548b26-27ac-46dc-8287-a04f37c60d00\",\"is_data_sent_for_action\":true}}",
    "data_json": "{\"data_grid\":[{\"id\":\"59dc519c-0c74-452e-a504-5de342139e41\",\"data_items\":[{\"data_item_id\":\"BE166A22-55DD-474A-8708-1B69FE82C6EB\",\"is_key_field\":true,\"o\":[{\"v\":\"59dc519c-0c74-452e-a504-5de342139e41\",\"d\":\"59dc519c-0c74-452e-a504-5de342139e41\"}],\"m\":[{\"v\":\"59dc519c-0c74-452e-a504-5de342139e41\",\"d\":\"59dc519c-0c74-452e-a504-5de342139e41\"}],\"tz\":\"\"},{\"data_item_id\":\"5C798957-BD1C-4EFA-8D0C-63E22787A7B6\",\"is_key_field\":false,\"o\":[{\"v\":\"Revised\",\"d\":\"Revised\"}],\"m\":[{\"v\":\"Revised\",\"d\":\"Revised\"}],\"tz\":\"\"},{\"data_item_id\":\"BC9AC795-6A7C-4BB8-ADAE-69F5351CBB2E\",\"is_key_field\":false,\"o\":[{\"v\":\"Create\",\"d\":\"Create\"}],\"m\":[{\"v\":\"Create\",\"d\":\"Create\"}],\"tz\":\"\"},{\"data_item_id\":\"2216B077-E275-41FE-9B99-ADA3D695916B\",\"is_key_field\":false,\"o\":[{\"v\":\"24\",\"d\":\"24\"}],\"m\":[{\"v\":\"24\",\"d\":\"24\"}],\"tz\":\"\"},{\"data_item_id\":\"8B798A5F-6130-4EE4-851C-DF0BB9CA1CA6\",\"is_key_field\":false,\"o\":[{\"v\":\"00220988\",\"d\":\"00220988\"}],\"m\":[{\"v\":\"00220988\",\"d\":\"00220988\"}],\"tz\":\"\"},{\"data_item_id\":\"D96E63D6-3527-4CAA-8D8C-F84416F9131E\",\"is_key_field\":false,\"o\":[{\"v\":\"24D\",\"d\":\"24D\"}],\"m\":[{\"v\":\"24D\",\"d\":\"24D\"}],\"tz\":\"\"},{\"data_item_id\":\"2CB26B9F-C782-4608-B478-303FBB17F65E\",\"is_key_field\":false,\"o\":[{\"v\":\"ASI20181100492\",\"d\":\"ASI20181100492\"}],\"m\":[{\"v\":\"ASI20181100492\",\"d\":\"ASI20181100492\"}],\"tz\":\"\"},{\"data_item_id\":\"BD8C859D-AFB3-42D5-827C-7790F6012186\",\"is_key_field\":false,\"o\":[{\"v\":\"1/18/2019 \",\"d\":\"1/18/2019 \"}],\"m\":[{\"v\":\"1/18/2019 \",\"d\":\"1/18/2019 \"}],\"tz\":\"\"},{\"data_item_id\":\"91C0984B-DD8C-4C5D-8D19-E493B6FD9556\",\"is_key_field\":false,\"o\":[{\"v\":\"ZIMUHCM000255685\",\"d\":\"ZIMUHCM000255685\"}],\"m\":[{\"v\":\"ZIMUHCM000255685\",\"d\":\"ZIMUHCM000255685\"}],\"tz\":\"\"}]},{\"id\":\"7e7f7b3f-cd7c-446e-8d9c-067696316ebc\",\"data_items\":[{\"data_item_id\":\"BE166A22-55DD-474A-8708-1B69FE82C6EB\",\"is_key_field\":true,\"o\":[{\"v\":\"7e7f7b3f-cd7c-446e-8d9c-067696316ebc\",\"d\":\"7e7f7b3f-cd7c-446e-8d9c-067696316ebc\"}],\"m\":[{\"v\":\"7e7f7b3f-cd7c-446e-8d9c-067696316ebc\",\"d\":\"7e7f7b3f-cd7c-446e-8d9c-067696316ebc\"}],\"tz\":\"\"},{\"data_item_id\":\"5C798957-BD1C-4EFA-8D0C-63E22787A7B6\",\"is_key_field\":false,\"o\":[{\"v\":\"Revised\",\"d\":\"Revised\"}],\"m\":[{\"v\":\"Revised\",\"d\":\"Revised\"}],\"tz\":\"\"},{\"data_item_id\":\"BC9AC795-6A7C-4BB8-ADAE-69F5351CBB2E\",\"is_key_field\":false,\"o\":[{\"v\":\"Create\",\"d\":\"Create\"}],\"m\":[{\"v\":\"Create\",\"d\":\"Create\"}],\"tz\":\"\"},{\"data_item_id\":\"2216B077-E275-41FE-9B99-ADA3D695916B\",\"is_key_field\":false,\"o\":[{\"v\":\"\",\"d\":\"\"}],\"m\":[{\"v\":\"\",\"d\":\"\"}],\"tz\":\"\"},{\"data_item_id\":\"8B798A5F-6130-4EE4-851C-DF0BB9CA1CA6\",\"is_key_field\":false,\"o\":[{\"v\":\"00227178, P000017334, P000017360, P000017512, P000017578\",\"d\":\"00227178, P000017334, P000017360, P000017512, P000017578\"}],\"m\":[{\"v\":\"00227178, P000017334, P000017360, P000017512, P000017578\",\"d\":\"00227178, P000017334, P000017360, P000017512, P000017578\"}],\"tz\":\"\"},{\"data_item_id\":\"D96E63D6-3527-4CAA-8D8C-F84416F9131E\",\"is_key_field\":false,\"o\":[{\"v\":\"RP, RP, 22, RP, RP\",\"d\":\"RP, RP, 22, RP, RP\"}],\"m\":[{\"v\":\"RP, RP, 22, RP, RP\",\"d\":\"RP, RP, 22, RP, RP\"}],\"tz\":\"\"},{\"data_item_id\":\"2CB26B9F-C782-4608-B478-303FBB17F65E\",\"is_key_field\":false,\"o\":[{\"v\":\"ASI20190900238\",\"d\":\"ASI20190900238\"}],\"m\":[{\"v\":\"ASI20190900238\",\"d\":\"ASI20190900238\"}],\"tz\":\"\"},{\"data_item_id\":\"BD8C859D-AFB3-42D5-827C-7790F6012186\",\"is_key_field\":false,\"o\":[{\"v\":\"10/5/2019 \",\"d\":\"10/5/2019 \"}],\"m\":[{\"v\":\"10/5/2019 \",\"d\":\"10/5/2019 \"}],\"tz\":\"\"},{\"data_item_id\":\"91C0984B-DD8C-4C5D-8D19-E493B6FD9556\",\"is_key_field\":false,\"o\":[{\"v\":\"\",\"d\":\"\"}],\"m\":[{\"v\":\"\",\"d\":\"\"}],\"tz\":\"\"}]},{\"id\":\"15d16c3c-8310-4fef-a9d9-ede4ab2d7eec\",\"data_items\":[{\"data_item_id\":\"BE166A22-55DD-474A-8708-1B69FE82C6EB\",\"is_key_field\":true,\"o\":[{\"v\":\"15d16c3c-8310-4fef-a9d9-ede4ab2d7eec\",\"d\":\"15d16c3c-8310-4fef-a9d9-ede4ab2d7eec\"}],\"m\":[{\"v\":\"15d16c3c-8310-4fef-a9d9-ede4ab2d7eec\",\"d\":\"15d16c3c-8310-4fef-a9d9-ede4ab2d7eec\"}],\"tz\":\"\"},{\"data_item_id\":\"5C798957-BD1C-4EFA-8D0C-63E22787A7B6\",\"is_key_field\":false,\"o\":[{\"v\":\"Revised\",\"d\":\"Revised\"}],\"m\":[{\"v\":\"Revised\",\"d\":\"Revised\"}],\"tz\":\"\"},{\"data_item_id\":\"BC9AC795-6A7C-4BB8-ADAE-69F5351CBB2E\",\"is_key_field\":false,\"o\":[{\"v\":\"Create\",\"d\":\"Create\"}],\"m\":[{\"v\":\"Create\",\"d\":\"Create\"}],\"tz\":\"\"},{\"data_item_id\":\"2216B077-E275-41FE-9B99-ADA3D695916B\",\"is_key_field\":false,\"o\":[{\"v\":\"24\",\"d\":\"24\"}],\"m\":[{\"v\":\"24\",\"d\":\"24\"}],\"tz\":\"\"},{\"data_item_id\":\"8B798A5F-6130-4EE4-851C-DF0BB9CA1CA6\",\"is_key_field\":false,\"o\":[{\"v\":\"00222597\",\"d\":\"00222597\"}],\"m\":[{\"v\":\"00222597\",\"d\":\"00222597\"}],\"tz\":\"\"},{\"data_item_id\":\"D96E63D6-3527-4CAA-8D8C-F84416F9131E\",\"is_key_field\":false,\"o\":[{\"v\":\"24D\",\"d\":\"24D\"}],\"m\":[{\"v\":\"24D\",\"d\":\"24D\"}],\"tz\":\"\"},{\"data_item_id\":\"2CB26B9F-C782-4608-B478-303FBB17F65E\",\"is_key_field\":false,\"o\":[{\"v\":\"ASI20231200002\",\"d\":\"ASI20231200002\"}],\"m\":[{\"v\":\"ASI20231200002\",\"d\":\"ASI20231200002\"}],\"tz\":\"\"},{\"data_item_id\":\"BD8C859D-AFB3-42D5-827C-7790F6012186\",\"is_key_field\":false,\"o\":[{\"v\":\"1/1/2024 \",\"d\":\"1/1/2024 \"}],\"m\":[{\"v\":\"1/2/2024\",\"d\":\"1/1/2024 \"}],\"tz\":\"\"},{\"data_item_id\":\"91C0984B-DD8C-4C5D-8D19-E493B6FD9556\",\"is_key_field\":false,\"o\":[{\"v\":\"COSU620249\",\"d\":\"COSU620249\"}],\"m\":[{\"v\":\"COSU620249\",\"d\":\"COSU620249\"}],\"tz\":\"\"}]}]}",
    "row_keys": "\"\"",
    "column_key": "\"\""
}
def test_action_navigation_blat_process_failure(action_navigation_request):
    with patch('app.internal.auth.validate_token', side_effect=mock_validate_token), \
         patch('app.service.agl_blat.perform_data_validation', side_effect=mock_perform_data_validation_failure), \
         patch('app.service.asi_nvo.action_navigation', side_effect = mock_asi_nvo_success_response), \
         patch('app.internal.auth.parse_cookies', side_effect=mock_parse_cookies):
        
        mock_headers = {
            "Authorization": "1234",
            "SessionID": "5678"
        }

        response = client.post("/V1/action", json=action_navigation_request, headers=mock_headers)
        assert response.status_code == 200
        response_data = response
        # Assert that the warning message is included in the response
        found_warning = False
        for message in response_data["messages"]:
            print(message)
            if message['message_type'] == 'WARNING' and message['message'] == "BLAT process failed. No validation messages available.":
                found_warning = True
                break
        assert found_warning == True
