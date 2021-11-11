# 0x00. AirBnB clone - The console 
`Release date: Nov-15-2021`
<!-- share on twitter -->
[![Twitter](https://img.shields.io/twitter/url?labe=share&style=social&url=https%3A%2F%2Fgithub.com%2Fralexrivero%2FAirBnB_clone)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fralexrivero%2FAirBnB_clone)

<img src="img/home_screen_custom.png" alt="AirBnB Custom banner">

## 0x00.Table of contents

* [0x01 Introduction](#0x01-Introduction)
* [0x02 Environment](#0x02-Environment)
* [0x03 Installation](#0x03-Installation)
* [0x04 Testing](#0x04-Testing)
* [0x05 Usage](#0x05-Usage)
* [0x06 License](#0x06-License)
* [0x07 Contributing](#0x07-Contributing)
* [0x08 Todo](#0x08-Todo)
* [0x09 Changelog](#0x09-Changelog)
* [0x0A Tests](#0x0A-Tests)
* [0x0B Questions](#0x0B-Questions)
* [0x0C Conclusion](#0x0C-Conclusion)
* [0x0D References](#0x0D-References)
* [0x0E Acknowledgements](#0x0E-Acknowledgements)
* [0x0F History](#0x0F-History)
* [0x10 Credits](#0x10-Credits)

## 0x01 Introduction

Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter to manage objects abstraction between objects and how they are stored

`BaseModel` 
## 0x02 Environment

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> <!--HTML5--> <a href="https://html.spec.whatwg.org/multipage/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=HTML5&color=E85827&logo=HTML5&logoColor=E34F26&labelColor=2F333A" alt="HTML5"></a> <!-- CSS3 --> <a href="https://www.w3.org/Style/CSS/Overview.en.html" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=CSS3&color=0071B5&logo=CSS3&logoColor=1572B6&labelColor=2F333A" alt="CSS3"></a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="Suite CRM"></a> <!-- atom --> 
<a href="https://atom.io/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Atom&color=66595C&logo=Atom&logoColor=f1f1f1&labelColor=2F333A" alt="Suite CRM"></a><!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>
 <!-- Style guidelines -->
- Style guidelines:
  - [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  - [PEP8](https://pep8.org/)

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.

## 0x03 Installation

```git clone https://github.com/ralexrivero/AirBnB_clone.git```

change to the `AirBnb` directory and run the command:

``` ./console.py ```
### Execution

In interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

in Non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## 0x04 Testing

### Documentation

- Modules: ```python3 -c 'print(__import__("my_module").__doc__)'```
- Classes: ```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```
- Functions (inside and outside a class): ```python3 -c 'print(__import__("my_module").my_function.__doc__)'```
and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```

### Python Unit Tests

- unittest module
- File extension ``` .py ```
- Files and folders star with ```test_```
- Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
- Execution command: ```python3 -m unittest discover tests```
- or: ```python3 -m unittest tests/test_models/test_base.py```

### run test in interactive mode

```
$ echo "python3 -m unittest discover tests" | bash
```

## 0x05 Usage

List of commands and examples usage:

The prompt (hbnb) waits for a command in an infinite loop.

- help

example:

- quit

example:

## 0x06 License

## 0x07 Contributing

## 0x08 Todo

## 0x09 Changelog

## 0x0A Tests

## 0x0B Questions

## 0x0C Conclusion

## 0x0D References

## 0x0E Acknowledgements

## 0x0F History

## 0x10 Credits

Rodrigo

<a href="https://www.linkedin.com/in/rodrigo-mato-pla/" target="_blank">  <img align="left" alt="Rodrigo Mato | LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=social&logo=linkedin" /> </a>

<a href="https://github.com/RodrigoMato00/" target="_blank">  <img align="left" src="https://img.shields.io/github/followers/RodrigoMato00?style=social" alt="RodrigoMato00 | Github"> </a>

<br/>
<br/>

Ronald

<a href="https://twitter.com/ralex_uy" target="_blank">  <img align="left" alt="Ronald Rivero | Twitter" src="https://img.shields.io/twitter/follow/ralex_uy?style=social" /> </a>

<a href="https://www.linkedin.com/in/ronald-rivero/" target="_blank">  <img align="left" alt="Ronald Rivero | LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=social&logo=linkedin" /> </a>

<a href="https://github.com/ralexrivero/" target="_blank">  <img align="left" src="https://img.shields.io/github/followers/ralexrivero?style=social" alt="Ralex | Github"> </a>

<br/>