
resource "aws_s3_bucket" "raw_data" {
  bucket = "healthcare-raw-data-bucket-12345"
}

resource "aws_s3_bucket" "processed_data" {
  bucket = "healthcare-processed-data-bucket-12345"
}