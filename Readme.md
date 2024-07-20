# Correct pronunciation errors in English sentences

I want to create a system that can correct mispronunciations of sentences in English. 

## 1. Based on Dictionary

### Idea
The first concept is to match words that have been translated into writing using speech_recognition and then see which ones are not in the dictionary. If something is not there, it is considered an object, and if something is slightly different, it is considered an error, and then corrected
### Problem
The problem arises because speech_recognition has ensured that all the words are correct, so that errors are minimal because words are considered other words by speech_recognition, and translated into those words, for example:
- metropolis ==> metabolic
- known ==> know
Because this word is a word that is also found in the English dictionary, therefore, even if it is wrong, the word is considered correct. 
### Solution
Therefore, references are needed to correct incorrect sentences

## 2. Based on Provided Reference

### Idea
The second concept is quite simple, namely by matching sentences translated by speech_recognition with reference sentences. Matching is done by marking which sentences are missing, wrong, or contain new words. Then the sentence is corrected according to the existing references.
### Problem
The problem is that this system is not a practical system. In fact, if matching is required using large sentences, this system becomes impractical.
### Solution
Therefore, a flexible reference is needed to detect and correct incorrect sentences

## Another Idea
After doing research, there is a system called Grammatical Error correction to detect and correct sentences. Next time
I will make it....