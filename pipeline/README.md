# Setup der Tekton Pipeline Demo

Diese Demo beruht auf der Anleitung aus der OpenShift Doku:

https://docs.openshift.com/container-platform/4.5/pipelines/creating-applications-with-cicd-pipelines.html

## Versionsinformationen

Diese Demo wurde mit den folgenden Software-Versionen getestet:

```
$ tkn version
Client version: 0.11.0
Pipeline version: v0.11.3
Triggers version: v0.4.0
```


## Einrichten der Doku im aktuellen Namespace

```
./setup_demo.sh
```

## Starten der Pipeline

```
tkn pipeline start build-and-deploy -p deployment-name=leapyear-api \
  -r git-repo=git-leapyear -r image=image-leapyear
```

## Verfolgen der Pipeline-Logs

```
tkn pipelinerun logs -f --last
```

