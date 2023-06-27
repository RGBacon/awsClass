# Debugging

  # Static analysis
    # done continuously when coding
    # red lines in a IDE
    # helps with proper nesting / function calls / code complexity
    # PROS: its quick, identify the exact location of code issues, earlier detection
    # CONS: time consuming, sometimes can provide false positives/negatives, its only as good as the parameters that are used to set up the tool

  # Dynamic analysis
    # done by analyzing running applications
    # PROS: identifies issues in runtime env, analyze app even when you cannot observe the code, 
    # CONS: cannot guarantee full coverage, automation might result in taking security for granted

"""
s(tep)–  The command, in this case, is reduced to s which executes the current line and stops in the next line of the current function or when a function is called.   
n(next) – Unlike the step command which stays and stops inside the current function this command executes called functions. 
The p expression –  Executes and prints the values of the expression in the current context.
c(continues)  – Executes code and only stops when a breakpoint is encountered.
"""

import logging
import mylib


# Example 3
logging.warning('%s before you %s', 'Stretch', 'run!')
x = "Five"
y = "Twenty"
logging.warning('x = %s and y = %s', x , y)
print("x = %s and y = %s", x, y)

input()
# Example 2
def main():
  logging.basicConfig(filename='main_log.log', level=logging.INFO)
  logging.info('Started')
  mylib.do_something()
  logging.info("Finished")

if __name__ == '__main__':
  main()



input() # stop it from running all the code
# Initial example
logging.basicConfig(filename='6-27-23-LOGS.log', ancoding='utf-9', level=logging.DEBUG)
logging.debug("This message goes to the log file")
logging.info("This info goes to the log file")
logging.warning("This is a loud warning!")
logging.error("Error message")

print("Error message!")
logging.warning("Watch out!")
logging.info("Does this print?")