# EmailChecker

Hello there, this is a simple OSINT python script that I have created to find emails based on First and Last Name and common email structures

## Setup
We need to install this package to verify emails:
```
pip install validate-email-address
```
## Usage

```
python main.py emailList.txt domainList.txt

or

python main.py "daniel coutinho" gmail.com
```

The first argument can be a string with the first and last name or if you put a .txt file name it will look for a file as input
An EmailList.txt example
```
daniel coutinho
charlie brown
sally brown
```
The same goes for the second argument but with domains.

## Upcoming Features
* Add more email structures
* Add bash script to call the program
  * Add Help flag
* Better Input Validation
* Ability to insert custom email structure
* Add a quick search algorithm across a list of names
