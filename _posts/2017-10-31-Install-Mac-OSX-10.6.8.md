---
layout: post
title: "Install Scientific Development Environment for Mac OSX 10.6.8"
date: 2017-10-31
---

It could take enormous time for installing some packages and preparing for a scientific development environment because this is an old version of Mac OSX (since 2009). In this tutorial, I will present how to install netCDF, python and boost using Homebrew.

First of all, we have to install Homebrew

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Next, we could install packages using 'brew' command.

Update brew
brew update

Check error or warning from brew
brew doctor

Check list of packages by brew
brew list

Change installation formulation
brew edit <package name>

Check package information
brew info <package name>

Remove package 
brew rm <package name>

Install XCode 3.2.6

In order to use xcode compiler for installing other packages such as numpy, scipy,...

Please download this file "xcode_3.2.6_and_ios_sdk_4.3.dmg" in http://developer.apple.com

Install following packages by brew
'gcc-4.8'
brew install gcc-4.8 --cc=gcc-4.2

'openssl' and 'curl'
brew install openssl
brew install curl

Error
curl: (77) error setting certificate verify locations:
CAfile: /etc/ssl/certs/ca-certificates.crt
CApath: /usr/local/etc/openssl/certs

This error [https://stackoverflow.com/questions/24675167/ca-certificates-mac-os-x/24694579#24694579]
Add CA certification [https://www.mercurial-scm.org/wiki/CACertificates#Mac_OS_X_10.6_and_higher]

OR
Turn off ssl temporally [https://github.com/Linuxbrew/brew/wiki/FAQ#why-does-curl-fail]

'wget' (optional)
'git'

'python'

brew install python2

brew install python3

'boost'

'hdf5'
Setup 
export FC=gfortran
export F77=gfortran

brew install hdf5 --cc=gcc-4.8 --c++11

'netCDF'
brew tap homebrew/science
brew install netcdf --cc=gcc-4.8 --c++11
brew install cdo --cc=gcc-4.8 --c++11
brew install nco --cc=gcc-4.8 --c++11
brew install ncview --cc=gcc-4.8 --c++11

Install python packages {numpy, scipy, netCDF4, Pillow, tqdm}

pip3 install numpy or pip2 install numpy
