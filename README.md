# **Slash_Product_Categorization**

## **Problem definition**

So the task is to build a Prodct Categorization model that can take the image of the product and predict it's category for example i give you a tshirt and you say its from fashion items but for
a keychain this one is considered a stationary item.

I will be playing with three main categories for the task ( Fashion - Accessories - Stationary ) 

Now let's get into the phases !

## **Phase 1 : Data Collection**

The problem had no dataset but we were asked to take some screenshots go more advanced so after some thinking i found out a good way to collect data faster than taking screenshots
which was scraping but slash is still an mobile application so after many tries i failed to scrap Slash yet i found another way!

Now Slash shows the brand of each product for example i can see a notebook by Dawenha so i decided to scrap dawenha instagram page for some pictures for stationary items and so on
Till i collected roughly 200 images for each category which would have taken sometime if i kept screenshoting.

Here is a quick look

https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/4fa82b92-af51-4698-8aaa-5a931ac829f2

For the test data i collected 15 sample from each category but this time by screenshots from the app

## **Phase 2 : Data Preparation**

After collecting the data I uploaded it on Google Drive we had 595 images for training from the three categories nearly 200 for each class and 45 unqiue images for testing taken from the app as I mentioned above 
after mounting the drive i preformed some preprocessing on the images including 
1- Resizing the images
2- Normalizing the images

Then checked some samples to check if there was any mistake loading the data but all was good
![image](https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/04bd8060-7c1f-4751-976d-c1c779e230f7)


## **Phase 3 : Building Models and Evaluating them

First i tried a CNN architecture that i built no fine tuning on pre trained models and it overfitted

![image](https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/4dcaceab-c70c-47a4-9705-3a2c59918668)

Then i Tried different Pretrained models all of them was better than earlier one

1-InceptionResNet

![image](https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/bf8329f7-1aea-4645-87fa-6809db6f2358)

2- MobileNet

![image](https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/91a6287f-1465-450d-89a5-35bcad040a68)

3- DenseNet

![image](https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/bc067d22-ea63-43d1-9c8a-abe68ac62726)

The competition between Inception & DenseNet was hard but evaluating the model on the test data showed us the better one
![image](https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/685a9a0e-cc3b-4203-9dfe-7b0ee39f5720)

As we can see DenseNet correclty classified 42 out of the 45 products we gave to it and after looking deeper into the results here is why it missclassified the 3 samples
the failed images was the ones with the models holding laptop sleeves as this can even confuse us humans if it is the clothes or the sleeve they are selling.

So finally DenseNet was the best option scoring 93 % accuracy on the test data
![image](https://github.com/Youssefsalem3/Slash_Product_Categorization/assets/101949937/6aaab0af-0f75-4850-84e3-4e5233e679aa)













