# Logistic Regression Sentiment Analysis 🚀

![Good](/assets/images/good.png)

## Project Overview
This project leverages logistic regression to classify sentiments in product reviews to enhance business understanding of customer attitudes. 
  
My model achieves around `91%` accuracy, a notable accomplishment given the complexity of language.

## Learnings and Challenges
This project enhanced my skills in machine learning and data preprocessing. I gained valuable experience in UI/UX design during front-end implementation. Learning about containerization and Docker was pivotal for managing dependencies and developing scalable, lightweight, and robust applications that are OS agnostic.

## Installation and Running Instructions
#### Prerequisites
- Install Docker ([Docker's Official Site](https://docs.docker.com/get-docker/))

#### Installation & Running
- Download and extract this repository.
- For Windows: `docker build -t sentiment . && start http://localhost:5000/ && docker run --rm -it -p 5000:5000 sentiment && docker rmi sentiment`
- For macOS: `docker build -t sentiment . && open http://localhost:5000/ && docker run --rm -it -p 5000:5000 sentiment && docker rmi sentiment`
- For Linux: `docker build -t sentiment . && xdg-open http://localhost:5000/ && docker run --rm -it -p 5000:5000 sentiment && docker rmi sentiment`

## Dataset
Trained on the open source [Amazon Reviews dataset](https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews).
