---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region slideshow={"slide_type": "slide"} -->
# EOSC 211:  Computer Methods in Earth, Ocean and Atmospheric Sciences

## Week 1: Introduction
**Today’s Class:** Introductions <br>
**Logistics:** syllabus, text, computer accounts, grading, workload, notes

**Why MATLAB?**
* What can we do with it?
* In-class exercise
* Problem solving

**To Do for next time**


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "subslide"} -->
### Who We Are and What We Do
**Instructors:** Catherine Johnson and Rich Pawlowicz <br>
**TA's:** Georgia Peterson, Sam Stevens, Geena Littel

<img src="media\week01-slide_1-000.png">
<img src="media\week01-slide_1-001.png">
<img src="media\week01-slide_1-002.png">
<img src="media\week01-slide_1-003.png">
<img src="media\week01-slide_1-004.png">


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Course Logistics 1

…See course syllabus for details

**Canvas**
* We will use Canvas for disseminating notes, worksheets, labs etc and for you to hand stuff in.

**Class is built around labs:**
* “Lectures” are mostly paper worksheets to prepare for labs (RP or CJ) 
* Tuesday class introduces concepts, Thursday summarizes… 
* “Labs” are computer work, modeled to be “pieces” of a real problems.  At least one instructor usually present plus TAs.

**Assignments:** 
* Like labs but more complex – like real problems. 
* Mid-term + final are like in-class worksheets

<!-- #endregion -->

## Course Logistics 2

<img src="media\week01-slide_00-002.png">

<!-- #region slideshow={"slide_type": "slide"} -->
## Course Logistics 3

…See course syllabus for details

**Group Work: Class/Exams** 
* We will assign you a group (4-5 people/group) 
* We will use groups for in-class work, also a group component to exams

**“Pair Programming” in Labs:**
* Just like it sounds, work in pairs, enforced in first few labs, later up to you
* Assignments will be done in pairs (or max groups of 3)

**Collaboration, Copying and Plagiarism Policy** <br>
“For labs we encourage collaboration using a pair-programming method. However, you are expected to TRUTHFULLY REPORT: the name of your partner(s), and the level of collaboration. Using someone else’s code and claiming it as your own is plagiarism and will be treated as such.”

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Course Logistics 4

…See course syllabus for details

**Final Assessment**
* Labs 30% 
* Assignments 25%
* Midterm 15%
* Final 25%
* Mini-quizzes 5%
* ***If you fail individual parts of midterm / final combined you fail the course.***

**Labs**
* 9, but week 2 not graded and final mark is best 7 of remaining 8
* Graded out of 10 – usually one of 10/8/5/0 mark
* Due ELECTRONICALLY 4pm Fridays, they take more time then the 2-hr lab section

**Assignments** 
* 2 of them 2 weeks each,
* Letter grade
* Due ON PAPER 4pm Wednesdays (except Part 1 of A1 which is due on Mon 10/22).

**Exams**
* Mid-term (in class) and Final (during exams)
* 80% individual, 20% group

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Course Logistics 5

…See course syllabus for details

**Getting access to MATLAB**
* Need either an EOS account $25 for year <br>
 …OR… <br>
* Install MATLAB on your laptop and bring it to the lab (free for UBC students this year) <br>

**Textbook** (required) <br>
* TEXT: *MATLAB: A Practical Introduction to Programming and problem Solving.*  At bookstore.
* NB: The old text is “Problem Solving using MATLAB”  (a custom text, no longer in print)

<img src="media\week01-slide_6-005.png">


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Course Logistics 6

**Wait list**
* Moved everyone from waitlist into course last week.
* Course is now FULL:  waitlist is blocked and if you’re not in the course already you will **NOT** get in.

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Why MATLAB?

<img src="media\week01-slide_9-006.png">


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Why MATLAB?

**What will you be able to do at the end of the course?** <br>
* Write computer programs to model and analyze data in the earth sciences <br>
* But Now to More Fun Stuff…..

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Examples

* plotting time series, geographically, histograms, contour plots
* extract data from given geographical region
* smooth data; deal with data gaps; compute variability in data
* compute a simple model and see how well it fits your data

<img src="media\week01-slide_11-008.png">

<img src="media\week01-slide_11-009.png">

<img src="media\week01-slide_11-010.png">

<img src="media\week01-slide_11-011.png">

<img src="media\week01-slide_11-012.png">


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Examples

Here’s an example of a data set where physics predicts that the quantity on the y axis will increase as the quantity on the x-axis increases.

<img src="media\week01-slide_00-001.png">

…hmmm… well kinda… but my points are hard to see – I could improve my plot <br><br>
What is all the scatter?

<!-- #endregion -->

## Examples

I suspect that another quantity that I also measure might be playing a role.  I can color-code my points by this quantity:

<img src="media\week01-slide_00-003.png">
Now we can see that indeed this quantity is important.
When it is high (reddish points) the quantity on the y-axis is systematically lower and vice versa


<!-- #region slideshow={"slide_type": "slide"} -->
## Examples

A complicated figure comparing 3 different data sources measuring currents at different palces and times in the Strait of Georgia…

<img src="media\week01-slide_14-015.png">

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Examples

…or plot on a map to see spatial trends!

<img src="media\week01-slide_15-016.png">


<img src="media\week01-slide_15-017.png">

<!-- #endregion -->


<!-- #region slideshow={"slide_type": "slide"} -->
## Why MATLAB?

**What will you be able to do at the end of the course?**

* Write computer programs to model and analyze data in the earth sciences

**What we have to practice to get to this…**
* Breaking down a problem into a set of logical steps (an algorithm)
* Writing and debugging MATLAB programs to implement your algorithm
* Modifying existing code to make it more readable /efficient / well-documented
* Creating scientifically informative and appealing plots
* But Now to More Fun Stuff…..

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Worksheet

## Intro Activity: Making Observations

---

**Name 1:**

**Name 2:**

**Name 3:**

GOALS: (1) Make observations from CO<sub>2</sub> and temperature records
to (1) decide how CO<sub>2</sub> and temperature have been, and are,
changing, (2) practice and example of “doing calculations by hand” to
provide test data for coding, (3) practice very rudimentary “algorithm
design”.

### Question 1

![Temp and C0_2](week01WS01_figs/media/image1.png)

#### A. Make 3 observations about each of the temperature and CO<sub>2</sub> records

Temp-1.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Temp-2.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Temp-3.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CO2-1.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CO2-2.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CO2-3.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### B. Write down one question you have about each record. (Try to pick a different question for each one)

i\.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ii\.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### C. Estimate (from the graphs) by how much temperature and CO<sub>2</sub> have between 1960 and the present.

Temperature:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CO2:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### D. Imagine you have a file that contains the data needed to make the
plot in 4 columns with year, month, temperature, and CO<sub>2</sub>
(i.e. an average value per month of CO<sub>2</sub> and temperature) in
each column and you wanted to write code to do the calculation in C.
What would your code need to do? Try to break this down into very
explicit steps (any number of steps)**

Step
1:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Step
2:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Step
3:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Step
4:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Step
5:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Step
6:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**D. Based on the data in the CO<sub>2</sub> plot, for how long do you
think you need to observe CO<sub>2</sub> to decide whether it is
increasing? Write down how you decided this.**

How
long?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Reason?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**E. Based on the data in the temperature plot, for how long do you
think you need to observe temperature to decide whether it is
increasing? Write down how you decided this.**

How
long?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


Reason?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## 5 Steps in Solving a problem

* State the problem clearly
* Describe inputs and outputs
* Work the problem by hand for a simple set of data
* Develop a MATLAB solution
* Test with a variety of data

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## To DO for next week:

**BEFORE first lab** <br>
Get a computer account - $25:  go to front desk in Earth Sciences Building, Room 2020, 9:00am-11:30 or 2:00-4:00pm
  * See Ian or Alicia
  * Exact cash only

OR

Install MATLAB on your laptop (free for UBC students)

**BEFORE TUES CLASS:**
* Week02 reading
* Pg 3-40, 75-80, 89-101 (parts of Chaps 1-3), and skim 557-564 (Appendix 1).

<!-- #endregion -->
