
echo -n "your_namespace" | base64
echo -n "your_username" | base64
echo -n "your_password" | base64

kubectl create secret generic registry-credentials \
  --from-literal=registry-namespace=<base64-encoded-namespace> \
  --from-literal=registry-username=<base64-encoded-username> \
  --from-literal=registry-password=<base64-encoded-password> \
  -n mlflow-tracking