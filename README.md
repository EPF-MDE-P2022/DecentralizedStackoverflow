
                                                                            Team:
                                      VILLEMIN Adrien / ZHANG Tianyuan / LADRE Alexis / RIBOUR Yoann / LORRAIN Yvan



Work:

For the back-end we managed to create a smart contract that would transfer tokens from 1 user to an other depending on the questions and answers to those
questions.

Sadly we have no way to test whether this works properly or not

            ----------

For the front end part. We used streamlit with python to build our webpage. To deploy it on the web we also used heroku.

The page is divided in two different sections.

The first one is about asking a question. It is like a survey to fill-in to post a question in the website.
For that you need to mention the title, the description, your wallet adress, and the reward you will gift 
to the person that will help you answering your problem.

Then when you press the button "confirm" your question will be posted on the main page which is "see the board"

When you click on the list on the left you can browse to the homepage and see all then question listed. If you add one it will also appear.
Then you can see more details about a question just by clicking it. So you can access to the title, the description, and also all the answers
provided by other people.

If one answer is the right one you can click on "Award!" and the award wil normally will be given to the right wallet. That's the part we didn't succeed
link together.

We did not succeed in linking the front and back-ends of the application but the idea would be to use metamask to login to the app and the solidity code would 
fetch the wallet id to make the transfers. Then when the user who asked the question would validate an answer the app would initiate the trnasfer of tokens 
from one user to another.
