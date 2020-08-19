#!/bin/bash

NAMESPACE=$(oc project -q)
export NAMESPACE

oc apply -f 01_apply_manifest_task.yml
oc apply -f 02_update_deployment_task.yml
oc apply -f 03_update_deploymentconfig_task.yml
oc apply -f 10_pipeline.yml
oc apply -f 20_res_git-leapyear.yml

cat 21_res_image-leapyear.yml.tmpl | envsubst | oc apply -f -

