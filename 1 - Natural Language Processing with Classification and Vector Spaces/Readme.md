# Natural Language Processing with Classification and Vector Spaces
Welcome to the [first course](https://www.coursera.org/learn/classification-vector-spaces-in-nlp) of the Natural Language Processing Specialization at [Coursera](https://www.coursera.org/specializations/natural-language-processing) which is moderated by [DeepLearning.ai](http://deeplearning.ai/). The course is taught by Younes Bensouda Mourri, Łukasz Kaiser and Eddy Shyu.
 
## Table of contents

- [Natural Language Processing with Classification and Vector Spaces](#natural-language-processing-with-classification-and-vector-spaces)
  - [Table of contents](#table-of-contents)
  - [Course summary](#course-summary)
  - [Logistic regression](#logistic-regression)
    - [x] [Supervised Machine Learning & Sentiment Analysis](#supervised-machine-learning--sentiment-analysis)
    - [x] [Feature Extraction](#feature-extraction)
    - [x] [Preprocessing](#preprocessing)
    - [x] [Training Logistic Regression](#training-logistic-regression)
    - [x] [Testing Logistic Regression](#testing-logistic-regression)
    - [x] [Cost Function](#cost-function)
  - [Naive Bayes](#naive-bayes)
    - [x] [Conditional Probability](#conditional-probability)
    - [x] [Bayes' rule](#bayes-rule)
    - [x] [Laplace smoothing](#laplace-smoothing)
    - [x] [Ratio of probabilities](#ratio-of-probabilities)
    - [x] [Likelihood times prior](#likelihood-times-prior)
    - [x] [Log Likelihood + log prior](#log-likelihood--log-prior)
    - [x] [Training Naïve Bayes](#training-naïve-bayes)
    - [x] [Testing Naïve Bayes](#testing-naïve-bayes)
    - [x] [Naïve Bayes Applications](#naïve-bayes-applications)
    - [x] [Sources of Errors in Naïve Bayes](#sources-of-errors-in-naïve-bayes)
  - [Word Embeddings](#word-embeddings)
    - [Vector space models](#vector-space-models)
    - [Word by Word Design](#word-by-word-design)
    - [Word by Document Design](#word-by-document-design)
    - [Euclidean distance](#euclidean-distance)
    - [Cosine similarity](#cosine-similarity)
    - [Manipulating Words in Vector Spaces](#manipulating-words-in-vector-spaces)
    - [PCA](#pca)
  - [Word Translation](#word-translation)
    - [Transforming word vectors](#transforming-word-vectors)
    - [K-nearest neighbors](#k-nearest-neighbors)
    - [Hash tables and hash functions](#hash-tables-and-hash-functions)
    - [Locality Sensitive Hashing](#locality-sensitive-hashing)
    - [Approximate nearest neighbors](#approximate-nearest-neighbors)
    - [Searching documents](#searching-documents)


## Course summary
This is the  course summary as its given on the course [link] (https://www.coursera.org/learn/classification-vector-spaces-in-nlp):

> In Course 1 of the Natural Language Processing Specialization, offered by deeplearning.ai, you will:
> a) Perform sentiment analysis of tweets using logistic regression and then naïve Bayes, 
> b) Use vector space models to discover relationships between words and use PCA to reduce the dimensionality of the vector space and visualize those relationships, and
c) Write a simple English to French translation algorithm using pre-computed word embeddings and locality sensitive hashing to relate words via approximate k-nearest neighbor search.
 
> Please make sure that you’re comfortable programming in Python and have a basic knowledge of machine learning, matrix multiplications, and conditional probability.

> By the end of this Specialization, you will have designed NLP applications that perform question-answering and sentiment analysis, created tools to translate languages and summarize text, and even built a chatbot!

> This Specialization is designed and taught by two experts in NLP, machine learning, and deep learning. Younes Bensouda Mourri is an Instructor of AI at Stanford University who also helped build the Deep Learning Specialization. Łukasz Kaiser is a Staff Research Scientist at Google Brain and the co-author of Tensorflow, the Tensor2Tensor and Trax libraries, and the Transformer paper.

Supervised Machine Learning
> Learn about supervised machine learning and specifically about logistic regression and the steps required in order to implement this algorithm.


## Logistic regression
### Supervised Machine Learning & Sentiment Analysis 

(Học có giám sát và phân loại cảm xúc) 

- Trong bài toán học máy có giám sát chúng ta sẽ có đầu vào features X và set labels Y.
- Mục tiêu là minimize error rates / cost càng nhiều càng tốt.
- Thực hiện: run prediction function để lấy ra các parameters data map với các features để dự đoán ra labels Ŷ
- Mapping tốt nhất giữa Labels được dự đoán ra và Labels thực tế là difference between giữa Y và Ŷ nhỏ nhất.
- The cost function F does this by comparing how closely the output Ŷ is to the label Y.
- Cập nhật các parameters và lặp lại cho tới khi cost nhỏ nhất.
   - ![](Images/01.png)
- The function F is equal to the sigmoid function
  - ![](Images/08.png)

- Example of Supervised machine learning classification task for sentiment analysis (Ví dụ về bài toán phân loại cảm xúc):
> Mục tiêu là để dự đoán 1 Tweet là tích cực (positive) hay tiêu cực (nagative)
   - Để xây dựng Logistic Regression Classifier, chúng ta cần 3 bước: extract features, train, predict:
      1. Xử lý dữ liệu thô và extract useful features.
         - Các Tweets mang tính tích cực (positive) được gán nhãn là 1, còn các Tweet tiêu cực gán nhãn là 0.
      2. Train your logistic regression classifier while minimizing the cost
      3. Make your predictions
   - ![](Images/02.png)

### Feature Extraction 
 1. Sparse Represenation (Phương pháp này là dim = chiều dài của từ điển, các từ nào có trong từ điển sẽ bằng 1, các từ nào không có sẽ bằng 0).
    - To represent a text as a vector, we have to build a vocabulary and that will allow to encode any text or any tweet as an array of numbers
    - The vocabulary *V* would be the list of unique words from your list of tweets. (**Chú ý là Unique**)
    - Sparse Represenation assign a value of 1 to that a word of a tweet, If it doesn't appear in the vocabulary V we assign a value of 0.
    - ![](Images/03.png)
    - Những vấn đề găp phải đối với phương pháp Sparse Represenation:
      - A logistic regression model would have to learn N+1 parameters, where N is the size of the vocabulary *V*  (Cần N + 1 parameters, trong đó N là size của bộ từ điển và 1 là bias).
      - Large training time (Tốn thời gian Train)
      - Large prediction time (Tốn thời gian Predict)
         - ![](Images/04.png)
        
 2. Negative and Positive Frequencies (Phương pháp đếm số lần xuất hiện - Hay còn gọi là tần số Negative và Positive)
    - Set a unique words from tweets corpus, your vocabulary. (Vẫn là lấy **Unique** các từ để tạo thành bộ từ điển)
    - Build two classes, One class associated with positive sentiment and the other with negative sentiment.
    - To get the positive frequency in any word in your vocabulary, you count the times as it appears in the positive tweets, and same apply for negative tweets. (Đếm số lần các từ xuất hiện trong bộ Tweet tích cực | và đếm số lần các từ xuất hiện trong bộ Tweet tiêu cực).
       - ![](Images/05.png)
    - In practice when coding, this table is a dictionary maps the word and its corresponding class to the frequency.
    - Use the dictionary to extract useful features for sentiment analysis, to represent a tweet in a vector of dimension 3 (DIM = 3)
       - [bias=1,sum of the positive frequencies for every unique word on tweet, sum of the negative frequencies for every unique word on tweet]
       - ![](Images/06.png)

### Preprocessing 
- Use of stemming and stop words for text pre-processing. (Dùng stem để đưa các từ về từ gốc | Stop-words loại bỏ các từ không có ý nghĩa). 
- Chú ý về stopwords sẽ tùy thuộc vào từng bài toán, đôi khi có bài toán những từ trong stopwords lại có ích đối với bài toán đó.
- Còn về dấu chấm câu, có thể vẫn phải để lại để biểu thị cảm xúc chẳng hạn.

- First, I remove all the words that don't add significant meaning to the tweets, aka. stop words and punctuation marks.
- In some contexts you won't have to eliminate punctuation. So you should think carefully about whether punctuation adds important information to your specific NLP task or not.
- Stemming in NLP is simply transforming any word to its base stem.
  - ![](Images/07.png)

### Training Logistic Regression 
- To train a logistic regression classifier, iterate until you find the set of parameters θ, that minimizes your cost function.
- Để thực hiện Train cho bài toán Logistic Regression Classifier, lặp lại cho đến khi tìm được parameters theta tối ưu cost function.
- Thuật toán này gọi làm Gradient Descent. 
- This algorithm of training is called gradient descent.
  - ![](Images/09.png)
  
### Testing Logistic Regression
- You will need X_val and Y_val, Data that was set-aside during trainings, also known as the validation sets and θ.
1. First, compute the sigmoid function for X_val with parameters θ (Bước 1: Tính sigmoid function của X_val với Parameters theta)
2. Second, evaluate if each value of h of Theta is greater than or equal to a threshold value, often set to 0.5 (Bước 2: giá trị của h nếu lớn hơn ngưỡng thì positive, ngược lại negative)
3. compute the accuracy of your model over the validation sets
   - ![](Images/10.png)

### Cost Function 
- The variable m, which is just the number of training examples in your training set indicates thesum over the cost of each training example.
- The equation has two terms that are added together:
  - the left part y(i)*log h(x(i),θ) is the logistic regression function log(Ŷ) applied to each training example y(i)
  - if y = 1 ==> L(Ŷ,1) = -log(Ŷ) ==> we want Ŷ to be the largest ==> Ŷ biggest value is 1 (Trong trường hợp y = 1 chúng ta mong muốn Y_hat lớn nhất => 1)
  - if y = 0 ==> L(Ŷ,0) = -log(1-Ŷ) ==> we want 1-Ŷ to be the largest ==> Ŷ to be smaller as possible because it can only has 1 value. (Trong trường hợp y = 0, ta mong muốn Y_hat nhỏ nhất => 0)
    - ![](Images/11.png)

## Naive Bayes
### Conditional Probability
(Xác suất có điều kiện)

- In a corpus of tweets that can be categorized as either positive or negative sentiment, such words are sometimes being labeled positive and sometimes negative.pain
- ![](Images/12.png)
- Defining events A as a tweet being labeled positive, then the probability of events A shown as P of A here is calculated as the ratio between the count of positive tweets and the corpus divided by the total number of tweets in the corpus. 
- Think about probabilities as counting how frequently an events occur. (đếm tần suất 1 sự kiện xảy ra)
- The probability of the tweets expressing a negative sentiment is just equal to one minus the probability of a positive sentiment.
- ![](Images/13.png)
- Conditional probabilities is the probability of an outcome B knowing that event A already happened. (Xác suất có điều kiện là xác suất của một kết quả B khi biết A xảy ra)
### Bayes' rule
(Công thức Bayes)

- Bayes' rule states that the probability of X given Y is equal to the probability of Y given X times the ratio of the probability of X over the probability of Y.
- ![](Images/14.png)
-  The first step for Naive Bayes allows you to compute the conditional probabilities of each word given the class. 
-  ![](Images/15.png)
### Laplace smoothing
- Laplacian smoothing, a technique you can use to avoid your probabilities being zero. (Kỹ thuật giúp tránh cho xác suất bằng 0).
- ![](Images/16.png)
- Appliying the formula on the table, the sum of probabilities will still be one and no longer has a probability of zero. (Tổng các xác suất vẫn bằng 1 nhưng không còn xác suất bằng 0 nữa).
- ![](Images/44.png)
### Ratio of probabilities
- based on the last table, ratio of probability are defined as the positive conditional probabilitie of a word divided by its negative probability.
- ![](Images/17.png)
### Likelihood times prior
- Likelihood times prior 
- ![](Images/18.png)
### Log Likelihood + log prior

- log prior: tỷ lệ các tweet positive / tweet negative để tránh lệch quá nhiều trong bộ từ điển.
- To avoid numerical underflow (due to multiplying small numbers) we compute the log of the likelihood
- ![](Images/19.png)
- If the Log Likelihood + log prior > 0 Then the tweet has a positive sentiment. Otherwise, the tweet has a negative sentiment.
### Training Naïve Bayes
- To training Naïve Bayes model you need to do:
    1. Get and annotate the dataset with positive and negative tweets
    2. Preprocess the tweets
       1. Lowecase
       2. Remove punctuation, urls, names
       3. Remove stop words
       4. Stemming: reducig words to their common stem
       5. Tokenize sentences: splitting the document into single words or tokens.
    3. computing the vocabulary for each word and class: freq(w,class)
    4. get probability for a given class by using the Laplacian smoothing formula: P(w|pos),P(w|neg)
    5. Compute λ(w), log of the ratio of your conditional probabilities
    6. Compute logprior=log(P(Pos)/P(Neg))
### Testing Naïve Bayes
- To test the trained model, we take the conditional probabilities and we use them to predict the sentiments of new unseen tweets.
- To evaluate the model, we use the test sets of annotated tweets 
- Given a test set X_val, Y_val we compute the score, which is a function of X_val, λ, log prior. The prediction is $pred = score>0
- The accuracy is then
  - ![](Images/20.png)
- Words that are not seen in the training set are considered neutral, and so add **0** to the score 
### Naïve Bayes Applications
- Naïve Bayes has many Applications
  - Sentiment analysis
    - ![](Images/21.png)
  - Author identification
    - ![](Images/22.png)
  - Spam filtering
    - ![](Images/23.png)
  - Information retrieval
    - ![](Images/24.png)
  - Word disambiguation
    - For example if we can not decide whether the word **bank** (for example) refers to the river or the financial institution, compute the ratio
    - ![](Images/25.png)
- Naïve Bayes Assumptions:
  - Trong công thức Naive Bayes giả sử độc lập => Not True in NLP.
  - Conditional Independence : Not True in NLP
  - Relative frequency of training classes affect the model and can be not representative of the real world distribution
### Sources of Errors in Naïve Bayes
- Naive bayes Error Analysis can happen at:
  - Preprocessing
    - Removing punctuation (example ':(' )
    - Removing stop words
  - Word order (not word order in the sentence)
    - Example : I am happy because I did not go Versus I am not happy because I did go
  - Adversarial attacks (Easily detected by humans but algorithms are usually terrible at it)
    - Sarcasm, Irony, Euphemisms, etc
    - Example: This is a ridiculously powerful movie. The plot was gripping and I cried right through until the ending

## Word Embeddings
### Vector space models
- Vector space models repesent words and documents as Vectors that captures relative meaning by identifying the context around
each word in the text
- Main use of Vector space models is to Identify similarities and dependencies
  - ![](Images/26.png)
- Fundamental concept : "You shall know a word by the company it keeps." Firth,1957
- Applications include:
  - Information Extraction
  - Machine Translation
  - Chatbots
### Word by Word Design
- Count the number of times each two words occur together within a certain distance k
  - ![](Images/27.png)
### Word by Document Design
- Count the number of times a word occurs within a certain category
  - ![](Images/28.png)
### Euclidean distance
- Euclidean distance is the length of the straight line between points
- For two vectors the formula and in python is :
  - ![](Images/29.png)
- Euclidean distance can be misleading when corpora have different sizes
### Cosine similarity
- For two vectors v,w the cosine of their angle β is given by :
  - ![](Images/30.png)
- Cosine similarity give values between 0 and 1
### Manipulating Words in Vector Spaces
- If the vectors space are representative of the meaning then we can do operations like
  - ![](Images/31.png) 
### PCA
-  Visualization words vector space which can be in a higher dimension into a 2 or 3 dimension space so you can see relationships between words.
- PCA consists in projecting your vectors in a lower dimension space, while trying to retain as much information as possible.
- PCA Algorithm :
  - Eigenvectors give the directions of uncorrelated features
  - Eigenvalues give the amount of information retained by each feature, the variance of the new feature:
    1. Mean Normalize Data, i.e. normalize **each feature** separately
    2. Get the Covariance Matrix 
    3. Perform SVD to get **U** with shape (num_features*num_features) and the Eigen vectors matrix and **S** the Eigen values matrix.
    4. Dot Product to Project Data on **k** dimensions which give the projection on uncorrelated features:
       - ![](Images/32.png) 
    5. Compute the percentage of Retained Variance:
       - ![](Images/33.png) 
  - The Eigenvalues should be sorted in descending order

## Word Translation
### Searching documents
- Documents can be represented as vectors with the same dimension as words.
- Add the word vectors that figure in the document.
  - ![](Images/43.png)
### Transforming word vectors
- In order to translate from a language a word vectors are X to another language a word vectors are Y we want to build a matrix R such that : 
  - ![](Images/34.png) 
- To solve for R we use gradient descent for the following loss:
  - ![](Images/35.png)
### K-nearest neighbors
- To translate from X to Y using the R matrix, you may find that XR doesn't correspond to any specific vector in Y.
- KNN can search for the K nearest neighbors from the computed vector XR
- Thus searching in the whole space can be slow, using a hash tables can minimize your search space
- Hash tables may omit some neighbors that are close to your computed vector
### Hash tables and hash functions
- A hush function maps an object to a bucket in a hash table
  - ![](Images/36.png)
- A simple hash function : Hash Value = vector % number of buckets
  - ![](Images/37.png)  
- This function does not store similar objects in the same bucket ⇒ Locality sensitive hashing
### Locality Sensitive Hashing
- Separate the space using hyperplanes
  - ![](Images/38.png)
- For each vector v compute its scalar product **sign** with a normal vector on a hyperplane h<sub>i</sub>.
- the product **sign** determines on which side the vector is. 
- If the dot product is positive the  h<sub>i</sub> = 1, else  h<sub>i</sub>=0
  - ![](Images/39.png)
- the hash value is:
  - ![](Images/40.png)
### Approximate nearest neighbors
- Subdivide the space using multiple sets of random planes
  - ![](Images/41.png)
- Each subdivision will give (probably) different vectors in the same bucket of the computed vector
- Those different vectors (from multiple subdivisions) are good candidates to be the k nearest neighbors
  - ![](Images/42.png)
- This Approximate nearest neighbors is not perfect but it is much faster than naïve search
