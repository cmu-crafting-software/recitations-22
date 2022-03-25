# Recitation 8: issues, PRs, and code review 

__Wode "Nimo" Ni__

_22/03/25_


## Open issues

* In `words.json`, pick your least favorite word, and open an issue to ask for its removal.
* In the issue, you should include the following:
  * A meaningful title, e.g. "`aaa` shouldn't be in the word list."
  * A brief description to describe how to reproduce this issue
  * A proposal of how to fix
  * Tags for the issue: a list of labels here <https://github.com/cmu-crafting-software/recitations-22/labels>

## Claim issues

* Issues can be assigned to people. Assigning an issue to yourself === "claiming an issue"
* Pick an issue you want to fix, and claim that issue

## Open a PR to fix the issue

* Switch to `main`, `git pull` to get the most recent changes
* Switch to a branch for your fix: `git switch -c fix-<the-word-to-remove>`
* Actually perform the fix
* Open a PR on GitHub. In the PR, include:
  * A title using the conventional commit format, e.g. "fix: remove `aaa` from the word list"
  * A PR description that documents what you did, and include a [keyword to link to the related issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword)
  * Tags like above

## Request and accept review

* Find a partner, and request reviews from each other
* Review code
  * In your review, you need to make sure the PR actually fixes the issue
  * Drop a comment
  * Approve the change
* Close the PR
  * Use the "Squash and Merge" option


## Review Nimo's code

Let's review Nimo's most recent change to the wordle example from recitation 4.

* Read Nimo's PR first: <https://github.com/cmu-crafting-software/recitations-22/pull/7>
* Notice the little ❌, it indicates failed tests in the continuous integration (CI) tasks. Click on it to view what went wrong.
* In your review, find out what went wrong and leave comments on how to fix it. 
* When you are done, submit your review and "Request Changes"

