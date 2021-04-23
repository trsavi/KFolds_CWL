# KFolds_CWL
Calculating accuracy and roc-auc score with KFolds cross-validation on dataset using Common Workflow Language. 

Run in terminal.

Requiremets:
 - cwltool (https://github.com/common-workflow-language/cwltool)
 - python dependencies in requirements.txt pip install -r requirements.txt
```
git pull https://github.com/trsavi/KFolds_CWL/

cwl-runner scatterPython.cwl.yaml config.yaml
```

Or with Docker container

Requirements:
 - Docker 

```
docker pull trsavi/cwl_kfolds
docker images
docker run -p 8000:8000 <trsavi/cwl_kfolds_IMAGE_ID>
```
