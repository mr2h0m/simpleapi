import logging
import re 

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    str = req.params.get('customstring')
    if not str:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            str = req_body.get('customstring')

    if str:
        regex = re.compile(r"((Oracle)|(Google)|(Microsoft)|(Amazon)|(Deloitte))", re.IGNORECASE)
        result_str = regex.sub(r"\1©", str)
        return func.HttpResponse(result_str)
    else:
        return func.HttpResponse(
             "Please pass a string as 'customstring=...' on the query string or in the request body",
             status_code=400
        )
