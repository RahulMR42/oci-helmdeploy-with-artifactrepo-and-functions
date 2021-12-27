# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import os
import json
import logging

import oci

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    try:
        body = json.loads(data.getvalue()) 
        logging.getLogger().info("Fetching the information")
        artifact_repo_id = body[0]['data']['stateChange']['current']['repositoryId']
        artifact_path = body[0]['data']['stateChange']['current']['artifactPath']
        artifact_version = body[0]['data']['stateChange']['current']['version']
        signer = oci.auth.signers.get_resource_principals_signer()
        os.environ['OCI_CLI_AUTH']="resource_principal" #set OCI CLI to use resource_principal authorization
        logging.getLogger().info(f'Input Params Repo = {artifact_repo_id} Path = {artifact_path}, Version = {artifact_version}')
        return response.Response(
            ctx, 
            response_data=json.dumps({"status": "Hello World! with customImage"}),
            headers={"Content-Type": "application/json"})
    except Exception as error:
        logging.getLogger().info(f'Exception - {error}')