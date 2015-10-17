#!/usr/bin/env python

#	Copyright 2013 AlchemyAPI
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

classes = []

def classify(pronoun):
    if 'social' in pronoun or 'friends' in pronoun or 'network' in pronoun:
        classes.append('social')
    if 'education' in pronoun or 'learning' in pronoun:
        classes.append('educational')
    if 'business' in pronoun or 'financial' in pronoun or 'trading' in pronoun or 'stocks' in pronoun or 'investment' in pronoun:
        classes.append('business')
    if 'software' or 'code' or 'program' in pronoun:
        classes.append('programming')
    if 'sport' in pronoun or 'basektball' in pronoun or 'baseball' in pronoun or 'football' in pronoun or 'tennis' in pronoun or 'swim' in pronoun or 'run' in pronoun or 'soccer' in pronoun:
        classes.append('sports')
    if 'politic' in pronoun:
        classes.append('politics')
    if 'news' in pronoun or 'articles' in pronoun or 'post' in pronoun or 'insider' in pronoun:
        classes.append('news')
    if 'religion' in pronoun or 'religious' in pronoun or 'god' in pronoun or 'prayer' in pronoun:
        classes.append('religion')
    if 'food' in pronoun or 'eat' in pronoun or 'cook' in pronoun or 'restaurant' in pronoun:
        classes.append('food')
    if 'shop' in pronoun or 'buy' in pronoun or 'purchase' in pronoun:
        classes.append('shopping')
    if 'travel' in pronoun or 'vacation' in pronoun or 'airline' in pronoun:
        classes.append('travel')
    if 'video game' in pronoun or 'gaming' in pronoun:
        classes.append('video games')
    if(len(classes) == 0):
        classes.append('other')
    print(classes)
#food, shopping, travel, video games, 

def relExtract():
    text = open('summary.txt')
    company = text.next()
    summary = text.next()

    alchemyapi = AlchemyAPI()

    print('Processing text: ', summary)
    print('')

    response = alchemyapi.relations('text', summary)

   # if response['status'] == 'OK':
    #    print('## Object ##')
     #   print(json.dumps(response, indent=4))

    for relation in response['relations']:
        if 'subject' in relation:
            if company.lower().strip() in relation['subject']['text'].encode('utf-8').lower():
                print(company.strip() + ' is ' +  relation['object']['text'].encode('utf-8'))
                #print('hi')
                classify(relation['object']['text'].encode('utf-8').lower())
                break

    #     print('')
    #     print('## Relations ##')
    #     for relation in response['relations']:
    #         if 'subject' in relation:
    #             print('Subject: ', relation['subject']['text'].encode('utf-8'))

    #         if 'action' in relation:
    #             print('Action: ', relation['action']['text'].encode('utf-8'))

    #         if 'object' in relation:
    #             print('Object: ', relation['object']['text'].encode('utf-8'))

    #         print('')
    # else:
    #     print('Error in relation extaction call: ', response['statusInfo'])


    print('')



# flag = 1
# while(flag == 1):
relExtract()