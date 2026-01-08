# Sample SNS send script for Powershell
# for a Standard topic - FIFO topics need more things specified

aws sns publish `
  --topic-arn "arn:aws:sns:eu-west-1:745580839125:mark-m-coffee-sales-notifications" `
  --message '{"sale": "Latte for Mark"}'
