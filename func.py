# Copyright (c) 2020 Oracle, Inc.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import os
import json
import logging

import oci

from fdk import response

class oci_artifact():
    def __init__(self,region,signer):
        """Init with  a region and resource principal signer"""
        self.region = region
        self.signer = signer
        


def handler(ctx, data: io.BytesIO=None):
    try:
        body = json.loads(data.getvalue()) 
        logging.getLogger().info("Fetching the information")
        artifact_repo_id = body[0]['data']['stateChange']['current']['repositoryId']
        artifact_path = body[0]['data']['stateChange']['current']['artifactPath']
        artifact_version = body[0]['data']['stateChange']['current']['version']
        region = os.environ['oci_region']
        signer = oci.auth.signers.get_resource_principals_signer()
        os.environ['OCI_CLI_AUTH']="resource_principal" #set OCI CLI to use resource_principal authorization
        logging.getLogger().info(f'Input Params Repo = {artifact_repo_id} Path = {artifact_path}, Version = {artifact_version}')
        artifact_handler = oci_artifact(region,signer)
        logging.getLogger.info(artifact_handler)
        return response.Response(
            ctx, 
            response_data=json.dumps({"status": "Hello World! with customImage"}),
            headers={"Content-Type": "application/json"})
    except Exception as error:
        logging.getLogger().info(f'Exception - {error}')
        return response.Response(
            ctx, 
            response_data=json.dumps({"status": f'Exception - str({error})'}),
            headers={"Content-Type": "application/json"})