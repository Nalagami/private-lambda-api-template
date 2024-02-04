## 準備物
- VPC
- subnet
- VPCエンドポイント

## 準備
- .env を以下の内容で作成する
```
VPC_ID=<vpc lambdaを作成するVPCのID>
SUBNET_ID=<vpc lambdaを作成するサブネットのID>
VPC_ENDPOINT_ID=<api gateway に接続するVPCエンドポイントのID>
SOURCE_SECURITY_GROUP=<VPC エンドポイントに割り当てているSGのID>
```

## インフラ構成図
![](./docs/infra.svg)