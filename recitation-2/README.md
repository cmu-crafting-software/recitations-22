# Recitation 2: REST and Web APIs

__Wode "Nimo" Ni__

_22/01/28_

## Announcement

* Office hours poll: appt vs. set time; Slack always good
* My setup:
  * VSCode: vim + VSCode
  * Feel free to ask any questions!

## Overview

* We learned how to access and programmatically manipulate data locally.
* Web API: programmatic access to remote data
* REST (Representation state transfer)
  * Architecture for designing an API
  * Stateless: doesn't store user data
  * HTTP (Hypertext transfer protocol)
* Why REST:
  * Less overhead of keeping track of context
  * Easier for testing
* Format:
  * respond in JSON format

## The census API

* Their homepage: <https://www.census.gov/data/developers/guidance/api-user-guide.Overview.html>
  * Step 0: request an API key
* Query example

```
https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&HISP=2&for=state:*
\_________Server address___________/\__endpoint__/\________query string__________/
```
* Getting overall population for each state

```
https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=state:*
```

* Getting overall population for each county

```
https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=county:*
```

* Getting 18+ population for each county

```
https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=county:*&AGEGROUP=29
```

## Exercise

1. Total population of Allegheny County

```
https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&in=state:42&for=county:003
```

2. Only 65+ in Allegheny County

```
https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&in=state:42&for=county:003&AGEGROUP=26

```

3. Under 18 Asian population of Pennsylvania

```
https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=state:42
```
