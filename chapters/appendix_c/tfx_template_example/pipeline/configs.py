# Lint as: python2, python3
# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""TFX complaint prediction template configurations.

This file defines environments for a TFX complaint prediction pipeline.
"""

# Pipeline name will be used to identify this pipeline.
PIPELINE_NAME = "complaint_prediction_pipeline"

# GCP related configs.

# Following code will retrieve your GCP project. You can choose which project
# to use by setting GOOGLE_CLOUD_PROJECT environment variable.
try:
    import google.auth  # pylint: disable=g-import-not-at-top

    try:
        _, GOOGLE_CLOUD_PROJECT = google.auth.default()
    except google.auth.exceptions.DefaultCredentialsError:
        GOOGLE_CLOUD_PROJECT = ""
except ImportError:
    GOOGLE_CLOUD_PROJECT = ""

# Specify your GCS bucket name here. You have to use GCS to store output files
# when running a pipeline with Kubeflow Pipeline on GCP or when running a job
# using Dataflow. Default is '<gcp_project_name>-kubeflowpipelines-default'.
# This bucket is created automatically when you deploy KFP from marketplace.
GCS_BUCKET_NAME = GOOGLE_CLOUD_PROJECT + "-kubeflowpipelines-default"

# TODO(step 8,step 9): (Optional) Set your region to use GCP services including
#                      BigQuery, Dataflow and Cloud AI Platform.
# GOOGLE_CLOUD_REGION = ''  # ex) 'us-central1'

PREPROCESSING_FN = "models.preprocessing.preprocessing_fn"
RUN_FN = "models.keras.model.run_fn"
# NOTE: Uncomment below to use an estimator based model.
# RUN_FN = 'models.estimator.model.run_fn'

TRAIN_NUM_STEPS = 100
EVAL_NUM_STEPS = 100

# Change this value according to your use cases.
EVAL_ACCURACY_THRESHOLD = 0.6

# Beam args to run data processing on DataflowRunner.
# TODO(step 8): (Optional) Uncomment below to use Dataflow.
# DATAFLOW_BEAM_PIPELINE_ARGS = [
#    '--project=' + GOOGLE_CLOUD_PROJECT,
#    '--runner=DataflowRunner',
#    '--temp_location=' + os.path.join('gs://', GCS_BUCKET_NAME, 'tmp'),
#    '--region=' + GOOGLE_CLOUD_REGION,
#    # TODO(tensorflow/tfx#1461) Remove `shuffle_mode` after default is changed.  # noqa pylint: disable=g-bad-todo
#    '--experiments=shuffle_mode=auto',
#    # TODO(tensorflow/tfx#1459) Remove `disk_size_gb` after default is
#    #                           increased.  # pylint: disable=g-bad-todo
#    '--disk_size_gb=50',
#    # If you are blocked by IP Address quota, using a bigger machine_type will
#    # reduce the number of needed IPs.
#    # '--machine_type=n1-standard-8',
#    ]

# A dict which contains the training job parameters to be passed to Google
# Cloud AI Platform. For the full set of parameters supported by Google
# Cloud AI Platform, refer to
# https://cloud.google.com/ml-engine/reference/rest/v1/projects.jobs#Job
# TODO(step 9): (Optional) Uncomment below to use AI Platform training.
# GCP_AI_PLATFORM_TRAINING_ARGS = {
#     'project': GOOGLE_CLOUD_PROJECT,
#     'region': GOOGLE_CLOUD_REGION,
#     # Starting from TFX 0.14, training on AI Platform uses custom containers:
#     # https://cloud.google.com/ml-engine/docs/containers-overview
#     # You can specify a custom container here. If not specified, TFX will use
#     # a public container image matching the installed version of TFX.
#     # TODO(step 9): (Optional) Set your container name below.
#     'masterConfig': {
#       'imageUri': 'gcr.io/' + GOOGLE_CLOUD_PROJECT + '/tfx-pipeline'
#     },
#     # Note that if you do specify a custom container, ensure the entrypoint
#     # calls into TFX's run_executor script (tfx/scripts/run_executor.py)
# }

# A dict which contains the serving job parameters to be passed to Google
# Cloud AI Platform. For the full set of parameters supported by Google Cloud AI
# Platform, refer to
# https://cloud.google.com/ml-engine/reference/rest/v1/projects.models
# TODO(step 9): (Optional) Uncomment below to use AI Platform serving.
# GCP_AI_PLATFORM_SERVING_ARGS = {
#     'model_name': PIPELINE_NAME,
#     'project_id': GOOGLE_CLOUD_PROJECT,
#     # The region to use when serving the model. See available regions here:
#     # https://cloud.google.com/ml-engine/docs/regions
#     # Note that serving currently only supports a single region:
#     # https://cloud.google.com/ml-engine/reference/rest/v1/projects.models#Model  # noqa pylint: disable=line-too-long
#     'regions': [GOOGLE_CLOUD_REGION],
# }
