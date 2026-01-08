## A little bit about networking in AWS

---

### What do we want to cover?

- There is a LOT to know about networking in AWS - we will not cover it all here, not get anywhere close :)
- This will look a little more at some of the ways our current AWS environment is set up, and some aspects of networking that you will have come across in the course so far
- You should not NEED any of this information to complete your projects, it is all just for extra context/interest

---

### Firstly - What is a VPC?

- We have created a VPC ('Virtual Private Cloud') within AWS for all of the things we are making for this bootcamp and some of the other bootcamps which we are running
- Think of a VPC as a 'cloud-within-a-cloud' - we have our own virtual network inside the broader AWS cloud which is dedicated to us
- It's 'virtual' because we still don't know or care exactly where our VPC is - it is just 'somewhere on the AWS servers' - but it is LOGICALLY separated from the rest of AWS rather than PHYSICALLY separated.

---

### Firstly - What is a VPC?

- The VPC has a subnet, or multiple subnets, which is a range of IP addresses - some can be public which means the subnet can connect to the internet, and some are private, which means they can not connect to the internet
- You can allow your VPC to communicate with the rest of the internet - this involves using something called in 'internet gateway' which you attach to your VPC. You can then control the traffic that comes through this internet gateway to control exactly who/what can access your resources. This links to the above idea of public and private subnets - generally the internet gateway is attached to your public subnets

---

### Firstly - What is a VPC?

- More info (quite technical) - https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html

---

### What is an IP address?

- A UNIQUE address that will identify a resource on a network or the internet
- The most common form of IP address you will see is IPV4 - made up of four sets of numbers in the format X.X.X.X -> where each 'X' can be any number from 0 - 255
- Theoretically, this means there is a maximum of about 4.2 billion IP addresses that can be assigned
- We are running out of new IP addresses to assign - https://en.wikipedia.org/wiki/IPv4_address_exhaustion
- Current drive to move to IPV6 - 3.4 x 10^38 addresses
- Each of our subnets will have a block of IP addresses, and each thing we create inside that subnet will be assigned an IP address.

---

### What do you need to talk to a computer?

- If we know the IP address of a particular resource on the internet or within our own network, is that enough to interact with it?
- Not quite....we will also need the port number
- If the IP address is the address of the system on a network, the port is the address of a particular service within that system
- We need to specify the port number so the system knows what part, or what service, we want to talk to, so that it can know what to do with our request?

---

### What do you need to talk to a computer?

- So now we know the IP address and port, we're good to go?
- Not just yet! One more thing to consider is the PROTOCOL. This is basically saying that we need to speak the language that the service we're talking to can understand.
- Protocols are a bit like a language - they set out the rules by which two services or two machines communicate - right down to exactly how the electronic signals are sent and interpreted

---

### What do you need to talk to a computer?

- With an IP address, a port and a protocol, we are pretty much set!
- The ports and protocols that particular services used tend to be established - so don't try remember them they can always be looked up, e.g.:
    - Http - port 80 - protocol TCP
    - Https - port 443 - protocol TCP
    - SSH - port 22 - protocol TCP
    - Postgres - 5432 - TCP
    - Grafana - 3000 - TCP
    - MySQL - 3306 - TCP
- You will find you don't often need to know the protocol - it will often be handled in the background

---

### What is a firewall?

- A device (physical or software) which analyses all the traffic which is coming in to a machine (inbound rules) or going out from a machine (outbound rules), and filters it based on rules which you write.
- Think of it like a barrier between the internet or a wider network, and a trusted subnetwork or a specific device
- A firewall rule generally consists of an action (Allow/Deny), a port number, a protocol, and a source/destination
- Let's say you start with a server which will accept no traffic, but you want to run Grafana on it. You would set an inbound and outbound rule on port 3000 for TCP protocol. This would allow Grafana to communicate out to whatever it is monitoring, and to receive back the data it needs

---

### Firewalls in AWS

- In AWS, we use 'security groups' in place of firewalls - just think of them as the same thing
- We created an EC2 instance and also a security group which we attached to it.
- The security group had two rules:
    - Http | port 80 | TCP | 0.0.0.0/0 -> allowed http connections through port 80. This basically meant you could browse to it in your web browser from anywhere on the internet.
    - SSH | port 22 | TCP | <your IP address> -> allowed SSH connections through port 22, but only from your IP address
- If traffic comes in that does not meet one of these rules, it is rejected

---

### A little more about subnets

- Mentioned above that you have the concept of a public and private subnet within your VPC. Let's think about this a little more in context of some of the things we've done.
- Every team (I think) has gone the route of having a postgres database in RDS, with a 'jump server' on EC2. Why?
    - Your RDS db is on a server in the background. AWS won't let us put a database server on a public subnet, we had to use a private one. This meant though, that we couldn't connect to it from our machines.
    - We can, however, create an EC2 instance, and put it on the public subnet, which is connected to the internet gateway, so we can make connections to it from outside our VPC.
    - Because the EC2 is in our VPC, we can connect to the RDS server from there
    - Hence, we created an EC2 server, and used this as the 'jump server' to get to our RDS server

---

### A little more about subnets

- When we wanted to connect to RDS from our Lambdas, we had to take a slightly different approach...
    - You'll recall that Lambdas are 'serverless' so they are more ephemeral and we don't control what server they are on.
    - There is a configuration option to 'attach' them to a VPC however, which we did
    - Once the lambda is attached to the VPC, we don't need to go through the EC2 server when you're running your code in the Lambda on AWS, as you're already inside the VPC so can get to the private subnet.
