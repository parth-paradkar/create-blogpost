#!/usr/bin/python3.7

import os
import datetime
import sys

# Enter the _posts directory here
posts_directory = ''
# Change the working directory to the _posts folder
os.chdir(posts_directory)
title = sys.argv[1]

date_time = datetime.datetime.now()
date, time = date_time.isoformat().split('T')
file_words = title.split(' ')
# Enter author name here
author = ''

for i in range(len(file_words) - 1):
    file_words[i] = file_words[i] + '-'

file_title = ''.join(file_words)
file_name = f"{date}-{file_title}.markdown"

with open(file_name, 'w') as file:
    file.write('---')
    file.write('\nlayout: post')
    file.write(f'\ntitle: {title}')
    file.write(f"\ndate: {date} {date_time.hour}:{date_time.minute}:{date_time.second} IST")
    # Enter a description here
    file.write("\ndescription: ")
    file.write(f"\nauthor: {author}")
    file.write('\n---')
    print(f"New blogpost file {file_name} created at {posts_directory}")
