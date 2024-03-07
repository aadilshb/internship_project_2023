from fastapi import FastAPI,Query,HTTPException
from typing import List
import requests
import json

app = FastAPI()

def create_whatsapp_request(mobile, template_name, language, header: bool, body_parameters: List[str], header_type=None, header_value=None, loc_name=None, loc_address=None, loc_latitude=None, loc_longitude=None,coupon_code:str=None):
    whatsapp_request_data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"91{mobile}",
        "type": "template",
        "template": {
            "name": template_name,
            "language": {"code": language},
            "components": []
        }
    }

    if header:
        if header_type is None:
            raise ValueError("When Header is true, header type needs to be specified")
        if header_value is None and header_type != "location":
            raise ValueError("When Header is true, header value needs to be specified")

        header_req = {}
        if header_type == "text":
            header_req = {"text": header_value}
        elif header_type == "location":
            header_req = {"location": {
                "name": loc_name,
                "address": loc_address,
                "latitude": loc_latitude,
                "longitude": loc_longitude
            }}
        elif header_type == "image" or header_type == "document" or header_type == "video":
            link={"link":header_value}
            header_req = {header_type: link}
        else:
            raise ValueError("Unsupported header_type")

        whatsapp_request_data['template']['components'].append({
            "type": "header",
            "parameters": [{"type": header_type, **header_req}]
        })

    emt_list = [{"type": "text", "text": param} for param in body_parameters]

    whatsapp_request_data['template']['components'].append({
        "type": "body",
        "parameters": emt_list
    })

    return whatsapp_request_data

@app.post("/send_whatsapp_message/")
async def send_whatsapp_message(
    mobile: int = Query(..., description="Mobile number"),
    template_name: str = Query(..., description="Name of the template"),
    language: str = Query(..., description="Language code"),
    header: bool = Query(..., description="Header is Present"),
    body_parameters: List[str] = Query(..., description="List of body parameters"),
    header_type: str = Query(None, description="Type of the header"),
    header_value: str = Query(None, description="Header Content"),
    loc_name:str=None,
    loc_address:str=None,
    loc_latitude=None,
    loc_longitude=None,
    coupon_code:str=None
):
    

    try:        
        whatsapp_request_data = create_whatsapp_request(
            mobile=mobile,
            template_name=template_name,
            language=language,
            header=header,
            body_parameters=body_parameters,
            header_type=header_type,
            header_value=header_value
        )

        if header_type == "location":
            whatsapp_request_data['template']['components'][0]['parameters'][0]['location'] = {
                "name": loc_name,
                "address": loc_address,
                "latitude": loc_latitude,
                "longitude": loc_longitude
            }

        if template_name.endswith("coupon"):
            if coupon_code is None:
                raise ValueError("Coupon code is required for COPY_CODE button")
            file={"type":"coupon_code","coupon_code":coupon_code}
            button = {
                "type": "button",
                "index": 0,
                "type": "button",
                "sub_type":"COPY_CODE",
                "parameters": [file]
            }
            whatsapp_request_data['template']['components'].append(button)
    except ValueError as err:
        raise HTTPException(status_code=400,detail=str(err))

    api_url = "https://graph.facebook.com/v17.0/126923810513291/messages"
    access_token = "EAAf0OEMx0AcBO0ziaHRQfGsIvZBymwQCr4PXMsnQVcPDNrjxZBHVsMrZC1OG70iHG4FfEKk8JY67SCa9Cobm1WqKo4xZA2J27El4sZA5ku923fSkYOKsRBJirndqoX9nRX01XX5R1huiVssHJUTiKxXLCzXHIHFD1MUuwRbCUtDslDq7KZClGoZAHvFGnWIuUIluhMrPZAHNu9g2DwMfi64ZD"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(whatsapp_request_data))
    return response.json()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)