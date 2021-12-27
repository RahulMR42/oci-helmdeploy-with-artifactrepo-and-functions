# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import json
import logging

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    body = json.loads(data.getvalue()) 
    logging.getLogger().info("Fetching the information")
    artifact_repo_id = body[0]['data']['stateChange']['current']['repositoryId']
    logging.getLogger().info(f'Input Params Repo = {artifact_repo_id}')
    
    return response.Response(
        ctx, 
        response_data=json.dumps({"status": "Hello World! with customImage"}),
        headers={"Content-Type": "application/json"}
    )