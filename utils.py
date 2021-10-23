def build_message(responce):
    message = {
        "success": True,
        "error": "",
    }
    if response.status >= 400:
        message["success"] = False
        message["error"] = response.body
    return message