#!/usr/bin/env python3

from flag import FLAG
from pow_lib import get_challenge, solve_challenge, SOLVER_URL, verify_challenge
import sys
import os
import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[33m"
NORM = '\033[0m'

banner = \
    r"""

    {Banner Here}

    """
    
QUESTIONS = [
    "[1]. ",
    "[2]. ",
    "[3]. ",
    "[4]. ",
    "[5]. ",
    "[6]. ",
    "[7]. "
]

ANSWERS = [
    "",
    "",
    "",
    "",
    "",
    "",
    ["MD5", "md5"]
]

assert len(QUESTIONS) == len(ANSWERS), f"Questions and Answers length mismatch! {len(QUESTIONS)} != {len(ANSWERS)}"


QnA = dict(zip(QUESTIONS, ANSWERS))

def checkInput():
    for i in range(len(QUESTIONS)):
        print(f"{QUESTIONS[i]}")
        user_input = input("==> ").strip()
        fflag = 0
        for ans in ANSWERS[i]:
           if user_input == ans:
               fflag = 1
               break
        if fflag == 0:
            print(f"{RED}Wrong answer!{NORM}")
            print(f"Disconnected. Bye!")
            sys.exit(0)
            return False
        print(f"{GREEN}Correct!{NORM}\n")
    return True

def get_flag():
    print(f"{GREEN}Congratulations! Here is your flag: {FLAG}{NORM}\n")
    
def powCheck():
    # ran = random.randint(20000, 50000)
    ran = 31337
    challenge = get_challenge(ran)
 
    banner = f"""
Before accessing the service, you must solve a proof of work (PoW) challenge.
Just run the solver with the following command:
python3 <(curl -sSL {SOLVER_URL}) solve {challenge}
===================

Solution? """

    print(banner, end="")
    sys.stdout.flush()
    solution = input().strip()
    
    if (verify_challenge(challenge, solution)):
        print("Correct")
        sys.stdout.flush()
        os.system('clear')
    else:
        print("Wrong")
        sys.exit(0)

if __name__ == "__main__":
    powCheck()
    print(banner)
    if checkInput():
        get_flag()
    else:
        os._exit(0)
        

            
