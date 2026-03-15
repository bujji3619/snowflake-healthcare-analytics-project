resource "aws_lambda_function" "etl_lambda" {

  function_name = "healthcare-etl"

  filename      = "lambda.zip"

  handler       = "etl_function.lambda_handler"

  runtime       = "python3.9"

  role          = aws_iam_role.lambda_role.arn

}