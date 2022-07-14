# Computational Social Sciences Methods in R
### Seminar: 1.07.251

Welcome to the seminar! You can find all seminal materials here. 
:star: You can download the **the course syllabus** [here](Slides/ol2022_computational_socialscience_R_syllabus.pdf)

---

# What's new
- :star: Course log for second block is available.
- :star: Exercise 2 is uploaded: [exercise2-list-function.ipynb](ml-text-classification/exercise2-list-function.ipynb). Please submit the exercise 2 by **7th July, 23:59**.
- :star: Information for the exam is now available.

---

## Exam
The exam consisted of one base task and five additional tasks. Completing a base task guarantees you 2.0 at maximum. You can obtain a higher grade by completing one or more additional tasks. 

### Base task
The base task is to conduct the text classification using SVM code. You can find the dataset for the task in the [Exam](Exam) folder. You can read the csv dataset file into Python using `read-dataset.ipynb` file.

- Explaining SVM 
- Explaining other techniques producing better performance in machine learning
	- i.e., tokenization, stemming, tfidf, grid search
- Evaluating the classification results

### Additional tasks
1. Use more/different techniques for the text cleaning before running the machine learning. e.g., remove stopwords and/or use a different stemmer.
2. Try machine learning algorithms with the same data and compare the results.
3. Provide ideas on how to improve the machine learning performance. For example, NLP techniques which were not introduced in the course.
4. Introduce other machine learning algorithms which possibly perform better than SVM. For example, LightGBM.
5. Introduce your research plan using the machine learning algorithm. It does not have to be a classification task. Please briefly explain your research design. i.e., research question, hypothesis, data, type of machine learning algorithm, etc.
6. Conduct machine learning using your own dataset. 

### Pages
Minimum three pages, English or German.

### Deadline
September 15th. 


---



# Course log

## First block (May 6 and May 7)
### May 6 (Fri)
* General introduction: [ol2022css-intro.pdf](Slides/ol2022css1-intro.pdf)
* Machine learning introduction: [ol2022css2-ml.pdf](Slides/ol2022css2-ml.pdf)

### May 7 (Sat)
* R refresher, section 1 (Obtain and install R and RStudio) to 4 (R Packages): [r_refresher_short.pdf](R_refresher/r_refresher_short.pdf)
* Python introduction: [ol2022-css-python-intro.pdf](Slides/ol2022-css-python-intro.pdf)
  * Reference: Lubanovic, Bill. (2014) Introducing Python: Modern Computing in Simple Packages. O’Reilly Media.


## Second block

### First Day (June 10)
- Introduction to machine learning : [ol2022css3-ml2.pdf](Slides/ol2022css3-ml2.pdf)
- Python basics : [python_data_type.ipynb](Python_basics_jupyter/python_data_type.ipynb)

### Second Day (June 11)
- Exercise 1: [exercise1-read-pickle-create-variables.ipynb](ml-text-classification/exercise1-read-pickle-create-variables.ipynb)
- Introduction to text classification : [ol2022css4-text-classification.pdf](Slides/ol2022css4-text-classification.pdf)
- Classifying tweets using Support Vector Machine (SVM) : [svm-detecting-author-twitter.ipynb](ml-text-classification/svm-detecting-author-twitter.ipynb
  - **Prerequisite**: `NLTK`, `scikit-learn` packages + two NLTK bundles. The section below explains how to install them. Also you need to have data files (`pkl` files) in the working directory. 
    
- Function in Python: [python_method.ipynb](Python_basics_jupyter/python_method.ipynb)


### How to install packages using conda
1. Open *Anaconda Prompt* (windows) or *Terminal* (mac)
2. Check if you already have the package or not. For this session, we need following two packages: `nltk` and `scikit-learn`. 
   ```
   conda list <package-name>
	```
3. In case you don't have the package,  install them.
   ```
   conda install nltk
   conda install scikit-learn
	```

#### NLTK download
To run the SVM code, you need to download NLTK bundles after you intalled the nltk package. 

```
import nltk
nltk.download()
```
When you execute the code above, there will be a small window allowing you to download NLTK bundles. Among them, download `punkt`, `stopwords`. 


## Third block

## First Day (July 8)
- Exercise 2 solve together.
	- function: python_method.ipynb
- Exercise 3: exercise3-for-loop.ipynb
	- for loop: python_loop_condition.ipynb

## Second Day (July 9)
- Walk through SVM code file (svm-detecting-author-twitter.ipynb).
	- Understand four functions in the code.
	- Documentation of Scikit-learn package.
		- [SVM](https://scikit-learn.org/stable/modules/svm.html#classification)
		- [Grid search](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV)
		  

  



---
## Preparation
### Install R and RStudio
:star: Install both R and RStudio in your laptop before Week 2.

#### R
- R is a language and environment for statistical computing and graphics.
- Free
- You can download here: [www.r-project.org](https://www.r-project.org)

#### RStudio
- RStudio provides integrated development environment for R (and other languages).
- Free
- You can download here: [www.rstudio.com](https://www.rstudio.com)

If you want to have more detailed instruction..check [here](https://courses.edx.org/courses/UTAustinX/UT.7.01x/3T2014/56c5437b88fa43cf828bff5371c6a924/).

#### For R beginners
RStudio Education provides a perfect roadmap how to start R with RStudio: [RStudio Education](https://education.rstudio.com/learn/beginner/)

In particular, you should check:
-  ModernDive [Getting Started with R and RStudio](https://moderndive.netlify.app/1-getting-started.html)
-  R-Ladies Sydney [Basic Basics](https://rladiessydney.org/courses/ryouwithme/01-basicbasics-0/)
