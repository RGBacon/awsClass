#!/bin/bash
#Jeremy
#Bank of America

accountBalance=500
loginCheck=0

function login {
	clear
	echo "Do you have an account with Bank of America? y/n"
	read -r accountYN

	if [[ $accountYN = [Yy]* ]];then
		echo "Please Enter your account name (case sensitive): "
		read -r nameLogin
		nameAuth=$(grep "$nameLogin" accounts.csv | cut -d ',' -f 1)
		pinAuth=$(grep "$nameLogin" accounts.csv | cut -d ',' -f 2)
		clear
		echo "Please enter your pin: "
		read -r pinLogin
		clear

		if [[ $pinLogin = "$pinAuth" ]] && [[ $nameLogin = "$nameAuth" ]];then
			#sucess correct name and pin
			echo "Sucessfuly logged in!"
			echo "Welcome back ""$nameLogin""!"
			loginCheck=1
		else
			echo "The authorities have been notified $USER"
			echo "Pres Enter to continue..."
			exit
		fi
	elif [[ $accountYN = [Nn]* ]];then
		#creating an account
		#
		#getting account name
		clear
		echo "Welcome to Bank of America!"
		echo "Please enter your name: "
		read -r accountName

		#creating a pin for the account
		clear
		echo "Please enter a pin code"
		read -r accountPin

		#storing the account information
		echo "$accountName,$accountPin" >> accounts.csv

		echo "Account created, please login"
	else
		echo "Invalid entry, expecting y or n"
		exit
	fi
}

function menu {
	clear
	echo "ATM for Bank of America"
	echo "Account: $nameLogin"
	echo "1. Check Balance"
	echo "2. Deposit"
	echo "3. Withdraw"
	echo "4. Logout"
}

function checkBalance {
	echo "Your balance is: $"$accountBalance""
}

function withdraw {
	echo "Enter amount to withdraw: "
	read -r withdrawAmount

	if (( accountBalance > withdrawAmount ))
	then
		accountBalance=$((accountBalance - withdrawAmount))
		echo "Please retreive your money below"
		echo "Updated account balance: $"$accountBalance""
	else
		echo "You are broke"
		echo "Your current balence is: $"$accountBalance""
	fi
}

function deposit {
	echo "Amount to deposit: "
	read -r depositAmount
	accountBalance=$((accountBalance + depositAmount))
	echo "Deposit sucessful. current balance: $"$accountBalance""
}

function easterEgg {
	#little easter egg
	#Wouldnt this be nice
	suprise=1000
	accountBalance=$((accountBalance + suprise))
	echo "For being a loyal Bank of America Customer,$"$suprise" was added to your account."
	echo "Current Balance: $"$accountBalance""
}

while true
do

	if [[ $loginCheck = 1 ]];then
		menu
		echo "Select a choice: "
		read -r choice

		if [ "$choice" = "1" ];then
			checkBalance
		elif [ "$choice" = "2" ];then
			deposit
		elif [ "$choice" = "3" ];then
			withdraw
		elif [ "$choice" = "4" ];then
			loginCheck=0
			echo "Successfully logged out. See you next time."
		elif [ "$choice" = "623" ];then
			easterEgg
		else
			echo "Incorrect Choice, 1 - 4 please"
		fi
	else
		login
	fi

	echo "Press Enter to continue..."
	read -r
done