# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


import os

from airflow import models
from airflow.providers.amazon.aws.transfers.sftp_to_s3 import SFTPToS3Operator
from airflow.utils.dates import days_ago

S3_BUCKET = os.environ.get("S3_BUCKET", "test-bucket")
S3_KEY = os.environ.get("S3_KEY", "key")

with models.DAG(
    "example_sftp_to_s3",
    schedule_interval=None,
    start_date=days_ago(1),  # Override to match your needs
) as dag:
    # [START howto_sftp_transfer_data_to_s3]
    create_sftp_to_s3_job = SFTPToS3Operator(
        task_id="create_sftp_to_s3_job",
        sftp_conn_id="sftp_conn_id",
        sftp_path="sftp_path",
        s3_conn_id="s3_conn_id",
        s3_bucket=S3_BUCKET,
        s3_key=S3_KEY,
    )
    # [END howto_sftp_transfer_data_to_s3]