import json
import collections
import argparse
import random
import numpy as np
import requests
import re

def your_api_key():
    YOUR_API_KEY = 'd19727847af1b9525830756b7e81a558d97249098b5cb3675013c86b2e3246ef'
    return YOUR_API_KEY

def your_prompt():
    """Returns a prompt to add to "[PREFIX]a+b[SUFFIX]", where a,b are integers
    Returns:
        A string.
    Example: a=1111, b=2222, prefix='Input: ', suffix='\nOutput: '

    You will have to fit your prompt in Prefix and Suffix format, you can later utilize 
    preprocessor to modify it if required.
    """
    #thought of using a 5 digit addition example which decreased mae but accuracy did not improve much
    #experimented with chain of throught, and multiple examples as well but never was able to get accruacy above 0.2
    prefix = '''Question: What is 12345+54321+67890?\nAnswer: 134556\n Question: What is 18653+84259+56227?\nAnswer: 159139\n Question: What is '''
    suffix = '?\nAnswer: '

    return prefix, suffix

def your_config():
    """Returns a config for prompting api
    Returns:
        For both short/medium, long: a dictionary with fixed string keys.
    Note:
        do not add additional keys. 
        The autograder will check whether additional keys are present.
        Adding additional keys will result in error.
    """
    config = {
        'max_tokens': 50, # max_tokens must be >= 50 because we don't always have prior on output length 
        'temperature': 0.7,
        'top_k': 50,
        'top_p': 0.7,
        'repetition_penalty': 1,
        'stop': []}
    
    return config


def your_pre_processing(s):
    return s


    
def your_post_processing(output_string):
    """Returns the post processing function to extract the answer for addition
    Returns:
        For: the function returns extracted result
    Note:
        do not attempt to "hack" the post processing function
        by extracting the two given numbers and adding them.
        the autograder will check whether the post processing function contains arithmetic additiona and the graders might also manually check.
    """
    first_line = output_string.splitlines()[0]
    only_digits = re.sub(r"\D", "", first_line)
    try:
        res = int(only_digits)
    except:
        res = 0
    return res