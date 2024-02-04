import json
import boto3

dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
# TODO: 環境変数から取得するようにする
table_name = "sampleTable"
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    print(event)
    path = event.get("path", "")
    method = event.get("httpMethod", "")
    user_id = event.get("queryStringParameters", {}).get("userid", "")
    if path == "/hello":
        if method == "GET":
            response = table.get_item(Key={"UserID": user_id})
            return {
                "statusCode": 200,
                "body": json.dumps(response["Item"]),
            }
        elif method == "POST":
            return {
                "statusCode": 200,
                "body": json.dumps({"msg": "world"}),
            }
        return {
            "statusCode": 404,
            "body": json.dumps({"msg": "Not Found"}),
        }
    # ログを出力する
    return {
        "statusCode": 404,
        "body": json.dumps({"msg": "Not Found"}),
    }
