---
title: Functional Testing
---

## Functional Testing

---

### Overview

- Why do we test?
- Types of testing
- What is functional testing?
- How do you ensure your software does the right thing?
- Regressions

---

### Learning Objectives

- Define both functional and non-functional tests
- Consider which tests will be beneficial for the mini-project

---

### Testing

Testing software increases your confidence and your client's confidence in the product.

Better tests enable you to develop new features, experiment and improve your codebase easier and with lower risk.

A good, repeatable testing process is critical to ensuring sustainable, continuous delivery.

---

### Testing

- How do you prove your application behaves as intended?
- Who do you prove it to?
    - Yourself
    - Your team
    - Your client (UAT)
    - Your users

Notes:
We need to consider a few things:

- Analyse whether the application meets the specified requirements
- Create a clear test plan
- Write test cases that cover all the requirements
- Get the PO to buy into test cases
- Execute test cases to detect bugs

---

### Test Types

- **Functional tests:** Check that the behaviour of the application matches the user's expectations. Anything not tied directly to a task or action that can be completed by the application.
- **Non-functional tests:** Check that the application operates within the expected parameters of speed, security, resource consumption, etc.

---

## Functional Tests

---

### Unit

Testing  small chunks of code, typically individual functions.

### Integration

Separate modules/units are combined and tested as a together.

![](img/unit-vs-int-test.gif =400x)<!-- .element: class="centered" -->

---

### E2E/UI

Test from the end user's experience by simulating real user scenarios and validating the system under test and its components for integration and data integrity.

### System

Test to checks features and functionalities of the system while E2E testing checks the complete flow of the system.

---

### User Acceptance Test (UAT)

Tests conducted in the **presence of the user** to determine if the requirements of the specification have been met.

### Exploratory Tests

Test cases are not created in advance but testers check system **on the fly**. They may note down ideas about what to test before test execution.

---

### Smoke Tests

Preliminary testing to reveal simple failures severe enough to stop the deployment process.

### Alpha/Beta

**Beta testing** is performed by clients who are not part of the organization.

**Alpha testing** is performed at developer's site. Both with the intension to identify and fix bugs.

---

### Non-functional Tests

---

### Performance

Tests how responsive and stable a system under a particular workload.

### Volume

Subjecting the system to an increased volume of data.

![](img/volume-testing.gif =300x)<!-- .element: class="centered" -->

---

### Security a.k.a. Pen Testing

An overlapping test type, as it has both a functional and a non-functional aspect to it.

**Penetration test:** Colloquially known as a pentest or ethical hacking, is an authorized simulated cyberattack on a computer system, performed to evaluate the security of the system.

### Soak Test

Testing the system with a typical production load, over a continuous availability period, to validate system behaviour under production use.

---

### Functional (E2E) Testing

- Making sure your app fulfils the user's expectations
- Are we building the right thing?

![](img/test-pyramid.jpg =400x)<!-- .element: class="centered" -->

Notes:
The main purpose is to test the end user's experience by simulating the real **user scenario** and validating the entire system under test and its components for integration and data integrity.

Before testing, designers and developers create a list of which UI, functions or features that need to be performed. They then track the system against this list. Recording any bugs or issues that need to be addressed.

---

## Test Scenarios

<!-- markdownlint-disable no-emphasis-as-heading -->
_Expecting the (Im)probable_

---

### The Happy Path

- App is launched
- I create a new round
- People submit orders
- I get a list of the lunch orders
- App exits

In other words, you're testing that your function works when the user does what you expect.

---

### The Unhappy Path

- App is launched
- I create a new order
- The order is assigned to a courier that doesn't exist on the system

How do you handle that?

- Take them to the New Courier screen and get them to enter their details and try again
- Or tell them they can't submit that request and exit

---

### The More Unhappy Path

- App is launched
- App cannot open or create its state files in the desired location

How should the application deal with that?

- Crash and exit
- Or capture the error, display an error message and exit
- Or operate in a degraded functionality mode

---

### The Unexpected Path

What if the user has a visual impairment?

- App is launched on Windows
- App crashes because it can't resolve the state file path due to Windows' different filepath scheme
- Bill Gates laughs at you

---

### Thinking like a tester

Consider the interactions between the user and the application that leads to the completion of an intended task...

- User journeys
- User input
- Application state
- Devices, resolutions, OS, software version, dependencies
- Network
- Hardware issues

---

### Black box and white box testing

**Black box:** Test the functionality and requirements of your code with no awareness of its internal makeup.

**White box:** Test your application to exercise specific paths within the source code.

---

### Regressions

![](img/whackamole.gif)<!-- .element: class="centered" -->

---

### Regressions

A **regression** is the accidental breakage of some part of your application due to a change made somewhere else in the codebase.

**Coupling:** When one component needs to have (detailed) knowledge of another component in order to do its job.

Complex codebases with tightly coupled components are harder to test and change, thus more prone to regressions.

Notes:
You should regression test your software before publishing a new version Ideally, your software should be regression tested every time changes are made to it.

---

### Terms and Definitions - recap

- **Functional Testing:** Functions are tested by feeding them input and examining the output.
- **Non-Functional Testing:** Testing to check non-functional aspects (performance, usability, reliability, etc)
- **Regressions:** Accidental breakage of some part of your application due to a change made somewhere else in the codebase.

---

### Overview - recap

- Why do we test?
- Types of testing
- What is functional testing?
- How do you ensure your software does the right thing?
- Regressions

---

### Learning Objectives - recap

- Define both functional and non-functional tests
- Consider which tests will be beneficial for the mini-project

---

### Further Reading

- [What is Functional Testing? (Complete Tutorial)](https://www.guru99.com/functional-testing.html)
- [Functional Testing (Fundamentals)](https://softwaretestingfundamentals.com/functional-testing/)
- [Functional Testing vs Non-Functional Testing (Video)](https://www.youtube.com/watch?v=j_79AXkG4PY)

---

### Emoji Check:

On a high level, do you think you understand the main concepts of this session? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content
