# Sample SQS send script for Bash / MacOS/ WSL / GitBash

aws sqs send-message \
    --queue-url "https://sqs.eu-west-1.amazonaws.com/123456789/mark-m-coffee-sales-queue" \
    --message-body '{"sale": "Latte for mark-m"}' \
    --profile sot-academy
