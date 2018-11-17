# Introduction

Thanks for considering contributing to <Name> please read this contributing guidelines so that we can become the next best thing  
... or not, the point is still having a little fun with Python

### Why should I follow the guidelines
While it's true that this project is made just for fun this doesn't mean it won't help someone in the future.  
Sure, time objects are easy to use but there's no unified experience on ticks or what should happen next, or even WHEN should it happen.  
This package will be trying to solve that.


### What am I looking for
What I am looking for includes but is not limited to:

* bug fixes (can't ever have enough bug fixes)
* new/improved docstrings, I'll try to document everything myself but I could always have some help
* new features, you figured out a new way to extend functionality? GREAT!! Add that in and I'll carefully read it and add it if convenient.

### Explain contributions you are NOT looking for (if any).

* please note that is different **USING** the package than **EXTENDING** the package, please save me the sorrow of turning down a great piece of code just because it's **USING** instead of **EXTENDING**


# Ground Rules

### Responsibilities
* Create issues for any major changes and enhancements that you wish to make. Discuss things transparently and get community feedback.
* Don't add any classes to the codebase unless absolutely needed. Err on the side of using functions.
* Keep feature versions as small as possible, preferably one new feature per version.
* Be welcoming to newcomers and encourage diverse new contributors from all backgrounds.

# Your First Contribution and How to Get Started
### You want to help but don't know where to start?  
Here's a small list of what you can do:  

* write some tests, as of the writing of this guide I don't know how to unit test python so al helo is apreciated.
* found a bug? squash it we'll all be thankfull for it
* you saw an open issue that's "way too easy to fix"? please do fix it, it's hard to prioritise bugs. your iniciative is highly apreciated

### First time contributing to an open source project?
Here are a couple of friendly tutorials: http://makeapullrequest.com/ and http://www.firsttimersonly.com/

### How to submit a contribution.

For something that is bigger than a one or two line fix:

1. Create your own fork of the code
2. Do the changes in your fork
3. If you like the change and think the project could use it:
    * Be sure you have followed the code style for the project.
    * Send a pull request with a TL;DR of the changes you made
4. Please **DO NOT** push your labels, unless explicited noted labels are for realeases only

### Disclaimer for Contributions
**I and any future code owners reserve the right to accept or reject any contribution under any excuse we come up with**
Inlcuding but not limited to:

* I didn't understand the code, even with comments
* I found your contribution importance/size ratio too low

# How to report a bug
### Security Disclosures
In theory this project should **NOT** create any security issues but sh*t does happen.  
If you find a security vulnerability, do NOT open an issue. Email danybeam@gmail.com with the subject: "PyTime-Utils Security Issue" instead.  
It will go straight to my personal e-mail and will react to the issue accordingly.  
I have to insist that you use **THAT** subject specifically, I have filters that will send all kinds of alarms so that I check it ASAP.

In order to determine whether you are dealing with a security issue, ask yourself these two questions:
* Can I access something that's not mine, or something I shouldn't have access to?
* Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably dealing with a security issue. Note that even if you answer "no" to both questions, you may still be dealing with a security issue, so if you're unsure, just email me.

# Code review process
### I PR-ed... now what?
Since this project was born from 100 days of code expect (almost) daily surveillance until April 16th 2018.  
After that date expect at best a weekly triage and at worst a monthly one.  
If the project gets big enough I might add more people to help with that.

# Community
There isn't a community per se but I'm free to discuss on twitter @danybeam  
or you can use the contact email danybeam@gmail.com I check it regularly so you can expect some kind of answer relatively soon.

# BONUS: Code, commit message and labeling conventions
### Commit Message Conventions.

Less is more. don't write a lot but be explicit.  
something like:  
"chandged file X" with an extended description of "changed X because Y check lines i trough j" is more than enough.  
If you changed 5 lines or less the main message is enough.

### Labeling Issues
* You like the package but you don't plan in programming X specific new feature:
    * Label it as "Feature Request"
* You ARE going to programm it yourself:
    * "Feature Sugestion" is the label for you
* Excuse me, waiter? there's a bug in my code:
    * why yes, we labeled clearly as "Bug" on the menu
* What does "Aproved" and "Open" mean:
    * "Aproved" means I/we like the feature and it's authorised to be developed at any time
    * "Open" refers to both "Bugs" and "Aproved" issues, it means I/we know they are there but haven't finished them yet
* I haven't finished X yet and I'm / my team is working on it:
    * "In progress" should be enough warning
        * I'm not going to heavily enforce the "In progress" exclusivity but whoever called dibs should have the credit
* So... is this finished yet?
    * If it's tagged "Closed" it sure is

Custom labels are welcomed but try to not overwhelm newcommers.




# Disclaimer
This CONTRIBUTING file was blattantly and shamelessly adapted from [nayafia template](https://github.com/nayafia/contributing-template/blob/master/CONTRIBUTING-template.md)
if you liked it, you can thank her. I just adapted it.
