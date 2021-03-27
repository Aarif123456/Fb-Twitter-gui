## What is this?  🤔 
    This program is automated spear phishing tool that works on both Facebook and Twitter. 
    THIS IS ONLY INTENDED FOR RESEARCH PURPOSES  

## Authors: 
- Abdullah Arif
- Abdullah Chattha
- Ashraf Taifour
- Mohamad Elchami
- Steve Pham

## Supervisor
    Dr. Sherif Saad Ahmed

## How to run
Program has been tested on Linux
1. Setup
* Make sure you have gecko driver installed: https://github.com/mozilla/geckodriver/releases
* Also, install TOR: https://www.torproject.org/download/ 
* Extract TorFolder to program directory
2. Recommended step: use virtual environment
```
python3 -m venv facebookEnv
source facebookEnv/bin/activate
```
4. Install dependencies 
`pip3 install -r requirements.txt`

5. Run program
    `python3 ScrapeAppGUI.py`

## troubleshooting
If you are running on a python version that doesn't have tkinter installed
please run 
`apt-get install python3-tk`

## Importance
Phishing attacks accounted for 80% of security incidents. And the pandemic has increased the number of cyber attacks. So, it is imperative that we study different social attacks. There is a more potent type of phishing called “spear-phishing”, where an attacker gathers information about a user and uses that to craft a more persuasive message. This technique has a much higher click through rate than average phishing attacks. Fortunately, this method is time-consuming and so the attacker cannot target as many people. However, we believe that you can use machine learning to automate this process. If this process becomes widespread, it would have disastrous consequences.

Our project will be to create this automated spear-phishing tool. We will then use our tool to analyze them to determine the effectiveness of various algorithms and the vulnerability on different platforms. We also hope to show the potency of this attack. So, we will compare it to normal phishing attacks and compare the results. We hope the results from our study will help future developers and cybersecurity researchers to create more effective safeguards against social attacks.

Most malware comes from email. However, there is a rising trend for phishing attacks conducted on social media. This is because social media contains a plethora of personal information which makes it possible to launch this type of automated spear-phishing attack.

Rather than creating a defensive tool like a phishing detector using machine learning, we have created an offensive tool. This is because when people are trying to break things, they look for the easiest ways to get the job done. The principle of easiest penetration states that a security system is as strong as its weakest link. So by thinking like an attacker, we can become better defenders.

Furthermore, we wanted to show how easy it is to scale our attack by using libraries like PySpark. This because for each user we only need a limited amount of tweets to generate believable tweets. However the challenge comes from having to deal with millions of users, since most users won't fall for the phishing attack. However, we can easily parallelize the training of our model by creating one worker per user. 
