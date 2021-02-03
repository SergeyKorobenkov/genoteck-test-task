yc serverless function create --name=cloud-function

yc serverless function version create \
--function-name=cloud-function \
--runtime python37-preview \
--entrypoint handler.handler \
--memory 128m \
--execution-timeout 5s \
--source-path ./genoteck-cloud-function.zip