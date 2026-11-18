# Writeup: TryHackMe Checkmate

## Challenge Premise

> Marco Bianchi, a systems administrator, recently deployed several internal services, including a firewall console, employee portal, social platform, and SSH access to critical infrastructure. Due to tight deadlines and operational pressure, Marco reused weak, predictable, and pattern-based passwords across multiple systems.  
>
> Your objective is to conduct a password security assessment to identify weaknesses in Marco’s authentication practices.

## Writeup

The first step of the challenge was to access the main application on port 5000 of the target machine. This accessed a hub where the rest of the challenge could continue.

![alt text](<Operation Checkmate Main Page.png>)

### Level 1: Default Credentials

The FirewallOS Management Console was hosted on port 5001 of the target machine. The information for level 1 was the following:

> Marco deployed a firewall at firewall.thm:5001 but kept default credentials.

To attempt to crack the password, Burp Suite Intruder was used. This would automate the process more than iterating credentials manually, and build up experience using the tool for future web application testing. Passwords from `rockyou.txt` were used, revealing the password to be `12345`.

### Level 2: Employee Login Portal

The following information was provided for level 2:

> Marco built an internal Employee Login panel on jobs.thm:5002 and used common company keywords as passwords.

To begin cracking the password, the company employee panel was first used.

![alt text](<Engineering Careers Landing Page.png>)

This contained a number of keywords. Cewl was used to scrape the page and put the output into `loginportalcewl.txt`

```bash
cewl http://10.128.171.154:5002/ -w loginportalcewl.txt
```

Burp Intruder was then used with the `loginportalcewl.txt` wordlist. As the task didn't specify a username format, it was assumed to be `marco`. `excellence` returned a 302 request, identifying the password.

![alt text](<Level 2 Burp Suite.png>)

### Level 3: Social Media

The following information was provided for level 3:

> Navigate to social.thm:5003 and derive Marco's password from personal info.

As no difference was specified in the username structure, it was assumed to be `marco` again. The website specified that the jobs portal would hold Marco's password.

![alt text](<Task 3 Marco's Profile Information.png>)
