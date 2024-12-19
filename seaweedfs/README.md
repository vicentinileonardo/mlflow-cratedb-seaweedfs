## Changes w.r.t. standard `values.yaml`

Main changes with respect to the original `values.yaml` of SeaweedFS helm chart (see references):

- changed some fields of the s3 section under filer to:
```yaml
filer:
  s3:
    enabled: true
    enableAuth: true
    existingConfigSecret: my-s3-secret
    createBuckets:
      - name: mlartifacts
        anonymousRead: false
```
- changed affinity to `affinity:""` everywhere in the `values.yaml`
- changed nodeSelector  (de-commented) across the `values.yaml`

## How to install

Add the helm repo:
```bash
helm repo add seaweedfs https://seaweedfs.github.io/seaweedfs/helm
```

Label the node:
```bash
kubectl label node YOUR_NODE_NAME sw-volume=true sw-backend=true
```

Create the namespace
```bash
kubectl create namespace seaweedfs
```

Create the secret:
```bash
chmod +x seaweedfs/secret.sh && ./seaweedfs/secret.sh
```

Set env variables for local testing:
```bash
export AWS_ACCESS_KEY_ID=<access_key>
export AWS_SECRET_ACCESS_KEY=<secret>
```

Install the helm chart:
```bash
helm install --values=values.yaml seaweedfs seaweedfs/seaweedfs --namespace=seaweedfs
```

Wait for the pods to be ready:
```bash
# Wait for master
kubectl wait --for=condition=ready pods -l app.kubernetes.io/component=master -n seaweedfs --timeout=300s

# Wait for volume servers
kubectl wait --for=condition=ready pods -l app.kubernetes.io/component=volume -n seaweedfs --timeout=300s

# Wait for filer
kubectl wait --for=condition=ready pods -l app.kubernetes.io/component=filer -n seaweedfs --timeout=300s
```


Port forward the s3 service:
```bash
kubectl port-forward service/seaweedfs-s3 8333:8333 -n seaweedfs
```

### Testing the installation of SeaweedFS

Reference:
- https://github.com/seaweedfs/seaweedfs/wiki/AWS-CLI-with-SeaweedFS

Install the aws cli:
```bash
pip install awscli
```

Make a bucket:
```bash
aws --endpoint-url http://localhost:8333 s3 mb s3://test1
```
<details>
<summary>Expected output (Click to expand) </summary>

```bash
make_bucket: test1
```
</details>

List buckets:
```bash
aws --endpoint-url http://localhost:8333 s3 ls
```
<details>
<summary>Expected output (Click to expand) </summary>

```bash
2024-12-18 18:43:00 test1
```
</details>

Add an object:
```bash
aws --endpoint-url http://localhost:8333 s3 cp README.md s3://test1
```
<details>
<summary>Expected output (Click to expand) </summary>

```bash
upload: ./README.md to s3://test1/README.md   
```
</details>

List files inside the bucket:
```bash
aws --endpoint-url http://localhost:8333 s3 ls s3://test1
```
<details>
<summary>Expected output (Click to expand) </summary>

```bash
2024-12-18 18:44:11        797 README.md  
```
</details>

Remove an object:
```bash
aws --endpoint-url http://localhost:8333 s3 rm s3://test1/README.md
```
<details>
<summary>Expected output (Click to expand) </summary>

```bash
delete: s3://test1/README.md 
```
</details>

Remove a bucket:
```bash
aws --endpoint-url http://localhost:8333 s3 rb s3://test1
```
<details>
<summary>Expected output (Click to expand) </summary>

```bash
remove_bucket: test1
```
</details>




## References:
- https://github.com/seaweedfs/seaweedfs/tree/master/k8s/charts/seaweedfs
- Original values.yaml: https://github.com/seaweedfs/seaweedfs/blob/ba0707af641e41ba3cbed2b533ed2432d21295ba/k8s/charts/seaweedfs/values.yaml

