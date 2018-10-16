# Problem Set 2

## Overview

In this assignment, you will write Python code to *simulate* some of the
streaming algorithms that we discussed in class on a **pseudo-streamed** data
set. We will use a text corpus called `leipzig100k.txt`, a file that contains a
little over 2 million English alphanumeric words. In order to simulate a stream
of words, you should *pretend* that your only access to the data is through the
generator, `data_stream`, that appears in the file `prep.py`.

An additional data file, `Proper.txt`, contains a proper subset of the words in
the data stream, all tagged as proper nouns by the `nltk` package (the Natural
Language Toolkit).

In a departure from the usual notebook, this assignment will also be done using
a **git** workflow on **github**. This will also provide some practice for those
of you that have not used git/github before: the class project to be announced
on Thursday, will be exclusively done via github too! If you haven't done so
already, please take the time to go through the [git lesson at Software
Carpentry](http://swcarpentry.github.io/git-novice/), or choose from literally
tens of tutorial sites like [this
one](https://guides.github.com/activities/hello-world/). You should become
comfortable with forking/cloning a repository (or, *repo*), creating a branch,
creating a commit, merging a branch, and creating a pull request. Don't worry if
you make mistakes in the beginning - the process will teach you a lot about how
useful versioning is once you become comfortable with git!

The workflow for the assignment will be as follows:

1. **Fork** or **clone** a copy of this repo (the `original` problem set repo),
either from the command line or from github's GUI interface into a local
repository (your local repository will be referred to as your `master` repo in
the rest of the assignment description).

2. All your code will **only** go into the file `set2.py` - do not modify the
other files! A skeleton file has been set up in the repo for you to start
editing and adding code. You will need to have additional fucntions and
scripting to complete various parts of the assignment.

3. The assignment has 3 parts. Each part should be implemented in a branch of
`master`, completed in that branch, committed in that branch, and then finally
merged back into the `master` repo. This means that I should eventually be able
to check all three versions of your `set2.py` file (assuming you have completed
them)!

## Part 1

Design a Bloom filter for the set of words contained in `Proper.txt`. The filter
should consist of a bit-vector of size 32KB - you should use the `bitarray`
package to create the vector (see [the bitarray
documentation](https://pypi.org/project/bitarray/) to understand how to install
and use this package. You should create 5 hash functions that map arbitrary
words into the Bloom filter (note that the range of each of the hash functions
should be a 18-bit number since 32KB equals 2^18 bits). Now initialize the
filter on the set of words in `Proper.txt` by hashing them and marking the
corresponding bit positions in the filter.

Determine the **total number of false positives** recorded when the entire data
stream is checked against the filter (a false positive corresponds to a word
that is not in `Proper.txt` but whose hashed positions are all marked).

Once completed, commit the code in the branch with the commit message `Completed
code for part 1` before merging it with the `master` repo.

### Part 2

Implement the Flajolet-Martin algorithm to count the approximate number of
distinct words in the data stream. Assuming that you have sampled your hash
functions in part 1 from a universal hash family, you should be able to use the
same family to create 35 hash functions for the FM algorithm: each function
should be able to map a word to a **24-bit** number.  You should then be able to
compute the largest trailing length of zeroes for each hash function and obtain
the 30 FM-estimates for the number of distinct elements. Note that each estimate
will be a power of 2.

Group the functions into seven groups, each group containing five
functions. Next, compute the average estimate per group and then choose the
median estimate of the seven group averages. This will be the value returned by
your implementation.

Once completed, commit the code in the branch with the commit message `Completed
code for part 2` before merging it with the `master` repo.


## Part 3

Implement the AMS algorithm using 512 variables to approximate the second and
third moments of the data stream. Note that you can keep track of the stream
length seen thus far to implement the appropriate sampling needed for the
reservoir (a word at a given position is supposed to be chosen uniformly at
random among all positions seen, hence the need for reservoir sampling).

Recall that the counts for the variables can be used to obtain individual
estimates for the moments. By averaging these estimates across all the
variables, you will obtain an estimate for the appropriate moment (compute both
second and third moments).

Once completed, commit the code in the branch with the commit message `Completed
code for part 3` before merging it with the `master` repo.

## Submission

You do not submit anything through Sakai - just initiate a **new pull request**
with an appropriate message describing the status of your master repos. I will
have access to your repos so will be able to check them individually.









